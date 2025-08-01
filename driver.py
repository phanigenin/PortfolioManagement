from datetime import datetime
from middletier.equity.transactions import register_transaction,get_trn_all,get_trn_bizdate
from middletier.equity.positions import get_pos_all_open
#register_transaction("COLPAL",trn_payload={"trn_buysell":"B","trn_price":1443.0,"trn_qty":250.0,"trn_date":dt1,"strategy":"value"})
#print(get_open_transactions())
#print(get_trn_all())
#print(get_trn_bizdate(dt1))
#print(get_trn_all())

#print(get_trn_bizdate(dt1))




#calc_pos_asof_bizdate(biz_date=dt1)
#close_pos_asof_bizdate(symbol="COLPAL",biz_date=dt1)
#print(get_pos_all_open())
#print(get_pos_asof_bizdate(biz_date=dt1))
dt1=datetime(year=2025,month=6,day=26).date()

from middletier.equity.mtm_realised import register_mtm_realised_asof_bizdate, register_mtm_realised_asof_bizdate_equity_dividends, register_mtm_realised_asof_bizdate_equity_derivatives
print(get_pos_all_open())
#register_transaction("GATEWAY",trn_payload={"trn_buysell":"B","trn_price":82.7,"trn_qty":3000.0,"trn_date":dt1,"strategy":"value"})
#calc_pos_asof_bizdate(biz_date=dt1)
#register_mtm_realised_asof_bizdate_equity_dividends(symbol="COLPAL",biz_date=dt1,strategy="dividends",mtm_realised=12750)
#register_mtm_realised_asof_bizdate_equity_dividends(symbol="INOXINDIA",biz_date=dt1,strategy="dividends",mtm_realised=50)
#register_mtm_realised_asof_bizdate_equity_derivatives(symbol="COLPAL",biz_date=dt1,strategy="coveredcall",mtm_realised=-81435)