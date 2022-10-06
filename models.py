from enum import unique
import string
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, unique=True, nullable=False, index=True)
    
    experiments = relationship(
        "Experiment", back_populates="project", cascade="delete, merge, save-update")


class Experiment(Base):
    __tablename__ = "experiments"

    experiment_no = Column(Integer, primary_key=True, index=True)
    experiment_name = Column(String, nullable=False, index=True)
    
    experiment_config_path = Column(String)

    token = Column(String,  unique=True)


    project_id = Column(Integer, ForeignKey(
        "projects.project_id"), nullable=False)

    project = relationship("Project", back_populates="experiments")