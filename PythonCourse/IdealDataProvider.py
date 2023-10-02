from DataProvider import DataProvider
from MetadataProvider import MetadataProvider

class IdealDataProvider(DataProvider):
      def __init__(self, connection_string, csv_path, table_name):
        super().__init__(connection_string, csv_path, table_name)        

      def prepareData(self, data_list):
        return list(map(lambda x: {"x":x[0], "y1":x[1], "y2":x[2], "y3":x[3], "y4":x[4], "y5":x[5], "y6":x[6], "y7":x[7], "y8":x[8], "y9":x[9], "y10":x[10], "y11":x[11], "y12":x[12], "y13":x[13], "y14":x[14], "y15":x[15], "y16":x[16], "y17":x[17], "y18":x[18], "y19":x[19], "y20":x[20], "y21":x[21], "y22":x[22], "y23":x[23], "y24":x[24], "y25":x[25], "y26":x[26], "y27":x[27], "y28":x[28], "y29":x[29], "y30":x[30], "y31":x[31], "y32":x[32], "y33":x[33], "y34":x[34], "y35":x[35], "y36":x[36], "y37":x[37], "y38":x[38], "y39":x[39], "y40":x[40], "y41":x[41], "y42":x[42], "y43":x[43], "y44":x[44], "y45":x[45], "y46":x[46], "y47":x[47], "y48":x[48], "y49":x[49], "y50":x[50]}, data_list.values.tolist()))        
              
      def createMetadata(self, table_name, meta_data):
        return MetadataProvider.createIdealMetadata(meta_data)        




