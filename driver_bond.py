from middletier.bonds.transactions import register_transaction
from middletier.bonds.instruments import register_instrument
from datetime import datetime

dt1=datetime(year=2025,month=6,day=26).date()

'''
#register_instrument(isin="INE125T07329",instr_payload={"descr":"Varthana Jun'25","issuer":"Varthana","coupon":11.5,"issue_dt":datetime(year=2025,month=1,day=29).date(),"mat_dt":datetime(year=2027,month=2,day=5).date(),
#                                                       "int_freq":"Quarterly","pmt_freq":"HalfYearly","bond_type":"NBFC",})
register_instrument(isin="INE0N5S07037",instr_payload={"descr":"Samunnati-2 Jun'25","issuer":"Samunnati","coupon":11.1,"issue_dt":datetime(year=2025,month=5,day=28).date(),"mat_dt":datetime(year=2026,month=6,day=6).date(),
                                                       "int_freq":"Monthly","pmt_freq":"Staggered","bond_type":"NBFC",})
register_instrument(isin="INE0RU307171",instr_payload={"descr":"Wint Capital-2 May'25","issuer":"Wint Capital","coupon":10.75,"issue_dt":datetime(year=2025,month=5,day=28).date(),"mat_dt":datetime(year=2026,month=7,day=5).date(),
                                                       "int_freq":"Monthly","pmt_freq":"Staggered","bond_type":"NBFC",})
register_instrument(isin="INE296Q07068",instr_payload={"descr":"MoneyBoxx Nov'24","issuer":"MoneyBoxx","coupon":12,"issue_dt":datetime(year=2024,month=11,day=11).date(),"mat_dt":datetime(year=2026,month=11,day=11).date(),
                                                       "int_freq":"Monthly","pmt_freq":"Staggered","bond_type":"NBFC",})
register_instrument(isin="INE275315013",instr_payload={"descr":"LoanX SAVE Oct’26","issuer":"SAVE","coupon":11.6,"issue_dt":datetime(year=2025,month=5,day=28).date(),"mat_dt":datetime(year=2026,month=10,day=5).date(),
                                                       "int_freq":"Monthly","pmt_freq":"Monthly","bond_type":"NBFC",})
register_instrument(isin="INE0NES07188",instr_payload={"descr":"Keertana Dec'26","issuer":"Keertana","coupon":11.2,"issue_dt":datetime(year=2024,month=12,day=11).date(),"mat_dt":datetime(year=2026,month=12,day=11).date(),
                                                       "int_freq":"Monthly","pmt_freq":"Monthly","bond_type":"NBFC",})
'''
'''
        self.trn_buysell    = kwargs.get('trn_buysell')
        self.trn_price      = kwargs.get('trn_price')
        self.trn_qty        = kwargs.get('trn_qty')
        self.trn_amt        = kwargs.get('trn_amt')
        self.trn_date       = kwargs.get('trn_date')
        self.strategy       = kwargs.get('strategy')
        self.trn_source     = kwargs.get('trn_source')
        self.trn_user       = kwargs.get('trn_user')

'''

