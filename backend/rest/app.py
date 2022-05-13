from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from database import dbServices
from flask_cors import CORS

app = Flask(__name__)
bcrypt = Bcrypt(app)
dbName = "database/marisons.db"

CORS(app)

#---------------- Generics ----------------
def getRows(table, columns):
    rows = dbServices.getRows(dbName, table, columns) 

    return jsonify(rows)


def getRowById(table, columns, id):
    identifier = ["id", id]
    row = dbServices.getRowBy(dbName, table, identifier, columns)

    return jsonify(row)


def setRow(table):
    newRow = request.json
    if "Contraseña" in newRow[0]:
        newRow[0]["Contraseña"] = bcrypt.generate_password_hash(newRow[0]["Contraseña"]).decode("utf-8")
    dbServices.setNewRow(dbName, table, newRow)
    
    return jsonify({"mesagge":"success"})

def updateRow(table, id):
    rowUpdated = request.json
    if "Contraseña" in rowUpdated[0]:
        rowUpdated[0]["Contraseña"] = bcrypt.generate_password_hash(rowUpdated[0]["Contraseña"]).decode("utf-8")
    identifier = [["id", id]]
    dbServices.updateRow(dbName, table, identifier, rowUpdated)
    
    return jsonify({"mesagge":"success"})

def deleteRow(table, id):
    identifier = [["id", id]]
    dbServices.deleteRow(dbName,table,identifier)

    return jsonify({"mesagge":"success"})

#------------------------------------------
#---------------- Usuarios ----------------
@app.route("/users", methods=["GET"])
def getUsers():
    columns = ["id", "Nombre", "Privilegio"]
    return getRows("Usuarios", columns)


@app.route("/user/<id>", methods=["GET"])
def getUserById(id):
    columns = ["id", "Nombre", "Privilegio"]
    return getRowById("Usuarios",columns, id)


@app.route("/user", methods=["POST"])
def setUser():
    return setRow("Usuarios")


@app.route("/user/<id>", methods=["PUT"])
def updateUser(id):
    return updateRow("Usuarios", id)


@app.route("/user/<id>", methods=["DELETE"])
def deletUser(id):
    return deleteRow("Usuarios", id)
    

#---------------------------------------------
#---------------- Proveedores ----------------

@app.route("/providers", methods=["GET"])
def getProvider():
    columns = ["id", "Descripcion", "RFC"]
    return getRows("Proveedores", columns)


@app.route("/provider/<id>", methods=["GET"])
def getProviderById(id):
    columns = ["id", "Descripcion", "RFC"]
    return getRowById("Proveedores",columns, id)


@app.route("/provider", methods=["POST"])
def setProvider():
    return setRow("Proveedores")


@app.route("/provider/<id>", methods=["PUT"])
def updateProvider(id):
    return updateRow("Proveedores", id)


@app.route("/provider/<id>", methods=["DELETE"])
def deletProvider(id):
    return deleteRow("Proveedores", id)


#----------------------------------------
#---------------- Grupos ----------------


@app.route("/groups", methods=["GET"])
def getGroup():
    columns = ["id", "Descripcion"]
    return getRows("Grupos", columns)


@app.route("/group/<id>", methods=["GET"])
def getGroupById(id):
    columns = ["id", "Descripcion"]
    return getRowById("Grupos",columns, id)


@app.route("/group", methods=["POST"])
def setGroup():
    return setRow("Grupos")


@app.route("/group/<id>", methods=["PUT"])
def updateGroup(id):
    return updateRow("Grupos", id)


@app.route("/group/<id>", methods=["DELETE"])
def deletGroup(id):
    return deleteRow("Grupos", id)


#-------------------------------------------
#---------------- Subgrupos ----------------


@app.route("/subgroups", methods=["GET"])
def getSubgroups():
    columns = ["id", "Descripcion", "Grupo"]
    return getRows("Subgrupos", columns)


@app.route("/subgroup/<id>", methods=["GET"])
def getSubgroupById(id):
    columns = ["id", "Descripcion", "Grupo"]
    return getRowById("Subgrupos",columns, id)


@app.route("/subgroup", methods=["POST"])
def setSubgroup():
    return setRow("Subgrupos")


@app.route("/subgroup/<id>", methods=["PUT"])
def updateSubgroup(id):
    return updateRow("Subgrupos", id)


@app.route("/subgroup/<id>", methods=["DELETE"])
def deletSubgroup(id):
    return deleteRow("Subgrupos", id)


#-----------------------------------------
#---------------- Insumos ----------------


@app.route("/supplies", methods=["GET"])
def getSupplies():
    columns = ["id", "Descripcion", "Unidad", "UnidadPorPaquete", "CostoPorUnidad", "CostoPublicoPorUnidad", "Existencia", "Grupo", "Subgrupo", "Proveedor", "Activo"]
    return getRows("Insumos", columns)


@app.route("/supplie/<id>", methods=["GET"])
def getSupplieById(id):
    columns = ["id", "Descripcion", "Unidad", "UnidadPorPaquete", "CostoPorUnidad", "CostoPublicoPorUnidad", "Existencia", "Grupo", "Subgrupo", "Proveedor", "Activo"]
    return getRowById("Insumos",columns, id)


@app.route("/supplie", methods=["POST"])
def setSupplie():
    return setRow("Insumos")


@app.route("/supplie/<id>", methods=["PUT"])
def updateSupplie(id):
    return updateRow("Insumos", id)


