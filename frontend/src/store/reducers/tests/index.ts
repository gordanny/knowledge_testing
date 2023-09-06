import { ITest } from '../../../models/ITest';

import { TestsAction, TestsActionType, TestsState } from './types';

const initialState: TestsState = {
  error: '',
  isLoading: false,
  tests: [] as ITest[],
};

export default function testsReducer(
  state = initialState,
  action: TestsAction
): TestsState {
  switch (action.type) {
    case TestsActionType.SET_ERROR:
      return { ...state, error: action.payload, isLoading: false };
    case TestsActionType.SET_IS_LOADING:
      return { ...state, isLoading: action.payload };
    case TestsActionType.SET_TESTS:
      return { ...state, tests: action.payload };
    default:
      return state;
  }
}
