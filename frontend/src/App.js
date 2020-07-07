import React from 'react';
import newsFetch from './services/newsFetch'
import './App.css';

function App() {

  newsFetch()
    .then(fuck => console.log(fuck))

  return (
    <div className="App">
      <header className="App-header">
        <p>
          <code>WGDash</code>
        </p>
      </header>
    </div>
  );
}

export default App;
