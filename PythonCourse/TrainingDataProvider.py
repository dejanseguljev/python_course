from DataProvider import DataProvider
from MetadataProvider import MetadataProvider

class TrainingDataProvider(DataProvider):
      def __init__(self, connection_string, csvPath, table_name):
        super().__init__(connection_string, csvPath, table_name)   
      def prepareData(self, data_list):
        return list(map(lambda x: {"x":x[0], "y1":x[1], "y2":x[2], "y3":x[3], "y4":x[4]}, data_list.values.tolist()))        
              
      def createMetadata(self, table_name, meta_data):
        return MetadataProvider.createTrainingMetadata(meta_data)