'''
#  4-Jun x 2
#register_transaction(isin="INE0RU307171",trn_payload={"trn_buysell":"B","trn_price":100.54,"trn_qty":50,"trn_amt":502734.65,"trn_date":datetime(year=2025,month=6,day=4).date(),"strategy":"BuyHold","trn_source":"WintWealth","trn_user":"PHANI"})
#register_transaction(isin="INE0RU307171",trn_payload={"trn_buysell":"B","trn_price":100.2578,"trn_qty":50,"trn_amt":501289.00,"trn_date":datetime(year=2025,month=6,day=4).date(),"strategy":"BuyHold","trn_source":"WintWealth","trn_user":"JANAKI"})

#  12-Jun x 2
register_transaction(isin="INE0N5S07037",trn_payload={"trn_buysell":"B","trn_price":100.54,"trn_qty":50,"trn_amt":502725.82,"trn_date":datetime(year=2025,month=6,day=12).date(),"strategy":"BuyHold","trn_source":"WintWealth","trn_user":"PHANI"})
register_transaction(isin="INE0N5S07037",trn_payload={"trn_buysell":"B","trn_price":99.6366,"trn_qty":50,"trn_amt":498183.00,"trn_date":datetime(year=2025,month=6,day=12).date(),"strategy":"BuyHold","trn_source":"WintWealth","trn_user":"JANAKI"})

#  13-Jun x 1
register_transaction(isin="INE296Q07068",trn_payload={"trn_buysell":"B","trn_price":100.7805,"trn_qty":3,"trn_amt":30234.14,"trn_date":datetime(year=2025,month=6,day=13).date(),"strategy":"BuyHold","trn_source":"WintWealth","trn_user":"JANAKI"})

#  3-Jul x 1
register_transaction(isin="INE125T07329",trn_payload={"trn_buysell":"B","trn_price":102.2115,"trn_qty":50,"trn_amt":511057.52,"trn_date":datetime(year=2025,month=7,day=3).date(),"strategy":"BuyHold","trn_source":"WintWealth","trn_user":"PHANI"})

#  9-Jul x 1
register_transaction(isin="INE0RU307171",trn_payload={"trn_buysell":"B","trn_price":111.981,"trn_qty":10,"trn_amt":1119811.82,"trn_date":datetime(year=2025,month=7,day=9).date(),"strategy":"BuyHold","trn_source":"GripInvest","trn_user":"PHANI"})

#  21-Jul x 1
register_transaction(isin="INE0NES07188",trn_payload={"trn_buysell":"B","trn_price":118.5262,"trn_qty":6,"trn_amt":592630.8,"trn_date":datetime(year=2025,month=7,day=21).date(),"strategy":"BuyHold","trn_source":"GoldenPi","trn_user":"PHANI"})
'''
from middletier.bonds.positions import calc_pos_asof_bizdate
'''
calc_pos_asof_bizdate(datetime(year=2025,month=6,day=4).date())
calc_pos_asof_bizdate(datetime(year=2025,month=6,day=12).date())
calc_pos_asof_bizdate(datetime(year=2025,month=6,day=13).date())
calc_pos_asof_bizdate(datetime(year=2025,month=7,day=3).date())
calc_pos_asof_bizdate(datetime(year=2025,month=7,day=9).date())
calc_pos_asof_bizdate(datetime(year=2025,month=7,day=21).date())
'''


from middletier.bonds.cashflows import register_cashflow

'''
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2025,month=7,day=5).date(),'received':0,'payment_amt':5964.00,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=5).date(),'received':0,'payment_amt':4565.07,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2025,month=9,day=5).date(),'received':0,'payment_amt':4565.07,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2025,month=10,day=5).date(),'received':0,'payment_amt':4417.81,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=5).date(),'received':0,'payment_amt':4565.07,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=5).date(),'received':0,'payment_amt':4417.81,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2026,month=1,day=5).date(),'received':0,'payment_amt':228.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=5).date(),'received':0,'payment_amt':228.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2026,month=3,day=5).date(),'received':0,'payment_amt':206.17,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2026,month=4,day=5).date(),'received':0,'payment_amt':228.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2026,month=5,day=5).date(),'received':0,'payment_amt':220.89,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=5).date(),'received':0,'payment_amt':228.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2026,month=7,day=5).date(),'received':0,'payment_amt':220.89,'payment_type':'INTEREST'})

register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=5).date(),'received':0,'payment_amt':475000.0,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE0RU307171",pos_id=2,cashflow_payload={'pay_date':datetime(year=2026,month=7,day=5).date(),'received':0,'payment_amt':25000.0,'payment_type':'PRINCIPAL'})
'''
''' - 4
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2025,month=6,day=28).date(),'received':0,'payment_amt':4242.15,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2025,month=7,day=28).date(),'received':0,'payment_amt':4105.35,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=28).date(),'received':0,'payment_amt':4713.7,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2025,month=9,day=28).date(),'received':0,'payment_amt':4713.7,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2025,month=10,day=28).date(),'received':0,'payment_amt':4561.65,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=28).date(),'received':0,'payment_amt':4713.7,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=28).date(),'received':0,'payment_amt':4561.65,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2026,month=1,day=28).date(),'received':0,'payment_amt':235.69,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=28).date(),'received':0,'payment_amt':235.69,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2026,month=3,day=28).date(),'received':0,'payment_amt':212.88,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2026,month=4,day=28).date(),'received':0,'payment_amt':235.69,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=28).date(),'received':0,'payment_amt':311.71,'payment_type':'INTEREST'})

register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=28).date(),'received':0,'payment_amt':475000.0,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE0N5S07037",pos_id=4,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=8).date(),'received':0,'payment_amt':25000.0,'payment_type':'PRINCIPAL'})
'''
#-6
'''
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=5).date(),'received':0,'payment_amt':14493.15,'payment_type':'INTEREST'})
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=5).date(),'received':0,'payment_amt':10869.87,'payment_type':'INTEREST'})
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=5).date(),'received':0,'payment_amt':10869.87,'payment_type':'INTEREST'})
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2026,month=5,day=5).date(),'received':0,'payment_amt':7010.28,'payment_type':'INTEREST'})
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2026,month=8,day=5).date(),'received':0,'payment_amt':7246.58,'payment_type':'INTEREST'})
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2026,month=11,day=5).date(),'received':0,'payment_amt':3623.29,'payment_type':'INTEREST'})
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2027,month=2,day=5).date(),'received':0,'payment_amt':3623.29,'payment_type':'INTEREST'})

register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=5).date(),'received':0,'payment_amt':125000,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=5).date(),'received':0,'payment_amt':125000,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2026,month=8,day=5).date(),'received':0,'payment_amt':125000,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE125T07329",pos_id=6,cashflow_payload={'pay_date':datetime(year=2027,month=2,day=5).date(),'received':0,'payment_amt':125000,'payment_type':'PRINCIPAL'})
'''

