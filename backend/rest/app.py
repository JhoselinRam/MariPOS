import json
import time
from bson.json_util import dumps, loads
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from database import dbServices
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
bcrypt = Bcrypt(app)
dbName = "marison"
CORS(app)

#---------------- Generics ----------------
def getDocuments(collection, fields):
    documents = dbServices.getDocuments(dbName, collection, fields) 

    return jsonify(json.loads(dumps(documents)))


def getDocumentById(collection, fields, id):
    identifier = ["_id", ObjectId(id)]
    document = dbServices.getDocumentBy(dbName, collection, identifier, fields)

    return jsonify(json.loads(dumps(document)))


def setDocument(collection):
    newDocument = loads(json.dumps(request.json))
    for document in newDocument:
        if "Contraseña" in document:
            document["Contraseña"] = bcrypt.generate_password_hash(document["Contraseña"]).decode("utf-8")
    
    dbServices.setNewDocument(dbName, collection, newDocument)
    
    return jsonify({"mesagge":"success"})

def updateDocument(collection, id):
    documentUpdated = loads(json.dumps(request.json))
    for document in documentUpdated:
        if "Contraseña" in document:
            document["Contraseña"] = bcrypt.generate_password_hash(document["Contraseña"]).decode("utf-8")
    
    identifier = [["_id", ObjectId(id)]]
    dbServices.updateDocument(dbName, collection, identifier, documentUpdated)
    
    return jsonify({"mesagge":"success"})

def deleteDocument(collection, id):
    identifier = [["_id", ObjectId(id)]]
    dbServices.deleteDocument(dbName,collection,identifier)

    return jsonify({"mesagge":"success"})


#------------------------------------------Routes---------------------------------------------------

#------------------------------------------
#---------------- Usuarios ----------------
@app.route("/users", methods=["GET"])
def getUsers():
    fields = ["_id", "Nombre", "Privilegio"]
    return getDocuments("Usuarios", fields)


@app.route("/user/<id>", methods=["GET"])
def getUserById(id):
    fields = ["_id", "Nombre", "Privilegio"]
    return getDocumentById("Usuarios", fields, id)


@app.route("/user", methods=["POST"])
def setUser():
    return setDocument("Usuarios")


@app.route("/user/<id>", methods=["PUT"])
def updateUser(id):
    return updateDocument("Usuarios", id)


@app.route("/user/<id>", methods=["DELETE"])
def deletUser(id):
    return deleteDocument("Usuarios", id)
    

# #---------------------------------------------
# #---------------- Proveedores ----------------

@app.route("/providers", methods=["GET"])
def getProvider():
    fields = []
    return getDocuments("Proveedores", fields)


@app.route("/provider/<id>", methods=["GET"])
def getProviderById(id):
    fields = []
    return getDocumentById("Proveedores", fields, id)


@app.route("/provider", methods=["POST"])
def setProvider():
    return setDocument("Proveedores")


@app.route("/provider/<id>", methods=["PUT"])
def updateProvider(id):
    return updateDocument("Proveedores", id)


@app.route("/provider/<id>", methods=["DELETE"])
def deletProvider(id):
    return deleteDocument("Proveedores", id)


# #----------------------------------------
# #---------------- Grupos ----------------


@app.route("/groups", methods=["GET"])
def getGroup():
    fields = []
    return getDocuments("Grupos", fields)


@app.route("/group/<id>", methods=["GET"])
def getGroupById(id):
    fields = []
    return getDocumentById("Grupos",fields, id)


@app.route("/group", methods=["POST"])
def setGroup():
    return setDocument("Grupos")


@app.route("/group/<id>", methods=["PUT"])
def updateGroup(id):
    return updateDocument("Grupos", id)


@app.route("/group/<id>", methods=["DELETE"])
def deletGroup(id):
    return deleteDocument("Grupos", id)


# #-------------------------------------------
# #---------------- Subgrupos ----------------


@app.route("/subgroups", methods=["GET"])
def getSubgroups():
    fields = []
    return getDocuments("Subgrupos", fields)


@app.route("/subgroup/<id>", methods=["GET"])
def getSubgroupById(id):
    fields = []
    return getDocumentById("Subgrupos",fields, id)


@app.route("/subgroup", methods=["POST"])
def setSubgroup():
    return setDocument("Subgrupos")


@app.route("/subgroup/<id>", methods=["PUT"])
def updateSubgroup(id):
    return updateDocument("Subgrupos", id)


