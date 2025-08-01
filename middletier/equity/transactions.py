def get_trn_all(sess=None):
    '''
    Get all Open Transactions

    :param sess:
    :return:
    '''
    from datamart.tables import TransactionsEquityIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess = sess if sess else get_valid_session()
    qry  = sess.query(TransactionsEquityIndia)
    return pd.read_sql(qry.statement, sess.bind)


def get_trn_bizdate(biz_date,sess=None):
    '''
    Get all Open Transactions on given bizDate

    :param sess:
    :return:
    '''
    from datamart.tables import TransactionsEquityIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess = sess if sess else get_valid_session()
    qry  = sess.query(TransactionsEquityIndia).filter(TransactionsEquityIndia.trn_date==biz_date)
    return pd.read_sql(qry.statement, sess.bind)

def register_transaction(symbol,trn_payload,sess=None):
    from datamart.tables import TransactionsEquityIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess    = sess if sess else get_valid_session()
    trn_obj = TransactionsEquityIndia(symbol=symbol,**trn_payload)
    print("adding transaction : {0}".format(str(trn_obj)))
    sess.add(trn_obj)
    sess.commit()

def consolidate_trns(trn_df):
    '''
    Given a bunch of transactions on a symbol x bizdate, calculate one lineitem transaction

    :param trn_df:
    :return:
    '''
    import pandas as pd

    sym      = list(set(trn_df["symbol"].values))[0]
    biz_date = list(set(trn_df["trn_date"].values))[0]
    strategy = ','.join(list(set(trn_df["strategy"].values)))
    qty,mv = 0,0
    for idx,row in trn_df.iterrows():
        trn_qty     = row['trn_qty']
        trn_price   = row['trn_price']
        trn_buysell = row['trn_buysell']

        qty = qty+trn_qty if trn_buysell=="B" else qty-trn_qty
        mv = mv + trn_qty*trn_price if trn_buysell == "B" else mv - trn_qty*trn_price

    if abs(qty)<0.1:
        return pd.DataFrame()
    else:
        net_trn_price = mv/qty
        net_buysell    = "B" if qty>0 else "S"

    trn_cons = {"symbol":sym, "trn_buysell":net_buysell,"trn_qty":qty,"trn_price":net_trn_price,"trn_date":biz_date,"strategy":strategy}
    return trn_cons



