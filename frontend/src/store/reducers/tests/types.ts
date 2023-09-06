import { ITest } from '../../../models/ITest';

export interface TestsState {
  error: string;
  isLoading: boolean;
  tests: ITest[];
}

export enum TestsActionType {
  SET_ERROR = 'SET_ERROR',
  SET_IS_LOADING = 'SET_IS_LOADING',
  SET_TESTS = 'SET_TESTS',
}

export interface SetErrorAction {
  type: TestsActionType.SET_ERROR;
  payload: string;
}

export interface SetIsLoadingAction {
  type: TestsActionType.SET_IS_LOADING;
  payload: boolean;
}

export interface SetTestsAction {
  type: TestsActionType.SET_TESTS;
  payload: ITest[];
}

export type TestsAction = SetErrorAction | SetIsLoadingAction | SetTestsAction;
