import { Box, Modal, Typography } from '@mui/material';
import React from 'react';

import { ITestResultRow } from '../models/ITestResultRow';

import ResultTable from './ResultTable';

export interface ITestResultModalProps {
  open: boolean;
  setOpen: React.Dispatch<React.SetStateAction<boolean>>;
  testResult: ITestResultRow[];
  isSuccess: boolean;
  rightAnswersPercent: number;
  testDescription: string;
}

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

const TestResultModal: React.FunctionComponent<ITestResultModalProps> = ({
  open,
  setOpen,
  isSuccess,
  rightAnswersPercent,
  testResult,
  testDescription,
}) => {
  const handleClose = () => setOpen(false);

  return (
    <div>
      <Modal open={open} onClose={handleClose}>
        <Box sx={style}>
          <ResultTable
            testResult={testResult}
            isSuccess={isSuccess}
            testDescription={testDescription}
          />
          <Typography
            variant='h6'
            component='h2'
            style={{ paddingTop: '10px' }}
          >
            {`Вы ответили правильно на ${rightAnswersPercent}% вопросов`}
          </Typography>
        </Box>
      </Modal>
    </div>
  );
};

export default TestResultModal;
