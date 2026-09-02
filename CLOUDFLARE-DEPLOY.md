# Cloudflare Preview Deployment

This repository is configured to deploy the following design artifact as a
Cloudflare static Worker:

`Noting/design/redstartrust-homepage-mockup.html`

The deployable copy is `public/index.html`. When the source mockup changes,
copy it to `public/index.html` before committing:

```sh
cp Noting/design/redstartrust-homepage-mockup.html public/index.html
cp -R Noting/design/logos/. public/logos/
```

## Cloudflare dashboard settings

- Repository: `yotsapatfx-ai/redstartrust`
- Production branch: `master`
- Build command: leave blank
- Deploy command: `npx wrangler deploy`
- Root directory: `/`

Deploy this as a preview first. Do not attach `supbest.win` until the preview
has passed UX/UI, content, responsive, and user-flow review.
