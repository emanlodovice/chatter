function parseJwt (token) {
  var base64Url = token.split('.')[1];
  var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
  var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));

  return JSON.parse(jsonPayload);
};


const Reducer = (state, action) => {
  switch (action.type) {
    case 'SET_TOKENS':
      const userInfo = {};
      if (action.payload.access) {
        userInfo.userId = parseJwt(action.payload.access)['user_id'];
      }
      return {
        ...state,
        ...userInfo,
        tokens: {
          ...state.tokens,
          ...action.payload
        }
      }
    case 'ADD_THREADS_AT_END':
      const existingIDs = {};
      state.threads.forEach(thread => {
        existingIDs[thread.uuid] = true
      });
      const newThreads = action.payload.threads.filter((thread) => (!existingIDs.hasOwnProperty(thread.uuid)));
      return {
        ...state,
        threads: [
          ...state.threads,
          ...newThreads,
        ]
      }
    default:
      return state
  }
};

export default Reducer;
