import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://licy2001.github.io',
  output: 'static',
  markdown: { shikiConfig: { theme: 'github-dark' } }
});
