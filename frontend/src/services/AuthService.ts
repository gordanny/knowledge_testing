import { AxiosResponse } from 'axios';

import api from '../api';
import { AuthResponse } from '../models/Response/AuthResponse';

export default class AuthService {
  static async login(
    username: string,
    password: string
  ): Promise<AxiosResponse<AuthResponse>> {
    return api.post<AuthResponse>('/api/v1/login', { username, password });
  }

  static async registration(
    username: string,
    password: string,
    fio: string
  ): Promise<AxiosResponse<AuthResponse>> {
    return api.post<AuthResponse>('/api/v1/user/create', {
      username,
      password,
      fio,
    });
  }
}
