import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

import { useTypedSelector } from '../hooks/useTypedSelector';

import Navbar from './Navbar';

export interface IPrivateRoutesProps {}

const PrivateRoutes: React.FunctionComponent<IPrivateRoutesProps> = () => {
  const { isAuth } = useTypedSelector(state => state.auth);

  if (isAuth) {
    return (
      <div>
        <Navbar />
        <Outlet />
      </div>
    );
  } else {
    return <Navigate to='/login' />;
  }
};

export default PrivateRoutes;
