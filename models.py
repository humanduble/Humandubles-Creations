from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, Sequence('video_id_seq'), primary_key=True)
    title = Column(String(200), nullable=False)  # Increased length to accommodate longer titles
    thumbnail = Column(String(250))
    url = Column(String(250))

engine = create_engine('sqlite:///db/videos.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
