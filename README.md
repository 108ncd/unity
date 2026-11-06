# Spiritual Unity Movement website

A static site: many traditions, one ocean of love.

Pages: `index.html` (home), `bhakti.html`, `darshanas.html`, `varnashrama.html`, shared `style.css`. No build step.

## Publish on GitHub Pages
1. Put these files at the root of a GitHub repository (keep `.nojekyll`).
2. In the repository, open Settings → Pages, choose "Deploy from a branch", branch `main`, folder `/ (root)`.
3. The site appears at `https://<your-username>.github.io/<repo-name>/`.

## Adding a quote
Copy a `<figure class="quote">` block in `bhakti.html`. Always include the speaker, the exact source, and the translator.

## Editing
Page content lives in `_build/src/*.body.html`; the shared header, nav and footer are in `_build/build.py`. Run `python3 _build/build.py` to regenerate the HTML pages at the repo root.
