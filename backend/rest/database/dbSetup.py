from pymongo import MongoClient
import time
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId


def main():
    dbName = "marison"
    client = MongoClient("localhost")
    client.drop_database(dbName)
    db     = client[dbName]

    createCollection_Proveedores(db, "Proveedores")
    createCollection_Grupos(db, "Grupos")
    createCollection_Subgrupos(db, "Subgrupos")
    createCollection_Insumos(db, "Insumos")
    createCollection_Productos(db, "Productos")
    createCollection_Clientes(db, "Clientes")
    createCollection_Ventas(db, "Ventas")
    createCollection_Descuentos(db, "Descuentos")
    createCollection_Privilegios(db, "Privilegios")
    createCollection_Usuarios(db, "Usuarios")
    createCollection_Acciones(db, "Acciones")
    createCollection_Inventarios(db, "Inventarios")
    createCollection_Compras(db, "Compras")
    createCollection_Mermas(db, "Mermas")
    createCollection_MotivosDeMerma(db, "MotivosDeMerma")


#-------------------------Proveedores-------------------------
#   Scheme: {
#       _id         : idObject
#       Descripcion : Text
#       RFC         : Text
# }
def createCollection_Proveedores(db, collectionName):
    collection = db[collectionName]

    collection.insert_one({
        "Descripcion" : "Proveedor Eliminado",
        "RFC" : "No Encontrado"
    })


#---------------------------Grupos----------------------------
#   Scheme: {
#       _id         : idObject
#       Descripcion : Text
# }
def createCollection_Grupos(db, collectionName):
    collection = db[collectionName]

    collection.insert_one({
        "Descripcion": "Grupo Eliminado"
    })


#--------------------------Subgrupos--------------------------
#   Scheme: {
#       _id         : ObjectId
#       Descripcion : Text
#       Grupo       : ObjectId
# }
def createCollection_Subgrupos(db, collectionName):
    collection = db[collectionName]
    groupID = db["Grupos"].find_one({"Descripcion": "Grupo Eliminado"})["_id"]
    
    collection.insert_one({
        "Descripcion" : "Subgrupo Eliminado",
        "Grupo" : groupID
    })


#--------------------------Insumos---------------------------
#   Scheme: {
#       _id                : ObjectId
#       Descripcion        : Text
#       Unidad             : Text
#       UnidadesPorPaquete : Text
#       CostoPorUnidad     : [{ Costo : Number,
#                               Fecha : Number  }]
#       Existencia         : Number
#       Proveedor          : ObjectId
# }
def createCollection_Insumos(db, collectionName):
    collection = db[collectionName]
    supplierId = db["Proveedores"].find_one({"Descripcion" : "Proveedor Eliminado"})["_id"]

    collection.insert_one({
        "Descripcion" : "Insumo Eliminado",
        "Unidad" : "No encontrado",
        "UnidadesPorPaquete" : 0,
        "CostoPorUnidad" : [{
            "Costo": 0,
            "Fecha" : time.time()
        }],
        "Existencia" : 0,
        "Proveedor" : supplierId
    })


#--------------------------Productos---------------------------
#   Scheme: {
#       _id          : ObjectId
#       Descripcion  : Text
#       Unidad       : Text
#       Receta       : [{ Insumo   : ObjectId,
#                         Cantidad : Number }]
#       CostoPublico : [{ Costo : Number,
#                         Fecha : Number }]
#       CostoMayoreo : [{ Costo : Number,
#                         Fecha : Number }]
#       Grupo        : ObjectId
#       SubGrupo     : ObjectId
#       Activo       : Boolean
# }
def createCollection_Productos(db, collectionName):
    collection = db[collectionName]
    groupID = db["Grupos"].find_one({"Descripcion": "Grupo Eliminado"})["_id"]
    subgroupId = db["Subgrupos"].find_one({"Descripcion": "Subgrupo Eliminado"})["_id"]
    supplyId = db["Insumos"].find_one({"Descripcion": "Insumo Eliminado"})["_id"]

    collection.insert_one({
        "Descripcion" : "Producto Eliminado",
        "Unidad" : "No Encontrado",
        "Receta" : [{
            "Insumo" : supplyId,
            "Cantidad" : 0
        }],
        "CostoPublico" : [{
            "Costo" : 0,
            "Fecha" : time.time()
        }],
        "CostoMayoreo" : [{
            "Costo" : 0,
            "Fecha" : time.time()
        }],
        "Grupo" : groupID,
        "Subgrupo" : subgroupId,
        "Activo" : False
    })


