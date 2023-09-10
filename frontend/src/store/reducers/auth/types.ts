import { IUser } from '../../../models/IUser';

export interface AuthState {
  error: string;
  isAuth?: boolean;
  isLoading: boolean;
  user: IUser;
}

export enum AuthActionType {
  SET_AUTH_ERROR = 'SET_AUTH_ERROR',
  SET_IS_AUTH = 'SET_IS_AUTH',
  SET_AUTH_IS_LOADING = 'SET_AUTH_IS_LOADING',
  SET_AUTH_USER = 'SET_AUTH_USER',
}

export interface SetAuthErrorAction {
  type: AuthActionType.SET_AUTH_ERROR;
  payload: string;
}

export interface SetIsAuthAction {
  type: AuthActionType.SET_IS_AUTH;
  payload: boolean;
}

export interface SetAuthIsLoadingAction {
  type: AuthActionType.SET_AUTH_IS_LOADING;
  payload: boolean;
}

export interface SetAuthUserAction {
  type: AuthActionType.SET_AUTH_USER;
  payload: IUser;
}

export type AuthAction =
  | SetAuthErrorAction
  | SetIsAuthAction
  | SetAuthIsLoadingAction
  | SetAuthUserAction;
