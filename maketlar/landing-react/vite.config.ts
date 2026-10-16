import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { viteSingleFile } from 'vite-plugin-singlefile'

// `npm run build:html` — barcha JS, CSS va rasmlar ichida bo'lgan bitta HTML fayl
export default defineConfig(({ mode }) => ({
  plugins: [react(), ...(mode === 'single' ? [viteSingleFile()] : [])],
  base: './',
  build: mode === 'single' ? { outDir: 'dist-html', assetsInlineLimit: 100_000_000 } : {},
}))
