> eslint for react hooks

```JavaScript
//https://github.com/pkellner/pluralsight-course-using-react-hooks/blob/master/03-More-React-Hooks-useContext-useReducer-useCallback-useMemo/clip02-React-Hooks-eslint-and-Usage/package.json

/*
How to add eslint to detect hooks syntax error:
Using React 17 Hooks - Ch3 - clip2
*/

  "devDependencies": {
    "eslint": "^7.22.0",
    "eslint-plugin-react": "^7.23.1",
    "eslint-plugin-react-hooks": "^4.2.0",
    "prettier": "2.2.1"
  }
```

> useContext
```
# setup from the top level
* https://github.com/pkellner/pluralsight-course-using-react-hooks/blob/master/03-More-React-Hooks-useContext-useReducer-useCallback-useMemo/clip06-Using-useContext-for-Global-Config/src/App.js

import React from 'react';
import Home from './Home';
import Speakers from './Speakers';

export const ConfigContext = React.createContext(); //create context

const pageToShow = (pageName) => {
  if (pageName === 'Home') return <Home />;
  if (pageName === 'Speakers') return <Speakers />;
  return <div>Not Found</div>;
};

const configValue = { //the default values of context
  showSpeakerSpeakingDays: true,
  showSignMeUp: false,
};

const App = ({ pageName }) => {
  return (
    <ConfigContext.Provider value={configValue}> //setup context for children
      <div>{pageToShow(pageName)}</div>
    </ConfigContext.Provider>
  );
};

export default App;
```