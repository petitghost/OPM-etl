from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, Date
from oracle_connect import Base, engine

class Opdomem(Base):
    __tablename__ = 'OPDOMEM'
    
    opdcaseno = Column(String(8), primary_key=True, nullable = False)
    omemrecno = Column(Numeric, nullable = False)
    examsite = Column(String(1), nullable = False)
    omedrcode = Column(String(1), nullable = False)
    lookcode = Column(String(2), nullable = False)
    hhisnum = Column(String(10), nullable = False)
    hnamec = Column(String(24), nullable = False)
    hidno = Column(String(10), nullable = False)
    hsex = Column(String(1), nullable = False)
    hbirthdt = Column(String(8), nullable = False)
    opddate = Column(String(8), nullable = False)
    mainsection = Column(String(4), nullable = True)
    opdsection = Column(String(4), nullable = True)
    hphonhm1 = Column(String(20), nullable = True)
    hpmobil = Column(String(20), nullable = True)
    zipareacode = Column(String(4), nullable = True)
    hopatadr = Column(String(200), nullable = False)
    omebetelnutcode = Column(String(1), nullable = False, default = '0')
    omesmokecode = Column(String(1), nullable = False, default = '0')
    omeresult = Column(String(2), nullable = False, default = '0')
    hospitalno = Column(String(10), nullable = True)
    hospitaltelno = Column(String(16), nullable = True)
    cancelyn = Column(String(1), nullable = False, default = 'N')
    canceldatetime = Column(String(14), nullable = True)
    cancelid = Column(String(15), nullable = True)
    cancelnmc = Column(String(24), nullable = True)
    procdatetime = Column(String(14), nullable = False)
    procid = Column(String(15), nullable = False)
    procnmc = Column(String(24), nullable = False)
    createdatetime = Column(String(14), nullable = False)
    createid = Column(String(15), nullable = False)
    createnmc = Column(String(24), nullable = False)
    transdrnmc = Column(String(24), nullable = True)
    omeresultmemo = Column(String(200), nullable = True)
    outhospno = Column(String(10), nullable = True)
    outhosptelno = Column(String(20), nullable = True)
    uploadyn = Column(String(1), nullable = False, default = 'N')
    smokestat100code = Column(String(2), nullable = True)
    smokestat30code = Column(String(2), nullable = True)
    smokeyearscode = Column(String(2), nullable = True)
    smokeamountcode = Column(String(2), nullable = True)
    smokequitchannelarray = Column(String(20), nullable = True)
    smokequitmonthcode = Column(String(2), nullable = True)
    smokequitdayscode = Column(String(2), nullable = True)
    education_level = Column(String(1), nullable = True)
    subjective_symptom_yn = Column(String(1), nullable = True)
    subseq_disposal = Column(String(1), nullable = True)
    abnormal_part = Column(String(50), nullable = True)
    abnormal_part_others = Column(String(100), nullable = True)
    surgical_biopsy = Column(String(2), nullable = True)
    surgical_biopsy_others = Column(String(200), nullable = True)
    esmoke = Column(String(1), nullable = True)
    drink = Column(String(1), nullable = True)
    smokefamily = Column(String(1), nullable = True)
    smokefamilytitle = Column(String(20), nullable = True)
    smokefamilytitleother = Column(String(20), nullable = True)
    sport = Column(String(1), nullable = True)

def __init__(self, opdcaseno, omemrecno, examsite, omedrcode, lookcode, hhisnum, hnamec, hidno, hsex, hbirthdt, opddate, mainsection, opdsection, hphonhm1, hpmobil, zipareacode, hopatadr, omebetelnutcode, omesmokecode, omeresult, hospitalno, hospitaltelno, cancelyn, canceldatetime, cancelid, cancelnmc, procdatetime, procid, procnmc, createdatetime, createid, createnmc, transdrnmc, omeresultmemo, outhospno, outhosptelno, uploadyn, smokestat100code, smokestat30code, smokeyearscode, smokeamountcode, smokequitchannelarray, smokequitmonthcode, smokequitdayscode, education_level, subjective_symptom_yn, subseq_disposal, abnormal_part, abnormal_part_others, surgical_biopsy, surgical_biopsy_others, esmoke, drink, smokefamily, smokefamilytitle, smokefamilytitleother, sport):
    self.opdcaseno = opdcaseno
    self.omemrecno = omemrecno
    self.examsite = examsite
    self.omedrcode = omedrcode
    self.lookcode = lookcode
    self.hhisnum = hhisnum
    self.hnamec = hnamec
    self.hidno = hidno
    self.hsex = hsex
    self.hbirthdt = hbirthdt
    self.opddate = opddate
    self.mainsection = mainsection
    self.opdsection = opdsection
    self.hphonhm1 = hphonhm1
    self.hpmobil = hpmobil
    self.zipareacode = zipareacode
    self.hopatadr = hopatadr
    self.omebetelnutcode = omebetelnutcode
    self.omesmokecode = omesmokecode
    self.omeresult = omeresult
    self.hospitalno = hospitalno
    self.hospitaltelno = hospitaltelno
    self.cancelyn = cancelyn
    self.canceldatetime = canceldatetime
    self.cancelid = cancelid
    self.cancelnmc = cancelnmc
    self.procdatetime = procdatetime
    self.procid = procid
    self.procnmc = procnmc
    self.createdatetime = createdatetime
    self.createid = createid
    self.createnmc = createnmc
    self.transdrnmc = transdrnmc
    self.omeresultmemo = omeresultmemo
    self.outhospno = outhospno
    self.outhosptelno = outhosptelno
    self.uploadyn = uploadyn
    self.smokestat100code = smokestat100code
    self.smokestat30code = smokestat30code
    self.smokeyearscode = smokeyearscode
    self.smokeamountcode = smokeamountcode
    self.smokequitchannelarray = smokequitchannelarray
    self.smokequitmonthcode = smokequitmonthcode
    self.smokequitdayscode = smokequitdayscode
    self.education_level = education_level
    self.subjective_symptom_yn = subjective_symptom_yn
    self.subseq_disposal = subseq_disposal
    self.abnormal_part = abnormal_part
    self.abnormal_part_others = abnormal_part_others
    self.surgical_biopsy = surgical_biopsy
    self.surgical_biopsy_others = surgical_biopsy_others
    self.esmoke = esmoke
    self.drink = drink
    self.smokefamily = smokefamily
    self.smokefamilytitle = smokefamilytitle
    self.smokefamilytitleother = smokefamilytitleother
    self.sport = sport