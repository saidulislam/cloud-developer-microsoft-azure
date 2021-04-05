import logging

import azure.functions as func
import pymongo
import os
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger deleteAdvertisement function processed a request.')
    
    id = req.params.get('id')

    if id:
        try:
            url = os.environ['SIMongoDBConnection']
            client = pymongo.MongoClient(url)
            database = client['neighborlyapp']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string", status_code=400)