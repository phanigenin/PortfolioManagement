def register_cashflow(isin,pos_id,cashflow_payload,sess=None):
    from PortfolioManagement.datamart.tables import CashFlowsBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    import pandas as pd

    sess    = sess if sess else get_valid_session()
    trn_obj = CashFlowsBondIndia(isin=isin,pos_id=pos_id,**cashflow_payload)
    print("adding Cashflow : {0}".format(str(trn_obj)))
    sess.add(trn_obj)
    sess.commit()

def get_cashflows_by_isin(isin,sess=None):
    from PortfolioManagement.datamart.tables import CashFlowsBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    import pandas as pd
    from PortfolioManagement.datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_

    sess    = sess if sess else get_valid_session()
    qry  = (
                sess.query(CashFlowsBondIndia.isin,CashFlowsBondIndia.pos_id,CashFlowsBondIndia.pay_date,CashFlowsBondIndia.payment_amt,
                           CashFlowsBondIndia.received,CashFlowsBondIndia.payment_type)
                .filter(and_ ( CashFlowsBondIndia.out_z>TODAY,CashFlowsBondIndia.isin==isin) )
           )
    return pd.read_sql(qry.statement, sess.bind)

def get_cashflows_by_user(user,biz_date,sess=None):
    from PortfolioManagement.datamart.tables import CashFlowsBondIndia,PositionBondIndia,InstrumentsBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    import pandas as pd
    from PortfolioManagement.datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_

    sess    = sess if sess else get_valid_session()
    qry  = (
                sess.query(PositionBondIndia.isin,PositionBondIndia.pos_user,PositionBondIndia.pos_amt,PositionBondIndia.pos_source,
                           InstrumentsBondIndia.issuer,CashFlowsBondIndia.received,
                           CashFlowsBondIndia.pay_date,CashFlowsBondIndia.payment_amt,CashFlowsBondIndia.payment_type)
                .join(InstrumentsBondIndia, InstrumentsBondIndia.isin==PositionBondIndia.isin)
                .join(CashFlowsBondIndia,CashFlowsBondIndia.isin==PositionBondIndia.isin,CashFlowsBondIndia.pos_id==PositionBondIndia.pos_id)
                .filter(and_ ( CashFlowsBondIndia.out_z>=THRU_Z_ETER, PositionBondIndia.pos_user==user, PositionBondIndia.out_z>=THRU_Z_ETER,PositionBondIndia.thru_z>=biz_date) )
           )
    return pd.read_sql(qry.statement, sess.bind)

def get_cashflows_for_open_positions(biz_date,sess=None):
    from PortfolioManagement.datamart.tables import CashFlowsBondIndia,PositionBondIndia,InstrumentsBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    import pandas as pd
    from PortfolioManagement.datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_
    from sqlalchemy import func, case

    sess    = sess if sess else get_valid_session()
    cashflow_month_number = func.strftime('%m', CashFlowsBondIndia.pay_date)

    cashflow_month_name = case(
        (cashflow_month_number == '01', 'January'),
        (cashflow_month_number == '02', 'February'),
        (cashflow_month_number == '03', 'March'),
        (cashflow_month_number == '04', 'April'),
        (cashflow_month_number == '05', 'May'),
        (cashflow_month_number == '06', 'June'),
        (cashflow_month_number == '07', 'July'),
        (cashflow_month_number == '08', 'August'),
        (cashflow_month_number == '09', 'September'),
        (cashflow_month_number == '10', 'October'),
        (cashflow_month_number == '11', 'November'),
        (cashflow_month_number == '12', 'December'),
    )

    qry  = (
                sess.query(PositionBondIndia.isin,PositionBondIndia.pos_user,PositionBondIndia.pos_amt,PositionBondIndia.pos_source,
                           InstrumentsBondIndia.issuer,CashFlowsBondIndia.received,
                           CashFlowsBondIndia.pay_date,CashFlowsBondIndia.payment_amt,CashFlowsBondIndia.payment_type,cashflow_month_name.label("month"))
                .join(InstrumentsBondIndia, InstrumentsBondIndia.isin==PositionBondIndia.isin)
                .join(CashFlowsBondIndia,and_(CashFlowsBondIndia.isin==PositionBondIndia.isin,CashFlowsBondIndia.pos_id==PositionBondIndia.pos_id))
                .filter(and_ ( CashFlowsBondIndia.out_z>=THRU_Z_ETER,  PositionBondIndia.out_z>=THRU_Z_ETER,PositionBondIndia.thru_z>=biz_date) )
           )
    return pd.read_sql(qry.statement, sess.bind)