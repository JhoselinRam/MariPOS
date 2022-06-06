import React from "react";

function Toolbar(){
    return (
        <div className="container-fluid toolbar">
            <div className='row'>
                <div className='col-sm-9'>
                    <div className='row'>
                        <div className='col-sm p-0'>
                            <div className='d-grid'>
                                <button className='btn btn-warning btn-sm' type='button'>Eliminar</button>
                            </div>
                        </div>
                        <div className='col-sm p-0'>
                            <div className='d-grid'>
                                <button className='btn  btn-outline-primary btn-sm' type='button'>Juntar Cuentas</button>
                            </div>
                        </div>
                        <div className='col-sm p-0'>
                            <div className='d-grid'>
                                <button className='btn btn-outline-primary btn-sm' type='button'>Dividir Cuenta</button>
                            </div>
                        </div>
                        <div className='col-sm p-0'>
                            <div className='d-grid'>
                                <button className='btn btn-outline-primary btn-sm' type='button'>Cliente</button>
                            </div>
                        </div>
                        <div className='col-sm p-0'>
                            <div className='d-grid'>
                                <button className='btn btn-outline-primary btn-sm' type='button'>Cobrar</button>
                            </div>
                        </div>
                    </div>

                    <div className='row'>
                        <div className='col-sm p-0'>
                            <div className='d-grid'>
                                <button className='btn btn-danger btn-sm' type='button'>Desechar cuenta</button>
                            </div>
                        </div>
                        <div className='col-sm p-0'>
                            <div className='d-grid'>
                                <button className='btn btn-outline-primary btn-sm' type='button'>Traspasar Productos</button>
                            </div>
                        </div>
                        <div className='col-sm p-0'>
                            <div className='d-grid'>
                                <button className='btn btn-outline-primary btn-sm' type='button'>Descuento</button>
                            </div>
                        </div>
                        <div className='col-sm p-0'>
                                <div className="dropdown">
                                    <div className='d-grid'>
                                        <button type="button" className="btn btn-outline-primary btn-sm dropdown-toggle" data-bs-toggle="dropdown">
                                            Invitado
                                        </button>
                                        <div className="dropdown-menu dropdown-menu-end">
                                            <span className="dropdown-item">Link 1</span>
                                            <span className="dropdown-item">Link 2</span>
                                            <span className="dropdown-item">Link 3</span>
                                    </div>
                                    </div>
                                </div>        
                        </div>
                        <div className='col-sm p-0'>
                            <div className='d-grid'>
                                <button className='btn btn-outline-primary btn-sm' type='button'>Capturar</button>
                            </div>
                        </div>
                    </div>
                </div>

                <div className='col-sm-3'>
                    <div className='d-grid mx-auto col-11 h-100'>
                        <button className='btn btn-primary btn-lg' type='button'>+ Nueva Venta</button>
                    </div>
                </div>
            </div>
        </div>
        
    );
}

export default Toolbar;