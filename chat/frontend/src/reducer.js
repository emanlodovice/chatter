const Reducer = (state, action) => {
  switch (action.type) {
    case 'SET_TOKENS':
      return {
        ...state,
        tokens: {
          ...state.tokens,
          ...action.payload
        }
      }
    default:
      return state
  }
};

export default Reducer;
