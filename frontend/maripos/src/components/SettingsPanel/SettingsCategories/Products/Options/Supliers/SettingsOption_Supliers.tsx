import React, { useState, useEffect } from "react";
import {SupliersList, SubmitPasswordResponse} from "../../../../../../interfaces/interfaces";
import SuplierListItem from "./SuplierListItem";
import SubmitPassword from "../../../../../SubmitPassword/SubmitPassword";

function SettingsOption_Supliers(){
    const [list, setList] = useState<SupliersList[]>([]);
    const [itemSelected, setItemSelected] = useState("");
    const [passwordId, setPasswordId] = useState({"toggler":"", "dismiss":""});
    const [action, setAction] = useState("");


    async function getSupliersList() {
        let supliersResponse = await fetch(`${process.env.REACT_APP_BACKEND}/providers`,{method:'GET'});
        let supliersList:SupliersList[] = await supliersResponse.json();
        supliersList = supliersList.filter((item:SupliersList)=>item["Descripcion"] !== "Proveedor Eliminado");
        supliersList = supliersList.map((item:SupliersList)=>{
            item["set"] = true;
            return item;
        });
        setList(supliersList);
        setItemSelected("");
    }

    useEffect(()=>{
        let supliersModal = document.getElementById('SupliersModal');
        supliersModal?.addEventListener('show.bs.modal', getSupliersList);
    }, []);

    function selectItem(selected:string){
        setItemSelected(selected);
    }

    function insertUser(){
        let newUser:SupliersList = {"Descripcion":"", "RFC":"", "_id":{"$oid":"new"},"set":false};
        setList((prevState)=>[...prevState, newUser]);
        setAction(`${process.env.REACT_APP_ACTIONS_NEW_SUPLIER}`);
    }





    function deleteUser(){
        let passwordButton = document.getElementById(passwordId["toggler"]) as HTMLButtonElement;
        passwordButton.click();
    }

    async function deleteSuccessful(response:SubmitPasswordResponse){
        let passwordButton = document.getElementById(passwordId["dismiss"]) as HTMLButtonElement;
        
        await fetch(`${process.env.REACT_APP_BACKEND}/provider/${itemSelected}`, {method:"DELETE"});
        passwordButton.click();
    }

    function deleteFailure(response:SubmitPasswordResponse){
        alert(`ERROR: ${response["message"]}`);
    }

    function paswordClose(){
        let passwordClose = document.getElementById(passwordId["dismiss"]) as HTMLButtonElement;
        passwordClose.click();
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
                                <button type="button" className="btn-close" data-bs-dismiss="modal"></button>
                            </div>
                            <div className="modal-body">
                                <div className="container-fluid">
                                    <table className="table table-striped table-responsive table-hover">
                                        <thead>
                                            <tr>
                                                <th>Nombre</th>
                                                <th>RFC</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {list.map((item)=>{
                                                return (
                                                    <SuplierListItem key={item["_id"]["$oid"]} item={item} onSelect={selectItem} selected={itemSelected}/>
                                                );
                                            })}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            <div className="modal-footer">
                                <button type="button" className={`btn btn-outline-danger me-auto ${action===""?"disabled":""}`}>Cancelar</button>
                                <div className="btn-group" role="group">
                                    <button type="button" className={`btn btn-outline-danger ${itemSelected===""?"disabled":""}`} onClick={deleteUser}>Eliminar</button>     
                                    <button type="button" className={`btn btn-outline-info ${itemSelected===""?"disabled":""}`}>Editar</button>
                                    <button type="button" className="btn btn-outline-primary" onClick={insertUser}>{action===`${process.env.REACT_APP_ACTIONS_NEW_SUPLIER}`?"Aceptar":"Nuevo"}</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div> 

            <SubmitPassword action={action} onSuccess={deleteSuccessful} onFailure={deleteFailure} onClose={paswordClose} parent="#SupliersModal" passId={(id)=>setPasswordId(id)}/>
        </>
        
    );
}

export default SettingsOption_Supliers;