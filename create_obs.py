from sqlalchemy.orm import Session
from oracle_connect import get_oracle_session
from psgre_connect import get_db_session
from observation_import import Observation_import
from types import NoneType
import read


def set_init_data():
    init_data = { "observation_type_concept_id":'38000280',
                  "observation_date":query.createdatetime[:8], 
                  "observation_datetime":query.createdatetime[:8]+" "+query.createdatetime[8:]  }
    return init_data

def set_init_smoke_data():
    data = merge_data(set_init_data(), observation_concept_id ='4275495') #Tobacco smoking behavior - finding             
    return data


def set_init_drink_data():
    data = merge_data(set_init_data(), observation_concept_id ='4042860')  #Alcohol drinking behavior         
    return data

def set_init_betelnut_data():
    data = merge_data(set_init_data(), observation_concept_id ='4254479')  #Finding related to substance use         
    return data

def merge_person_data(data, **person_elements):
    data.update(person_elements)
    return


def merge_data(data,**merge_elements): 
    data.update(merge_elements)
    return data


def create_whole_obs(db: Session, obs_data: list) -> None: #Typing
    db.add_all(obs_data)
    db.commit()    
    
def create_singal_obs(db: Session, obs_data: dict) -> None: #Typing
    created_test = Observation_import(**obs_data)
    db.add(created_test)
    db.commit()
    
    

if __name__ == '__main__':   
    _db_oracle = next(get_oracle_session())  
    _db_psgre = next(get_db_session())         

    behavoirs = read.get_whole_behavior(_db_oracle) 
    observation_id = 0
    
    allset = []
    all_drink_set = []
    all_betelnut_data = []
        
    
    for query in behavoirs:
        if type(query) is NoneType:
            print ("query.opdcaseno (createdatetime is null) : ", query.opdcaseno)
            continue
        
        q_visit = read.get_visit_by_id(_db_psgre, query.opdcaseno)         
        if type(q_visit) is NoneType:
            print ("query.opdcaseno (person_id is null) : ", query.opdcaseno)
            continue
        
 ################ 病人吸菸狀態  ##########################################      
        data = set_init_smoke_data()
        data = merge_data(data, 
                          person_id = q_visit.person_id,  #person_source_value in table PERSON                          
                          visit_occurrence_id = q_visit.visit_occurrence_id) #vghtc_caseno in table VISIT_OCCURRENCE
        

       # match query.omesmokecode:
        if(query.omesmokecode == '0'): #無
            observation_id += 1
            data = merge_data(data, observation_id = observation_id,
                                    value_as_concept_id = '4222303',   #non-smoker
                                    observation_source_value = query.omesmokecode)
            
            #create_singal_obs(_db_psgre, data)
            allset.append(Observation_import(**data))
            
            
            
        elif(query.omesmokecode == '6'): #有
            observation_id += 1   
            data = merge_data(data, observation_id = observation_id,
                                    value_as_concept_id = '4298794',   #smoker
                                    observation_source_value = query.omesmokecode)
            
            #create_singal_obs(_db_psgre, data)
            allset.append(Observation_import(**data))                         
            
            
        elif(query.omesmokecode == '1'): #已戒
            observation_id += 1
            data = merge_data(data, observation_id = observation_id,
                                    value_as_concept_id = '4052032',   #quit
                                    observation_source_value = query.omesmokecode)  
            
            #create_singal_obs(_db_psgre, data)
            allset.append(Observation_import(**data)) 
            
#############  嚼檳榔  ################################            
        
        betelnut_data = set_init_betelnut_data()
        betelnut_data = merge_data(betelnut_data, 
                          person_id = q_visit.person_id,  #person_source_value in table PERSON                          
                          visit_occurrence_id = q_visit.visit_occurrence_id) #vghtc_caseno in table VISIT_OCCURRENCE
        

        if(query.omebetelnutcode == '6'): #有
            observation_id += 1
            betelnut_data = merge_data(betelnut_data, observation_id = observation_id,
                                    value_as_concept_id = '44784160',   # Chews betel quid (finding)
                                    observation_source_value = query.omebetelnutcode)
            
            all_betelnut_data.append(Observation_import(**betelnut_data))
            
            
            
        elif(query.omebetelnutcode == '0'): #無
            observation_id += 1   
            betelnut_data = merge_data(betelnut_data, observation_id = observation_id,
                                    value_as_concept_id = '',   #還沒找到
                                    observation_source_value = query.omebetelnutcode)
            
            all_betelnut_data.append(Observation_import(**betelnut_data))                         
            
            
        elif(query.omebetelnutcode == '1'): #已戒
            observation_id += 1
            betelnut_data = merge_data(betelnut_data, observation_id = observation_id,
                                    value_as_concept_id = '',   #還沒找到
                                    observation_source_value = query.omebetelnutcode)  
            
            all_betelnut_data.append(Observation_import(**betelnut_data)) 
            
                    
########### 喝酒  ####################################   
        drink_data = set_init_drink_data()
        drink_data = merge_data(drink_data, 
                          person_id = q_visit.person_id,  #person_source_value in table PERSON                          
                          visit_occurrence_id = q_visit.visit_occurrence_id) #vghtc_caseno in table VISIT_OCCURRENCE
        

        if(query.drink == '0'): #不喝酒
            observation_id += 1
            drink_data = merge_data(drink_data, observation_id = observation_id,
                                    value_as_concept_id = '4022664',   #Non - drinker
                                    observation_source_value = query.drink)
            
            all_drink_set.append(Observation_import(**drink_data))
            
            
            
        elif(query.drink == '1'): # 偶爾喝酒或應酬才喝
            observation_id += 1   
            drink_data = merge_data(drink_data, observation_id = observation_id,
                                    value_as_concept_id = '4042862',   #Light drinker (finding)
                                    observation_source_value = query.drink)
            
            all_drink_set.append(Observation_import(**drink_data))                         
            
            
        elif(query.drink == '2'): # 經常喝酒
            observation_id += 1
            drink_data = merge_data(drink_data, observation_id = observation_id,
                                    value_as_concept_id = '4336673',   #Heavy drinker (finding)
                                    observation_source_value = query.drink)  
            
            all_drink_set.append(Observation_import(**drink_data)) 


    print("# of allset: ",len(allset))
    create_whole_obs(_db_psgre, allset)
    create_whole_obs(_db_psgre, all_betelnut_data)
    create_whole_obs(_db_psgre, all_drink_set)

    
       
   
    
   
    
   
    
    
    
    
