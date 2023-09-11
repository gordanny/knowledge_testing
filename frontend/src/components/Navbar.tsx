import { Button, Grid } from '@mui/material';
import React from 'react';
import { useNavigate } from 'react-router-dom';

import { RouteNames } from '../enums/routes';

import Menu from './Menu';

export interface INavbarProps {}

const Navbar: React.FunctionComponent<INavbarProps> = () => {
  const navigate = useNavigate();
  const statisticsHandler = () => {
    navigate(RouteNames.STATISTICS);
  };

  const mainHandler = () => {
    navigate(RouteNames.MAIN);
  };

  return (
    <Grid
      container
      justifyContent={'space-between'}
      alignItems={'center'}
      style={{ backgroundColor: '#4a8cc7' }}
    >
      <Grid style={{ padding: '0 20px' }}>
        <Button
          onClick={mainHandler}
          style={{ color: 'white', margin: '0 20px' }}
        >
          Тесты
        </Button>
        <span style={{ color: 'white' }}>|</span>
        <Button
          onClick={statisticsHandler}
          style={{ color: 'white', margin: '0 20px' }}
        >
          Статистика
        </Button>
      </Grid>
      <Grid style={{ textAlign: 'right' }}>
        <Menu />
      </Grid>
    </Grid>
  );
};

export default Navbar;
