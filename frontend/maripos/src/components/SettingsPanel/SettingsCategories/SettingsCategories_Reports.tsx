import React from 'react'

function SettingsCategorie_Reports(){
    return (
        <div className='accordion-item border-0'>
            <h3 className='accordion-header'>
                <button className='accordion-button collapsed settingsPanelIndicators' type='button' data-bs-toggle='collapse' data-bs-target='#ReportsCollapse'>
                    Reportes
                </button>
            </h3>
            <div className='accordion-collapse collapse settingsPanelSection' id='ReportsCollapse' data-bs-parent='#settingsAcordion'>
                <div className='accordion-body ps-0 pe-0'>
                    <div className='list-group list-group-flush'>
                        <a className='list-group-item list-group-item-action' role='button'>Monitor de venta</a>
                        <a className='list-group-item list-group-item-action' role='button'>Ventas</a>
                        <a className='list-group-item list-group-item-action' role='button'>Descuentos</a>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default SettingsCategorie_Reports;