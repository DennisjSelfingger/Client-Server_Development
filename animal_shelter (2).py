from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    # Creating a class to handle CRUD operations for the animal shelter database
    
    def __init__(self, username, password):
        # Setting up MongoDB connection details
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30568
        DB = 'AAC'
        COL = 'animals'        
        # Connecting to MongoDB with my credentials
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        # Adding new animals to database
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Error creating entry: {e}")
                return False
        else:
            raise Exception("No data to save")

    def read(self, search_criteria):
        # Finding animals that match search terms
        if search_criteria is not None:
            try:
                results = self.collection.find(search_criteria)
                return list(results)
            except Exception as e:
                print(f"Error finding animals: {e}")
                return []
        else:
            raise Exception("Need search criteria")

    def update(self, search_criteria, update_data):
        # Updating animal info in database
        if search_criteria is not None and update_data is not None:
            try:
                result = self.collection.update_many(search_criteria, {"$set": update_data})
                return result.modified_count
            except Exception as e:
                print(f"Error updating animals: {e}")
                return 0
        else:
            raise Exception("Need both search criteria and update data")

    def delete(self, search_criteria):
        # Removing animals from database when adopted
        if search_criteria is not None:
            try:
                result = self.collection.delete_many(search_criteria)
                return result.deleted_count
            except Exception as e:
                print(f"Error deleting animals: {e}")
                return 0
        else:
            raise Exception("Need search criteria")