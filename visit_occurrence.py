from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, Date
from psgre_connect import Base, engine

class Visit_occurrence(Base):
    __tablename__ = 'visit_occurrence'
    
    visit_occurrence_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable = True)
    visit_concept_id = Column(Integer, nullable = True)
    visit_start_date = Column(Date, nullable = True)
    visit_start_datetime = Column(TIMESTAMP, nullable = True)
    visit_end_date = Column(Date, nullable = True)
    visit_end_datetime = Column(TIMESTAMP, nullable = True)
    visit_type_concept_id = Column(Integer, nullable = True)
    provider_id = Column(Integer, nullable = True)
    care_site_id = Column(Integer, nullable = True)
    visit_source_value = Column(String(50), nullable = True)
    visit_source_concept_id = Column(Integer, nullable = True)
    admitting_from_concept_id = Column(Integer, nullable = True)
    admitting_from_source_value = Column(String(50), nullable = True)
    discharge_to_concept_id = Column(Integer, nullable = True)
    discharge_to_source_value = Column(String(50), nullable = True)
    preceding_visit_occurrence_id = Column(Integer, nullable = True)
    vghtc_source_type = Column(String(20), nullable = True)
    vghtc_caseno = Column(String(20), nullable = True)
    admitting_source_concept_id = Column(Integer, nullable = True)
    admitting_source_value = Column(String(50), nullable = True)
    nhi_dept = Column(String(10), nullable = True)
    nhi_dept_source_value = Column(String(10), nullable = True)

def __init__(self, visit_occurrence_id, person_id, visit_concept_id, visit_start_date, visit_start_datetime, visit_end_date, visit_end_datetime, visit_type_concept_id, provider_id, care_site_id, visit_source_value, visit_source_concept_id, admitting_from_concept_id, admitting_from_source_value, discharge_to_concept_id, discharge_to_source_value, preceding_visit_occurrence_id, vghtc_source_type, vghtc_caseno, admitting_source_concept_id, admitting_source_value, nhi_dept, nhi_dept_source_value):
    self.visit_occurrence_id = visit_occurrence_id
    self.person_id = person_id
    self.visit_concept_id = visit_concept_id
    self.visit_start_date = visit_start_date
    self.visit_start_datetime = visit_start_datetime
    self.visit_end_date = visit_end_date
    self.visit_end_datetime = visit_end_datetime
    self.visit_type_concept_id = visit_type_concept_id
    self.provider_id = provider_id
    self.care_site_id = care_site_id
    self.visit_source_value = visit_source_value
    self.visit_source_concept_id = visit_source_concept_id
    self.admitting_from_concept_id = admitting_from_concept_id
    self.admitting_from_source_value = admitting_from_source_value
    self.discharge_to_concept_id = discharge_to_concept_id
    self.discharge_to_source_value = discharge_to_source_value
    self.preceding_visit_occurrence_id = preceding_visit_occurrence_id
    self.vghtc_source_type = vghtc_source_type
    self.vghtc_caseno = vghtc_caseno
    self.admitting_source_concept_id = admitting_source_concept_id
    self.admitting_source_value = admitting_source_value
    self.nhi_dept = nhi_dept
    self.nhi_dept_source_value = nhi_dept_source_value
