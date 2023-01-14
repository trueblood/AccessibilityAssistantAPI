from app.pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["website_info"]

class DatabaseHelper():
    # write to database
    def writeToDatabase(id, website, element, cleaned, type, question):   
        item = {
                "id": id,
                "element": str(element),
                "website": str(website),
                "cleaned": str(cleaned),
                "type": str(type),
                "question": str(question)
            }   
        collection_name.insert_one(item)

    def findDataByQuestion(question, website):
        item_details = collection_name.find({"$and": [{"question": question}, {"website": website}]}).limit(1)
        value = ""
        for item in item_details:
            value = item['cleaned']
        return value