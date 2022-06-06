import React from "react";

function TotalDisplay(){
    return (
        <div className="container-fluid">
            <div className="row">
                <div className="col-4 pt-2">
                    <div className="row">
                        <div className="col-4">Total:</div>
                        <div className="col-8">$138.75</div>
                    </div>
                    <div className="row">
                        <div className="col-4">Descuento:</div>
                        <div className="col-8">$0</div>
                    </div>
                </div>
                <div className="col-8 display-4 text-end">TOTAL: $138.75</div>
            </div>
        </div>
    );
}

export default TotalDisplay;