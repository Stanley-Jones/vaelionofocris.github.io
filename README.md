# Vaelion of Ocris — The Witness Cycle (Static Site)

This is a minimal, elegant static website for the Witness Cycle — built for GitHub Pages + custom domain.

## Structure
- `index.html` — Home (covers, buy buttons, manifesto link)
- `manifesto.html` — Full text of The Witness Cycle Manifesto
- `about.html` — Short author bio + contact
- `style.css` — Shared style (black + bronze aesthetic)
- `images/` — Book covers

## Deploy on GitHub Pages
1. Create a public repository named `vaelionofocris.github.io`.
2. Upload all files to the root of the repository.
3. Go to **Settings → Pages → Deploy from branch → main** and Save.
4. (Optional) Add **Custom Domain**: `vaelionofocris.com`. Point DNS to GitHub Pages:

A records:
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153

CNAME:
Host: `www`
Value: `vaelionofocris.github.io`

## Replace links
In `index.html`, replace the `href="#"` with your real Amazon / Goodreads links.

## License
All content © Vaelion of Ocris. The CSS and HTML scaffold can be reused by the author.
