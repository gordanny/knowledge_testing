import {
  Autocomplete,
  Button,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
} from '@mui/material';
import React, { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';

import api from '../api';
import { useTypedSelector } from '../hooks/useTypedSelector';
import { TestsActionCreators } from '../store/reducers/tests/action-creators';

import BasicStacking from './BasicStacking';

export interface IStatisticsProps {}

const Statistics: React.FunctionComponent<IStatisticsProps> = () => {
  const dispatch = useDispatch();
  const { tests } = useTypedSelector(state => state.tests);

  const [test, setTest] = useState(null);
  const [answersStats, setAnswersStats] = useState(null);
  const [participantsQty, setParticipantsQty] = useState(null);

  useEffect(() => {
    dispatch(TestsActionCreators.getTests());
  }, [dispatch]);

  const onClickHandler = async () => {
    try {
      const response = await api.get(`/api/v1/statistics/${test.id}`);
      setParticipantsQty(response.data.participantsQty);
      setAnswersStats(response.data.answersStats);
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <div
      style={{
        padding: '30px',
        display: 'flex',
        flexDirection: 'column',
        margin: '0 20%',
      }}
    >
      <Autocomplete
        options={tests.map(option => {
          return { label: option.description, id: option.id };
        })}
        renderInput={params => <TextField {...params} label='Тесты' />}
        value={test}
        onChange={(e, value) => setTest(value)}
        isOptionEqualToValue={(option, value) => option?.id === value?.id}
        noOptionsText={'Ничего не найдено'}
        getOptionLabel={option => option.label}
        style={{
          margin: '0 30%',
        }}
      />
      <Button onClick={onClickHandler}>Показать статистику</Button>
      {answersStats && (
        <>
          <TableContainer
            component={Paper}
            style={{ marginBottom: '20px', width: '50%' }}
          >
            <Table size='small'>
              <TableBody>
                <TableRow>
                  <TableCell>Название теста</TableCell>
                  <TableCell>{test.label}</TableCell>
                </TableRow>
                <TableRow>
                  <TableCell>Кол-во тестируемых</TableCell>
                  <TableCell>{participantsQty}</TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </TableContainer>
          <TableContainer component={Paper}>
            <Table size='small'>
              <TableHead>
                <TableRow>
                  <TableCell>№ вопроса</TableCell>
                  <TableCell>Правильно</TableCell>
                  <TableCell>Неправильно</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {answersStats?.map(row => (
                  <TableRow
                    key={row.questionNumber}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component='th' scope='row'>
                      {row.questionNumber}
                    </TableCell>
                    <TableCell>{row.rightAnswers}</TableCell>
                    <TableCell>{row.wrongAnswers}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
          <BasicStacking answersStats={answersStats} />
        </>
      )}
    </div>
  );
};

export default Statistics;