@app.route("/subgroup/<id>", methods=["DELETE"])
def deletSubgroup(id):
    return deleteDocument("Subgrupos", id)


# #-----------------------------------------
# #---------------- Insumos ----------------


@app.route("/supplies", methods=["GET"])
def getSupplies():
    fields = []
    return getDocuments("Insumos", fields)


@app.route("/supplie/<id>", methods=["GET"])
def getSupplieById(id):
    fields = []
    return getDocumentById("Insumos",fields, id)


@app.route("/supplie", methods=["POST"])
def setSupplie():
    return setDocument("Insumos")


@app.route("/supplie/<id>", methods=["PUT"])
def updateSupplie(id):
    return updateDocument("Insumos", id)


@app.route("/supplie/<id>", methods=["DELETE"])
def deletSupplie(id):
    return deleteDocument("Insumos", id)


# #-----------------------------------------
# #-------------- Productos ----------------


@app.route("/products", methods=["GET"])
def getProducts():
    fields = []
    return getDocuments("Productos", fields)


@app.route("/product/<id>", methods=["GET"])
def getProductById(id):
    fields = []
    return getDocumentById("Productos",fields, id)


@app.route("/product", methods=["POST"])
def setProduct():
    return setDocument("Productos")


@app.route("/product/<id>", methods=["PUT"])
def updateProduct(id):
    return updateDocument("Productos", id)


@app.route("/product/<id>", methods=["DELETE"])
def deletProduct(id):
    return deleteDocument("Productos", id)


# #------------------------------------------
# #---------------- Clientes ----------------


@app.route("/clients", methods=["GET"])
def getClients():
    fields = []
    return getDocuments("Clientes", fields)


@app.route("/client/<id>", methods=["GET"])
def getClientById(id):
    fields = []
    return getDocumentById("Clientes",fields, id)


@app.route("/client", methods=["POST"])
def setClient():
    return setDocument("Clientes")


@app.route("/client/<id>", methods=["PUT"])
def updateClient(id):
    return updateDocument("Clientes", id)


@app.route("/client/<id>", methods=["DELETE"])
def deletClient(id):
    return deleteDocument("Clientes", id)


# #-----------------------------------------
# #----------------- Ventas ----------------


@app.route("/sales", methods=["GET"])
def getTickets():
    fields = []
    return getDocuments("Ventas", fields)


@app.route("/sale/<id>", methods=["GET"])
def getTicketById(id):
    fields = []
    return getDocumentById("Ventas",fields, id)


@app.route("/sale", methods=["POST"])
def setTicket():
    return setDocument("Ventas")


@app.route("/sale/<id>", methods=["PUT"])
def updateTicket(id):
    return updateDocument("Ventas", id)


# #-----------------------------------------
# #------------- Descuentos ----------------


@app.route("/discounts", methods=["GET"])
def getDiscounts():
    fields = []
    return getDocuments("Descuentos", fields)


@app.route("/discount/<id>", methods=["GET"])
def getDiscountById(id):
    fields = []
    return getDocumentById("Descuentos",fields, id)


@app.route("/discount", methods=["POST"])
def setDiscount():
    return setDocument("Descuentos")


@app.route("/discount/<id>", methods=["PUT"])
def updateDiscount(id):
    return updateDocument("Descuentos", id)


@app.route("/discount/<id>", methods=["DELETE"])
def deletDiscount(id):
    return deleteDocument("Descuentos", id)


# #---------------------------------------------
# #---------------- Privilegios ----------------


@app.route("/privileges", methods=["GET"])
def getPrivileges():
    fields = []
    return getDocuments("Privilegios", fields)


@app.route("/privilege/<id>", methods=["GET"])
def getPrivilegeById(id):
    fields = []
    return getDocumentById("Privilegios",fields, id)


# #------------------------------------------
# #---------------- Acciones ----------------


@app.route("/actions", methods=["GET"])
def getActions():
    fields = []
    return getDocuments("Acciones", fields)


@app.route("/action/<id>", methods=["GET"])
def getActionById(id):
    fields = []
    return getDocumentById("Acciones",fields, id)


@app.route("/action", methods=["PUT"])
def updateAction():
    data = request.json
    actionDone = dbServices.getDocumentBy(dbName,"Acciones",["_id",ObjectId(data["accion"])],["Historial"])[0]

    
    newAction = {"Usuario" : ObjectId(data["usuario"])}
    newAction["Fecha"] = time.time()

    actionDone["Historial"].append(newAction)

    dbServices.updateDocument(dbName,"Acciones",[["_id",ObjectId(data["accion"])]],[actionDone])



    return jsonify({"status":"success"})


