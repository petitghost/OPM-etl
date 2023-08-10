from sqlalchemy.orm import Session
from observation_import import Observation_import
from visit_occurrence import Visit_occurrence
from opdomem import Opdomem
from operator import is_not
from functools import partial


def get_obs_by_id(db: Session, test_id: int) -> Observation_import:
    result = db.query(Observation_import).filter_by(observation_id=test_id).first()
    return result

def get_visit_by_id(db: Session, q_case_id: str) -> Visit_occurrence:
    db.commit()
    result = db.query(Visit_occurrence).filter_by(vghtc_caseno=q_case_id).first()
    
    #if type(result) is not Visit_occurrence:
        #print("query is :", type(result)) 
    return result

def get_whole_behavior(db: Session) -> list:
    #result = db.query(Opdomem).all()
    result = db.query(Opdomem).yield_per(100)
    #print("# of result :", len(result))
    #list(filter(partial(is_not, None), result))
    #print("# of filterd result :", len(result))
    return result

#if __name__ == '__main__':
   
        
        
    
        
    
   
    
    
    
    