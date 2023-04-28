import json
from pathlib import Path
import pandas as pd

review_cols = ["asin","date","id","name","rating","review","title","verified_purchase"]

def get_jsondata(data_path: str = "test_response.json") -> json:
    with open(data_path, "r") as f:
        data = json.load(f)
    return data

jsondata = get_jsondata("response2.json")

def extract_data_from_review(dict) -> list:
    return [
        dict["asin"]["original"],
        dict["date"]["date"],
        dict["id"],
        dict["name"],
        dict["rating"],
        dict["review"],
        dict["title"],
        dict["verified_purchase"],
    ]

# sum acts as a concatinator for any number of lists, needs a default empty list to start with
reviews_ls = []
for x in jsondata:
    if "result" not in x:
        continue
    # list.append(1,2,3) - Adds the tupple as one element to the list
    # list.extend(1,2,3) - Adds 3 elements to the list
    # Each page here has 10 reviews and we want each review to be an item in the list, hence using extend function
    reviews_ls.extend(list(map(extract_data_from_review,x["result"])))

reviews = pd.DataFrame(
    reviews_ls,
    columns=review_cols,
)

reviews['total_review'] = 'Title: ' + reviews['title'] + ' Review: ' + reviews['review']

reviews.to_csv('reviews_csv.csv',index = False)