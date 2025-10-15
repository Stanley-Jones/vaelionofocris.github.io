# Deploying the site (GitHub Pages, static) — 2025-10-15

This site is fully static and works on GitHub Pages.

## Blog comments (giscus)
- `blog.html` includes a giscus embed configured for `Stanley-Jones/vaelionofocris.github.io`.
- Ensure **Discussions** are enabled in the repository and giscus is installed and authorized.
- Comments will work on Pages without a backend.

## Payments (Stripe Payment Links)
- The site uses Stripe **Payment Links** (`https://buy.stripe.com/...`) for purchases.
- No backend is required.
- Configure each Payment Link in your Stripe Dashboard to use:
  - **Success URL** → `https://<your-domain>/success.html`
  - **Cancel URL** → `https://<your-domain>/cancel.html`
  - **Collect customer email** → enabled (so buyers get receipts and you can fulfill digital delivery when needed).

### Digital delivery
If you want automated protected downloads, you will need a small serverless backend (e.g., Vercel Functions) to validate the Checkout session and generate expiring download links. That setup existed in `api/` + `download.html` but was removed here to keep the site 100% static for GitHub Pages.

If you keep it static:
- Email buyers a download link manually after purchase, or
- Use a separate digital delivery service.
- You can also add a note on `success.html` explaining the delivery timeline.

## How to publish on GitHub Pages
1. Create a repo named `vaelionofocris.github.io` (or use an existing one).
2. Upload all files from the root of this folder (not the directory itself).
3. In repo **Settings → Pages**, select "Deploy from branch", branch `main`, folder `/ (root)`.
4. Wait for Pages to build; your site will be live at `https://<user>.github.io/` or your custom domain.
