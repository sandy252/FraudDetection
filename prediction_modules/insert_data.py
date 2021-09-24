import pymongo
import pandas as pd
import json
from prediction_modules.logger import log_class
import pymongo

folder_path = './log_files/'
file_name = 'log_file.txt'

logger = log_class(folder_path,file_name)
logger.create_log_file("Sending data to the database")
client = pymongo.MongoClient("localhost:27017")
df = pd.read_csv("creditcard.csv")
data = df.to_dict(orient = "records")
db = client["fraud_transaction"]
db.creditcardfraud.insert_many(data)
logger.create_log_file("Data successfully inserted to the database")


