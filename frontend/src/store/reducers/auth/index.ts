import { IUser } from '../../../models/IUser';

import { AuthAction, AuthActionType, AuthState } from './types';

const initialState: AuthState = {
  error: '',
  isAuth: false,
  isLoading: false,
  user: {} as IUser,
};

export default function authReducer(
  state = initialState,
  action: AuthAction
): AuthState {
  switch (action.type) {
    case AuthActionType.SET_ERROR:
      return { ...state, error: action.payload, isLoading: false };
    case AuthActionType.SET_IS_AUTH:
      return { ...state, isAuth: action.payload, isLoading: false };
    case AuthActionType.SET_IS_LOADING:
      return { ...state, isLoading: action.payload };
    case AuthActionType.SET_USER:
      return { ...state, user: action.payload };
    default:
      return state;
  }
}
