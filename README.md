# Hidden Oak

Static website for **Hidden Oak Banya**, built with [Astro](https://astro.build) and deployable to Cloudflare Pages. Static output only — no server runtime beyond hosting — with a single client-side embed (Cal.com) for bookings.

## Stack

- **Astro 7** — static site generator, zero JS shipped by default
- **Vanilla CSS** — design tokens in `src/styles/global.css`, no UI framework
- **Cal.com** — booking widget embedded client-side on `/book`
- **Cloudflare Pages** — static hosting, build command `npm run build`, output `dist/`

## Project structure

```
hidden-oak/
├── public/
│   ├── favicon.svg
│   └── images/            # hero, gallery photos
├── src/
│   ├── components/
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── Hero.astro
│   │   ├── CTAButton.astro
│   │   ├── SectionDivider.astro
│   │   └── BookingEmbed.astro
│   ├── layouts/
│   │   └── BaseLayout.astro
│   ├── pages/
│   │   ├── index.astro            → /
│   │   ├── about-banya.astro      → /about-banya
│   │   ├── services-benefits.astro → /services-benefits
│   │   ├── prices-memberships.astro → /prices-memberships
│   │   ├── gallery.astro          → /gallery
│   │   ├── book.astro             → /book
│   │   └── contact.astro          → /contact
│   └── styles/
│       └── global.css             # design tokens: color, type, spacing
├── astro.config.mjs
├── tsconfig.json
└── package.json
```

## Commands

| Command           | Action                                       |
| :---------------- | :------------------------------------------- |
| `npm install`     | Install dependencies                          |
| `npm run dev`     | Start dev server at `localhost:4321`         |
| `npm run build`   | Build production site to `./dist/`           |
| `npm run preview` | Preview the production build locally          |

## Deploy to Cloudflare Pages

1. Push this repo to GitHub.
2. In the Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
3. Set:
   - **Framework preset:** Astro
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
   - **Node version:** 20+ (set env `NODE_VERSION=22`)
4. Deploy. No environment variables or secrets are required — the site is fully static and the Cal.com embed is hard-coded into `BookingEmbed.astro`.

### Cal.com

The booking widget is configured in `src/components/BookingEmbed.astro`. Replace the `data-url` namespace (`hidden-oak`) with your actual Cal.com organization/username, and the event slug as needed.

## Environment

No secrets are needed. `.env.example` documents the optional `PUBLIC_SITE_URL`. Astro only ever exposes `PUBLIC_`-prefixed variables to the client bundle.
