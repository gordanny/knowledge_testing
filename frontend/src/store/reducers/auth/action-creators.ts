import axios from 'axios';

import { IUser } from '../../../models/IUser';
import { AuthResponse } from '../../../models/Response/AuthResponse';
import AuthService from '../../../services/AuthService';
import { AppDispatch } from '../../index';

import {
  AuthActionType,
  SetErrorAction,
  SetIsAuthAction,
  SetIsLoadingAction,
  SetUserAction,
} from './types';

export const AuthActionCreators = {
  setError: (payload: string): SetErrorAction => ({
    type: AuthActionType.SET_ERROR,
    payload,
  }),
  setIsAuth: (auth: boolean): SetIsAuthAction => ({
    type: AuthActionType.SET_IS_AUTH,
    payload: auth,
  }),
  setIsLoading: (payload: boolean): SetIsLoadingAction => ({
    type: AuthActionType.SET_IS_LOADING,
    payload,
  }),
  setUser: (user: IUser): SetUserAction => ({
    type: AuthActionType.SET_USER,
    payload: user,
  }),
  login:
    (username: string, password: string) => async (dispatch: AppDispatch) => {
      try {
        dispatch(AuthActionCreators.setIsLoading(true));
        const response = await AuthService.login(username, password);
        localStorage.setItem('token', response.data.accessToken);
        dispatch(AuthActionCreators.setIsAuth(true));
        dispatch(AuthActionCreators.setUser(response.data.user));
        dispatch(AuthActionCreators.setIsLoading(false));
      } catch (e) {
        dispatch(AuthActionCreators.setError(e.response?.data?.message));
        dispatch(AuthActionCreators.setIsLoading(false));
      }
    },
  logout: () => async (dispatch: AppDispatch) => {
    dispatch(AuthActionCreators.setIsAuth(false));
    dispatch(AuthActionCreators.setUser({} as IUser));
    localStorage.removeItem('token');
  },
  check_auth: () => async (dispatch: AppDispatch) => {
    try {
      dispatch(AuthActionCreators.setIsLoading(true));
      const response = axios.get<AuthResponse>('api/v1/refresh', {
        withCredentials: true,
      });
      localStorage.setItem('token', response.data.accessToken);
      dispatch(AuthActionCreators.setIsAuth(true));
      dispatch(AuthActionCreators.setUser(response.data.user));
      dispatch(AuthActionCreators.setIsLoading(false));
    } catch (e) {
      dispatch(AuthActionCreators.setError(e.response?.data?.message));
      dispatch(AuthActionCreators.setIsLoading(false));
    }
  },
};
