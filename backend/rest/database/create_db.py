import sqlite3 as sql

def main():
    dbName = "marisons.db"
    createDB(dbName)

    createTable_Proveedores(dbName)
    createTable_Grupos(dbName)
    createTable_Subgrupos(dbName)
    createTable_Insumos(dbName)
    createTable_Clientes(dbName)
    createTable_Tickets(dbName)
    createTable_Ventas(dbName)
    createTable_Privilegios(dbName)
    createTable_Usuarios(dbName)
    createTable_Acciones(dbName)
    createTable_AccionesTomadas(dbName)
    createTable_Inventarios(dbName)
    createTable_InsumosInventariados(dbName)
    addDefaultValues(dbName)





def createDB(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    connection.commit()
    connection.close() 

def createTable_Proveedores(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Proveedores(
            id INTEGER PRIMARY KEY,
            Descripcion TEXT NO NULL UNIQUE,
            RFC TEXT NO NULL UNIQUE
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Grupos(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Grupos(
            id INTEGER PRIMARY KEY,
            Descripcion TEXT NO NULL UNIQUE
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Subgrupos(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Subgrupos(
            id INTEGER PRIMARY KEY,
            Descripcion TEXT NO NULL UNIQUE,
            Grupo INTEGER DEFAULT 1,
            FOREIGN KEY(Grupo) REFERENCES Grupos(id)
            ON DELETE SET DEFAULT
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Insumos(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Insumos(
            id INTEGER PRIMARY KEY,
            Descripcion TEXT NO NULL UNIQUE,
            Unidad TEXT NO NULL,
            UnidadPorPaquete REAL NO NULL,
            CostoPorUnidad REAL NO NULL,
            CostoPublicoPorUnidad REAL NO NULL,
            Existencia REAL NO NULL,
            Grupo INTEGER DEFAULT 1,
            Subgrupo INTEGER DEFAULT 1,
            Proveedor INTEGER DEFAULT 1,
            Activo INTEGER NO NULL,
            FOREIGN KEY(Grupo) REFERENCES Grupos(id)
            ON DELETE SET DEFAULT,
            FOREIGN KEY(Subgrupo) REFERENCES Subgrupos(id)
            ON DELETE SET DEFAULT,
            FOREIGN KEY(Proveedor) REFERENCES Proveedores(id)
            ON DELETE SET DEFAULT
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Clientes(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Clientes(
            id INTEGER PRIMARY KEY,
            Nombre TEXT NO NULL,
            Telefono TEXT NO NULL,
            Direccion TEXT NO NULL,
            Colonia TEXT NO NULL,
            Cruzamiento1 TEXT,
            Cruzamiento2 TEXT
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Tickets(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Tickets(
            id INTEGER PRIMARY KEY,
            Total REAL NO NULL,
            Fecha TEXT NO NULL,
            Cliente INTEGER DEFAULT 1,
            Cancelado INTEGER NO NULL DEFAULT 0,
            FOREIGN KEY(Cliente) REFERENCES Clientes(id)
            ON DELETE SET DEFAULT
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Ventas(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Ventas(
            Ticket INTEGER,
            Insumo INTEGER DEFAULT 1,
            Cantidad REAL NO NULL,
            FOREIGN KEY(Ticket) REFERENCES Tickets(id),
            FOREIGN KEY(Insumo) REFERENCES Insumos(id) 
            ON DELETE SET DEFAULT,
            CONSTRAINT VentasPK PRIMARY KEY(Ticket, Insumo)
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Privilegios(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Privilegios(
            id INTEGER PRIMARY KEY,
            Descripcion TEXT NO NULL
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Usuarios(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Usuarios(
            id INTEGER PRIMARY KEY,
            Nombre TEXT NO NULL UNIQUE,
            Privilegio INTEGER,
            FOREIGN KEY(Privilegio) REFERENCES Privilegios(id)
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Acciones(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Acciones(
            id INTEGER PRIMARY KEY,
            Descripcion TEXT NO NULL,
            Privilegio INTEGER,
            FOREIGN KEY(Privilegio) REFERENCES Privilegios(id)
        )"""
    )
    connection.commit()
    connection.close()

def createTable_AccionesTomadas(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE AccionesTomadas(
            id INTEGER PRIMARY KEY,
            Usuario INTEGER DEFAULT 1,
            Accion INTEGER,
            Fecha TEXT NO NULL,
            Descripcion TEXT,
            FOREIGN KEY(Usuario) REFERENCES Usuarios(id)
            ON DELETE SET DEFAULT,
            FOREIGN KEY(Accion) REFERENCES Acciones(id)
        )"""
    )
    connection.commit()
    connection.close()

def createTable_Inventarios(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Inventarios(
            id INTEGER PRIMARY KEY,
            Fecha TEXT NO NULL,
            Eliminado INTEGER NO NULL DEFAULT 0
        )"""
    )
    connection.commit()
    connection.close()

def createTable_InsumosInventariados(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE InsumosInventariados(
            id INTEGER PRIMARY KEY,
            Inventario INTEGER,
            Insumo INTEGER DEFAULT 1,
            CantidadCalculada REAL NO NULL,
            CantidadIngresada REAL NO NULL,
            FOREIGN KEY(Inventario) REFERENCES Inventarios(id),
            FOREIGN KEY(Insumo) REFERENCES Insumos(id)
            ON DELETE SET DEFAULT
        )"""
    )
    connection.commit()
    connection.close()

def addDefaultValues(name):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()
    cursor.execute(
        """INSERT INTO Proveedores (Descripcion, RFC) 
           VALUES ('Proveedor Eliminado', 'No encontrado')"""
    )

    cursor.execute(
        """INSERT INTO Grupos (Descripcion) 
           VALUES ('Grupo Eliminado')"""
    )

    cursor.execute(
        """INSERT INTO Subgrupos (Descripcion) 
           VALUES ('Subgrupo Eliminado')"""
    )

    cursor.execute(
        """INSERT INTO Insumos (Descripcion, Unidad, UnidadPorPaquete, CostoPorUnidad, CostoPublicoPorUnidad, Existencia, Activo) 
           VALUES ('Insumo Eliminado', 'No encontrado', 0, 0, 0, 0, 0)"""
    )

    cursor.execute(
        """INSERT INTO Clientes (Nombre, Telefono, Direccion, Colonia) 
           VALUES ('Cliente Eliminado', 'No encontrado', 'No encontrado', 'No encontrado')"""
    )

    cursor.execute(
        """INSERT INTO Clientes (Nombre, Telefono, Direccion, Colonia) 
           VALUES ('Invitado', 'No aplica', 'No aplica', 'No aplica')"""
    )

    cursor.executemany(
        "INSERT INTO Privilegios (Descripcion) VALUES (?);",[
            ("Inactivo",),
            ("Cajero",),
            ("Gerente",),
            ("Administrador",)
        ]
    )

    cursor.execute(
        """INSERT INTO Usuarios (Nombre, Privilegio) 
           VALUES ('Usuario Eliminado', 1)"""
    )

    cursor.executemany(
        "INSERT INTO Acciones (Descripcion, Privilegio) VALUES (?, ?);",[
            ("Cancelacion de venta", 3),
            ("Restauracion de venta", 3),
            ("Apertura de turno", 2),
            ("Corte X", 2),
            ("Corte Y", 2),
            ("Descuento", 3),
            ("Añadir insumo", 4),
            ("Modificar insumo", 4),
            ("Eliminar insumo", 4),
            ("Añadir proveedor", 4),
            ("Modificar proveedor", 4),
            ("Eliminar proveedor", 4),
            ("Añadir grupo", 4),
            ("Modificar grupo", 4),
            ("Eliminar grupo", 4),
            ("Añadir subgrupo", 4),
            ("Modificar subgrupo", 4),
            ("Eliminar subgrupo", 4),
            ("Añadir cliente", 2),
            ("Modificar cliente", 3),
            ("Eliminar cliente", 4),
            ("Añadir usuario", 4),
            ("Modificar usuario", 4),
            ("Eliminar usuario", 4),
            ("Extraer reporte", 3),
            ("Ingresar Inventario", 3),
            ("Modificar Inventario", 4),
            ("Eliminar Inventario", 4)
        ]
    )

    connection.commit()
    connection.close()



if __name__ == "__main__":
    main()