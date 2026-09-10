# Quantum Gravity & Holography — lab website

Static site for the QG & Holography group, Department of Physics, Sogang University.
No framework, no build dependencies beyond Python 3. Free to host forever on
GitHub Pages.

```
data.py            ← all content lives here (people, publications, courses)
build.py           ← generates the HTML pages
make_preview.py    ← optional: merges everything into one preview.html
assets/style.css   ← the whole design system
assets/hero.js     ← the Poincaré-disk figure on the home page
index.html  research.html  people.html  publications.html  teaching.html
```

## Editing the site

Almost everything you'll ever change is in `data.py`.

**Add a paper** — put one line at the top of `PUBLICATIONS`:

```python
(2026, "Author One, Junho Hong, Author Three",
 "Title of the paper",
 "JHEP 06 (2026) 271",       # "" for a preprint
 "2603.18248",                # arXiv id, "" if none
 "10.1007/JHEP06(2026)271"),  # DOI, "" if none
```

Your name is bolded automatically. `<i>N</i>`, `<sub>7</sub>`, `<sup>3</sup>`
work inside titles.

**Add or remove a person** — edit `PEOPLE`. Each group is
`("Role label", [ ...members... ])`, and a member is a `dict` with `name_en`,
optional `name_ko`, optional `degree`, and a `term` list of lines.

**Courses** — edit `COURSES`, and delete the `COURSES_NOTE` line once the real
courses are in.

Then regenerate:

```bash
python3 build.py
```

Commit the changed `.html` files along with `data.py`.

## Publishing on GitHub Pages (free, no ads, custom domain)

1. Create a **public** repository — free GitHub Pages requires public.
2. Push everything in this folder to the `main` branch.
3. Repo → **Settings → Pages** → Source: *Deploy from a branch*, branch `main`,
   folder `/ (root)`. Save.
4. A minute later the site is live at
   `https://<username>.github.io/<repo>/`.

### Keeping the sogang.ac.kr address

To serve the site at the current `qgholography.sogang.ac.kr` instead:

1. Ask Sogang IT to point a **CNAME** record for `qgholography.sogang.ac.kr` at
   `<username>.github.io`.
2. In **Settings → Pages → Custom domain**, enter `qgholography.sogang.ac.kr`.
   GitHub writes a `CNAME` file into the repo — leave it there.
3. Tick **Enforce HTTPS** once the certificate is issued (usually within an hour).

Existing links to the lab keep working, and hosting stays free.

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Notes

- Fonts (Spectral, IBM Plex Sans, IBM Plex Mono) load from Google Fonts; the
  page falls back to system serif/sans if that is ever blocked.
- Light and dark themes both ship — the site follows the visitor's OS setting.
- `.nojekyll` tells GitHub Pages to serve the files as-is.
