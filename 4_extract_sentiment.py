import json
from pathlib import Path
import pandas as pd
import utility

sentimentdata = utility.get_jsondata('sample_llmoutput.json')
sentimentdata['aspects']

def get_sentiments_todf(data: dict) -> pd.DataFrame:
    sentimentdatals = []
    for key, value in data['aspects'].items():
        sentimentdatals.append([key, value['sentiment'],value['justification']])
    return pd.DataFrame(sentimentdatals, columns= ['aspect', 'sentiment', 'justification'])

get_sentiments_todf(sentimentdata)