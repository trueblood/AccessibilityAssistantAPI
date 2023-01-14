import pandas as pd
import re

class Matcher:
# this function is used to get printable results
    def getResults(questions, fn):
        def getResult(q):
            answer = fn(q)
            return [answer]
        return pd.DataFrame(list(map(getResult, questions)), columns=["A"])
    
 
    def getNaiveAnswer(q):
        data = pd.read_json('data/data.json')
        # regex helps to pass some punctuation signs
        row = data.loc[data['question'].str.contains(re.sub(r"[^\w'\s)]+", "", q),case=False)]
        if len(row) > 0:
            return row["id"].values[0]
        return "Sorry, I didn't get you.", 0, ""

 