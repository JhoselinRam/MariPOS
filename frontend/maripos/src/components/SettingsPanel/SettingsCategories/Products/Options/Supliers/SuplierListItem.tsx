import React from "react";
import {SuplierItemsProps} from "../../../../../../interfaces/interfaces";

function SuplierListItem({item, onSelect, selected} : SuplierItemsProps){

    return (
        <tr onClick={()=>onSelect(item["_id"]['$oid'])} className={item["_id"]['$oid']===selected?"table-info":""}>
            <td>{item["set"]===true?item["Descripcion"]:<input id="NewSuplierInput" className="form-control" type="text"/>}</td>
            <td>{item["set"]===true?item["RFC"]:<input id="NewRFCInput" className="form-control" type="text"/>}</td>
        </tr>
    );
}

export default SuplierListItem;