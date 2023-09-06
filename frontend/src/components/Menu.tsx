import Button from '@mui/material/Button';
import React from 'react';
import { useDispatch } from 'react-redux';

import { useTypedSelector } from '../hooks/useTypedSelector';
import { AuthActionCreators } from '../store/reducers/auth/action-creators';

export interface IBasicMenuProps {}

const BasicMenu: React.FunctionComponent<IBasicMenuProps> = () => {
  const { user } = useTypedSelector(state => state.auth);
  const dispatch = useDispatch();

  return (
    <div>
      <Button
        onClick={() => dispatch(AuthActionCreators.logout())}
        style={{ color: 'white' }}
      >
        {user.username}
      </Button>
    </div>
  );
};

export default BasicMenu;
