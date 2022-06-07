import React from "react";
import {SuplierItemsProps} from "../../../../../../interfaces/interfaces";

function SuplierListItem({item, onSelect, selected} : SuplierItemsProps){

    return (
        <tr key={item["_id"]['$oid']} onClick={()=>onSelect(item["_id"]['$oid'])} className={item["_id"]['$oid']===selected?"table-info":""}>
            <td>{item["Descripcion"]}</td>
            <td>{item["RFC"]}</td>
        </tr>
    );
}

export default SuplierListItem;