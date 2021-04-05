import logging

import azure.functions as func
import pymongo
import os
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger updateAdvertisement function processed a request.')

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = os.environ['SIMongoDBConnection']
            client = pymongo.MongoClient(url)
            database = client['neighborlyapp']
            collection = database['advertisements']
            
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": eval(request)}
            record_id = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)