#----------------------------Clientes---------------------------
#   Scheme: {
#       _id          : ObjectId
#       Nombre       : Text
#       Telefono     : Text
#       Direccion    : Text     
#       Colonia      : Text
#       Cruzamiento1 : Text
#       Cruzamiento2 : Text
# }
def createCollection_Clientes(db, collectionName):
    collection = db[collectionName]

    collection.insert_many([
        {
        "Nombre" : "Cliente Eliminado",
        "Telefono": "No enccontrado",
        "Direccion" : "No encontrado",
        "Colonia" : "No encontrado",
        "Cruzamiento1" : "No encontrado",
        "Cruzamiento2" : "No encontrado"
        },
        {
        "Nombre" : "Invitado",
        "Telefono": "No aplica",
        "Direccion" : "No aplica",
        "Colonia" : "No aplica",
        "Cruzamiento1" : "No aplica",
        "Cruzamiento2" : "No aplica"
        }
    ])


#----------------------------Ventas----------------------------
#   Scheme: {
#       _id       : ObjectId
#       Productos : [{ Producto  : ObjectId,
#                      Cantidad  : Number,
#                      Descuento : { Concepto : ObjectId
#                                    Cantidad : Number} }]
#       Fecha     : Number
#       Cliente   : ObjectId
#       Cancelado : Boolean
# }
def createCollection_Ventas(db, collectionName):
    collection = db[collectionName]


#--------------------------Descuentos--------------------------
#   Scheme: {
#       _id         : ObjectId
#       Descripcion : Text
#       Porcentaje  : Number
# }
def createCollection_Descuentos(db, collectionName):
    collection = db[collectionName]

    collection.insert_one({
        "Descripcion" : "Sin descuento",
        "Porcentaje"  : 0
    })


#-------------------------Privilegios------------------------
#   Scheme: {
#       _id         : ObjectId
#       Descripcion : Text
# }
def createCollection_Privilegios(db, collectionName):
    collection = db[collectionName]

    collection.insert_many([
        {
            "Descripcion" : "Inactivo",
            "Permiso" : 0
        },
        {
            "Descripcion" : "Cajero",
            "Permiso" : 1
        },
        {
            "Descripcion" : "Gerente",
            "Permiso" : 2 
        },
        {
            "Descripcion" : "Administrador",
            "Permiso" : 3
        }
    ])


#---------------------------Usuarios-------------------------
#   Scheme: {
#       _id        : ObjectId
#       Nombre     : Text
#       Privilegio : ObjectId
#       Contraseña : Text
# }
def createCollection_Usuarios(db, collectionName):
    collection = db[collectionName]
    inactiveId = db["Privilegios"].find_one({"Descripcion":"Inactivo"})["_id"]
    adminId = db["Privilegios"].find_one({"Descripcion":"Administrador"})["_id"]

    bcrypt = Bcrypt()

    collection.insert_many([
        {
            "Nombre" : "Usuario Eliminado",
            "Privilegio" : inactiveId,
            "Contraseña" : bcrypt.generate_password_hash("0000").decode("utf-8")
        },
        {
            "Nombre" : "Admin",
            "Privilegio" : adminId,
            "Contraseña" : bcrypt.generate_password_hash("1234").decode("utf-8")
        }
    ])


