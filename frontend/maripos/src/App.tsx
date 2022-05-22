import React from 'react';
import Navigation from './components/Navigation/Navigation';
import MainSaleWindow from './components/MainSaleWindow/MainSaleWindow';

function App() {
  return (
    <div className='container-fluid p-0' style={{backgroundColor:"#ededed"}}>
      <Navigation/>
      <MainSaleWindow/>
    </div>
  );
}

export default App;