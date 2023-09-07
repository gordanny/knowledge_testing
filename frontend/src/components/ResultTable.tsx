import {
  Checkbox,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material';
import React from 'react';

import { useTypedSelector } from '../hooks/useTypedSelector';
import { ITestResultRow } from '../models/ITestResultRow';

export interface IResultTableProps {
  testResult: ITestResultRow[];
  isSuccess: boolean;
  testDescription: string;
}

const ResultTable: React.FunctionComponent<IResultTableProps> = ({
  testResult,
  isSuccess,
  testDescription,
}) => {
  const { user } = useTypedSelector(state => state.auth);
  return (
    <>
      <TableContainer
        component={Paper}
        style={{ marginBottom: '20px', width: '50%' }}
      >
        <Table size='small'>
          <TableBody>
            <TableRow>
              <TableCell>Название теста</TableCell>
              <TableCell>{testDescription}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>ФИО тестируемого</TableCell>
              <TableCell>{user.fio}</TableCell>
            </TableRow>
            <TableRow>
              <TableCell>Результат теста</TableCell>
              <TableCell>{isSuccess ? 'Пройден' : 'Не пройден'}</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </TableContainer>
      <TableContainer component={Paper}>
        <Table size='small'>
          <TableHead>
            <TableRow>
              <TableCell>№</TableCell>
              <TableCell>Формулировка вопроса</TableCell>
              <TableCell>Ответ тестируемого</TableCell>
              <TableCell>Правильный ответ</TableCell>
              <TableCell>Результат</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {testResult.map(row => (
              <TableRow
                key={row.questionNumber}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component='th' scope='row'>
                  {row.questionNumber}
                </TableCell>
                <TableCell>{row.questionDescription}</TableCell>
                <TableCell>{row.userAnswer}</TableCell>
                <TableCell>{row.rightAnswer}</TableCell>
                <TableCell>
                  <Checkbox disabled checked={row.isRight} />
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
};

export default ResultTable;
