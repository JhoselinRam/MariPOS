import React, { useEffect, useState } from "react";
import {SubmitPasswordProps} from "../../interfaces/interfaces"

function SubmitPassword({action, onSuccess, onFailure, onClose, parent}:SubmitPasswordProps){

    const [keyTyped, setKeyTyped] = useState("");

    useEffect(()=>{
        let passwordSubmitPanel = document.getElementById("PasswordModal");
        let input = document.getElementById("PasswordInput");

        passwordSubmitPanel?.addEventListener("shown.bs.modal", ()=>{
            let input = document.getElementById("PasswordInput") as HTMLInputElement;
            input.focus();
        });
        
        passwordSubmitPanel?.addEventListener("hide.bs.modal",()=>{
            let input = document.getElementById("PasswordInput") as HTMLInputElement;
            input.value = "";
        });

        input?.addEventListener("keydown",(e)=>{
            setKeyTyped(e.key);
        })
    }, []);

    useEffect(()=>{
        if(keyTyped === "Enter")
            submit();
    },[keyTyped]);

    async function submit(){
        let passwordInput = document.getElementById("PasswordInput") as HTMLInputElement;
        let password = passwordInput.value;

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
             <button data-bs-toggle='modal' id="submitPasswordToggler" data-bs-target='#PasswordModal' style={{display:"none"}}></button>
             <div className="modal fade" id="PasswordModal" data-bs-backdrop="static" data-bs-keyboard="false">
                <div className="modal-dialog modal-dialog-centered">
                    <div className="modal-content">
                        <div className="modal-header">
                            <h5 className="modal-title">Esta acción requiere permiso</h5>
                        </div>
                        <div className="modal-body">
                           
                                <label htmlFor="#PasswordInput">Contraseña</label>
                                <input type="password" id="PasswordInput" className="form-control" autoComplete="off"/>
                           
                        </div>
                        <div className="modal-footer">
                            <button type="button" id="PasswordDismiss" data-bs-dismiss="modal" data-bs-toggle="modal" data-bs-target={parent?parent:""} style={{display:"none"}}></button>
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