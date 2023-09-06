import {
  Button,
  Divider,
  FormControl,
  FormControlLabel,
  FormLabel,
  Radio,
  RadioGroup,
} from '@mui/material';
import axios from 'axios';
import React from 'react';

import { useTypedSelector } from '../hooks/useTypedSelector';
import { IQuestion } from '../models/IQuestion';
import { IResult } from '../models/IResult';

import TestResultModal from './TestResultModal';

export interface ITestProps {
  testId: number;
  questions?: IQuestion[];
}

const Test: React.FunctionComponent<ITestProps> = ({ testId, questions }) => {
  const { user } = useTypedSelector(state => state.auth);
  const [results, setResults] = React.useState({});
  const [modalOpen, setModalOpen] = React.useState(false);
  const [isSuccess, setIsSuccess] = React.useState(undefined);
  const [rightAnswersPercent, setRightAnswersPercent] = React.useState(0);

  const handleChange = (
    event: React.ChangeEvent<HTMLInputElement>,
    questionId: number
  ) => {
    setResults({
      ...results,
      [questionId]: (event.target as HTMLInputElement).value,
    });
  };

  const handleClick = async () => {
    const response = await axios.post<IResult>('/api/v1/attempts/add', {
      username: user.username ?? 'admin',
      testId: testId,
      userAnswers: Object.keys(results).map(key => {
        return {
          questionId: key,
          answerId: results[key],
        };
      }),
    });
    setIsSuccess(response.data.isSuccess);
    setRightAnswersPercent(response.data.percent);
    setResults({});
    setModalOpen(true);
  };
  return (
    <>
      <div>
        {questions?.map(question => {
          return (
            <div key={question.id}>
              <Divider />
              <FormControl style={{ padding: '20px' }}>
                <FormLabel style={{ fontStyle: 'italic' }}>
                  {question.description}
                </FormLabel>
                <RadioGroup
                  value={results[question.id] ?? ''}
                  onChange={e => handleChange(e, question.id)}
                  row
                >
                  {question.answers.map(answer => {
                    return (
                      <FormControlLabel
                        key={answer.id}
                        value={answer.id}
                        control={<Radio />}
                        label={answer.text}
                      />
                    );
                  })}
                </RadioGroup>
              </FormControl>
            </div>
          );
        })}
      </div>
      {questions?.length === Object.keys(results).length && (
        <div style={{ margin: 'auto', width: '150px' }}>
          <Button variant='contained' color='success' onClick={handleClick}>
            Отправить
          </Button>
        </div>
      )}
      <TestResultModal
        open={modalOpen}
        setOpen={setModalOpen}
        isSuccess={isSuccess}
        rightAnswersPercent={rightAnswersPercent}
      />
    </>
  );
};

export default Test;
