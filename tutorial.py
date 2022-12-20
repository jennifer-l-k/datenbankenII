import pymongo
from pprint import pprint

# Connect to default database host
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Create new database table 
db = client['med_data']

# Create new collection to that database
my_collection = db['patient_data']

# Insert data in JavaScript Notation
patient_record = {
   "Name": "Maureen Skinner",
   "Age": 87,
   "Sex": "F",
   "Blood pressure": [{"sys": 156}, {"dia": 82}],
   "Heart rate": 82
}

# Add data in database collection
my_collection.insert_one(patient_record)

# Update data 
my_collection.update_one({"Name": "Maureen Skinner"}, {"$set":{"Name": "Maureen Jay Skinner"}})

# View content with 'python tutorial.py'
for item in my_collection.find():
    pprint(item)