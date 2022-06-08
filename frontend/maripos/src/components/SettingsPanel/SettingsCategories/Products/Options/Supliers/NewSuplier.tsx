import React, { useEffect, useState } from "react";
import {SupliersList, SubmitPasswordResponse} from "../../../../../../interfaces/interfaces";
import SubmitPassword from "../../../../../SubmitPassword/SubmitPassword"

type newSuplierProps = {
    list:SupliersList[];
};

function NewSuplier({list}:newSuplierProps){

    const [validSuplier, setValidSuplier] = useState(false);
    const [validMessage, setValidMessage] = useState("");
    const [passwordId, setPasswordId] = useState<{"toggler":string, "dismiss":string}>({"toggler":"", "dismiss":""});

    useEffect(()=>{
        let panel = document.getElementById("NewSuplierPanel");
        panel?.addEventListener("shown.bs.modal", ()=>{
            let nameInput = document.getElementById("NewSuplierField");
            nameInput?.focus();
        })
    }, []);

    function resetForm(){
        let newSuplierName = document.getElementById("NewSuplierField") as HTMLInputElement;
        let newRFCName = document.getElementById("NewRFCField") as HTMLInputElement;
        newSuplierName.value = "";
        newRFCName.value = "";
        setValidSuplier(false);
        setValidMessage("");
    }

    function checkValidSuplier(){
        let newSuplierName = document.getElementById("NewSuplierField") as HTMLInputElement;
        
        for(let i=0; i<list.length;i++){
            let input = newSuplierName.value.toLowerCase().replaceAll(" ","");
            let previous = list[i]["Descripcion"].toLowerCase().replaceAll(" ","");
            if(input===previous){
                setValidSuplier(false);
                setValidMessage("Este proveedor ya existe");
                return;
            }
            if(input===""){
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
        let modalToggler = document.getElementById("newSuplierToggler") as HTMLButtonElement;
        resetForm();
        modalToggler.click();
    }

    async function submitSuccessful(response:SubmitPasswordResponse){
        let passwordButton = document.getElementById(passwordId["toggler"]) as HTMLButtonElement;
        let newNameInput = document.getElementById("NewSuplierField") as HTMLInputElement
        let newRFCinput = document.getElementById("NewRFCField") as HTMLInputElement
        let newSuplierObject = [{"Descripcion":newNameInput.value,
                                "RFC":newRFCinput.value}];

        passwordButton.click();
        await fetch(`${process.env.REACT_APP_BACKEND}/provider`,{
            method:"POST",
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

    function getPasswordId(id:{"toggler":string, "dismiss":string}){
        setPasswordId(id);
    }

    return (
        <>
            <div className="modal fade" id="NewSuplierPanel" data-bs-backdrop="static" data-bs-keyboard='false'>
                <div className="modal-dialog modal-dialog-centered modal-lg">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h5>Nuevo Proveedor</h5>
                        </div>
                        <div className="modal-body">
                            <div className="container">
                                <form>
                                    <div className="row">
                                        <div className="col">
                                            <div className="form-floating">
                                                <input type="text" className="form-control" id="NewSuplierField" placeholder="Proveedor" autoComplete="off" onInput={checkValidSuplier}/>
                                                <label htmlFor="NewSuplierField">Proveedor</label>
                                                <div className="form-text text-danger ms-2">{validMessage}</div>
                                            </div>   
                                        </div>
                                        <div className="col">
                                            <div className="form-floating">
                                                <input type="text" className="form-control" id="NewRFCField" placeholder="RFC" autoComplete="off"/>
                                                <label htmlFor="NewRFCField">RFC</label>
                                            </div>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div className="modal-footer">
                            <button type="button" id="newSuplierToggler" data-bs-target="#SupliersModal" data-bs-toggle="modal" data-bs-dismiss="modal" style={{display:"none"}}></button>
                            <div className="btn-group" role="group">
                                <button type="button" className="btn btn-outline-danger" onClick={cancel}>Cancelar</button>
                                <button type="button" className={`btn btn-outline-primary ${validSuplier===false?"disabled":""}`} onClick={submitSuplier}>Aceptar</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <SubmitPassword action={`${process.env.REACT_APP_ACTIONS_NEW_SUPLIER}`} onSuccess={submitSuccessful} onFailure={submitFailure} onClose={paswordClose} parent="#NewSuplierPanel" passId={getPasswordId} />
        </>        
    );
}

export default NewSuplier;
