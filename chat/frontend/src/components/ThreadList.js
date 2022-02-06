import React, {useContext, useEffect} from 'react';
import Avatar from './Avatar.js';
import SearchForm from './SearchForm.js';
import ThreadListItem from './ThreadListItem.js';
import { GlobalContext } from './../store';
import { baseURL } from './../constants';
import axios from 'axios';
import './ThreadList.css';

function ThreadList() {
  const store = useContext(GlobalContext);

  useEffect(() => {
    if (!store.state.threads.length && store.state.tokens.access) {
      axios.get(`${baseURL}/rooms`, {
        headers: {
          Authorization: `Bearer ${store.state.tokens.access}`
        }
      })
        .then(response => {
          const threads = response.data.results;
          store.dispatch({type: 'ADD_THREADS_AT_END', payload: {threads: threads}});
        });
    }
  });

  const user = {
    avatar: 'https://avatars.githubusercontent.com/u/3273867?v=4',
    username: 'emanlodovice'
  }
  return (
    <div>
      {store.state.tokens.access &&
        <div className="thread-list">
          <div className="flex items-center">
            <Avatar user={user} />
            <h1 className="text-2xl font-bold ml-3">{user.username}</h1>
          </div>
          <SearchForm />
          <div className="items pt-2">
            {store.state.threads.map(function(thread, index){
              return <ThreadListItem thread={thread} key={index}/>
            })}
          </div>
        </div>
      }
      {!store.state.tokens.access &&
        <p>Please authenticaticate</p>
      }
    </div>
  );
}

export default ThreadList;