# - 1
'''
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2025,month=7,day=5).date(),'received':0,'payment_amt':5964.00,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=5).date(),'received':0,'payment_amt':4565.07,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2025,month=9,day=5).date(),'received':0,'payment_amt':4565.07,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2025,month=10,day=5).date(),'received':0,'payment_amt':4417.81,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=5).date(),'received':0,'payment_amt':4565.07,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=5).date(),'received':0,'payment_amt':4417.81,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2026,month=1,day=5).date(),'received':0,'payment_amt':228.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=5).date(),'received':0,'payment_amt':228.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2026,month=3,day=5).date(),'received':0,'payment_amt':206.17,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2026,month=4,day=5).date(),'received':0,'payment_amt':228.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2026,month=5,day=5).date(),'received':0,'payment_amt':220.89,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=5).date(),'received':0,'payment_amt':228.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2026,month=7,day=5).date(),'received':0,'payment_amt':220.89,'payment_type':'INTEREST'})

register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=5).date(),'received':0,'payment_amt':475000.0,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE0RU307171",pos_id=1,cashflow_payload={'pay_date':datetime(year=2026,month=7,day=5).date(),'received':0,'payment_amt':25000.0,'payment_type':'PRINCIPAL'})
'''

# - 3
'''
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2025,month=7,day=28).date(),'received':0,'payment_amt':4105.35,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=28).date(),'received':0,'payment_amt':4713.7,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2025,month=9,day=28).date(),'received':0,'payment_amt':4713.7,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2025,month=10,day=28).date(),'received':0,'payment_amt':4561.65,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=28).date(),'received':0,'payment_amt':4713.7,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=28).date(),'received':0,'payment_amt':4561.65,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2026,month=1,day=28).date(),'received':0,'payment_amt':235.69,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=28).date(),'received':0,'payment_amt':235.69,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2026,month=3,day=28).date(),'received':0,'payment_amt':212.88,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2026,month=4,day=28).date(),'received':0,'payment_amt':235.69,'payment_type':'INTEREST'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=28).date(),'received':0,'payment_amt':311.71,'payment_type':'INTEREST'})

register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=28).date(),'received':0,'payment_amt':475000.0,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE0N5S07037",pos_id=3,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=8).date(),'received':0,'payment_amt':25000.0,'payment_type':'PRINCIPAL'})
'''

