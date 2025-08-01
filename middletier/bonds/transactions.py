def get_trn_all(sess=None):
    '''
    Get all Open Transactions

    :param sess:
    :return:
    '''
    from datamart.tables import TransactionsBondIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess = sess if sess else get_valid_session()
    qry  = sess.query(TransactionsBondIndia)
    return pd.read_sql(qry.statement, sess.bind)


def get_trn_bizdate(biz_date,sess=None):
    '''
    Get all Open Transactions on given bizDate

    :param sess:
    :return:
    '''
    from datamart.tables import TransactionsBondIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess = sess if sess else get_valid_session()
    qry  = sess.query(TransactionsBondIndia).filter(TransactionsBondIndia.trn_date==biz_date)
    return pd.read_sql(qry.statement, sess.bind)

def register_transaction(isin,trn_payload,sess=None):
    from datamart.tables import TransactionsBondIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess    = sess if sess else get_valid_session()
    trn_obj = TransactionsBondIndia(isin=isin,**trn_payload)
    print("adding transaction : {0}".format(str(trn_obj)))
    sess.add(trn_obj)
    sess.commit()

def consolidate_trns(isin,trn_user,trn_df):
    '''
    Given a bunch of transactions on a symbol x bizdate, calculate one lineitem transaction

    :param trn_df:
    :return:
    '''
    import pandas as pd

    #isin      = list(set(trn_df["isin"].values))[0]
    source    = list(set(trn_df["trn_source"].values))[0]
    #user      = list(set(trn_df["trn_user"].values))[0]
    biz_date  = list(set(trn_df["trn_date"].values))[0]
    strategy  = ','.join(list(set(trn_df["strategy"].values)))
    qty,mv,net_trn_price,net_buysell = 0,0,0,''
    for idx,row in trn_df.iterrows():
        trn_qty     = row['trn_qty']
        trn_price   = row['trn_price']
        trn_buysell = row['trn_buysell']
        trn_amt     = row['trn_amt']
        qty = qty+trn_qty if trn_buysell=="B" else qty-trn_qty
        #mv = mv + trn_qty*trn_price if trn_buysell == "B" else mv - trn_qty*trn_price
        mv = mv + trn_amt if trn_buysell == "B" else mv - trn_amt

    if abs(qty)<0.1:
        return pd.DataFrame()
    else:
        net_trn_price = mv/(qty*100)# for BONDS quote
        net_buysell    = "B" if qty>0 else "S"

    trn_cons = {"isin":isin, "trn_buysell":net_buysell,"trn_qty":qty,"trn_price":net_trn_price,"trn_date":biz_date,
                "strategy":strategy,"trn_amt":mv,"trn_source":source,"trn_user":trn_user}
    return trn_cons
