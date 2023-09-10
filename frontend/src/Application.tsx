import { Backdrop, CircularProgress, Grid } from '@mui/material';
import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import PrivateRoutes from './components/PrivateRoutes';
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
    } else {
      dispatch(AuthActionCreators.setIsAuth(false));
    }
  }, [dispatch]);

  if (isAuth === undefined) {
    return (
      <Grid
        container
        justifyContent={'center'}
        alignItems={'center'}
        direction={'column'}
        sx={{ minHeight: '100vh' }}
      >
        <Backdrop style={{ zIndex: 100 }} open={true}>
          <CircularProgress color='primary' />
        </Backdrop>
      </Grid>
    );
  }

  return (
    <BrowserRouter>
      <Routes>
        <Route element={<PrivateRoutes />}>
          <Route path={RouteNames.MAIN} element={<Main />} />
        </Route>
        <Route path={RouteNames.REGISTRATION} element={<Registration />} />
        <Route path={RouteNames.LOGIN} element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Application;
