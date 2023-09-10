import axios from 'axios';

import { AuthResponse } from '../models/Response/AuthResponse';

const api = axios.create({
  withCredentials: true,
});

api.interceptors.request.use(config => {
  config.headers.Authorization = `Bearer ${localStorage.getItem('token')}`;
  return config;
});

api.interceptors.response.use(
  config => {
    return config;
  },
  async error => {
    const originalRequest = { ...error.config };
    originalRequest._isRetry = true;
    if (error.response.status == 401) {
      try {
        const response = await api.get<AuthResponse>('api/v1/refresh', {
          withCredentials: true,
        });
        localStorage.setItem('token', response.data.accessToken);
        return api.request(originalRequest);
      } catch (e) {
        console.log(e);
      }
    }
  }
);

export default api;
