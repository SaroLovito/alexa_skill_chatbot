import requests
import os
import json

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# TOKEN = "Bearer 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"

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"


headers = {"Authorization": os.environ['TOKEN']}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")
    print(event)
    
    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
 
  
    topic =  event["currentIntent"]["slots"]["Topic"]
    prompt = f"About {topic} is what I think:"

    output = query({
        "inputs": prompt,
    })
    print(output)
    res_for_lex_2 = {
        #"sessionAttributes": event['sessionAttributes'],
        "dialogAction": {
            "fulfillmentState":"Fulfilled",
            "type":"Close",
            "message":
                {
                    "contentType":"PlainText",
                    "content": output[0]["generated_text"]
                }
        }
        
    }
    print(res_for_lex_2)
    return res_for_lex_2
