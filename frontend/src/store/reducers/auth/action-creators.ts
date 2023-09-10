import { IUser } from '../../../models/IUser';
import { AuthResponse } from '../../../models/Response/AuthResponse';
import AuthService from '../../../services/AuthService';
import { AppDispatch } from '../../index';

import {
  AuthActionType,
  SetAuthErrorAction,
  SetIsAuthAction,
  SetAuthIsLoadingAction,
  SetAuthUserAction,
} from './types';

export const AuthActionCreators = {
  setAuthError: (payload: string): SetAuthErrorAction => ({
    type: AuthActionType.SET_AUTH_ERROR,
    payload,
  }),
  setIsAuth: (auth: boolean): SetIsAuthAction => ({
    type: AuthActionType.SET_IS_AUTH,
    payload: auth,
  }),
  setAuthIsLoading: (payload: boolean): SetAuthIsLoadingAction => ({
    type: AuthActionType.SET_AUTH_IS_LOADING,
    payload,
  }),
  setAuthUser: (user: IUser): SetAuthUserAction => ({
    type: AuthActionType.SET_AUTH_USER,
    payload: user,
  }),
  login:
    (username: string, password: string) => async (dispatch: AppDispatch) => {
      try {
        dispatch(AuthActionCreators.setAuthIsLoading(true));
        const response = await AuthService.login(username, password);
        localStorage.setItem('token', response.data.accessToken);
        dispatch(AuthActionCreators.setIsAuth(true));
        dispatch(AuthActionCreators.setAuthUser(response.data.user));
        dispatch(AuthActionCreators.setAuthIsLoading(false));
      } catch (e) {
        dispatch(AuthActionCreators.setAuthError(e.response?.data?.message));
        dispatch(AuthActionCreators.setAuthIsLoading(false));
      }
    },
  logout: () => async (dispatch: AppDispatch) => {
    dispatch(AuthActionCreators.setIsAuth(false));
    dispatch(AuthActionCreators.setAuthUser({} as IUser));
    localStorage.removeItem('token');
  },
  check_auth: () => async (dispatch: AppDispatch) => {
    try {
      dispatch(AuthActionCreators.setAuthIsLoading(true));
      const response = await AuthService.refreshToken<AuthResponse>();
      localStorage.setItem('token', response.data.accessToken);
      dispatch(AuthActionCreators.setIsAuth(true));
      dispatch(AuthActionCreators.setAuthUser(response.data.user));
      dispatch(AuthActionCreators.setAuthIsLoading(false));
    } catch (e) {
      dispatch(AuthActionCreators.setAuthError(e.response?.data?.message));
      dispatch(AuthActionCreators.setAuthIsLoading(false));
    }
  },
};
