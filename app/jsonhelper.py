import json
import os
import time
import random

class JsonHelper():

    def write_to_json(id, element, cleaned, type, question):
    
    # Read Existing JSON File
        with open('./data/data.json') as f:
            data = json.load(f)
        
        # Append new object to list data
        data.append({
                "id": id,
                "element": str(element),
                "cleaned": str(cleaned),
                "type": str(type),
                "question": str(question)
            })
        
        # Create new JSON file
        with open('./data/data.json', 'w') as f:
            json.dump(data, f, indent=2)
        
        # Closing file
        f.close()

    def read_from_json():
        # Opening JSON file
        f = open('./data/data.json')
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        
        # Iterating through the json
        # list
        for i in data:
            #print(i['id'])
            print(i)
        
        # Closing file
        f.close()

    def read_from_json_data():
        f = open('./data/data.json')
        data = json.load(f)
        value = ""
        for i in data:
            value = i['cleaned']
        return value

    def get_json_byQuestion(question):
        path_to_file = "./data/data.json";

        with open(path_to_file) as data_file:
            data = json.load(data_file)
        length = (len(data))
        id = question
        for x in range(length):
            currentValue = data[x]["id"]
            if (str(currentValue) == id):
                return data[x]["cleaned"]
   

    def write_machinelearning_questions(data):
        fname = "./data/machinelearningdata.json"
        if os.path.exists(fname):
            #read existing file and append new data
            with open(fname,"r") as f:
                loaded = json.load(f)
            #loaded.append({'appended': time.time()})
        else:
            #create new json
            loaded = [data]

        #overwrite/create file
        with open(fname,"w") as f:
            json.dump(loaded,f)

        #clean up the brackets after the json file is created or appended too
        if os.path.exists(fname):
            #read existing file and append new data
            with open(fname,"r") as f:
                loaded = json.load(f)

    def write_machinelearning_questions_toFile(data):        
        with open("./data/machinelearningdata.json", "w") as outfile:
            json.dump(data, outfile)
   