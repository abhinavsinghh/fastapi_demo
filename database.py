from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_link = 'postgresql://postgres:12345678@localhost:5432/abhinav'
engine = create_engine(db_link)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)