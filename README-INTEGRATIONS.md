# Deployment & Integrations

## Stripe success URL
Set in Stripe Payment Links:
```
https://vaelionofocris.com/download?session_id={CHECKOUT_SESSION_ID}
```

## Blog comments (giscus)
Embedded with mapping="pathname". Script set for repo `Stanley-Jones/vaelionofocris.github.io`.

## Secure downloads (tokenized)
- `download.html` calls `/api/verify-download?session_id=...`
- `/api/verify-download.js` returns **signed 30‑min** links like `/api/download?token=...`
- `/api/download.js` validates token and streams the file from **private storage**

### Environment variables (Vercel)
- `STRIPE_SECRET_KEY` — your Stripe secret key
- `JWT_SECRET` — long random string
- `DOWNLOAD_BASE_URL` — private storage base (Vercel Blob / S3 / R2)

### Expected filenames in private storage
- `Unwritten_Path.epub`
- `The_Crack_in_the_Mask.epub`
- `Unwritten_Path.pdf` (later)
- `The_Crack_in_the_Mask.pdf` (later)

**Do not commit files to the public repo.**
Upload them to private storage and ensure `DOWNLOAD_BASE_URL` points to that location.
