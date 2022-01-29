import React, {useEffect, useContext} from 'react';
import axios from 'axios';
import ThreadList from './components/ThreadList.js'
import Auth from './components/Auth.js'
import './App.css';
import Store, { Context } from './store';


function App() {
  return (
    <Store>
      <Auth />
      <ThreadList />
    </Store>
  );
}

export default App;
