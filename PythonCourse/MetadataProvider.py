import sqlalchemy as db

class MetadataProvider(object):
    @staticmethod    
    def createTrainingMetadata(meta_data):
      return db.Table("training_functions", meta_data, 
        db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
        db.Column("x", db.Float, nullable=True),
        db.Column("y1", db.Float, nullable=True),
        db.Column("y2", db.Float, nullable=True),
        db.Column("y3", db.Float, nullable=True),
        db.Column("y4", db.Float, nullable=True))          

    def createIdealMetadata(meta_data):
      return db.Table("training_functions", meta_data, 
        db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
        db.Column("x", db.Float, nullable=True),
        db.Column("y1", db.Float, nullable=True),
        db.Column("y2", db.Float, nullable=True),
        db.Column("y3", db.Float, nullable=True),
        db.Column("y4", db.Float, nullable=True))       




