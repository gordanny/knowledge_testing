import api from '../../../api';
import { ITest } from '../../../models/ITest';
import { AppDispatch } from '../../index';

import {
  TestsActionType,
  SetTestsErrorAction,
  SetTestsIsLoadingAction,
  SetTestsAction,
} from './types';

export const TestsActionCreators = {
  setTestsError: (payload: string): SetTestsErrorAction => ({
    type: TestsActionType.SET_TESTS_ERROR,
    payload,
  }),
  setTestsIsLoading: (payload: boolean): SetTestsIsLoadingAction => ({
    type: TestsActionType.SET_TESTS_IS_LOADING,
    payload,
  }),
  setTests: (tests: ITest[]): SetTestsAction => ({
    type: TestsActionType.SET_TESTS,
    payload: tests,
  }),
  getTests: () => async (dispatch: AppDispatch) => {
    try {
      dispatch(TestsActionCreators.setTestsIsLoading(true));
      const response = await api.get<ITest[]>('/api/v1/tests');
      const tests = response.data;
      if (tests) {
        dispatch(TestsActionCreators.setTests(tests));
      } else {
        dispatch(TestsActionCreators.setTestsError('Тесты не найдены'));
      }
      dispatch(TestsActionCreators.setTestsIsLoading(false));
    } catch (e) {
      dispatch(TestsActionCreators.setTestsError('Произошла ошибка запроса'));
      dispatch(TestsActionCreators.setTestsIsLoading(false));
    }
  },
};
