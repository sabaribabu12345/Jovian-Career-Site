from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://2CtnWCmGkgYWAib.root:hLqA84dOZrVRsY6p@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/joviancareers"

engine = create_engine(DATABASE_URL, echo=True)


        