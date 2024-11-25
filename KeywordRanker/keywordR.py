from pytrends.request import TrendReq
import pandas as pd

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
        

        intrest_by_city = pytrends.interest_by_region(resolution='CITY')
        

        



