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
  testDescription: string;
}

const Test: React.FunctionComponent<ITestProps> = ({
  testId,
  questions,
  testDescription,
}) => {
  const { user } = useTypedSelector(state => state.auth);
  const [results, setResults] = React.useState({});
  const [modalOpen, setModalOpen] = React.useState(false);
  const [isSuccess, setIsSuccess] = React.useState(undefined);
  const [rightAnswersPercent, setRightAnswersPercent] = React.useState(0);
  const [testResult, setTestResult] = React.useState([]);

  const handleChange = (
    event: React.ChangeEvent<HTMLInputElement>,
    questionId: number,
    questionNumber: number
  ) => {
    setResults({
      ...results,
      [questionNumber]: {
        questionId: questionId,
        answerId: (event.target as HTMLInputElement).value,
      },
    });
  };
  const handleClick = async () => {
    const response = await axios.post<IResult>('/api/v1/attempts/add', {
      username: user.username ?? 'admin',
      testId: testId,
      userAnswers: Object.keys(results).map(key => {
        return results[key];
      }),
    });
    setTestResult(
      response.data.rightAnswers.map(rightAnswer => {
        const userAnswer = results[rightAnswer.questionNumber].answerId;
        const question = questions?.find(
          q => q.questionNumber === rightAnswer.questionNumber
        );
        return {
          questionNumber: rightAnswer.questionNumber,
          questionDescription: question.description,
          userAnswer: question.answers.find(a => a.id == userAnswer).text,
          rightAnswer: rightAnswer.answer,
          isRight: userAnswer === rightAnswer.answer,
        };
      })
    );
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
                  value={results[question.questionNumber]?.answerId ?? ''}
                  onChange={e =>
                    handleChange(e, question.id, question.questionNumber)
                  }
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
        testResult={testResult}
        testDescription={testDescription}
      />
    </>
  );
};

export default Test;
