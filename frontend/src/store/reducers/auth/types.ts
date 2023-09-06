import { IUser } from '../../../models/IUser';

export interface AuthState {
  error: string;
  isAuth: boolean;
  isLoading: boolean;
  user: IUser;
}

export enum AuthActionType {
  SET_ERROR = 'SET_ERROR',
  SET_IS_AUTH = 'SET_IS_AUTH',
  SET_IS_LOADING = 'SET_IS_LOADING',
  SET_USER = 'SET_USER',
}

export interface SetErrorAction {
  type: AuthActionType.SET_ERROR;
  payload: string;
}

export interface SetIsAuthAction {
  type: AuthActionType.SET_IS_AUTH;
  payload: boolean;
}

export interface SetIsLoadingAction {
  type: AuthActionType.SET_IS_LOADING;
  payload: boolean;
}

export interface SetUserAction {
  type: AuthActionType.SET_USER;
  payload: IUser;
}

export type AuthAction =
  | SetErrorAction
  | SetIsAuthAction
  | SetIsLoadingAction
  | SetUserAction;
