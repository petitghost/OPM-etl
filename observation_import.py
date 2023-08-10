from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, Date
from psgre_connect import Base, engine


class Observation_import(Base):
    __tablename__ = 'observation_import'
    
    observation_id = Column(Integer, primary_key=True, autoincrement=True)  #ALTER TABLE table_name AUTO_INCREMENT=起始數字;
    person_id = Column(Integer, nullable = True)
    observation_concept_id = Column(Integer, nullable = True)
    observation_date = Column(Date, nullable = True)
    observation_datetime = Column(TIMESTAMP, nullable = True)
    observation_type_concept_id = Column(Integer, nullable = True)
    value_as_number = Column(Numeric, nullable = True)
    value_as_string = Column(String(60), nullable = True)
    value_as_concept_id = Column(Integer, nullable = True)
    qualifier_concept_id = Column(Integer, nullable = True)
    unit_concept_id = Column(Integer, nullable = True)
    provider_id = Column(Integer, nullable = True)
    visit_occurrence_id = Column(Integer, nullable = True)
    visit_detail_id = Column(Integer, nullable = True)
    observation_source_value = Column(String(50), nullable = True)
    observation_source_concept_id = Column(Integer, nullable = True)
    unit_source_value = Column(String(50), nullable = True)
    qualifier_source_value = Column(String(50), nullable = True)
    observation_event_id = Column(Integer, nullable = True)
    obs_event_field_concept_id = Column(Integer, nullable = True)
    value_as_datetime = Column(TIMESTAMP, nullable = True)
    last_update_time = Column(Date, nullable = True)
    vghtc_source_type = Column(String(20), nullable = True)
    vghtc_caseno = Column(String(20), nullable = True)
    vghtc_ordseq = Column(String(20), nullable = True)
    vghtc_key = Column(String(200), nullable = True)

def __init__(self, observation_id, person_id, observation_concept_id, observation_date, observation_datetime, observation_type_concept_id, value_as_number, value_as_string, value_as_concept_id, qualifier_concept_id, unit_concept_id, provider_id, visit_occurrence_id, visit_detail_id, observation_source_value, observation_source_concept_id, unit_source_value, qualifier_source_value, observation_event_id, obs_event_field_concept_id, value_as_datetime, last_update_time, vghtc_source_type, vghtc_caseno, vghtc_ordseq, vghtc_key):    
    self.observation_id = observation_id
    self.person_id = person_id
    self.observation_concept_id = observation_concept_id
    self.observation_date = observation_date
    self.observation_datetime = observation_datetime
    self.observation_type_concept_id = observation_type_concept_id
    self.value_as_number = value_as_number
    self.value_as_string = value_as_string
    self.value_as_concept_id = value_as_concept_id
    self.qualifier_concept_id = qualifier_concept_id
    self.unit_concept_id = unit_concept_id
    self.provider_id = provider_id
    self.visit_occurrence_id = visit_occurrence_id
    self.visit_detail_id = visit_detail_id
    self.observation_source_value = observation_source_value
    self.observation_source_concept_id = observation_source_concept_id
    self.unit_source_value = unit_source_value
    self.qualifier_source_value = qualifier_source_value
    self.observation_event_id = observation_event_id
    self.obs_event_field_concept_id = obs_event_field_concept_id
    self.value_as_datetime = value_as_datetime
    self.last_update_time = last_update_time
    self.vghtc_source_type = vghtc_source_type
    self.vghtc_caseno = vghtc_caseno
    self.vghtc_ordseq = vghtc_ordseq
    self.vghtc_key = vghtc_key


def create_table():
  Base.metadata.create_all(engine)

def drop_table():
  Base.metadata.drop_all(engine)
 