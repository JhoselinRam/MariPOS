import React, { useEffect } from "react";
import {SuplierItemsProps} from "../../../../../../interfaces/interfaces";

function SuplierListItem({item, onSelect, selected, userInputCheck} : SuplierItemsProps){

    useEffect(()=>{
        let input = document.getElementById("NewSuplierInput");
        input?.addEventListener("input",()=>{
            let input = document.getElementById("NewSuplierInput") as HTMLInputElement;
            userInputCheck(input.value.toLowerCase().replaceAll(" ",""));
        })
        input?.focus();
    },[]);

    return (
        <tr onClick={()=>onSelect(item["_id"]['$oid'])} className={item["_id"]['$oid']===selected?"table-info":""}>
            <td>{item["_id"]["$oid"]!=="new"?item["Descripcion"]:<input id="NewSuplierInput" className="form-control" type="text" autoComplete="off"/>}</td>
            <td>{item["_id"]["$oid"]!=="new"?item["RFC"]:<input id="NewRFCInput" className="form-control" type="text" autoComplete="off"/>}</td>
        </tr>
    );
}

export default SuplierListItem;