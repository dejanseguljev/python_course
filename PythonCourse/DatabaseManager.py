import sqlalchemy as db
from IdealDataProvider import IdealDataProvider
from MetadataProvider import MetadataProvider

from TrainingDataProvider import TrainingDataProvider

class DatabaseManager(object):
  connection_string = "mysql+pymysql://root:admin@localhost/assignment"  
  ideal_csv_path = r"C:\Development\Research\PythonCourse\Docs\ideal.csv" 
  ideal_table_name = "ideal_functions"  
  training_csv_path = r"C:\Development\Research\PythonCourse\Docs\train.csv"     
  training_table_name = "training_functions"  
  
  def createDatabase(self):
    engine = db.create_engine(self.connection_string)
    connection = engine.connect()
    meta_data = db.MetaData()
    
    training_functions = MetadataProvider.createTrainingMetadata(meta_data)    
    ideal_functions = MetadataProvider.createIdealMetadata(meta_data)                
    test_functions = MetadataProvider.createTestMetadata(meta_data)       

    meta_data.create_all(engine)    


  def loadData(self):
   ideal_provider = IdealDataProvider(self.connection_string, self.ideal_csv_path, self.ideal_table_name)  
   ideal_provider.loadData()   

    # training_provider = TrainingDataProvider(self.connection_string, self.training_csv_path, self.training_table_name) 
    # training_provider.loadData()           
       




