import { Accordion, AccordionDetails, AccordionSummary } from '@mui/material';
import React, { useEffect } from 'react';
import { useDispatch } from 'react-redux';

import Test from '../components/Test';
import { useTypedSelector } from '../hooks/useTypedSelector';
import { TestsActionCreators } from '../store/reducers/tests/action-creators';

export interface IMainProps {}

function ExpandMoreIcon() {
  return null;
}

const Main: React.FunctionComponent<IMainProps> = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(TestsActionCreators.getTests());
  }, [dispatch]);
  const { tests } = useTypedSelector(state => state.tests);

  return (
    <div
      style={{
        padding: '30px',
        display: 'flex',
        flexDirection: 'column',
        margin: '0 20%',
      }}
    >
      {tests.map(test => {
        return (
          <Accordion key={test.id}>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <p style={{ fontWeight: 'bold', fontSize: '24px' }}>
                {test.description}
              </p>
            </AccordionSummary>
            <AccordionDetails>
              <Test
                questions={test.questions}
                testId={test.id}
                testDescription={test.description}
              />
            </AccordionDetails>
          </Accordion>
        );
      })}
    </div>
  );
};

export default Main;
