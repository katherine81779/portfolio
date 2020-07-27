import json
import urllib.parse
from urllib.request import Request, urlopen
import requests

# Majority of the time I used in this project was spent on finding an API that was 
# free of charge and could tell us more information about the car. 
# Initially we wanted a picture of the car to tell the user that this website knows
# what car the user is trying to get a rating of. However, we realized that the API
# we found for imaging was inaccurate. We decided to move on and found a query that could
# help us at least display some information given the brand, model, and year of the car.

BASE_URL = 'https://www.carqueryapi.com/api/0.3/?cmd=getTrims&' # this is to get the model id


def getBasicURL(brand, model, year):
    query_parameters = [('make', brand), ('model', model), ('year', year)]
    theStatement = BASE_URL + urllib.parse.urlencode(query_parameters)
    return theStatement
    
def getBasicResult(url):
    response = Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
    json_text = urlopen(response).read()
    return json.loads(json_text)

def getCarDictBase(searchInfo):
    carDict = searchInfo['Trims'][0]
    return carDict
