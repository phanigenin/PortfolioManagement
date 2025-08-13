from sqlalchemy import String,Numeric,Date,Float,DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import (Column,Integer,Unicode,ForeignKey,UnicodeText,and_,create_engine)
from sqlalchemy.orm import relationship
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

from datamart.consts import OUT_Z_ETER,TODAY,ORIGIN,THRU_Z_ETER,NOW

Base = declarative_base()

class PositionEquityIndia(Base):
    __tablename__    = 'position_equity_india'

    symbol             = Column(String,primary_key=True,index=True)
    open_price         = Column(Float)
    open_qty           = Column(Float)
    from_z             = Column(Date)
    thru_z             = Column(Date,primary_key=True, index=True,default=THRU_Z_ETER)
    strategy           = Column(String,nullable=True)
    in_z               = Column(DateTime,default=NOW)
    out_z              = Column(DateTime,default=OUT_Z_ETER,primary_key=True,index=True)

    def __init__(self, symbol, **kwargs):
        self.symbol           = symbol
        self.open_price       = kwargs.get('open_price')
        self.open_qty         = kwargs.get('open_qty')
        self.from_z           = kwargs.get('biz_date')
        self.strategy         = kwargs.get('strategy')


    def __repr__(self):
        return "<PositionEquityIndia(SYM: '%s', PRICE: '%s', QTY:'%s')>" % (self.symbol, self.open_price,self.open_qty)

class MTMRealisedEquityIndia(Base):
    __tablename__    = 'mtm_realised_equity_india'

    symbol             = Column(String,primary_key=True,index=True)
    mtm_realised       = Column(Float)
    biz_date           = Column(Date,index=True,primary_key=True)#kwargs.get('biz_date')
    strategy           = Column(String,nullable=True)
    in_z               = Column(DateTime,default=NOW)
    out_z              = Column(DateTime,default=OUT_Z_ETER,index=True,primary_key=True)

    def __init__(self, symbol, **kwargs):
        self.symbol             = symbol
        self.mtm_realised       = kwargs.get('mtm_realised')
        self.biz_date           = kwargs.get('biz_date')
        self.strategy           = kwargs.get('strategy')


    def __repr__(self):
        return "<MTMRealisedEquityIndia(SYM: '%s', MTM_REALISED: '%s', BIZDATE:'%s', STRAT: '%s')>" % (self.symbol, self.mtm_realised,self.biz_date,self.strategy)

class MTMRealisedEquityIndiaDividends(Base):
    __tablename__    = 'mtm_realised_equity_india_dividends'

    symbol             = Column(String,primary_key=True,index=True)
    mtm_realised       = Column(Float)
    biz_date           = Column(Date,index=True,primary_key=True)#kwargs.get('biz_date')
    strategy           = Column(String,nullable=True,default="dividends")
    in_z               = Column(DateTime,default=NOW)
    out_z              = Column(DateTime,default=OUT_Z_ETER,index=True,primary_key=True)

    def __init__(self, symbol, **kwargs):
        self.symbol             = symbol
        self.mtm_realised       = kwargs.get('mtm_realised')
        self.biz_date           = kwargs.get('biz_date')
        self.strategy           = kwargs.get('strategy')


    def __repr__(self):
        return "<MTMRealisedEquityIndiaDividends(SYM: '%s', MTM_REALISED: '%s', BIZDATE:'%s', STRAT: '%s')>" % (self.symbol, self.mtm_realised,self.biz_date,self.strategy)

class MTMRealisedEquityIndiaDerivatives(Base):
    __tablename__    = 'mtm_realised_equity_india_derivatives'

    symbol             = Column(String,primary_key=True,index=True)
    mtm_realised       = Column(Float)
    biz_date           = Column(Date,index=True,primary_key=True)#kwargs.get('biz_date')
    strategy           = Column(String,nullable=True,default="coveredcall")
    in_z               = Column(DateTime,default=NOW)
    out_z              = Column(DateTime,default=OUT_Z_ETER,index=True,primary_key=True)

    def __init__(self, symbol, **kwargs):
        self.symbol             = symbol
        self.mtm_realised       = kwargs.get('mtm_realised')
        self.biz_date           = kwargs.get('biz_date')
        self.strategy           = kwargs.get('strategy')


    def __repr__(self):
        return "<MTMRealisedEquityIndiaDerivatives(SYM: '%s', MTM_REALISED: '%s', BIZDATE:'%s', STRAT: '%s')>" % (self.symbol, self.mtm_realised,self.biz_date,self.strategy)


