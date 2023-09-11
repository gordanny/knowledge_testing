import { Button, Card, Grid, TextField } from '@mui/material';
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { Navigate, useNavigate } from 'react-router-dom';

import { RouteNames } from '../enums/routes';
import { useTypedSelector } from '../hooks/useTypedSelector';
import AuthService from '../services/AuthService';
import { AuthActionCreators } from '../store/reducers/auth/action-creators';

export interface IRegistrationProps {}

const Registration: React.FunctionComponent<IRegistrationProps> = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const { isAuth } = useTypedSelector(state => state.auth);

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const [fio, setFio] = useState('');
  const [error, setError] = useState('');

  if (isAuth) {
    return <Navigate to={RouteNames.MAIN} />;
  }

  const validatePassword = (password: string, repeatPassword: string) => {
    return password === repeatPassword;
  };

  const registrationHandler = async () => {
    if (validatePassword(password, repeatPassword)) {
      try {
        await AuthService.registration(username, password, fio);
        dispatch(AuthActionCreators.login(username, password));
      } catch (e) {
        setError(e.response?.data?.message);
      }
    }
  };

  const loginHandler = () => {
    navigate(RouteNames.LOGIN);
  };

  return (
    <Grid
      container
      justifyContent={'center'}
      alignItems={'center'}
      direction={'column'}
      sx={{ minHeight: '100vh' }}
    >
      <Card variant='outlined' sx={{ padding: '20px' }}>
        <Grid
          container
          justifyContent={'center'}
          alignItems={'center'}
          direction={'column'}
        >
          <TextField
            margin={'normal'}
            required
            label='Имя пользователя'
            autoComplete='username'
            value={username}
            onChange={event => setUsername(event.target.value)}
          />
          <TextField
            margin={'normal'}
            required
            label='Пароль'
            type='password'
            autoComplete='current-password'
            value={password}
            onChange={event => setPassword(event.target.value)}
          />
          <TextField
            margin={'normal'}
            required
            label='Пароль ещё раз'
            type='password'
            value={repeatPassword}
            onChange={event => setRepeatPassword(event.target.value)}
          />
          <TextField
            margin={'normal'}
            required
            label='ФИО'
            value={fio}
            onChange={event => setFio(event.target.value)}
          />
          {error && <div style={{ color: 'red' }}>{error}</div>}
          <Button onClick={registrationHandler}>Зарегистрироваться</Button>
          <Button onClick={loginHandler}>Войти</Button>
        </Grid>
      </Card>
    </Grid>
  );
};

export default Registration;
