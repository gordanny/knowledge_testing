import axios from 'axios';

import { ITest } from '../../../models/ITest';
import { AppDispatch } from '../../index';

import {
  TestsActionType,
  SetErrorAction,
  SetIsLoadingAction,
  SetTestsAction,
} from './types';

export const TestsActionCreators = {
  setError: (payload: string): SetErrorAction => ({
    type: TestsActionType.SET_ERROR,
    payload,
  }),
  setIsLoading: (payload: boolean): SetIsLoadingAction => ({
    type: TestsActionType.SET_IS_LOADING,
    payload,
  }),
  setTests: (tests: ITest[]): SetTestsAction => ({
    type: TestsActionType.SET_TESTS,
    payload: tests,
  }),
  getTests: () => async (dispatch: AppDispatch) => {
    try {
      dispatch(TestsActionCreators.setIsLoading(true));
      const response = await axios.get<ITest[]>('/api/v1/tests');
      const tests = response.data;
      if (tests) {
        dispatch(TestsActionCreators.setTests(tests));
      } else {
        dispatch(TestsActionCreators.setError('Тесты не найдены'));
      }
      dispatch(TestsActionCreators.setIsLoading(false));
    } catch (e) {
      dispatch(TestsActionCreators.setError('Произошла ошибка запроса'));
      dispatch(TestsActionCreators.setIsLoading(false));
    }
  },
};
