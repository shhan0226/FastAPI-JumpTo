import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    host: '192.168.0.5',
    port: 5173, // 원하는 포트 번호로 변경할 수 있습니다
  },
})