'''
# = 5
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2025,month=7,day=11).date(),'received':0,'payment_amt':266.3,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=11).date(),'received':0,'payment_amt':305.75,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2025,month=9,day=11).date(),'received':0,'payment_amt':305.75,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2025,month=10,day=11).date(),'received':0,'payment_amt':295.89,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=11).date(),'received':0,'payment_amt':305.75,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=11).date(),'received':0,'payment_amt':147.95,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=1,day=11).date(),'received':0,'payment_amt':152.88,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=11).date(),'received':0,'payment_amt':152.88,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=3,day=11).date(),'received':0,'payment_amt':138.08,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=4,day=11).date(),'received':0,'payment_amt':152.88,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=5,day=11).date(),'received':0,'payment_amt':147.95,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=11).date(),'received':0,'payment_amt':152.88,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=7,day=11).date(),'received':0,'payment_amt':147.95,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=8,day=11).date(),'received':0,'payment_amt':152.88,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=9,day=11).date(),'received':0,'payment_amt':152.88,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=10,day=11).date(),'received':0,'payment_amt':147.95,'payment_type':'INTEREST'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=11,day=11).date(),'received':0,'payment_amt':152.88,'payment_type':'INTEREST'})

register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=11).date(),'received':0,'payment_amt':15000.0,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE296Q07068",pos_id=5,cashflow_payload={'pay_date':datetime(year=2026,month=11,day=11).date(),'received':0,'payment_amt':15000.0,'payment_type':'PRINCIPAL'})
'''
# - INE275315013
'''
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=7,day=11).date(),'received':0,'payment_amt':6037.56,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=11).date(),'received':0,'payment_amt':9426.09,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=9,day=11).date(),'received':0,'payment_amt':8761.1,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=10,day=11).date(),'received':0,'payment_amt':7831.43,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=11).date(),'received':0,'payment_amt':7417.46,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=11).date(),'received':0,'payment_amt':6523.23,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=1,day=11).date(),'received':0,'payment_amt':6058.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=11).date(),'received':0,'payment_amt':5373.4,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=3,day=11).date(),'received':0,'payment_amt':4231.76,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=4,day=11).date(),'received':0,'payment_amt':3988.44,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=5,day=11).date(),'received':0,'payment_amt':3183.29,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=11).date(),'received':0,'payment_amt':2587.85,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=7,day=11).date(),'received':0,'payment_amt':1789.26,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=8,day=11).date(),'received':0,'payment_amt':1229.49,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=9,day=11).date(),'received':0,'payment_amt':804.12,'payment_type':'INTEREST'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=10,day=11).date(),'received':0,'payment_amt':399.39,'payment_type':'INTEREST'})


register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=7,day=11).date(),'received':0,'payment_amt':160735.93,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=11).date(),'received':0,'payment_amt':67498.04,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=9,day=11).date(),'received':0,'payment_amt':67865.62,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=10,day=11).date(),'received':0,'payment_amt':68515.97,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=11).date(),'received':0,'payment_amt':68695.57,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=11).date(),'received':0,'payment_amt':69265.6,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=1,day=11).date(),'received':0,'payment_amt':69514.2,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=11).date(),'received':0,'payment_amt':69856.73,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=3,day=11).date(),'received':0,'payment_amt':70719.03,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=4,day=11).date(),'received':0,'payment_amt':70953.45,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=5,day=11).date(),'received':0,'payment_amt':71208.84,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=11).date(),'received':0,'payment_amt':75004.39,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=7,day=11).date(),'received':0,'payment_amt':62871.41,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=8,day=11).date(),'received':0,'payment_amt':43176.22,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=9,day=11).date(),'received':0,'payment_amt':39728.65,'payment_type':'PRINCIPAL'})
register_cashflow(isin="INE275315013",pos_id=7,cashflow_payload={'pay_date':datetime(year=2026,month=10,day=11).date(),'received':0,'payment_amt':41890.37,'payment_type':'PRINCIPAL'})
'''
'''
#- INE0NES07188 8
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2025,month=8,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2025,month=9,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2025,month=10,day=11).date(),'received':0,'payment_amt':5523.3,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2025,month=11,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2025,month=12,day=11).date(),'received':0,'payment_amt':5523.3,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=1,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=2,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=3,day=11).date(),'received':0,'payment_amt':5155.08,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=4,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=5,day=11).date(),'received':0,'payment_amt':5523.3,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=6,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=7,day=11).date(),'received':0,'payment_amt':5523.3,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=8,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=9,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=10,day=11).date(),'received':0,'payment_amt':5523.3,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=11,day=11).date(),'received':0,'payment_amt':5707.38,'payment_type':'INTEREST'})
register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2026,month=12,day=11).date(),'received':0,'payment_amt':5523.3,'payment_type':'INTEREST'})

register_cashflow(isin="INE0NES07188",pos_id=8,cashflow_payload={'pay_date':datetime(year=2025,month=7,day=11).date(),'received':0,'payment_amt':600000,'payment_type':'PRINCIPAL'})
'''