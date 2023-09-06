import { IQuestion } from './IQuestion';

export interface ITest {
  id: number;
  description: string;
  questions: IQuestion[];
}
