import React from 'react';
import { useEffect } from 'react';
import SettingsCategorie_Products from './SettingsCategories/SettingsCategorie_Products';
import SettingsCategorie_Reports from './SettingsCategories/SettingsCategories_Reports';

function SettingsPanel(){
    
  useEffect(()=>{
     let settingsPanel = document.getElementById("settingsPanel");
     settingsPanel?.addEventListener("hidden.bs.offcanvas",()=>{
        let sections = document.getElementsByClassName("settingsPanelSection");
        let indicators = document.getElementsByClassName("settingsPanelIndicators");

        Array.from(sections).forEach(section => section.classList.remove("show"));
        Array.from(indicators).forEach(indicator => indicator.classList.add("collapsed"));
   });
 },[]);

  return(
      <div className='offcanvas offcanvas-end' id="settingsPanel">
        <div className='offcanvas-header'>
          <h1 className='offcanvas-title'>Configuración</h1>
          <button type='button' className='btn-close text-reset' data-bs-dismiss="offcanvas"></button>
        </div>
        <div className='offcanvas-body'>
          <div className='acordion' id='settingsAcordion'>
              <SettingsCategorie_Products/>
              <SettingsCategorie_Reports/>
          </div>
        </div>
      </div>
  );
}

export default SettingsPanel;