import pandas as pd
from pytrends.request import TrendReq

# Initialize Pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Input keyword
keyword = input("Enter a keyword: ")

# List of cities (e.g., from a specific region)
cities = ["Colombo", "Dehiwala-Mount Lavinia", "Maharagama", "Kandy", "Galle"]

# Create an empty dictionary to store city scores
city_scores = {}

# Loop through each city and fetch the trend data
for city in cities:
    try:
        # Build payload with the city and keyword
        pytrends.build_payload(
            kw_list=[keyword],
            cat=0,
            timeframe='today 12-m',
            geo=f'LK',  # Country code for Sri Lanka
            gprop=''    # Default (web search)
        )
        
        # Get interest by region (resolution='CITY')
        interest_by_region = pytrends.interest_by_region(resolution='CITY')

        print(interest_by_region.head())  # Print the specific regions with the highest interest on the keyword

        # Check if city exists in the data
        # if city in interest_by_region.index:
        #     city_scores[city] = interest_by_region.loc[city, keyword]
        # else:
        #     city_scores[city] = 0  # Assign 0 if city data is not available
    except Exception as e:
        print(f"Error processing city {city}: {e}")
        city_scores[city] = 0

# # Convert dictionary to DataFrame
# df = pd.DataFrame(list(city_scores.items()), columns=["City", "Popularity Score"])

# # Sort DataFrame by "Popularity Score" in descending order
# df = df.sort_values(by="Popularity Score", ascending=False).reset_index(drop=True)

# # Display the DataFrame
# print(f"\nCities ranked by popularity for keyword '{keyword}':\n")
# print(df)
