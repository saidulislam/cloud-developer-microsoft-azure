import logging

import azure.functions as func
import pymongo
import os
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger getAdvertisements function processed a request.')

    try:
        url = os.environ['SIMongoDBConnection']
        client = pymongo.MongoClient(url)
        database = client['neighborlyapp']
        collection = database['advertisements']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb", status_code=400)