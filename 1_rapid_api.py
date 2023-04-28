#@ Title using rapid API's amazon reviews freemium API. Here - https://rapidapi.com/restyler/api/amazon23
import requests # Need this to scrape websites
from pathlib import Path # dealing with file paths
import json # writing reviews to json file format 

def get_product_review(asin:str, page_nbr: int) -> dict:
    # This code along with pagination is from Rapid API Amazon reviews API
    # When you call this function, it extracts reviews for specified product for specified page
    url = "https://amazon23.p.rapidapi.com/reviews"

    querystring = {"asin":asin,"sort_by":"helpful","page":str(page_nbr),"country":"US"}

    headers = {
        "X-RapidAPI-Key": "Insert-your-key-here",
        "X-RapidAPI-Host": "amazon23.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()


if __name__ == '__main__':
    # Incase the response.json doesn't exist, create it
    if not Path('./response.json').exists():
        Path('./response.json').touch()
    # Add the response results to the product_reviews list
    product_reviews = []
    # Paginate to get as many reviews as allowed by API subscription
    for page_nbr in range(1, 50):
        # In case API doesn't provide a response, try again going to the next page of reviews
        try:
            product_reviews.append(get_product_review('B09R95CGSW', page_nbr))
        except Exception:
            pass
    # Write the json file to local 
    Path('./response.json').write_text(json.dumps(product_reviews))
    print(Path('./response.json').absolute())