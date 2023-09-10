import { ITest } from '../../../models/ITest';

export interface TestsState {
  error: string;
  isLoading: boolean;
  tests: ITest[];
}

export enum TestsActionType {
  SET_TESTS_ERROR = 'SET_TESTS_ERROR',
  SET_TESTS_IS_LOADING = 'SET_TESTS_IS_LOADING',
  SET_TESTS = 'SET_TESTS',
}

export interface SetTestsErrorAction {
  type: TestsActionType.SET_TESTS_ERROR;
  payload: string;
}

export interface SetTestsIsLoadingAction {
  type: TestsActionType.SET_TESTS_IS_LOADING;
  payload: boolean;
}

export interface SetTestsAction {
  type: TestsActionType.SET_TESTS;
  payload: ITest[];
}

export type TestsAction =
  | SetTestsErrorAction
  | SetTestsIsLoadingAction
  | SetTestsAction;
