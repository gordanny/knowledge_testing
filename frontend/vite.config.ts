import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';

const proxyConfig = {
  target: 'http://127.0.0.1:8000',
  changeOrigin: true,
};
const devServerPort = 3000;

export default defineConfig({
  plugins: [react()],
  server: {
    port: devServerPort,
    proxy: {
      '/api': proxyConfig,
    },
  },
});
