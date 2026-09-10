#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the built site into one self-contained page for previewing.

Not part of the published site — this only exists so the whole thing can be
looked at from a single file. Run after build.py.
"""

import base64
import os
import re

import build

HERE = os.path.dirname(os.path.abspath(__file__))
SLUGS = [(f, f.replace(".html", "")) for f, _ in build.NAV]
SLUGS[0] = ("index.html", "home")


def main():
    css = open(os.path.join(HERE, "assets/style.css"), encoding="utf-8").read()
    js = open(os.path.join(HERE, "assets/hero.js"), encoding="utf-8").read()

    # The preview is a single file, so portraits are embedded as data URIs
    photos = {}
    pdir = os.path.join(HERE, "assets/people")
    if os.path.isdir(pdir):
        for name in sorted(os.listdir(pdir)):
            if name.lower().endswith((".jpg", ".jpeg", ".png")):
                mime = "image/png" if name.lower().endswith(".png") else "image/jpeg"
                with open(os.path.join(pdir, name), "rb") as fh:
                    b64 = base64.b64encode(fh.read()).decode("ascii")
                photos["assets/people/" + name] = "data:%s;base64,%s" % (mime, b64)

    parts = []
    for fname, slug in SLUGS:
        src = open(os.path.join(HERE, fname), encoding="utf-8").read()
        body = re.search(r"<main>(.*?)</main>", src, re.S).group(1)
        for f2, s2 in SLUGS:
            body = body.replace('href="%s"' % f2, 'href="#%s"' % s2)
        for rel, uri in photos.items():
            body = body.replace('src="%s"' % rel, 'src="%s"' % uri)
        parts.append(
            '<div class="view" id="view-%s"%s>%s</div>'
            % (slug, "" if slug == "home" else " hidden", body)
        )

    head = re.search(r"<header.*?</header>", open(
        os.path.join(HERE, "index.html"), encoding="utf-8").read(), re.S).group(0)
    foot = re.search(r"<footer.*?</footer>", open(
        os.path.join(HERE, "index.html"), encoding="utf-8").read(), re.S).group(0)
    for f2, s2 in SLUGS:
        head = head.replace('href="%s"' % f2, 'href="#%s"' % s2)
        foot = foot.replace('href="%s"' % f2, 'href="#%s"' % s2)

    out = """<title>Quantum Gravity &amp; Holography</title>
%s
<style>
%s
</style>
%s
<main>
%s
</main>
%s
<script>
(function () {
  var slugs = %s;
  function show() {
    var s = (location.hash || "#home").slice(1);
    if (slugs.indexOf(s) < 0) s = "home";
    slugs.forEach(function (k) {
      var el = document.getElementById("view-" + k);
      if (el) el.hidden = (k !== s);
    });
    document.querySelectorAll(".nav a").forEach(function (a) {
      if (a.getAttribute("href") === "#" + s) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    });
    window.scrollTo(0, 0);
  }
  window.addEventListener("hashchange", show);
  show();
})();
</script>
<script>
%s
</script>
""" % (build.FONTS, css, head, "\n".join(parts), foot,
       repr([s for _, s in SLUGS]).replace("'", '"'), js)

    path = os.path.join(HERE, "preview.html")
    open(path, "w", encoding="utf-8").write(out)
    print("wrote preview.html", len(out), "bytes")


if __name__ == "__main__":
    main()
