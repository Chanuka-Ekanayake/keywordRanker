from pytrends.request import TrendReq
import pandas as pd
import requests
import json

class keywordRanker:


    def __init__(self, keywords = [], region = [], time = "today 12-m", gprop = ' ', cat = 0):
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
        
        try:
            intrest_by_region = pytrends.interest_by_region(resolution='REGION')

            if not intrest_by_region.empty:
                top_regions = intrest_by_region.sort_values(by=self.keyowrds[0], ascending=False)
                
                print("--- Top Regions for the keyword {self.keywords}: ---".center(120))
                print(top_regions.head()) #Prints the spesific regions with the highest interest on the keyword


                regions_list = top_regions.index.tolist()

                top_region = regions_list[0].split(" ").strip()
                self.region = top_region
                
                print(top_regions.head()) #Prints the spesific regions with the highest interest on the keyword


            else:
                print("Sorry No data available for the keyword {slef.keywords}")

        except Exception as e:
            print("Sorry service is currentlty unavailable. Please try again later.")
            return
        


    
    def CityRankbyRegion(self):

        if not self.region:
            region = input("\nEnter the region/province : ")

            top_region = region.split(" ").strip()

            if len(top_region) > 2 or len(top_region) < 1:
                print("Invalid region/province. Please try again.")
                return
            
            elif len(top_region) == 1:
                top_region.append({"Province"})

            elif len(top_region) == 2:
                top_region[0] = top_region[0].capitalize()
                top_region[1] = top_region[1].capitalize()

                if not top_region[1] == "Province":
                    top_region[1] = "Province"

        else:
            top_region = self.region
                    


        cities = importLocations(f"https://api.geonames.org/searchJSON?q={top_region[0]}+{top_region[1]}&maxRows=1&username=demo")
        cityScore = {}

        pytrends = TrendReq(hl='en-US', tz=360)

        pytrends.build_payload(
            self.keyowrds, 
            cat=self.cat,  #Default category - All
            timeframe = self.time, 
            geo="LK", 
            gprop= self.gprop)
        
        

        try:
            intrest_by_city = pytrends.interest_by_region(resolution='CITY')

            if not intrest_by_city.empty:
                top_cities = intrest_by_city.sort_values(by=self.keyowrds[0], ascending=False)


                for city in cities:
                    for top_cities in top_cities.index:
                        if city in top_cities:
                            cityScore[city] = intrest_by_city.loc[city, self.keyowrds]
                            

            else:
                print("Sorry No data available for the keyword {slef.keywords}")

        
        except Exception as e:
            print("Sorry service is currentlty unavailable. Please try again later.")
            print("Error: ", e)
            citySscores[city] = 0
            return


def importLocations(GeoapiKey):
        url = GeoapiKey
        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        response_data = json.loads(response.text)
        cities = [entry['name'] for entry in response_data['geonames']]
        return cities

        # print(len(cities))


    
    



        

        



