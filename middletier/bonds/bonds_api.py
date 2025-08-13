from datetime import datetime
def get_all_bond_positions(biz_date=datetime.today().date()):
    '''
    Simple OPEN bond positions query
    :param biz_date:
    :return:
    '''
    from positions import get_pos_asof_bizdate
    return get_pos_asof_bizdate(biz_date)

def get_all_bond_positions_detail(biz_date=datetime.today().date()):
    '''
    Query OPEN bond positions, along with ISIN, issuer Details
    :param biz_date:
    :return:
    '''
    from middletier.bonds.positions import get_pos_asof_bizdate_detail
    return get_pos_asof_bizdate_detail(biz_date)

def get_all_bond_positions_closed(biz_date=datetime.today().date()):
    '''
    Query CLOSED bond positions, along with ISIN, issuer Details
    :param biz_date:
    :return:
    '''
    from positions import get_pos_closed_asof_bizdate_detail
    return get_pos_closed_asof_bizdate_detail(biz_date)

def get_all_bond_positions_detail_by_user(user,biz_date=datetime.today().date()):
    '''
    Query CLOSED bond positions, along with ISIN, issuer Details, by USER
    :param user:
    :param biz_date:
    :return:
    '''
    from positions import get_pos_asof_bizdate_detail_by_user
    return get_pos_asof_bizdate_detail_by_user(user,biz_date)

def get_cashflows_by_isin(isin):
    '''
    Query ALL cashflows by ISIN
    :param isin:
    :return:
    '''
    from cashflows import get_cashflows_by_isin
    return get_cashflows_by_isin(isin)

def get_cashflows_by_user(user,biz_date=datetime.today().date()):
    '''
    QUERY ALL cashflows, for a user
    :param user:
    :param biz_date:
    :return:
    '''
    from cashflows import get_cashflows_by_user
    return get_cashflows_by_user(user,biz_date)

def get_cashflows_by_month(biz_date=datetime.today().date()):
    '''
    QUERY ALL cashflows
    :param user:
    :param biz_date:
    :return:
    '''
    from cashflows import get_cashflows_for_open_positions
    return get_cashflows_for_open_positions(biz_date)

def get_cashflows_upcoming(biz_date=datetime.today().date(),months=2):
    '''
    QUERY ALL cashflows, for next N months
    :param biz_date:
    :param months:
    :return:
    '''
    from cashflows import get_cashflows_for_open_positions
    from dateutil.relativedelta import relativedelta

    res      = get_cashflows_for_open_positions(biz_date)
    tgt_date = biz_date + relativedelta(months=months)
    return res[(res["pay_date"]<=tgt_date)&(res["received"]==0)]

def get_cashflows_received(biz_date=datetime.today().date()):
    '''
    QUERY ALL cashflows, for next N months, ALREADY Received
    :param biz_date:
    :param months:
    :return:
    '''
    from cashflows import get_cashflows_for_open_positions

    res      = get_cashflows_for_open_positions(biz_date)
    return res[(res["pay_date"]<=biz_date)&(res["received"]==1)]

def get_amount_invested_details(biz_date=datetime.today().date()):
    '''
    Amount invested, in open positions + principal received
    Locked = Invested - received

    :param biz_date:
    :return:
    '''
    from positions import get_pos_asof_bizdate_detail
    import pandas as pd

    res = get_pos_asof_bizdate_detail(biz_date)
    cash_received = get_cashflows_received(biz_date)

    principal_received = cash_received[cash_received["payment_type"]=="PRINCIPAL"].groupby(['pos_user','isin'], as_index=False)['payment_amt'].sum()\
        .rename(columns={'payment_amt': 'princial_received'})

    invested = res.groupby(['pos_user','isin'], as_index=False)['pos_amt'].sum()\
        .rename(columns={'pos_amt': 'invested'})

    inv_detail = pd.merge(invested,principal_received,how="left",on=['pos_user','isin'])
    inv_detail = inv_detail.fillna(0)
    inv_detail["principal_locked"] = inv_detail.apply(lambda x: x["invested"] - x["princial_received"],axis=1)
    inv_detail["principal_pct_locked"] = inv_detail.apply(lambda x: ((x["invested"] - x["princial_received"])/x["invested"])*100, axis=1)
    return inv_detail


def get_interest_received_details(biz_date=datetime.today().date()):
    '''
    Amount invested, in open positions

    :param biz_date:
    :return:
    '''
    from positions import get_pos_asof_bizdate_detail
    import pandas as pd

    res           = get_pos_asof_bizdate_detail(biz_date)
    cash_received = get_cashflows_received(biz_date)

    interest_received = cash_received[cash_received["payment_type"]=="INTEREST"].groupby(['pos_user','isin'], as_index=False)['payment_amt'].sum()\
        .rename(columns={'payment_amt': 'interest_received'})

    invested =  res.groupby(['pos_user','isin'], as_index=False)['pos_amt'].sum()\
        .rename(columns={'pos_amt': 'invested'})

    inv_detail = pd.merge(invested, interest_received, how="left", on=['pos_user', 'isin'])
    inv_detail = inv_detail.fillna(0)

    inv_detail["interest_pct_return"] = inv_detail.apply(lambda x: (x["interest_received"]/x["invested"])*100,axis=1)

    return inv_detail

def calculate_investment_returns(biz_date=datetime.today().date()):
    import pandas as pd

    principal_rets = get_amount_invested_details(biz_date)
    interest_rets  = get_interest_received_details(biz_date)
    #print(interest_rets.columns)
    interest_rets  = interest_rets.drop(columns=["invested"])
    returns_detail = pd.merge(principal_rets, interest_rets, how="left", on=['pos_user', 'isin'])
    return returns_detail

def get_bond_instruments():
    import pandas as pd
    from instruments import get_instruments
    return get_instruments()

def get_bond_instruments_by_isins(isins):
    import pandas as pd
    from instruments import get_instrument_by_isins
    return get_instrument_by_isins(isins)

def get_instrument_by_issuers(issuers):
    import pandas as pd
    from instruments import get_instrument_by_issuers
    return get_instrument_by_issuers(issuers)

#print(get_all_bond_positions_detail())
#print(get_all_bond_positions_closed())
#print(get_all_bond_positions_detail_by_user("PHANI"))
#print(get_all_bond_positions_detail_by_user("JANAKI"))

#print(get_cashflows_by_isin("INE0RU307171"))

'''
print(get_cashflows_by_month())
print(get_cashflows_upcoming())
print(get_cashflows_received())
'''

#print(get_amount_invested_details())
#print(get_interest_received_details())
#print(calculate_investment_returns())
#print(calculate_investment_returns().columns)