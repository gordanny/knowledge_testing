import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Navbar from './components/Navbar';
import { useTypedSelector } from './hooks/useTypedSelector';
import Login from './pages/Login';
import Main from './pages/Main';

export interface IApplicationProps {}

export enum RouteNames {
  LOGIN = '/login',
  MAIN = '/',
  TEST = '/test/:testId',
  ALL = '*',
}

const Application: React.FunctionComponent<IApplicationProps> = () => {
  const { isAuth } = useTypedSelector(state => state.auth);
  return (
    <BrowserRouter>
      {isAuth && <Navbar />}
      <Routes>
        {isAuth && <Route path={RouteNames.ALL} element={<Main />} />}
        <Route path={RouteNames.ALL} element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Application;
