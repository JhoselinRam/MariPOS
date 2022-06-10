import React, { useEffect } from "react";
import {SuplierItemsProps} from "../../../../../../interfaces/interfaces";

function SuplierListItem({item, onSelect, selected, userInputCheck, action} : SuplierItemsProps){

    function setInputEventListener(){
        let input = document.getElementById("NewSuplierInput") as HTMLInputElement;
        let rfc = document.getElementById("NewRFCInput") as HTMLInputElement;
        userInputCheck(input.value.toLowerCase().replaceAll(" ",""), rfc.value.toLowerCase().replaceAll(" ",""));
    }
    
    useEffect(()=>{
        let input = document.getElementById("NewSuplierInput");
        let rfc = document.getElementById("NewRFCInput"); 

        input?.addEventListener("input",setInputEventListener);
        rfc?.addEventListener("input",setInputEventListener);

        input?.focus();
    },[action]);

    function renderSuplierInput(){
        if (item["_id"]["$oid"]==="new")
            return <input id="NewSuplierInput" className="form-control" type="text" autoComplete="off"/>;
        if(action===`${process.env.REACT_APP_ACTIONS_MODIFY_SUPLIER}` && item["_id"]["$oid"]===selected)
            return <input id="NewSuplierInput" className="form-control" type="text" autoComplete="off" defaultValue={item["Descripcion"]}/>;
        
        return item["Descripcion"];
    }

    function renderRFCInput(){
        if (item["_id"]["$oid"]==="new")
            return <input id="NewRFCInput" className="form-control" type="text" autoComplete="off"/>;
        if(action===`${process.env.REACT_APP_ACTIONS_MODIFY_SUPLIER}` && item["_id"]["$oid"]===selected)
            return <input id="NewRFCInput" className="form-control" type="text" autoComplete="off" defaultValue={item["RFC"]}/>;
        
        return item["RFC"];
    }

    return (
        <tr onClick={()=>onSelect(item["_id"]['$oid'])} className={item["_id"]['$oid']===selected && action!==`${process.env.REACT_APP_ACTIONS_MODIFY_SUPLIER}`?"table-info":""}>
            <td>{renderSuplierInput()}</td>
            <td>{renderRFCInput()}</td>
        </tr>
    );
}

export default SuplierListItem;