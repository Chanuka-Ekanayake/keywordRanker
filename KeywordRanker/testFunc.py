from pytrends.request import TrendReq

# Initialize Pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Input keyword
keyword = "technology"

# Build the payload with the keyword
pytrends.build_payload(
    kw_list=[keyword],  # Keyword list
    cat=0,              # Default category
    timeframe='today 12-m',  # Last 12 months
    geo='LK',           # Sri Lanka
    gprop=''            # Default (web search)
)

# Get interest by region
interest_by_region = pytrends.interest_by_region(resolution='REGION')

# Check if data is available
if not interest_by_region.empty:
    # Sort regions by popularity in descending order
    # top_regions = interest_by_region.sort_values(by=keyword, ascending=False)
    # print(f"\nTop regions for the keyword '{keyword}':")
    print(interest_by_region) 
    
    # regions = top_regions.index.tolist()
    # print(regions)
else:
    print(f"\nNo data available for the keyword '{keyword}'.")

