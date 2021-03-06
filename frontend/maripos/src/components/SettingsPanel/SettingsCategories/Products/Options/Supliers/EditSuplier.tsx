import React, { useEffect, useState } from "react";
import {EditSuplierProps, SubmitPasswordResponse} from "../../../../../../interfaces/interfaces";
import SubmitPassword from "../../../../../SubmitPassword/SubmitPassword"


function EditSuplier({list, idItem}:EditSuplierProps){

    const [validSuplier, setValidSuplier] = useState(false);
    const [validMessage, setValidMessage] = useState("");
    const [passwordId, setPasswordId] = useState({"toggler":"", "dismiss":""});

    useEffect(()=>{
        let panel = document.getElementById("EditSuplierPanel");
        panel?.addEventListener("shown.bs.modal", ()=>{
            let nameInput = document.getElementById("EditSuplierField") as HTMLInputElement;
            let newRFCinput = document.getElementById("EditRFCField") as HTMLInputElement;
            
            nameInput.value = idItem!==""?list.filter(item=>item["_id"]["$oid"]===idItem)[0]["Descripcion"]:""
            newRFCinput.value = idItem!==""?list.filter(item=>item["_id"]["$oid"]===idItem)[0]["RFC"]:""
            nameInput.focus();
        })
    });

    function resetForm(){
        let newSuplierName = document.getElementById("EditSuplierField") as HTMLInputElement;
        let newRFCName = document.getElementById("EditRFCField") as HTMLInputElement;
        newSuplierName.value = "";
        newRFCName.value = "";
        setValidSuplier(false);
        setValidMessage("");
    }

    function checkValidSuplier(){
        let newSuplierName = document.getElementById("EditSuplierField") as HTMLInputElement;
        let newSuplierRFC = document.getElementById("EditRFCField") as HTMLInputElement;
        let name = newSuplierName.value.toLowerCase().replaceAll(" ","");
        let rfc = newSuplierRFC.value.toLowerCase().replaceAll(" ","");


        for(let i=0; i<list.length;i++){
            let previousName = list[i]["Descripcion"].toLowerCase().replaceAll(" ","");
            let previousRFC = list[i]["RFC"].toLowerCase().replaceAll(" ","");
            
            if(name === previousName){
                if(list[i]["_id"]["$oid"] !== idItem){
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
            if(name===""){
                setValidSuplier(false);
                setValidMessage("Introduce un nombre");
                return;
            }
        }
        setValidSuplier(true);
        setValidMessage("");
        
    }

    function submitSuplier(){
        let passwordButton = document.getElementById(passwordId["toggler"]) as HTMLButtonElement;
        passwordButton.click();
    }

    function cancel(){
        let modalToggler = document.getElementById("editSuplierToggler") as HTMLButtonElement;
        resetForm();
        modalToggler.click();
    }

    async function submitSuccessful(response:SubmitPasswordResponse){
        let passwordButton = document.getElementById(passwordId["toggler"]) as HTMLButtonElement;
        let newNameInput = document.getElementById("EditSuplierField") as HTMLInputElement
        let newRFCinput = document.getElementById("EditRFCField") as HTMLInputElement
        let newSuplierObject = [{"Descripcion":newNameInput.value,
                                "RFC":newRFCinput.value}];

        passwordButton.click();
        await fetch(`${process.env.REACT_APP_BACKEND}/provider/${idItem}`,{
            method:"PUT",
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify(newSuplierObject)
        });

        cancel();

    }

    function submitFailure(response:SubmitPasswordResponse){
        alert(`ERROR: ${response["message"]}`);
    }

    function paswordClose(){
        let passwordClose = document.getElementById(passwordId["dismiss"]) as HTMLButtonElement;
        passwordClose.click();
    }

    return (
        <>
            <div className="modal fade" id="EditSuplierPanel" data-bs-backdrop="static" data-bs-keyboard='false'>
                <div className="modal-dialog modal-dialog-centered modal-lg">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h5>Editar Proveedor</h5>
                        </div>
                        <div className="modal-body">
                            <div className="container">
                                <form>
                                    <div className="row">
                                        <div className="col">
                                            <div className="form-floating">
                                                <input type="text" className="form-control" id="EditSuplierField" placeholder="Proveedor" autoComplete="off" onInput={checkValidSuplier}/>
                                                <label htmlFor="#EditSuplierField">Proveedor</label>
                                                <div className="form-text text-danger ms-2">{validMessage}</div>
                                            </div>   
                                        </div>
                                        <div className="col">
                                            <div className="form-floating">
                                                <input type="text" className="form-control" id="EditRFCField" placeholder="RFC" autoComplete="off" onInput={checkValidSuplier}/>
                                                <label htmlFor="EditRFCField">RFC</label>
                                            </div>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div className="modal-footer">
                            <button type="button" id="editSuplierToggler" data-bs-target="#SupliersModal" data-bs-toggle="modal" data-bs-dismiss="modal" style={{display:"none"}}></button>
                            <div className="btn-group" role="group">
                                <button type="button" className="btn btn-outline-danger" onClick={cancel}>Cancelar</button>
                                <button type="button" className={`btn btn-outline-primary ${validSuplier===false?"disabled":""}`} onClick={submitSuplier}>Aceptar</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <SubmitPassword action={`${process.env.REACT_APP_ACTIONS_MODIFY_SUPLIER}`} onSuccess={submitSuccessful} onFailure={submitFailure} onClose={paswordClose} parent="#EditSuplierPanel" passId={(id)=>setPasswordId(id)} />
        </>        
    );
}

export default EditSuplier;