#-----------------------------Acciones--------------------------
#   Scheme: {
#       _id         : ObjectId
#       Descripcion : Text
#       Privilegio  : ObjectId
#       Historial   : [{ Usuario : ObjectId, 
#                        Fecha   : Number }]
# }
def createCollection_Acciones(db, collectionName):
    collection = db[collectionName]
    cashierId = db["Privilegios"].find_one({"Descripcion":"Cajero"})["_id"]
    managerId = db["Privilegios"].find_one({"Descripcion":"Gerente"})["_id"]
    adminId = db["Privilegios"].find_one({"Descripcion":"Administrador"})["_id"]

    collection.insert_many([
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8a6"),
            "Descripcion" : "Cancelacion",
            "Privilegio" : managerId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8a7"),
            "Descripcion" : "Restauracion",
            "Privilegio" : managerId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8a8"),
            "Descripcion" : "Apertura de turno",
            "Privilegio" : cashierId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8a9"),
            "Descripcion" : "Cierre de turno",
            "Privilegio" : managerId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8aa"),
            "Descripcion" : "Descuento",
            "Privilegio" : cashierId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8ab"),
            "Descripcion" : "Añadir insumo",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8ac"),
            "Descripcion" : "Modificar insumo",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8ad"),
            "Descripcion" : "Eliminar insumo",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8ae"),
            "Descripcion" : "Añadir producto",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8af"),
            "Descripcion" : "Modificar producto",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b0"),
            "Descripcion" : "Eliminar producto",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b1"),
            "Descripcion" : "Añadir proveedor",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b2"),
            "Descripcion" : "Modificar proveedor",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b3"),
            "Descripcion" : "Eliminar proveedor",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b4"),
            "Descripcion" : "Añadir grupo",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b5"),
            "Descripcion" : "Modificar grupo",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b6"),
            "Descripcion" : "Eliminar grupo",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b7"),
            "Descripcion" : "Añadir subgrupo",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b8"),
            "Descripcion" : "Modificar subgrupo",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8b9"),
            "Descripcion" : "Eliminar subgrupo",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8ba"),
            "Descripcion" : "Añadir cliente",
            "Privilegio" : cashierId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8bb"),
            "Descripcion" : "Modificar cliente",
            "Privilegio" : managerId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8bc"),
            "Descripcion" : "Eliminar cliente",
            "Privilegio" : managerId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8bd"),
            "Descripcion" : "Añadir usuario",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8be"),
            "Descripcion" : "Modificar usuario",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8bf"),
            "Descripcion" : "Eliminar usuario",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8c0"),
            "Descripcion" : "Ingresar inventario",
            "Privilegio" : managerId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8c1"),
            "Descripcion" : "Modificar inventario",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8c2"),
            "Descripcion" : "Generar reporte",
            "Privilegio" : managerId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8c3"),
            "Descripcion" : "Ingresar compra",
            "Privilegio" : managerId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8c4"),
            "Descripcion" : "Modificar compra",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8c5"),
            "Descripcion" : "Eliminar compra",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8c6"),
            "Descripcion" : "Ingresar merma",
            "Privilegio" : managerId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8c7"),
            "Descripcion" : "Modificar merma",
            "Privilegio" : adminId,
            "Historial" : []
        },
        {
            "_id" : ObjectId("6286fe2a567ac6bb216ff8c8"),
            "Descripcion" : "Eliminar merma",
            "Privilegio" : adminId,
            "Historial" : []
        }
    ])


#-----------------------------Inventarios--------------------------
#   Scheme: {
#       _id     : ObjectId
#       Insumos : [{ Insumo            : ObjectId
#                    CantidadCalculada : Number
#                    CantidadIngresada : Number}]
#       Fecha   : Number  
# }
def createCollection_Inventarios(db, collectionName):
    collection = db[collectionName]


#-----------------------------Compras--------------------------
#   Scheme: {
#       _id       : ObjectId
#       Insumos   : [{ Insumo   : ObjectId
#                    Cantidad : Number }]
#       Fecha     : Number
#       Proveedor : ObjectId  
# }
def createCollection_Compras(db, collectionName):
    collection = db[collectionName]


#-----------------------------Mermas--------------------------
#   Scheme: {
#       _id     : ObjectId
#       Insumos : [{ Insumo   : ObjectId
#                    Cantidad : Number 
#                    Motivo   : ObjectId}]
#       Fecha   : Number  
# }
def createCollection_Mermas(db, collectionName):
    collection = db[collectionName]


#-------------------------Motivos de Merma----------------------
#   Scheme: {
#       _id         : ObjectId
#       Descripcion : Text  
# }
def createCollection_MotivosDeMerma(db, collectionName):
    collection = db[collectionName]










if __name__ == "__main__":
    main()