class TransactionsEquityIndia(Base):
    __tablename__    = 'transactions_equity_india'
    trn_id           = Column(Integer,autoincrement=True,primary_key=True)
    symbol           = Column(String)
    trn_buysell      = Column(String,default="S")
    trn_price        = Column(Float)
    trn_qty          = Column(Float)
    trn_date         = Column(Date)
    strategy         = Column(String,nullable=True)
    in_z             = Column(DateTime,default=NOW)

    def __init__(self, symbol, **kwargs):
        self.symbol         = symbol
        self.trn_buysell    = kwargs.get('trn_buysell')
        self.trn_price      = kwargs.get('trn_price')
        self.trn_qty        = kwargs.get('trn_qty')
        self.trn_date       = kwargs.get('trn_date')
        self.strategy       = kwargs.get('strategy')

    def __repr__(self):
        return "<TransactionsEquityIndia(SYM: '%s', BUYSEL: '%s' ,PRICE: '%s',QTY: '%s', DT: '%s', STRATEGY: '%s' )>" % (self.symbol,self.trn_buysell,self.trn_price ,

                                                                                                                        self.trn_qty,self.trn_date,self.strategy)

#------------------------------------------------ BONDS INDIA TABLES BEGIN ---------------------------------------------------------

class InstrumentsBondIndia(Base):
    __tablename__    = 'instruments_bond_india'

    isin               = Column(String,primary_key=True,index=True)
    descr              = Column(String)
    issuer             = Column(String)
    coupon             = Column(Float)
    issue_dt           = Column(Date)
    mat_dt             = Column(Date)
    int_freq           = Column(String)
    pmt_freq           = Column(String)
    bond_type          = Column(String)
    in_z               = Column(DateTime,default=NOW)
    out_z              = Column(DateTime,default=OUT_Z_ETER,primary_key=True,index=True)

    def __init__(self, isin, **kwargs):
        self.isin             = isin
        self.descr            = kwargs.get('descr')
        self.issuer           = kwargs.get('issuer')
        self.coupon           = kwargs.get('coupon')
        self.issue_dt         = kwargs.get('issue_dt')
        self.mat_dt           = kwargs.get('mat_dt')
        self.int_freq         = kwargs.get('int_freq')
        self.pmt_freq         = kwargs.get('pmt_freq')
        self.bond_type        = kwargs.get('bond_type')


    def __repr__(self):
        return "<InstrumentsBondIndia(ISIN: '%s', DESC: '%s' , MAT : '%s' )>" % (self.isin, self.descr,self.mat_dt)

class PositionBondIndia(Base):
    __tablename__    = 'position_bond_india'

    pos_id             = Column(Integer, autoincrement=True,primary_key=True,)
    isin               = Column(String)
    open_price         = Column(Float)
    open_qty           = Column(Float)
    pos_amt            = Column(Float)
    pos_source         = Column(String)
    pos_user           = Column(String)
    from_z             = Column(Date,default=TODAY)
    thru_z             = Column(Date,default=THRU_Z_ETER)
    strategy           = Column(String,nullable=True)
    in_z               = Column(DateTime,default=NOW)
    out_z              = Column(DateTime,default=OUT_Z_ETER)

    def __init__(self, isin, **kwargs):
        self.isin             = isin
        self.open_price       = kwargs.get('open_price')
        self.open_qty         = kwargs.get('open_qty')
        self.pos_amt          = kwargs.get('pos_amt')
        self.pos_source       = kwargs.get('pos_source')
        self.pos_user         = kwargs.get('pos_user')
        self.from_z           = kwargs.get('biz_date')
        self.strategy         = kwargs.get('strategy')


    def __repr__(self):
        return "<PositionBondIndia(ISIN: '%s', AMT : '%s', QTY:'%s')>" % (self.isin, self.pos_amt,self.open_qty)


