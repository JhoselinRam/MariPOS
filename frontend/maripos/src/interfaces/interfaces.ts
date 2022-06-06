export interface SupliersList{
    _id:{$oid:string},
    Descripcion:string,
    RFC:string
}

export interface SubmitPasswordProps{
    action: string,
    onSuccess: (arg0: SubmitPasswordResponse)=>void,
    onFailure: (arg0: SubmitPasswordResponse)=>void,
    onClose: ()=>void,
    parent?:string
}

export interface SubmitPasswordResponse{
    status:number,
    message:string
}