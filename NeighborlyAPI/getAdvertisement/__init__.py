import logging

import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

# example api call http://localhost:7071/api/getAdvertisement/?id=<some id>
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger getAdvertisement function processed a request.')

    id = req.params.get('id')
    
    if id:
        try:
            url = os.environ['SIMongoDBConnection']
            client = pymongo.MongoClient(url)
            database = client['neighborlyapp']
            collection = database['advertisements']
           
            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)

            result = dumps(result)
            print(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)