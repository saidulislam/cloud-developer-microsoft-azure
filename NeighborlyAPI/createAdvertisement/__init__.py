import logging

import azure.functions as func
import pymongo
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger createAdvertisement function processed a request.')
    request = req.get_json()

    if request:
        try:
            url = os.environ['SIMongoDBConnection']
            client = pymongo.MongoClient(url)
            database = client['neighborlyapp']
            collection = database['advertisements']

            record_id = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse("Please pass name in the body", status_code=400)
