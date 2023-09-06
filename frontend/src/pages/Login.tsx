import {
  Backdrop,
  Button,
  Card,
  CircularProgress,
  Grid,
  TextField,
} from '@mui/material';
import React, { useState } from 'react';
import { useDispatch } from 'react-redux';

import { useTypedSelector } from '../hooks/useTypedSelector';
import { AuthActionCreators } from '../store/reducers/auth/action-creators';

export interface ILoginProps {}

const Login: React.FunctionComponent<ILoginProps> = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const dispatch = useDispatch();
  const { error, isLoading } = useTypedSelector(state => state.auth);

  const onClick = () => {
    dispatch(AuthActionCreators.login(username, password));
  };

  return (
    <Grid
      container
      justifyContent={'center'}
      alignItems={'center'}
      direction={'column'}
      sx={{ minHeight: '100vh' }}
    >
      <Backdrop style={{ zIndex: 100 }} open={isLoading}>
        <CircularProgress color='primary' />
      </Backdrop>
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
          {error && <div style={{ color: 'red' }}>{error}</div>}
          <Button onClick={onClick}>Войти</Button>
        </Grid>
      </Card>
    </Grid>
  );
};

export default Login;
