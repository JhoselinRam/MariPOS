import React, {useEffect, useState} from "react";

function SaleList(){
    const [height, setHeight] = useState(0);

    useEffect(() => {
        let offset = 24
        let navbarHeight  = document.getElementsByClassName("navbar")[0].clientHeight;
        let toolbarHeight = document.getElementsByClassName("toolbar")[0].clientHeight;
        let userHeight    = window.innerHeight;

        setHeight(userHeight-navbarHeight-toolbarHeight - offset);
    }, [])

    return (
        <div className="container-fluid ps-0 pe-0 pt-0 pb-2" style={{height:height}}>
            <ul className="list-group border border-1 border-dark rounded-1 h-100 ms-3 me-3 mt-3 bg-white">
                <li className="list-group-item list-group-item-action"> Venta 13-05-22/20-36</li>
                <li className="list-group-item list-group-item-action"> Venta 13-05-22/20-40</li>
                <li className="list-group-item list-group-item-action"> Venta 13-05-22/20-44</li>
            </ul>
        </div>
    );
}

export default SaleList;