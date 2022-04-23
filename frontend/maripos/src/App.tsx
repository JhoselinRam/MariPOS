import React from 'react';

function App() {

  if(localStorage.getItem("test")==null){
    checkUsers();
  }

  return (
    <>
      <h1>Program starts here</h1>
    </>
  );
}


function checkUsers(){
  const API = process.env.REACT_APP_BACKEND;
  console.log(API);
}


export default App;
