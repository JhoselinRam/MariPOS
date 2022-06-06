import React from 'react'

function SettingsCategorie_Products(){

    function launchProductsPanel(id:string){
        let closeSettingsPanel = document.getElementById("closeSettingsPanel");
        let panel = document.getElementById(id);
        let panelButton = panel?.getElementsByTagName("button")[0];

        closeSettingsPanel?.click()
        setTimeout(()=>{
            if(panelButton!=undefined)
                panelButton.click()
        }, 250);
    }

    return (
        <div className='accordion-item border-0'>
            <h3 className='accordion-header'>
                <button className='accordion-button collapsed settingsPanelIndicators' type='button' data-bs-toggle='collapse' data-bs-target='#ProductsCollapse'>
                    Productos
                </button>
            </h3>
            <div className='accordion-collapse collapse settingsPanelSection' id='ProductsCollapse' data-bs-parent='#settingsAcordion'>
                <div className='accordion-body ps-0 pe-0'>
                    <ul className='list-group list-group-flush'>
                        <li className='list-group-item list-group-item-action' role='button'>Insumos</li>
                        <li className='list-group-item list-group-item-action' role='button'>Productos</li>
                        <li className='list-group-item list-group-item-action' role='button' onClick={()=>launchProductsPanel("SupliersPanel")}>Proovedores</li>
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default SettingsCategorie_Products;