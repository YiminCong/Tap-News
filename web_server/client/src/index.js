import ReactDom from 'react-dom';
import React from 'react';

import { browserHistory, Router } from 'react-router';
import routes from './routes';

ReactDom.render(
  <Router history={browserHistory} routes={routes} />,
  document.getElementById('root')
);