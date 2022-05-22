import React from 'react';
import logo from '../../assets/MariPos_logo.png';
import settings_icon from '../../assets/settings_icon.png';

function Navigation(){
    return (
      <>
        <nav className='navbar p-0 navbar-expand-sm navbar-dark bg-dark justify-content-between'>
        
          <span className='nav-brand ms-2'>
            <img src={logo} alt="MariPOS" />
          </span>
          <div className='navbar-nav'>
            <a href="#" className='nav-link h5'> Inicio</a>
            <a href="#" className='nav-link h5'>Venta</a>
          </div>

          <div className='navbar-nav'>
            <a href="#settingsPanel" data-bs-toggle="offcanvas" className='nav-link'>
              <img src={settings_icon} alt="Configuracion" style={{marginLeft:73}}/>
            </a>
          </div>
        </nav>

        <div className='offcanvas offcanvas-end' id="settingsPanel">
          <div className='offcanvas-header'>
            <h1 className='offcanvas-title'>Configuración</h1>
            <button type='button' className='btn-close text-reset' data-bs-dismiss="offcanvas"></button>
          </div>
          <div className='offcanvas-body'>
            <p>cosa 1</p>
            <p>cosa 2</p>
            <p>cosa 3</p>
            <p>cosa 1</p>
            <p>cosa 2</p>
            <p>cosa 3</p>
            <p>cosa 1</p>
            <p>cosa 2</p>
            <p>cosa 3</p>
            <p>cosa 1</p>
            <p>cosa 2</p>
            <p>cosa 3</p>
            <p>cosa 1</p>
            <p>cosa 2</p>
            <p>cosa 3</p>
            <p>cosa 1</p>
            <p>cosa 2</p>
            <p>cosa 3</p>
            <p>cosa 1</p>
            <p>cosa 2</p>
            <p>cosa 3</p>

          </div>
        </div>

      </>
    );
}

export default Navigation;