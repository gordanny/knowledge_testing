import axios from 'axios';
import { redirect } from 'react-router-dom';

import { RouteNames } from '../../../Application';
import { IUser } from '../../../models/IUser';
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
        const response = await axios.post<IUser>('/api/v1/login', {
          username: username,
          password: password,
        });
        const user = response.data;
        if (user) {
          dispatch(AuthActionCreators.setIsAuth(true));
          dispatch(AuthActionCreators.setUser(user));
        } else {
          dispatch(
            AuthActionCreators.setError('Неправильный логин или пароль')
          );
        }
        dispatch(AuthActionCreators.setIsLoading(false));
        return redirect(RouteNames.MAIN);
      } catch (e) {
        dispatch(AuthActionCreators.setError('Произошла ошибка авторизации'));
        dispatch(AuthActionCreators.setIsLoading(false));
      }
    },
  logout: () => async (dispatch: AppDispatch) => {
    dispatch(AuthActionCreators.setIsAuth(false));
    dispatch(AuthActionCreators.setUser({} as IUser));
    return redirect(RouteNames.LOGIN);
  },
};
