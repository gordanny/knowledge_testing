import { Box, Modal, Typography } from '@mui/material';
import React from 'react';

export interface ITestResultModalProps {
  open: boolean;
  setOpen: React.Dispatch<React.SetStateAction<boolean>>;
  isSuccess: boolean;
  rightAnswersPercent: number;
}

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
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
}) => {
  const handleClose = () => setOpen(false);
  const bgColor = isSuccess ? 'green' : 'red';

  return (
    <div>
      <Modal open={open} onClose={handleClose}>
        <Box sx={style} style={{ backgroundColor: bgColor }}>
          <Typography variant='h6' component='h2'>
            {isSuccess}
            {`Вы ответили правильно на ${rightAnswersPercent}% вопросов`}
          </Typography>
        </Box>
      </Modal>
    </div>
  );
};

export default TestResultModal;
