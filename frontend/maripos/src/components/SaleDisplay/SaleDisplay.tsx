import React, {useState, useEffect} from "react";

function SaleDisplay(){
    const [height, setHeight] = useState(0);

    useEffect(() => {
        let offset = 100
        let navbarHeight  = document.getElementsByClassName("navbar")[0].clientHeight;
        let toolbarHeight = document.getElementsByClassName("toolbar")[0].clientHeight;
        let userHeight    = window.innerHeight;

        setHeight(userHeight-navbarHeight-toolbarHeight - offset);
    }, [])

    return (
        <div className="container-fluid p-0" style={{height:height}}>
            <div className="table-responsive border border-1 border-dark rounded-1 h-100 mt-3 ps-2 pe-2 bg-white">
                <table className="table table-sm table-hover table-striped">
                    <thead>
                        <tr>
                            <th>Artículo</th>
                            <th>Cantidad</th>
                            <th>Precio</th>
                            <th>Descuento</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Jamon Andalucia de Pavo</td>
                            <td>0.75</td>
                            <td>$95.0</td>
                            <td>0</td>
                            <td>$71.25</td>
                        </tr>
                        <tr>
                            <td>Queso Oaxaca</td>
                            <td>0.5</td>
                            <td>$135.0</td>
                            <td>0</td>
                            <td>$67.5</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    );

}

export default SaleDisplay;