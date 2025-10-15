# Deploying the site (GitHub Pages, static) — 2025-10-15

This site is static and uses Stripe Payment Links and giscus.

## Blog
- `blog.html` lists posts. Each post lives in `/posts/<slug>.html` with its own giscus thread.
- Mapping: `pathname`, repo: `Stanley-Jones/vaelionofocris.github.io` (as configured in the giscus snippet).

## Stripe Payment Links
- In each Payment Link → *After payment* → **Don't show confirmation page** → Redirect to: `https://vaelionofocris.com/success.html`.
- Cancel redirect is not available for Payment Links — that's expected.
- Ensure **Collect customer email** is enabled.

## Publish on GitHub Pages
1. Push contents of this folder into your repo (root).
2. Settings → Pages → Deploy from branch (root).
3. Add custom domain and CNAME if applicable.
