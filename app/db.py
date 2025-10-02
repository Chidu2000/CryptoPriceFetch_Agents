
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy.sql import func


database_url = "sqlite:///database.db"    # configure 
engine = create_engine(database_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    source = Column(String)
    published_at = Column(DateTime)
    content = Column(String)
    # coin = Column(String, index=True)
    sentiment_score = Column(Float, nullable=True)

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())  # FIXED    horizon_hours = Column(Integer)
    pred_label = Column(String)
    probability = Column(Float)
    ground_truth = Column(Float, nullable=True)
    correct = Column(Boolean, nullable=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def log_prediction(db,symbol,timestamp, pred_label, probability, ground_truth=None, correct=None):
    pred = Prediction(
        symbol=symbol,
        timestamp=timestamp,
        pred_label=pred_label,
        probability=probability,
        ground_truth=ground_truth,
        correct=correct
    )
    db.add(pred)
    db.commit()
    db.refresh(pred)
    return pred

    
    
    
    
    
    
    
