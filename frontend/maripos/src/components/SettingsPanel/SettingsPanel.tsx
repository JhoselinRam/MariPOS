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
          <button type='button' id='closeSettingsPanel' className='btn-close mt-1' data-bs-dismiss="offcanvas" style={{background: `url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='M.293.293a1 1 0 011.414 0L8 6.586 14.293.293a1 1 0 111.414 1.414L9.414 8l6.293 6.293a1 1 0 01-1.414 1.414L8 9.414l-6.293 6.293a1 1 0 01-1.414-1.414L6.586 8 .293 1.707a1 1 0 010-1.414z'/%3e%3c/svg%3e") center/1em auto no-repeat`}}></button>
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