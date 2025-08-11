def register_cashflow(isin,pos_id,cashflow_payload,sess=None):
    from PortfolioManagement.datamart.tables import CashFlowsBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    import pandas as pd

    sess    = sess if sess else get_valid_session()
    trn_obj = CashFlowsBondIndia(isin=isin,pos_id=pos_id,**cashflow_payload)
    print("adding Cashflow : {0}".format(str(trn_obj)))
    sess.add(trn_obj)
    sess.commit()