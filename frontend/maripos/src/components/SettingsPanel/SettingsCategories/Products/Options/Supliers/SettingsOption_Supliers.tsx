import React, { useState, useEffect } from "react";
import NewSuplier from "./NewSuplier";
import EditSuplier from "./EditSuplier";
import {SupliersList} from "../../../../../../interfaces/interfaces";
import SuplierListItem from "./SuplierListItem";

function SettingsOption_Supliers(){
    const [list, setList] = useState<SupliersList[]>([]);
    const [itemSelected, setItemSelected] = useState("");

    async function getSupliersList() {
        let supliersResponse = await fetch(`${process.env.REACT_APP_BACKEND}/providers`,{method:'GET'});
        let supliersList = await supliersResponse.json();
        supliersList = supliersList.filter((item:SupliersList)=>item["Descripcion"] !== "Proveedor Eliminado");
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
                                <div className="btn-group" role="group">
                                    <button type="button" className="btn btn-outline-danger">Eliminar</button>     
                                    <button type="button" className={`btn btn-outline-info ${itemSelected===""?"disabled":""}`} data-bs-toggle="modal" data-bs-target="#EditSuplierPanel">Editar</button>
                                    <button type="button" className="btn btn-outline-primary" data-bs-target="#NewSuplierPanel" data-bs-toggle="modal">Nuevo</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div> 

            <NewSuplier list={list}/>
            <EditSuplier list={list} idItem={itemSelected}/>
        </>
        
    );
}

export default SettingsOption_Supliers;