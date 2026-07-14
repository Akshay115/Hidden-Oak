// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
// Output is static by default: Cloudflare Pages serves the built `dist/` folder,
// no server-side runtime required. The only embed (Cal.com) loads client-side.
export default defineConfig({
  site: 'https://hidden-oak.pages.dev',
  output: 'static',
});