@app.route("/supplie/<id>", methods=["DELETE"])
def deletSupplie(id):
    return deleteRow("Insumos", id)


#------------------------------------------
#---------------- Clientes ----------------


@app.route("/clients", methods=["GET"])
def getClients():
    columns = ["id", "Nombre", "Telefono", "Direccion", "Colonia", "Cruzamiento1, Cruzamiento2"]
    return getRows("Clientes", columns)


@app.route("/client/<id>", methods=["GET"])
def getClientById(id):
    columns = ["id", "Nombre", "Telefono", "Direccion", "Colonia", "Cruzamiento1, Cruzamiento2"]
    return getRowById("Clientes",columns, id)


@app.route("/client", methods=["POST"])
def setClient():
    return setRow("Clientes")


@app.route("/client/<id>", methods=["PUT"])
def updateClient(id):
    return updateRow("Clientes", id)


@app.route("/client/<id>", methods=["DELETE"])
def deletClient(id):
    return deleteRow("Clientes", id)


#-----------------------------------------
#---------------- Tickets ----------------


@app.route("/tickets", methods=["GET"])
def getTickets():
    columns = ["id", "Total", "Fecha", "Cliente", "Cancelado"]
    return getRows("Tickets", columns)


@app.route("/ticket/<id>", methods=["GET"])
def getTicketById(id):
    columns = ["id", "Total", "Fecha", "Cliente", "Cancelado"]
    return getRowById("Tickets",columns, id)


@app.route("/ticket", methods=["POST"])
def setTicket():
    return setRow("Tickets")


@app.route("/ticket/<id>", methods=["PUT"])
def updateTicket(id):
    return updateRow("Tickets", id)


#-----------------------------------------
#---------------- Ventas ----------------


@app.route("/sales", methods=["GET"])
def getSales():
    columns = ["Ticket", "Insumo", "Cantidad"]
    return getRows("Ventas", columns)


@app.route("/sale/<id>", methods=["GET"])
def getSaleById(id):
    columns = ["Ticket", "Insumo", "Cantidad"]
    return getRowById("Ventas",columns, id)


@app.route("/sale", methods=["POST"])
def setSale():
    return setRow("Ventas")


@app.route("/sale/<id>", methods=["PUT"])
def updateSale(id):
    return updateRow("Ventas", id)


@app.route("/sale/<id>", methods=["DELETE"])
def deletSale(id):
    return deleteRow("Ventas", id)


#---------------------------------------------
#---------------- Privilegios ----------------


@app.route("/privileges", methods=["GET"])
def getPrivileges():
    columns = ["id", "Descripcion"]
    return getRows("Privilegios", columns)


@app.route("/privilege/<id>", methods=["GET"])
def getPrivilegeById(id):
    columns = ["id", "Descripcion"]
    return getRowById("Privilegios",columns, id)


#------------------------------------------
#---------------- Acciones ----------------


@app.route("/actions", methods=["GET"])
def getActions():
    columns = ["id", "Descripcion", "Privilegio"]
    return getRows("Acciones", columns)


@app.route("/action/<id>", methods=["GET"])
def getActionById(id):
    columns = ["id", "Descripcion", "Privilegio"]
    return getRowById("Acciones",columns, id)


#--------------------------------------------------
#---------------- Acciones Tomadas ----------------


@app.route("/actionsTaken", methods=["GET"])
def getActionsTaken():
    columns = ["id", "Usuario", "Accion", "Fecha", "Descripcion"]
    return getRows("AccionesTomadas", columns)


@app.route("/actionTaken/<id>", methods=["GET"])
def getActionTakenById(id):
    columns = ["id", "Usuario", "Accion", "Fecha", "Descripcion"]
    return getRowById("AccionesTomadas",columns, id)


@app.route("/actionTaken", methods=["POST"])
def setActionTaken():
    return setRow("AccionesTomadas")


#---------------------------------------------
#---------------- Inventarios ----------------


@app.route("/inventories", methods=["GET"])
def getInventories():
    columns = ["id", "Fecha"]
    return getRows("Inventarios", columns)


@app.route("/inventory/<id>", methods=["GET"])
def getInventoryById(id):
    columns = ["id", "Fecha"]
    return getRowById("Inventarios",columns, id)


@app.route("/inventory", methods=["POST"])
def setInventory():
    return setRow("Inventarios")


@app.route("/inventory/<id>", methods=["PUT"])
def updateInventory(id):
    return updateRow("Inventarios", id)


#-------------------------------------------------------
#---------------- Insumos Inventariados ----------------


@app.route("/inventoriedSupplies", methods=["GET"])
def getInventoriedSupplies():
    columns = ["id", "Inventario", "Insumo", "CantidadCalculada", "CantidadIngresada"]
    return getRows("InsumosInventariados", columns)


@app.route("/inventoriedSupplie/<id>", methods=["GET"])
def getInventoriedSupplieById(id):
    columns = ["id", "Inventario", "Insumo", "CantidadCalculada", "CantidadIngresada"]
    return getRowById("InsumosInventariados",columns, id)


@app.route("/inventoriedSupplie", methods=["POST"])
def setInventoriedSupplie():
    return setRow("InsumosInventariados")


@app.route("/inventoriedSupplie/<id>", methods=["PUT"])
def updateInventoriedSupplie(id):
    return updateRow("InsumosInventariados", id)






if __name__ == "__main__":
    app.run(debug=True, port=5000)