class TransactionsBondIndia(Base):
    __tablename__    = 'transactions_bond_india'
    trn_id           = Column(Integer,autoincrement=True,primary_key=True)
    isin             = Column(String)
    trn_buysell      = Column(String,default="B")
    trn_price        = Column(Float)
    trn_qty          = Column(Float)
    trn_amt          = Column(Float)
    trn_date         = Column(Date)
    trn_source       = Column(String)
    trn_user         = Column(String)
    strategy         = Column(String,nullable=True)
    in_z             = Column(DateTime,default=NOW)
    out_z            = Column(DateTime, default=OUT_Z_ETER)

    def __init__(self, isin, **kwargs):
        self.isin           = isin
        self.trn_buysell    = kwargs.get('trn_buysell')
        self.trn_price      = kwargs.get('trn_price')
        self.trn_qty        = kwargs.get('trn_qty')
        self.trn_amt        = kwargs.get('trn_amt')
        self.trn_date       = kwargs.get('trn_date')
        self.strategy       = kwargs.get('strategy')
        self.trn_source     = kwargs.get('trn_source')
        self.trn_user       = kwargs.get('trn_user')

    def __repr__(self):
        return "<TransactionsBondIndia(ISIN: '%s', BUYSEL: '%s' ,PRICE: '%s',QTY: '%s',AMT: '%s', DT: '%s', STRATEGY: '%s' )>" % (self.isin,self.trn_buysell,self.trn_price ,

                                                                                                                        self.trn_qty,self.trn_amt,self.trn_date,self.strategy)
class MTMRealisedBondIndia(Base):
    __tablename__    = 'mtm_realised_bond_india'
    mtm_id             = Column(Integer, autoincrement=True, primary_key=True)
    isin               = Column(String)
    mtm_realised       = Column(Float)
    biz_date           = Column(Date)#kwargs.get('biz_date')
    mtm_user           = Column(String)
    strategy           = Column(String,nullable=True,default="buyhold")
    in_z               = Column(DateTime,default=NOW)
    out_z              = Column(DateTime,default=OUT_Z_ETER)

    def __init__(self, isin, **kwargs):
        self.isin               = isin
        self.mtm_realised       = kwargs.get('mtm_realised')
        self.biz_date           = kwargs.get('biz_date')
        self.strategy           = kwargs.get('strategy')
        self.mtm_user           = kwargs.get('mtm_user')

    def __repr__(self):
        return "<MTMRealisedBondIndia(ISIN: '%s', MTM_REALISED: '%s', BIZDATE:'%s', STRAT: '%s')>" % (self.symbol, self.mtm_realised,self.biz_date,self.strategy)

class CashFlowsBondIndia(Base):
    __tablename__    = 'cashflows_bond_india'
    cf_id              = Column(Integer,autoincrement=True,primary_key=True)
    isin               = Column(String)
    pos_id             = Column(Integer)
    payment_amt        = Column(Float)
    pay_date           = Column(Date)#kwargs.get('biz_date')
    received           = Column(Integer,default=0)
    payment_type       = Column(String)
    in_z               = Column(DateTime,default=NOW)
    out_z              = Column(DateTime,default=OUT_Z_ETER)

    def __init__(self, isin,pos_id, **kwargs):
        self.isin              = isin
        self.pos_id            = pos_id
        self.payment_amt       = kwargs.get('payment_amt')
        self.pay_date          = kwargs.get('pay_date')
        self.received          = kwargs.get('received',0)
        self.payment_type      = kwargs.get('payment_type')#INTEREST,PRINCIPAL
        #self.strategy = kwargs.get('strategy')


    def __repr__(self):
        return "<CashFlowsBondIndia(ISIN: '%s', PAYMENT: '%s', PAYDATE:'%s', TYPE: '%s' , RECEIVED: '%s')>" \
            % (self.isin, self.payment_amt,self.pay_date,self.payment_type,self.received)

#------------------------------------------------ BONDS INDIA TABLES END  ---------------------------------------------------------

class Watchlist(Base):
    __tablename__    = 'watchlist'

    symbol             = Column(String,primary_key=True,index=True)
    tgt                = Column(Float)
    remarks            = Column(String,nullable=True)
    in_z               = Column(DateTime,default=NOW)

    def __init__(self, symbol, **kwargs):
        self.symbol             = symbol
        self.tgt                = kwargs.get('tgt')
        self.remarks            = kwargs.get('remarks')


    def __repr__(self):
        return "<Watchlist(SYM: '%s', TGT: '%s', REMARKS:'%s')>" % (self.symbol, self.tgt,self.remarks)

def get_database_session(base=Base,repository_path=""):
    from sqlalchemy import create_engine,MetaData
    from sqlalchemy.orm import sessionmaker

    engine   = create_engine(repository_path, echo=True)
    base.metadata.create_all(engine,checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()# create a Session
    return engine,session
