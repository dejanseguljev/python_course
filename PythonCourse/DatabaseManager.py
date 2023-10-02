import sqlalchemy as db

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
    training_functions = db.Table("training_functions", meta_data, 
      db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
      db.Column("x", db.Float, nullable=True),
      db.Column("y1", db.Float, nullable=True),
      db.Column("y2", db.Float, nullable=True),
      db.Column("y3", db.Float, nullable=True),
      db.Column("y4", db.Float, nullable=True))    
    ideal_functions = db.Table("ideal_functions", meta_data, 
      db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
      db.Column("x", db.Float, nullable=True),
      db.Column("y1", db.Float, nullable=True),
      db.Column("y2", db.Float, nullable=True),
      db.Column("y3", db.Float, nullable=True),
      db.Column("y4", db.Float, nullable=True),
      db.Column("y5", db.Float, nullable=True),     
      db.Column("y6", db.Float, nullable=True),
      db.Column("y7", db.Float, nullable=True),
      db.Column("y8", db.Float, nullable=True),
      db.Column("y9", db.Float, nullable=True),
      db.Column("y10", db.Float, nullable=True),
      db.Column("y11", db.Float, nullable=True),
      db.Column("y12", db.Float, nullable=True),
      db.Column("y13", db.Float, nullable=True),
      db.Column("y14", db.Float, nullable=True),
      db.Column("y15", db.Float, nullable=True),    
      db.Column("y16", db.Float, nullable=True),
      db.Column("y17", db.Float, nullable=True),
      db.Column("y18", db.Float, nullable=True),
      db.Column("y19", db.Float, nullable=True),
      db.Column("y20", db.Float, nullable=True),
      db.Column("y21", db.Float, nullable=True),
      db.Column("y22", db.Float, nullable=True),
      db.Column("y23", db.Float, nullable=True),
      db.Column("y24", db.Float, nullable=True),
      db.Column("y25", db.Float, nullable=True),
      db.Column("y26", db.Float, nullable=True),
      db.Column("y27", db.Float, nullable=True),
      db.Column("y28", db.Float, nullable=True),
      db.Column("y29", db.Float, nullable=True),
      db.Column("y30", db.Float, nullable=True),
      db.Column("y31", db.Float, nullable=True),
      db.Column("y32", db.Float, nullable=True),
      db.Column("y33", db.Float, nullable=True),
      db.Column("y34", db.Float, nullable=True),
      db.Column("y35", db.Float, nullable=True),
      db.Column("y36", db.Float, nullable=True),
      db.Column("y37", db.Float, nullable=True),
      db.Column("y38", db.Float, nullable=True),
      db.Column("y39", db.Float, nullable=True),
      db.Column("y40", db.Float, nullable=True),
      db.Column("y41", db.Float, nullable=True),
      db.Column("y42", db.Float, nullable=True),
      db.Column("y43", db.Float, nullable=True),
      db.Column("y44", db.Float, nullable=True),
      db.Column("y45", db.Float, nullable=True),   
      db.Column("y46", db.Float, nullable=True),
      db.Column("y47", db.Float, nullable=True),
      db.Column("y48", db.Float, nullable=True),
      db.Column("y49", db.Float, nullable=True),
      db.Column("y50", db.Float, nullable=True))     
             
    test_functions = db.Table("test_functions", meta_data, 
      db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
      db.Column("x", db.Float, nullable=True),
      db.Column("y", db.Float, nullable=True),
      db.Column("delta_y", db.Float, nullable=True),
      db.Column("ideal_count", db.Integer, nullable=True))          

    meta_data.create_all(engine)    


  def loadData(self):
   # ideal_provider = IdealDataProvider(self.connection_string, self.ideal_csv_path, self.ideal_table_name)  
   # ideal_provider.loadData()   

    training_provider = TrainingDataProvider(self.connection_string, self.training_csv_path, self.training_table_name) 
    training_provider.loadData()           
       




