import { IRightAnswer } from './IRigthAnswer';

export interface IResult {
  isSuccess: boolean;
  percent: number;
  rightAnswers: IRightAnswer[];
}
