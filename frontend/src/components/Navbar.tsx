import { Grid } from '@mui/material';
import React from 'react';

import Menu from './Menu';

export interface INavbarProps {}

const Navbar: React.FunctionComponent<INavbarProps> = () => {
  return (
    <Grid
      container
      justifyContent={'end'}
      style={{ backgroundColor: '#4a8cc7' }}
    >
      <Menu />
    </Grid>
  );
};

export default Navbar;
