import React, { useEffect, useState, useId } from "react";
import {SubmitPasswordProps} from "../../interfaces/interfaces"

function SubmitPassword({action, onSuccess, onFailure, onClose, parent, passId}:SubmitPasswordProps){

    const [keyTyped, setKeyTyped] = useState("");
    const passwordToggler = `paswordId${useId()}`.replaceAll(":","-");
    const passwordModal = `paswordId${useId()}`.replaceAll(":","-");
    const passwordInput = `paswordId${useId()}`.replaceAll(":","-");
    const passwordDismiss = `paswordId${useId()}`.replaceAll(":","-");

    useEffect(()=>{
        let passwordSubmitPanel = document.getElementById(passwordModal);
        let input = document.getElementById(passwordInput);
        let ids = {"toggler":passwordToggler, "dismiss":passwordDismiss};

        passwordSubmitPanel?.addEventListener("shown.bs.modal", ()=>{
            let input = document.getElementById(passwordInput);
            input?.focus();
        });
        
        passwordSubmitPanel?.addEventListener("hide.bs.modal",()=>{
            let input = document.getElementById(passwordInput) as HTMLInputElement;
            input.value = "";
        });

        input?.addEventListener("keydown",(e)=>{
            setKeyTyped(e.key);
        });

        passId(ids);    
        
    });

    useEffect(()=>{
        if(keyTyped === "Enter")
            submit();
    },[keyTyped]);

    async function submit(){
        let input = document.getElementById(passwordInput) as HTMLInputElement;
        let password = input.value;

        let submitRessponse = await fetch(`${process.env.REACT_APP_BACKEND}/check_permission`,{method:'POST',
                                                                                               headers:{'Content-Type':'application/json'},
                                                                                               body:JSON.stringify({action,password})});
        let response = await submitRessponse.json();
        
        if(response["status"] === 200){
            onSuccess(response);
        }
        else
            onFailure(response);
    }

    return (
        <>
             <button data-bs-toggle='modal' id={passwordToggler} data-bs-target={`#${passwordModal}`} style={{display:"none"}}></button>
             <div className="modal fade" id={passwordModal} data-bs-backdrop="static" data-bs-keyboard="false">
                <div className="modal-dialog modal-dialog-centered">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h5 className="modal-title">Esta acción requiere permiso</h5>
                        </div>
                        <div className="modal-body">
                           
                                <label htmlFor={`#${passwordInput}`}>Contraseña</label>
                                <input type="password" id={passwordInput} className="form-control" autoComplete="off"/>
                           
                        </div>
                        <div className="modal-footer">
                            <button type="button" id={passwordDismiss} data-bs-dismiss="modal" data-bs-toggle="modal" data-bs-target={parent?parent:""} style={{display:"none"}}></button>
                            <div className="btn-group" role="group">
                                <button type="button" className="btn btn-outline-danger" onClick={onClose}>Cancelar</button>
                                <button type="button" className="btn btn-outline-primary" onClick={submit}>Aceptar</button>
                            </div>
                        </div>
                    </div>
                </div>
             </div>
        </>
    );
}

export default SubmitPassword;