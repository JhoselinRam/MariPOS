import React, {useState, useEffect} from 'react';
import Toolbar from '../Toolbar/Toolbar';
import SaleDisplay from '../SaleDisplay/SaleDisplay';
import SaleList from '../SaleList/SaleList';
import TotalDisplay from '../TotalDispaly/TotalDisplay';

function MainSaleWindow(){
    return (
        <div className='container-fluid pt-1 ps-2 pe-0'>
            <Toolbar/>

            <div className='container-fluid'>
                <div className='row'>
                    <div className='col-sm-9 p-0'>
                        <SaleDisplay/>
                        <TotalDisplay/>
                    </div>

                    <div className='col-sm-3 p-0'>
                        <SaleList/>
                    </div>
                </div>
            </div>
            
        </div>
    );
}

export default MainSaleWindow;