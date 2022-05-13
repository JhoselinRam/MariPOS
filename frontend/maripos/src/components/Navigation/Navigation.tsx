import React from 'react'
import logo from '../../assets/MariPos_logo.png'
import settings_icon from '../../assets/settings_icon.png'

function Navigation(){
    return (
        <nav className='navbar navbar-expand-sm navbar-dark bg-dark justify-content-between'>
        
          <span className='nav-brand ms-2'>
            <img src={logo} alt="MariPOS" />
          </span>
          <div className='navbar-nav'>
            <a href="#" className='nav-link h5'> Inicio</a>
            <a href="#" className='nav-link h5'>Venta</a>
          </div>

          <div className='navbar-nav'>
            <a href="#" className='nav-link'>
              <img src={settings_icon} alt="Configuracion" style={{marginLeft:73}}/>
            </a>
          </div>
      </nav>
    );
}

export default Navigation;