import React, {useEffect, useContext} from 'react';
import axios from 'axios';
import { GlobalContext } from './../store';
import { baseURL } from './../constants';


function updateJWT(store, refreshToken) {
  axios.post(`${baseURL}/refresh-token`, { refresh: refreshToken })
    .then(response => {
      const accessToken = response.data.access;
      let refresh = refreshToken;
      if (response.data.refresh) {
        refresh = response.data.refresh;
      }
      store.dispatch({type: 'SET_TOKENS', payload: {access: accessToken, refresh: refresh}});
    });
}

function Auth() {
  const store = useContext(GlobalContext);

  const urlParams = new URLSearchParams(window.location.search);
  let refreshToken = urlParams.get('refresh');

  useEffect(() => {
    if (store.state.tokens.access) {
      return;
    }
    const token = store.state.tokens.refresh || refreshToken;
    updateJWT(store, token);
    setTimeout(() => {
      store.dispatch({type: 'SET_TOKENS', payload: {access: null}});
    }, 60000)
  });

  return (
    <div/>
  );
}

export default Auth;
