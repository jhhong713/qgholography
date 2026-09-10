#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for the Quantum Gravity & Holography lab site.

Usage:  python3 build.py
Writes index.html, research.html, people.html, publications.html, teaching.html
next to this script. Nothing is needed at runtime except a web server.
"""

import html
import itertools
import os

import data

HERE = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Home"),
    ("research.html", "Research"),
    ("people.html", "People"),
    ("publications.html", "Publications"),
    ("teaching.html", "Teaching"),
]

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    'family=IBM+Plex+Mono:wght@400;500&'
    'family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&'
    'family=Spectral:ital,wght@0,500;0,600;1,600&display=swap">'
)


def nav_html(current):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        out.append('<a href="%s"%s>%s</a>' % (href, cur, label))
    return '<nav class="nav" aria-label="Main">%s</nav>' % "".join(out)


def page(current, title, description, body, extra_head="", extra_body=""):
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="website">
%(fonts)s
<link rel="stylesheet" href="assets/style.css">
%(extra_head)s
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="index.html">
      <b>Quantum Gravity &amp; Holography</b>
      <span>Sogang University &middot; Department of Physics</span>
    </a>
    %(nav)s
  </div>
</header>
<main>
%(body)s
</main>
<footer class="site-foot">
  <div class="wrap">
    <address class="addr">
      <b>Quantum Gravity &amp; Holography Group</b>
      Department of Physics, Sogang University<br>
      35 Baekbeom-ro, Mapo-gu, Seoul 04107, Republic of Korea<br>
      Tel. +82-2-705-8427
    </address>
    <div class="foot-links">
      <a href="mailto:%(email)s">%(email)s</a>
      <a href="%(inspire)s">INSPIRE-HEP</a>
      <a href="https://physics.sogang.ac.kr">Department of Physics</a>
      <a href="https://www.sogang.ac.kr">Sogang University</a>
    </div>
    <div class="copy">&copy; Quantum Gravity &amp; Holography, Sogang University</div>
  </div>
</footer>
%(extra_body)s
</body>
</html>
""" % dict(
        title=html.escape(title),
        desc=html.escape(description),
        fonts=FONTS,
        nav=nav_html(current),
        body=body,
        extra_head=extra_head,
        extra_body=extra_body,
        email=data.PI_EMAIL,
        inspire=data.INSPIRE_URL,
    )


def page_head(h1, lede):
    return """<section class="page-head">
  <div class="wrap">
    <h1>%s</h1>
    <p class="lede">%s</p>
  </div>
</section>
""" % (h1, lede)


# --------------------------------------------------------------- research ---

TOPICS = [
    ("Quantum gravity &amp; string theory",
     "Quantum gravity explores gravitational physics at length scales where quantum "
     "effects become significant &mdash; a regime that neither general relativity nor "
     "quantum field theory describes on its own. String theory is currently the most "
     "promising candidate for such a theory, so understanding its physical "
     "implications is the starting point of our work."),
    ("Holographic duality",
     "Holography states that a string theory on a (<i>d</i>+1)-dimensional anti-de "
     "Sitter space, together with a (9&minus;<i>d</i>)-dimensional internal manifold, "
     "is equivalent to a <i>d</i>-dimensional conformal field theory living on the "
     "conformal boundary &mdash; the AdS/CFT correspondence. It gives one of the most "
     "concrete routes to string theory as a theory of quantum gravity: the physics of "
     "strings in AdS can be read off from the dual CFT."),
    ("Exact partition functions",
     "Supersymmetric localization turns path integrals of superconformal field theories "
     "into finite-dimensional matrix integrals. We compute these partition functions "
     "and superconformal indices exactly, then push their large-<i>N</i> expansions "
     "well beyond the leading order."),
    ("Black holes &amp; quantum corrections",
     "Matching subleading terms &mdash; logarithmic corrections, Airy-function "
     "resummations, non-perturbative saddles &mdash; against supergravity gives a "
     "precision test of the microscopic counting behind black hole entropy in AdS."),
]


