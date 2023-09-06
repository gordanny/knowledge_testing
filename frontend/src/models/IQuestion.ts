import { IAnswer } from './IAnswer';

export interface IQuestion {
  id: number;
  description: string;
  questionNumber: number;
  answers: IAnswer[];
}
