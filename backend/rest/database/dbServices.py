from pymongo import MongoClient

def getDocuments(name, collection, fields = []):
    client = MongoClient("localhost")
    db     = client[name]

    showFiels = {field:1 for field in fields}
    if "_id" not in fields:
        showFiels["_id"] = 0

    documentCursor = db[collection].find() if len(fields)==0 else db[collection].find({},showFiels)
    documents = list(documentCursor)

    client.close()

    return documents


def getDocumentBy(name, collection, identifier, fields = []):
    client = MongoClient("localhost")
    db     = client[name]

    if len(identifier) == 2:
        identifier.append("$eq")
    elif identifier[2] == "=":
        identifier[2] = "$eq"
    elif identifier[2] == "!=":
        identifier[2] = "$ne"
    elif identifier[2] == "<":
        identifier[2] = "$lt"
    elif identifier[2] == ">":
        identifier[2] = "$gt"
    elif identifier[2] == "<=":
        identifier[2] = "$lte"
    elif identifier[2] == ">=":
        identifier[2] = "$gte"
    
    query = {identifier[0] : {identifier[2] : identifier[1]}}
    showFiels = {field:1 for field in fields}
    if "_id" not in fields:
        showFiels["_id"] = 0
    
    documentCursor = db[collection].find(query) if len(fields)==0 else db[collection].find(query,showFiels)
    documents = list(documentCursor)
    
    client.close()

    return documents


def setNewDocument(name, collection, documents):
    client = MongoClient("localhost")
    db     = client[name]

    for document in documents:
        db[collection].insert_one(document)

    client.close()


def updateDocument(name, collection, identifiers, documents):
    client = MongoClient("localhost")
    db     = client[name]

    for identifier in identifiers:
        if len(identifier) == 2:
            identifier.append("$eq")
        elif identifier[2] == "=":
            identifier[2] = "$eq"
        elif identifier[2] == "!=":
            identifier[2] = "$ne"
        elif identifier[2] == "<":
            identifier[2] = "$lt"
        elif identifier[2] == ">":
            identifier[2] = "$gt"
        elif identifier[2] == "<=":
            identifier[2] = "$lte"
        elif identifier[2] == ">=":
            identifier[2] = "$gte"

    queryes = [{identifier[0] : {identifier[2] : identifier[1]}} for identifier in identifiers]

    for query, document in zip(queryes, documents):
        db[collection].update_one(query,{"$set":document})
    
    client.close()


def deleteDocument(name,collection,identifiers):
    client = MongoClient("localhost")
    db     = client[name]

    for identifier in identifiers:
        if len(identifier) == 2:
            identifier.append("$eq")
        elif identifier[2] == "=":
            identifier[2] = "$eq"
        elif identifier[2] == "!=":
            identifier[2] = "$ne"
        elif identifier[2] == "<":
            identifier[2] = "$lt"
        elif identifier[2] == ">":
            identifier[2] = "$gt"
        elif identifier[2] == "<=":
            identifier[2] = "$lte"
        elif identifier[2] == ">=":
            identifier[2] = "$gte"
    
    queryes = [{identifier[0] : {identifier[2] : identifier[1]}} for identifier in identifiers]
    for query in queryes:
        db[collection].delete_one(query)

    client.close()
