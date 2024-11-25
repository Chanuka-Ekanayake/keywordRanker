from pytrends.request import TrendReq
import pandas as pd
import requests
import json

class keywordRanker:


    def __init__(self, keywords = "Business", region = "Western", time = "today 12-m", gprop = ' ', cat = 0):
        self.keyowrds = keywords
        self.region = region
        self.time = time
        self.gprop = gprop
        self.cat = cat

    def RegionbyKeyword(self):
        pytrends = TrendReq(hl='en-US', tz=360)

        pytrends.build_payload(
            self.keyowrds, 
            cat=self.cat,  #Default category - All
            timeframe = self.time, 
            geo="LK", 
            gprop= self.gprop) #Default gprop - Websearch
        

        intrest_by_region = pytrends.interest_by_region(resolution='REGION')

        if not intrest_by_region.empty:
            top_regions = intrest_by_region.sort_values(by=self.keyowrds[0], ascending=False).head(2)

    
    def importLocations(self, GeoapiKey):
        url = GeoapiKey
        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        response_data = json.loads(response.text)
        cities = [entry['name'] for entry in response_data['geonames']]

        print(len(cities))



        

        



