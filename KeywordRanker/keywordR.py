from pytrends.request import TrendReq
import pandas as pd
import requests
import json

class keywordRanker:


    def __init__(self, keywords = "Business", region = "Western", time = "today 12-m", gprop = ' ', cat = 0):
        self.keyowrds = keywords
        self.region = region
        self.time = time  #OPtions: 'now 1-H': Last hour, 'now 7-d': Last 7 days, 'today 1-m': Last 30 days, 'today 3-m': Last 90 days, 'today 12-m': Last 12 months, '2023-01-01 2023-12-31'
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
            top_regions = intrest_by_region.sort_values(by=self.keyowrds[0], ascending=False)
            
            print(top_regions.head()) #Prints the spesific regions with the highest interest on the keyword

    
    def importLocations(self, GeoapiKey):
        url = GeoapiKey
        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        response_data = json.loads(response.text)
        cities = [entry['name'] for entry in response_data['geonames']]

        print(len(cities))



        

        



