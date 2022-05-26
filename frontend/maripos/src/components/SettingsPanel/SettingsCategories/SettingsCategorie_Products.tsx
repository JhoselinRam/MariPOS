import React from 'react'
import SettingsOption_Supliers from './SettingsOptions/SettingsOption_Supliers';

function SettingsCategorie_Products(){
    return (
        <>
            <div className='accordion-item border-0'>
                <h3 className='accordion-header'>
                    <button className='accordion-button collapsed settingsPanelIndicators' type='button' data-bs-toggle='collapse' data-bs-target='#ProductsCollapse'>
                        Productos
                    </button>
                </h3>
                <div className='accordion-collapse collapse settingsPanelSection' id='ProductsCollapse' data-bs-parent='#settingsAcordion'>
                    <div className='accordion-body ps-0 pe-0'>
                        <div className='list-group list-group-flush'>
                            <a className='list-group-item list-group-item-action' role='button'>Insumos</a>
                            <a className='list-group-item list-group-item-action' role='button'>Productos</a>
                            <a className='list-group-item list-group-item-action' role='button' href='#SupliersPanel' data-bs-toggle='modal'>Proovedores</a>
                        </div>
                    </div>
                </div>
            </div>

            <SettingsOption_Supliers/>
        </>
    );
}

export default SettingsCategorie_Products;