import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Navbar from './components/Navbar';
import { RouteNames } from './enums/routes';
import { useTypedSelector } from './hooks/useTypedSelector';
import Login from './pages/Login';
import Main from './pages/Main';
import Registration from './pages/Registration';
import { AuthActionCreators } from './store/reducers/auth/action-creators';

export interface IApplicationProps {}

const Application: React.FunctionComponent<IApplicationProps> = () => {
  const { isAuth } = useTypedSelector(state => state.auth);
  const dispatch = useDispatch();

  useEffect(() => {
    if (localStorage.getItem('token')) {
      dispatch(AuthActionCreators.check_auth());
    }
  }, [dispatch]);

  return (
    <BrowserRouter>
      {isAuth && <Navbar />}
      <Routes>
        {isAuth && <Route path={RouteNames.ALL} element={<Main />} />}
        <Route path={RouteNames.REGISTRATION} element={<Registration />} />
        <Route path={RouteNames.ALL} element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Application;
