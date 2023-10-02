import pandas as pd
import sqlalchemy as db
from sqlalchemy import insert

class DataProvider(object):
    connection_string = ""    
    csvPath = ""    
    table_name = ""
        
    def __init__(self, connection_string, csvPath, table_name):
      self.connection_string = connection_string        
      self.csvPath = csvPath        
      self.table_name = table_name      
      
    def prepareData(self, data_list):
      return data_list         

    def createMetadata(self, table_name, meta_data):
      return db.Table(table_name, meta_data)
    
    def loadData(self):
      try:    
        engine = db.create_engine(self.connection_string)
        connection = engine.connect()
        meta_data = db.MetaData()

        target_table = self.createMetadata(self.table_name, meta_data)                

        data_list = self.__loadFromCSV(self.csvPath);
        data_list = self.prepareData(data_list);           

        result = connection.execute(insert(target_table), data_list)
        connection.commit()        

      except Exception as e:
        print (e)                
                
    def __loadFromCSV(self, path):
      return pd.read_csv(filepath_or_buffer=path)         