def research_page():
    topics = "".join(
        '<div class="topic"><h3>%s</h3><p>%s</p></div>' % (t, b) for t, b in TOPICS
    )
    body = page_head(
        "Research",
        "We study string theory as a theory of quantum gravity, using holographic "
        "duality as the main tool.",
    )
    body += """<section class="section">
  <div class="wrap">
    <div class="topics">%s</div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2 class="section-title">Methods and themes</h2>
    <div class="prose">
      <p>Concretely, the group works on superconformal field theories and their
      supersymmetric localization, large-<i>N</i> expansions and their non-perturbative
      completions, gauged and ten- or eleven-dimensional supergravities, and the
      black holes and black strings they support.</p>
      <p>A recurring theme is <strong>precision holography</strong>: computing an
      observable exactly on the field-theory side, expanding it at large <i>N</i>,
      and identifying every term with a specific effect in the bulk &mdash; classical
      supergravity, higher-derivative corrections, or one-loop quantum effects.</p>
    </div>
  </div>
</section>
""" % topics
    return page("research.html", "Research — Quantum Gravity & Holography",
                "Research directions of the Quantum Gravity & Holography group at "
                "Sogang University: string theory, AdS/CFT, exact partition functions, "
                "and black holes.", body)


# ----------------------------------------------------------------- people ---

def person_html(m, is_pi=False):
    name = '<span class="name">%s' % html.escape(m["name_en"])
    if m.get("name_ko"):
        name += ' <span class="ko">%s</span>' % html.escape(m["name_ko"])
    name += "</span>"

    parts = [name]

    if m.get("degree"):
        parts.append('<span class="term">%s</span>' % html.escape(m["degree"]))

    if is_pi:
        blocks = []
        if m.get("education"):
            rows = "".join(
                "<dt>%s</dt><dd>%s</dd>" % (html.escape(y), html.escape(v))
                for y, v in m["education"]
            )
            blocks.append("<h4>Education</h4><dl>%s</dl>" % rows)
        if m.get("career"):
            rows = "".join(
                "<dt>%s</dt><dd>%s</dd>" % (html.escape(y), html.escape(v))
                for y, v in m["career"]
            )
            blocks.append("<h4>Appointments</h4><dl>%s</dl>" % rows)
        parts.append('<div class="cv-block">%s</div>' % "".join(blocks))
    elif m.get("term"):
        parts.append(
            '<span class="term">%s</span>'
            % "".join("<span>%s</span>" % html.escape(t) for t in m["term"])
        )

    if m.get("links"):
        chips = "".join(
            '<a class="chip" href="%s"%s>%s</a>'
            % (u, "" if u.startswith("mailto:") else ' target="_blank" rel="noopener"',
               html.escape(l))
            for l, u in m["links"]
        )
        parts.append('<div class="person-links">%s</div>' % chips)

    body_html = '<div class="person-body">%s</div>' % "".join(parts)
    portrait = ""
    if m.get("photo"):
        portrait = ('<img class="portrait" src="assets/people/%s" alt="%s" '
                    'width="400" height="500" loading="lazy" decoding="async">'
                    % (m["photo"], html.escape(m["name_en"])))
    return '<div class="person%s">%s%s</div>' % (
        " is-pi" if is_pi else "", portrait, body_html)


def people_page():
    groups = []
    for role, members in data.PEOPLE:
        is_pi = role == "Principal Investigator"
        people = "".join(person_html(m, is_pi) for m in members)
        groups.append(
            '<div class="role-group"><div class="role-label">%s</div>'
            '<div class="role-people">%s</div></div>' % (html.escape(role), people)
        )

    body = page_head(
        "People",
        "The group is based in the Department of Physics at Sogang University.",
    )
    body += """<section class="section">
  <div class="wrap">
    <div class="roster">%s</div>
  </div>
</section>
""" % "".join(groups)
    return page("people.html", "People — Quantum Gravity & Holography",
                "Members of the Quantum Gravity & Holography group at Sogang "
                "University, led by Junho Hong.", body)


# ----------------------------------------------------------- publications ---

def bold_pi(authors):
    return authors.replace(data.PI_NAME, "<b>%s</b>" % data.PI_NAME)


def pub_html(entry):
    year, authors, title, ref, arxiv, doi = entry
    parts = ['<div class="title">%s</div>' % title,
             '<div class="authors">%s</div>' % bold_pi(authors)]

    if ref:
        parts.append('<div class="ref">%s</div>' % ref)
    else:
        parts.append('<div class="ref"><span class="preprint">Preprint</span></div>')

    links = []
    if arxiv:
        links.append('<a class="chip" href="https://arxiv.org/abs/%s" '
                     'target="_blank" rel="noopener">arXiv:%s</a>' % (arxiv, arxiv))
    if doi:
        links.append('<a class="chip" href="https://doi.org/%s" '
                     'target="_blank" rel="noopener">DOI</a>' % doi)
    if links:
        parts.append('<div class="pub-links">%s</div>' % "".join(links))

    return '<article class="pub">%s</article>' % "".join(parts)


