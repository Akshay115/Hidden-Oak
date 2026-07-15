# Hidden Oak

Static website for **Hidden Oak Banya** — a traditional Russian banya in Arambol, Goa. Built with [Astro](https://astro.build), deployable to Cloudflare Pages.

## Stack

- **Astro 7** — static site generator, zero JS shipped by default
- **Vanilla CSS** — earthy design tokens (`src/styles/global.css`), no UI framework
- **Cloudflare Pages** — static hosting + one Pages Function for the contact form
- **Cal.com** — booking widget embedded client-side on `/book`
- **Brevo** — CRM + transactional email for contact form submissions
- **Fraunces + Manrope** — Google Fonts (warm serif headings, humanist sans body)

## Quick start

```bash
npm install      # install dependencies
npm run dev      # dev server at http://localhost:4321
npm run build    # build to dist/
npm run preview  # preview the production build locally
```

## Project structure

```
hidden-oak/
├── public/
│   ├── _routes.json          # Cloudflare: only /api/* hits the Function
│   ├── robots.txt
│   ├── favicon.svg
│   └── images/               # hero poster, OG image, gallery placeholders
├── src/
│   ├── components/           # Header, Footer, Hero, CTAButton, etc.
│   ├── layouts/
│   │   └── BaseLayout.astro   # HTML shell, SEO meta, JSON-LD, fonts
│   ├── pages/                # 8 routes (7 public + style-guide)
│   └── styles/
│       └── global.css         # design tokens + base styles
├── functions/
│   └── api/
│       └── contact.ts         # Pages Function → Brevo CRM + email
├── wrangler.toml              # Cloudflare Pages config
├── astro.config.mjs           # Astro + sitemap config
└── package.json
```

## Pages

| Route | Purpose |
|---|---|
| `/` | Homepage — hero, what we offer, why Hidden Oak, pricing/membership teasers |
| `/the-banya` | About — the history and cultural story of the Russian banya |
| `/services` | Practical breakdown — sauna, ice bath, shower, session comparison, FAQ |
| `/pricing` | Walk-in prices + membership tiers |
| `/gallery` | Masonry grid with category filter + accessible lightbox |
| `/book` | Cal.com inline booking embed |
| `/location` | Map, address, hours, directions, contact form (→ Brevo) |
| `/style-guide` | Design token reference (internal, excluded from sitemap) |

## Deploy to Cloudflare Pages

### Prerequisites

- A GitHub account with the repo pushed to `https://github.com/Akshay115/Hidden-Oak`
- A Cloudflare account (free tier is sufficient)

### Method 1: GitHub integration (recommended — auto-deploys on push)

1. **Push to GitHub** (if not already done):
   ```bash
   git add -A && git commit -m "Prep for deployment" && git push
   ```

2. **Connect the repo in Cloudflare:**
   - Log into the [Cloudflare dashboard](https://dash.cloudflare.com)
   - Go to **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
   - Authorize Cloudflare to access the `Akshay115/Hidden-Oak` repository
   - Select the repo

3. **Configure build settings:**
   | Setting | Value |
   |---|---|
   | Framework preset | **Astro** |
   | Build command | `npm run build` |
   | Build output directory | `dist` |
   | Root directory | `/` (leave default) |
   | Node version | Set env var `NODE_VERSION=22` |

4. **Add environment variables** (see [Environment variables](#environment-variables) below)

5. **Save and Deploy.** First deploy takes ~1–2 minutes. Subsequent pushes to `main` auto-deploy.

### Method 2: Wrangler CLI (manual deploys)

```bash
# Install wrangler if not already available
npm install -D wrangler

# Login to Cloudflare (opens browser)
npx wrangler login

# Build and deploy (runs `wrangler pages deploy dist` under the hood)
npm run deploy

# Or deploy to a preview branch
npm run deploy:preview
```

### Environment variables

Set these in the Cloudflare dashboard: **Pages project → Settings → Environment variables**. Add to both **Production** and **Preview** scopes.

| Variable | Required | Purpose |
|---|---|---|
| `NODE_VERSION` | ✅ | Set to `22` — tells Cloudflare's build which Node to use |
| `BREVO_API_KEY` | ✅ (for form) | Brevo API key (`xkeysib...`). **Must be encrypted (secret).** |
| `BREVO_LIST_ID` | Optional | Numeric Brevo contact list ID (to segment website enquiries) |
| `CONTACT_EMAIL` | Optional | Notification recipient (defaults to `thehiddenoak@gmail.com`) |

**For secrets**, use the encrypted option:
- Dashboard → Settings → Environment variables → Add → **Encrypt**
- Or via CLI: `npx wrangler pages secret put BREVO_API_KEY --project-name hidden-oak`

The `wrangler.toml` file already declares `CONTACT_EMAIL` as a non-secret `[var]`. You can override it in the dashboard if needed.

> **Cal.com config** (`hidden-oak/banya-session`) is hard-coded in `src/pages/book.astro` — no environment variable needed. Change it there when you have your real Cal.com event URL.

### Brevo setup (for the contact form)

The contact form on `/location` posts to `/api/contact`, a Cloudflare Pages Function (`functions/api/contact.ts`) that:

1. Creates/updates a contact in Brevo CRM
2. Sends a notification email to `thehiddenoak@gmail.com`

To activate:

1. Create a [Brevo](https://www.brevo.com) account (free tier: 300 emails/day)
2. Generate an API key: **Settings → SMTP & API → API Keys → Generate**
3. Verify the sender address (`thehiddenoak@gmail.com`): **Settings → Senders & IP → Add**
4. (Optional) Create a contact list and note its numeric ID
5. Set `BREVO_API_KEY` and `BREVO_LIST_ID` in Cloudflare (see above)
6. Redeploy

Until the env vars are set, the form returns a graceful "Server is not configured" message.

### Custom domain

After deploying, attach a custom domain:
- Dashboard → **Pages project → Custom domains → Set up a domain**
- Cloudflare handles SSL automatically
- Update `site` in `astro.config.mjs` and the canonical URLs in `BaseLayout.astro` to the new domain

### Verifying the deployment

After the first deploy, check:

- [ ] `https://hidden-oak.pages.dev` loads the homepage
- [ ] All 7 routes return 200 (Home, The Banya, Services, Pricing, Gallery, Book, Location)
- [ ] `/sitemap-index.xml` loads
- [ ] `/robots.txt` loads
- [ ] The Cal.com embed loads on `/book` (requires a valid Cal.com event URL)
- [ ] The contact form on `/location` submits successfully (requires Brevo env vars)
- [ ] Google Maps embed loads on `/location`

## Commands

| Command | Action |
|---|---|
| `npm install` | Install dependencies |
| `npm run dev` | Start dev server at `localhost:4321` |
| `npm run build` | Build production site to `dist/` |
| `npm run preview` | Preview the production build locally |
| `npm run deploy` | Build + deploy to Cloudflare Pages (via Wrangler) |
| `npm run deploy:preview` | Build + deploy to a preview branch |

## Tech notes

- **Build output:** ~280 KB total (HTML + minified CSS + SVG assets, zero external JS)
- **Pages Function:** only `/api/*` routes invoke the Worker runtime (`_routes.json`); all other paths are served as static files for maximum performance
- **SEO:** per-page meta descriptions, Open Graph tags, canonical URLs, `sitemap.xml`, `robots.txt`, and JSON-LD `LocalBusiness` structured data on every page
- **Accessibility:** WCAG AA color contrast, keyboard navigation throughout, `prefers-reduced-motion` support, ARIA labels on all interactive elements
