import React, { useState, useEffect } from "react";
import {SupliersList, SubmitPasswordResponse} from "../../../../../../interfaces/interfaces";
import SuplierListItem from "./SuplierListItem";
import SubmitPassword from "../../../../../SubmitPassword/SubmitPassword";
import EditSuplier from "./EditSuplier";

function SettingsOption_Supliers(){
    const [list, setList] = useState<SupliersList[]>([]);
    const [itemSelected, setItemSelected] = useState("");
    const [passwordId, setPasswordId] = useState({"toggler":"", "dismiss":""});
    const [action, setAction] = useState("");
    const [validMessage, setValidMessage] = useState("");
    const [validSuplier, setValidSuplier] = useState(false);


    async function getSupliersList() {
        let supliersResponse = await fetch(`${process.env.REACT_APP_BACKEND}/providers`,{method:'GET'});
        let supliersList:SupliersList[] = await supliersResponse.json();
        
        let input = document.getElementById("NewSuplierInput");
        input?.focus();
        
        supliersList = supliersList.filter((item:SupliersList)=>item["Descripcion"] !== "Proveedor Eliminado");
        setList(prev=>{
            if(prev.length===0)
                return supliersList;
            return prev;
        });
        setItemSelected("");
    }

    function resetSupliersList(){
        setList([]); 
        setValidMessage("");
        setAction("");
        setValidSuplier(false);
    }

    useEffect(()=>{
        let supliersModal = document.getElementById('SupliersModal');
        supliersModal?.addEventListener('shown.bs.modal', getSupliersList);
    },[]);

    function closePanel(){
        let close = document.getElementById("CloseSupliersPanel") as HTMLButtonElement;
        
        close.click();
        resetSupliersList();
    }

    function selectItem(selected:string){
        if(action==="")
            setItemSelected(selected);
    }

    function insertSuplier(){
        let newUser:SupliersList = {"Descripcion":"", "RFC":"", "_id":{"$oid":"new"}};
        setList((prevState)=>[...prevState, newUser]);
        setAction(`${process.env.REACT_APP_ACTIONS_NEW_SUPLIER}`);
        setItemSelected("");
    }

    function editSuplier(){
        setAction(`${process.env.REACT_APP_ACTIONS_MODIFY_SUPLIER}`);
    }

    function deleteSuplier(){
        setAction(`${process.env.REACT_APP_ACTIONS_DELETE_SUPLIER}`);
        submit();
    }

    function cancel(){
        let cancelButton = document.getElementById('SupliersCancelButton');
        cancelButton?.blur();
        resetSupliersList();
        getSupliersList();
    }

    function submit(){
        let passwordButton = document.getElementById(passwordId["toggler"]) as HTMLButtonElement;
        passwordButton.click();
    }

    async function submitSuccessful(response:SubmitPasswordResponse){
        let passwordButton = document.getElementById(passwordId["dismiss"]) as HTMLButtonElement;
        let newNameInput = document.getElementById("NewSuplierInput") as HTMLInputElement;
        let newRFCinput = document.getElementById("NewRFCInput") as HTMLInputElement;
        let newSuplierObject = [{"Descripcion":newNameInput?.value,
                                "RFC":newRFCinput?.value}];

                                
        if(action===`${process.env.REACT_APP_ACTIONS_NEW_SUPLIER}`){
            await fetch(`${process.env.REACT_APP_BACKEND}/provider`,{
                method:"POST",
                headers:{'Content-Type':'application/json'},
                body:JSON.stringify(newSuplierObject)
            });
        }
        if(action===`${process.env.REACT_APP_ACTIONS_MODIFY_SUPLIER}`){
            await fetch(`${process.env.REACT_APP_BACKEND}/provider/${itemSelected}`,{
                method:"PUT",
                headers:{'Content-Type':'application/json'},
                body:JSON.stringify(newSuplierObject)
            });
        }
        if(action===`${process.env.REACT_APP_ACTIONS_DELETE_SUPLIER}`){
            await fetch(`${process.env.REACT_APP_BACKEND}/provider/${itemSelected}`, {method:"DELETE"});
        }

        resetSupliersList();
        passwordButton.click();
    }
    
    function submitFailure(response:SubmitPasswordResponse){
        alert(`ERROR: ${response["message"]}`);
    }

    function paswordClose(){
        let passwordClose = document.getElementById(passwordId["dismiss"]) as HTMLButtonElement;
        passwordClose.click();
    }

    function checkValidSuplier(input:string, rfc:string){
        
        for(let i=0; i<list.length;i++){
            let previous = list[i]["Descripcion"].toLowerCase().replaceAll(" ","");
            let previousRFC = list[i]["RFC"].toLowerCase().replaceAll(" ","");

            if(input===""){
                setValidSuplier(false);
                setValidMessage("Introduce un nombre");
                return;
            }
            if(input===previous){
                if(action===`${process.env.REACT_APP_ACTIONS_NEW_SUPLIER}`){
                    setValidSuplier(false);
                    setValidMessage("Este proveedor ya existe");
                    return;
                }
                if(action===`${process.env.REACT_APP_ACTIONS_MODIFY_SUPLIER}`){
                    if(list[i]["_id"]["$oid"] !== itemSelected){
                        setValidSuplier(false);
                        setValidMessage("Este proveedor ya existe");
                        return;
                    }
                    else if(rfc === previousRFC){
                        setValidSuplier(false);
                        setValidMessage("Este proveedor ya existe");
                        return;
                    }
                }
            }
        }
        setValidSuplier(true);
        setValidMessage("");
        
    }

    return (
        <>
            <div id="SupliersPanel">
                <button data-bs-toggle='modal' data-bs-target='#SupliersModal' style={{display:"none"}}></button>
                <div className="modal fade" id="SupliersModal" data-bs-backdrop="static" data-bs-keyboard='false'>
                    <div className="modal-dialog modal-dialog-centered modal-lg modal-dialog-scrollable">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title">Proveedores</h5>
                                <button type="button" className="btn-close" onClick={closePanel}></button>
                                <button type="button" data-bs-dismiss="modal" id="CloseSupliersPanel" style={{display:"none"}}></button>
                            </div>
                            <div className="modal-body">
                                <div className="container-fluid">
                                    <table className={`table table-striped table-responsive ${action===""?"table-hover":""}`}>
                                        <thead>
                                            <tr>
                                                <th>Nombre</th>
                                                <th>RFC</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {list.map((item)=>{
                                                return (
                                                    <SuplierListItem key={item["_id"]["$oid"]} item={item} onSelect={selectItem} selected={itemSelected} userInputCheck={checkValidSuplier} action={action}/>
                                                );
                                            })}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div className="modal-footer">
                                <div className="me-auto">
                                    <button type="button" id="SupliersCancelButton" className="btn btn-outline-danger" disabled={action===""?true:false} onClick={cancel}>Cancelar</button>
                                    <span className="text-danger ms-3">{validMessage}</span>
                                </div>
                                
                                <div className="btn-group" role="group">
                                    <button type="button" className="btn btn-outline-danger" disabled={itemSelected==="" || action===`${process.env.REACT_APP_ACTIONS_MODIFY_SUPLIER}`?true:false} onClick={deleteSuplier}>Eliminar</button>     
                                    <button type="button" className="btn btn-outline-info" disabled={itemSelected==="" || action===`${process.env.REACT_APP_ACTIONS_MODIFY_SUPLIER}`?true:false} onClick={editSuplier}>Editar</button>
                                    {action===""?<button type="button" className="btn btn-outline-primary" onClick={insertSuplier}>Nuevo</button>:
                                                 <button type="button" className="btn btn-outline-primary" disabled={!validSuplier} onClick={submit}>Aceptar</button>}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div> 

            <SubmitPassword action={action} onSuccess={submitSuccessful} onFailure={submitFailure} onClose={paswordClose} parent="#SupliersModal" passId={(id)=>setPasswordId(id)}/>
        </>
        
    );
}

export default SettingsOption_Supliers;