# #---------------------------------------------
# #---------------- Inventarios ----------------


@app.route("/inventories", methods=["GET"])
def getInventories():
    fields = []
    return getDocuments("Inventarios", fields)


@app.route("/inventory/<id>", methods=["GET"])
def getInventoryById(id):
    fields = []
    return getDocumentById("Inventarios",fields, id)


@app.route("/inventory", methods=["POST"])
def setInventory():
    return setDocument("Inventarios")


@app.route("/inventory/<id>", methods=["PUT"])
def updateInventory(id):
    return updateDocument("Inventarios", id)


#------------------------------------------
#----------------- Compras ----------------
@app.route("/purchases", methods=["GET"])
def getPurchases():
    fields = []
    return getDocuments("Compras", fields)


@app.route("/purchase/<id>", methods=["GET"])
def getPurchaseById(id):
    fields = []
    return getDocumentById("Compras", fields, id)


@app.route("/purchase", methods=["POST"])
def setPurchase():
    return setDocument("Compras")


@app.route("/purchase/<id>", methods=["PUT"])
def updatePurchase(id):
    return updateDocument("Compras", id)


@app.route("/purchase/<id>", methods=["DELETE"])
def deletPurchase(id):
    return deleteDocument("Compras", id)


#------------------------------------------
#----------------- Mermas -----------------
@app.route("/losses", methods=["GET"])
def getLosses():
    fields = []
    return getDocuments("Mermas", fields)


@app.route("/losse/<id>", methods=["GET"])
def getLosseById(id):
    fields = []
    return getDocumentById("Mermas", fields, id)


@app.route("/losse", methods=["POST"])
def setLosse():
    return setDocument("Mermas")


@app.route("/losse/<id>", methods=["PUT"])
def updateLosse(id):
    return updateDocument("Mermas", id)


@app.route("/losse/<id>", methods=["DELETE"])
def deletLosse(id):
    return deleteDocument("Mermas", id)


#------------------------------------------
#------------ Motivos de Merma ------------
@app.route("/losses_cause", methods=["GET"])
def getLossesCause():
    fields = []
    return getDocuments("MotivosDeMerma", fields)


@app.route("/losse_cause/<id>", methods=["GET"])
def getLosseCauseById(id):
    fields = []
    return getDocumentById("MotivosDeMerma", fields, id)


@app.route("/losse_cause", methods=["POST"])
def setLosseCause():
    return setDocument("MotivosDeMerma")


@app.route("/losse_cause/<id>", methods=["PUT"])
def updateLosseCause(id):
    return updateDocument("MotivosDeMerma", id)


@app.route("/losse_cause/<id>", methods=["DELETE"])
def deletLosseCause(id):
    return deleteDocument("MotivosDeMerma", id)


#------------------------------------------
#--------------- Especiales ---------------
@app.route("/check_permission", methods=["POST"])
def checkPermission():
    data = request.json

    users = dbServices.getDocuments(dbName,"Usuarios", ["_id", "Privilegio", "Contraseña"])
    action = dbServices.getDocumentBy(dbName, "Acciones", ["_id",ObjectId(data["action"])], ["Privilegio"])
    
    if len(action) == 0:
        return jsonify({"status":404, "message":"Accion no encontrada", "user":"Usuario no encontrado"})
    
    foundUser = {}
    for user in users:
        if bcrypt.check_password_hash(user["Contraseña"], data["password"]):
            foundUser = user

    if len(foundUser) == 0:
        return jsonify({"status":404, "message":"Usuario no encontrado","user":"Usuario no encontrado"})
    
    userPermission = dbServices.getDocumentBy(dbName,"Privilegios", ["_id",foundUser["Privilegio"]], ["Permiso"])[0]["Permiso"]
    actionPermission = dbServices.getDocumentBy(dbName,"Privilegios", ["_id",action[0]["Privilegio"]], ["Permiso"])[0]["Permiso"]
    
    if userPermission < actionPermission:
        return jsonify(json.loads(dumps({"status":403, "message":"No cuentas con los privilegios para realizar esta acción", "user":foundUser["_id"]})))
    
    return jsonify(json.loads(dumps({"status":200, "message":"Acción permitida", "user":foundUser["_id"]})))




if __name__ == "__main__":
    app.run(debug=True, port=5000)
