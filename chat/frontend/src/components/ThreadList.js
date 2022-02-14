import React, {useContext, useEffect, useState, useRef} from 'react';
import Avatar from './Avatar.js';
import SearchForm from './SearchForm.js';
import ThreadListItem from './ThreadListItem.js';
import { GlobalContext } from './../store';
import { baseURL } from './../constants';
import axios from 'axios';
import './ThreadList.css';

function ThreadList() {
  const store = useContext(GlobalContext);
  const [fetchLock, setFetchLock] = useState(false);

  const fetchThreads = (url) => {
    if (fetchLock) {
      return;
    }
    setFetchLock(true);
    url = url || `${baseURL}/rooms`;
    axios.get(url, {
      headers: {
        Authorization: `Bearer ${store.state.tokens.access}`
      }
    })
      .then(response => {
        const threads = response.data.results;
        store.dispatch({type: 'ADD_THREADS_AT_END', payload: {threads: threads}});
        store.dispatch({type: 'SET_NEXT_THREAD_LIST_URL', payload: response.data.next});
        setFetchLock(false);
      });
  }

  let prevY = 0;

  const observer = new IntersectionObserver(
    (entities, observer) => {
      const y = entities[0].boundingClientRect.y;
      if (prevY > y && store.state.nextThreadListUrl) {
        fetchThreads(store.state.nextThreadListUrl);
      }
      prevY = y;
    },
    {
      root: null,
      rootMargin: "0px",
      threshold: 1.0
    }
  );

  const loadingRef = useRef(null);
  useEffect(() => {
    if (!store.state.threads.length && store.state.tokens.access) {
      fetchThreads();
    }
    if (loadingRef.current && store.state.nextThreadListUrl) {
      observer.observe(loadingRef.current);
    }
    return function cleanup() {
      if (loadingRef.current) {
        observer.unobserve(loadingRef.current);
      }
    };
  });

  const user = {
    avatar: 'https://avatars.githubusercontent.com/u/3273867?v=4',
    username: 'emanlodovice'
  }
  const loadingTextCSS = { display: fetchLock ? "block" : "none" };
  return (
    <div>
      {store.state.tokens.access &&
        <div className="thread-list">
          <div className="flex items-center">
            <Avatar user={user} />
            <h1 className="text-2xl font-bold ml-3">{user.username}</h1>
          </div>
          <SearchForm />
          <div className="items pt-2" >
            {store.state.threads.map(function(thread, index){
              return <ThreadListItem thread={thread} key={index}/>
            })}
          </div>
          <div
            ref={loadingRef}
          >
            <span style={loadingTextCSS}>Loading...</span>
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
