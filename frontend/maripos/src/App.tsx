import React from 'react';
import Navigation from './components/Navigation/Navigation';
import MainSaleWindow from './components/MainSaleWindow/MainSaleWindow';
import SettingsOption_Supliers from './components/SettingsPanel/SettingsCategories/Products/Options/Supliers/SettingsOption_Supliers';

function App() {
  return (
    <div className='container-fluid p-0' style={{backgroundColor:"#dedede"}}>
      <Navigation/>
      <MainSaleWindow/>

      <SettingsOption_Supliers/>
    </div>
  );
}

export default App;