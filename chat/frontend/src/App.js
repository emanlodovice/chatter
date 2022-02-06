import React from 'react';
import ThreadList from './components/ThreadList.js'
import Auth from './components/Auth.js'
import './App.css';
import Store from './store';


function App() {
  return (
    <Store>
      <Auth />
      <ThreadList />
    </Store>
  );
}

export default App;