def publications_page():
    blocks = []
    total = len(data.PUBLICATIONS)
    for year, group in itertools.groupby(data.PUBLICATIONS, key=lambda e: e[0]):
        items = list(group)
        n = len(items)
        blocks.append(
            '<div class="year-block">'
            '<div class="year-num">%d<small>%d %s</small></div>'
            '<div class="pub-list">%s</div></div>'
            % (year, n, "item" if n == 1 else "items",
               "".join(pub_html(e) for e in items))
        )

    body = page_head(
        "Publications",
        'The complete, always-current record lives on '
        '<a href="%s" target="_blank" rel="noopener">INSPIRE-HEP</a>.'
        % data.INSPIRE_URL,
    )
    body += """<section class="section">
  <div class="wrap">%s</div>
</section>
""" % "".join(blocks)
    return page("publications.html", "Publications — Quantum Gravity & Holography",
                "Publications of the Quantum Gravity & Holography group at Sogang "
                "University.", body)


# --------------------------------------------------------------- teaching ---

def teaching_page():
    groups = []
    for inst, meta, courses in data.TEACHING:
        rows = "".join(
            '<div class="course-row"><div class="when">%s</div>'
            '<div class="what">%s</div><div class="who">%s</div></div>'
            % (term, title, role)
            for term, title, role in courses
        )
        if len(data.TEACHING) == 1:
            groups.append('<div class="course-rows">%s</div>' % rows)
        else:
            groups.append(
                '<div class="inst-group">'
                '<div class="inst-label"><b>%s</b><span>%s</span></div>'
                '<div class="course-rows">%s</div></div>' % (inst, meta, rows)
            )

    body = page_head(
        "Teaching",
        "Courses taught in the Department of Physics at Sogang University.",
    )
    body += """<section class="section">
  <div class="wrap">
    <div class="course-list">%(groups)s</div>
    <div class="award-note">
      <span class="medal">Best Teaching Award</span>
      <p>%(award)s</p>
    </div>
  </div>
</section>
""" % dict(groups="".join(groups), award=data.TEACHING_AWARD)

    return page("teaching.html", "Teaching &mdash; Quantum Gravity & Holography",
                "Courses taught by Junho Hong in the Department of Physics at "
                "Sogang University.", body)


# ------------------------------------------------------------------- home ---

def home_page():
    recent = data.PUBLICATIONS[:4]
    pubs = "".join(pub_html(e) for e in recent)

    topics = "".join(
        '<div class="topic"><h3>%s</h3><p>%s</p></div>' % (t, b)
        for t, b in TOPICS[:2]
    )

    body = """<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <p class="eyebrow">Sogang University &middot; Department of Physics</p>
      <h1>Reading quantum gravity off its <em>boundary</em>.</h1>
      <div class="actions">
        <a class="btn btn-primary" href="research.html">Research</a>
        <a class="btn" href="publications.html">Publications</a>
        <a class="btn" href="people.html">People</a>
      </div>
    </div>
    <figure class="hero-figure">
      <canvas id="adsDisk" width="320" height="320"
              role="img"
              aria-label="A {7,3} hyperbolic tiling of the Poincare disk, a constant-time slice of anti-de Sitter space"></canvas>
      <figcaption>Poincar&eacute; disk &middot; {7,3} tiling &middot; a time slice of AdS<sub>3</sub></figcaption>
    </figure>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="section-title">What we work on</h2>
    <div class="topics">%(topics)s</div>
    <div class="actions"><a class="btn" href="research.html">All research directions</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="section-title">Recent work</h2>
    <div class="pub-list">%(pubs)s</div>
    <div class="actions">
      <a class="btn" href="publications.html">All %(total)d publications</a>
      <a class="btn" href="%(inspire)s" target="_blank" rel="noopener">INSPIRE-HEP</a>
    </div>
  </div>
</section>
""" % dict(topics=topics, pubs=pubs, total=len(data.PUBLICATIONS),
           inspire=data.INSPIRE_URL)

    return page("index.html", "Quantum Gravity & Holography — Sogang University",
                "The Quantum Gravity & Holography group at Sogang University studies "
                "string theory and AdS/CFT, led by Junho Hong.",
                body, extra_body='<script src="assets/hero.js"></script>')


PAGES = {
    "index.html": home_page,
    "research.html": research_page,
    "people.html": people_page,
    "publications.html": publications_page,
    "teaching.html": teaching_page,
}


def main():
    for name, fn in PAGES.items():
        path = os.path.join(HERE, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(fn())
        print("wrote", name)


if __name__ == "__main__":
    main()
