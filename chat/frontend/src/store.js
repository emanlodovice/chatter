import React, { createContext, useReducer, useMemo } from "react";
import Reducer from "./reducer";


const initialState = {
  tokens: {
    access: null,
    refresh: null,
  },
  userId: null,
  threads: [],
  nextThreadListUrl: null,
};

export const GlobalContext = createContext(initialState);

const GlobalStore = ({children}) => {
  const [state, dispatch] = useReducer(Reducer, initialState);
  const store = useMemo(() => ({state, dispatch}), [state]);
  return (
    <GlobalContext.Provider value={store}>
      {children}
    </GlobalContext.Provider>
  );
};

export default GlobalStore;