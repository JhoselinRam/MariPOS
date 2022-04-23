import sqlite3 as sql

def getRows(name, table, columns = []):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    query = f"SELECT {'*' if len(columns)==0 else ', '.join(columns)} FROM {table};"
    cursor.execute(query)
    columNames = [description[0] for description in cursor.description]
    data = cursor.fetchall()
    rows = [{columnName:columnValue for columnName, columnValue in zip(columNames, row)} for row in data]
    
    connection.commit()
    connection.close()

    return rows


def getRowBy(name, table, identifier, columns = []):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    query = f"SELECT {'*' if len(columns)==0 else ', '.join(columns)} FROM {table}\
                     WHERE {identifier[0]}{'=' if len(identifier)<3 else identifier[2]}{identifier[1]};"
    cursor.execute(query)
    columNames = [description[0] for description in cursor.description]
    data = cursor.fetchall()
    rows = [{columnName:columnValue for columnName, columnValue in zip(columNames, row)} for row in data]
    
    connection.commit()
    connection.close()

    return rows


def setNewRow(name, table, entries):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    for entry in entries:
        columnNames = list(entry.keys())
        data = tuple(entry.values())
        query =  f"INSERT INTO {table} ({', '.join(columnNames)}) \
                VALUES ({','.join(['?' for column in columnNames])})"
        cursor.execute(query, data)

    connection.commit()
    connection.close()


def updateRow(name, table, identifiers, entries):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    for entry, identifier in zip(entries, identifiers):
        columnNames = list(entry.keys())
        data = tuple(entry.values())
        query =  f"UPDATE {table} SET {', '.join([f'{column} = ?' for column in columnNames])} WHERE {identifier[0]}{'=' if len(identifier)<3 else identifier[2]}{identifier[1]};"
        cursor.execute(query, data)
    
    connection.commit()
    connection.close()


def deleteRow(name,table,identifiers):
    connection = sql.connect(name)
    connection.execute("PRAGMA foreign_keys = 1")
    cursor = connection.cursor()

    for identifier in identifiers:
        query = f"DELETE FROM {table} WHERE {identifier[0]}{'=' if len(identifier)<3 else identifier[2]}{identifier[1]};"
        cursor.execute(query)

    connection.commit()
    connection.close()
