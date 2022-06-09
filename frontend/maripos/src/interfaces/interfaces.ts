export interface SupliersList{
    _id:{$oid:string},
    Descripcion:string,
    RFC:string,
    set?:boolean
}

export interface SubmitPasswordProps{
    action: string,
    onSuccess: (arg0: SubmitPasswordResponse)=>void,
    onFailure: (arg0: SubmitPasswordResponse)=>void,
    onClose: ()=>void,
    parent?:string,
    passId:(arg0:{"toggler":string, "dismiss":string})=>void
}

export interface SubmitPasswordResponse{
    status:number,
    message:string,
    user:{$oid:string}
}

export interface SuplierItemsProps{
    item:SupliersList, 
    onSelect:(arg0:string)=>void, 
    selected:string
}

export interface EditSuplierProps{
    list:SupliersList[],
    idItem:string
}