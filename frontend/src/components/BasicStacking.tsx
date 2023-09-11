import { BarChart } from '@mui/x-charts';
import React from 'react';

export interface IBasicStackingProps {
  answersStats: any;
}

const BasicStacking: React.FunctionComponent<IBasicStackingProps> = ({
  answersStats,
}) => {
  const ra = answersStats?.map(question => question.rightAnswers);
  const wa = answersStats?.map(question => question.wrongAnswers);

  const series = [
    {
      ...{
        data: ra,
        label: 'Правильно',
        color: '#4a8cc7',
      },
      stack: 'total',
    },
    {
      ...{
        data: wa,
        label: 'Неправильно',
        color: '#e15759',
      },
      stack: 'total',
    },
  ];
  return (
    <div
      style={{
        padding: '30px',
        display: 'flex',
        flexDirection: 'column',
        margin: '0 20%',
      }}
    >
      <BarChart
        width={600}
        height={300}
        series={series}
        sx={{ '--ChartsLegend-rootSpacing': '40px' }}
      />
    </div>
  );
};

export default BasicStacking;
