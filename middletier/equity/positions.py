def get_pos_all_open(sess=None):
    from datamart.consts import TODAY
    return get_pos_asof_bizdate(TODAY,sess)

def get_pos_asof_bizdate(biz_date,sess=None):
    from datamart.tables import PositionEquityIndia
    from datamart.access import get_valid_session
    import pandas as pd
    from datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_

    sess = sess if sess else get_valid_session()
    qry  = sess.query(PositionEquityIndia).filter(and_(PositionEquityIndia.out_z>TODAY,PositionEquityIndia.from_z<=biz_date,PositionEquityIndia.thru_z==THRU_Z_ETER))
    return pd.read_sql(qry.statement, sess.bind)

def close_pos_asof_bizdate(symbol,biz_date,sess=None):
    from datamart.tables import PositionEquityIndia
    from datamart.access import get_valid_session
    from datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_,update

    sess = sess if sess else get_valid_session()
    qry  = (update(PositionEquityIndia).where(and_(PositionEquityIndia.out_z>TODAY,PositionEquityIndia.from_z<=biz_date,PositionEquityIndia.thru_z==THRU_Z_ETER,PositionEquityIndia.symbol==symbol)).values({PositionEquityIndia.thru_z:biz_date}))
    sess.execute(qry)
    sess.commit()

def register_pos_asof_bizdate(symbol,biz_date,price,qty,strategy,sess=None):
    from datamart.tables import PositionEquityIndia
    from datamart.access import get_valid_session

    sess = sess if sess else get_valid_session()
    obj  = PositionEquityIndia(symbol=symbol,open_price=price,open_qty=qty,biz_date=biz_date,strategy=strategy)
    sess.add(obj)
    sess.commit()

def calc_pos_asof_bizdate(biz_date,sess=None):
    from middletier.equity.transactions import get_trn_bizdate,consolidate_trns
    from middletier.equity.mtm_realised import register_mtm_realised_asof_bizdate

    trn_asof = get_trn_bizdate(biz_date=biz_date,sess=sess)
    pos_asof = get_pos_asof_bizdate(biz_date=biz_date,sess=sess)
    print(pos_asof)


    all_syms = set(pos_asof["symbol"].values).union( set(trn_asof["symbol"].values) )
    add_objs,update_objs = [],[]
    for sym,group_df in trn_asof.groupby("symbol"):
        print("Calculating Position for sym:", sym)
        trn_cons     = consolidate_trns(group_df)
        existing_pos = pos_asof[pos_asof["symbol"]==sym]

        if not len(trn_cons):
            print(" No new transaction impact ! skipping...")
            continue

        mtm_realised = 0
        if not len(existing_pos):
            print("New position entered ! ")
            register_pos_asof_bizdate(symbol=sym,strategy=trn_cons["strategy"],price=trn_cons["trn_price"],qty=trn_cons["trn_qty"],biz_date=trn_cons["trn_date"],sess=sess)
        else:
            print("netting with existing positions")

            old_pos_qty   = (existing_pos["open_qty"].values)[0]
            old_pos_price = (existing_pos["open_price"].values)[0]
            old_pos_strategy = (existing_pos["strategy"].values)[0]
            print(old_pos_qty,old_pos_price,trn_cons["trn_qty"])
            if trn_cons["trn_buysell"] == "B":#additional buy
                new_pos_qty    = old_pos_qty + trn_cons["trn_qty"]
                new_pos_price  = (old_pos_price*old_pos_qty +  trn_cons["trn_qty"]*trn_cons["trn_price"])/new_pos_qty
            else:
                new_pos_qty    = old_pos_qty - trn_cons["trn_qty"]
                #new_pos_price  = (old_pos_price*old_pos_qty -  trn_cons["trn_qty"]*trn_cons["trn_price"])/new_pos_qty
                #if abs(new_pos_qty)>abs(old_pos_qty):# Sold more than existing
                #   new_pos_price = trn_cons["trn_price"]
                #else:
                #   new_pos_price = old_pos_price
                new_pos_price = trn_cons["trn_price"] if abs(new_pos_qty)>abs(old_pos_qty) else old_pos_price
                mtm_realised  = old_pos_price*old_pos_qty + trn_cons["trn_qty"]*trn_cons["trn_price"]
                #mtm_realised = abs(trn_cons["trn_qty"])*( - old_pos_price+trn_cons["trn_price"])
                print("matching sell... NewQty : {0} , OldQty : {1} , NewPrice : {2} , MtmRealised : {3} ".format( new_pos_qty, old_pos_qty, new_pos_price , mtm_realised) )

            strats = set([old_pos_strategy,trn_cons["strategy"]])
            new_strategy   = ','.join(strats)
            close_pos_asof_bizdate(symbol=sym,biz_date=trn_cons["trn_date"],sess=sess)

            if abs(new_pos_qty)>0:
               register_pos_asof_bizdate(symbol=sym, strategy=new_strategy, price=new_pos_price,
                                          qty=new_pos_qty, biz_date=trn_cons["trn_date"],sess=sess)

            if abs(mtm_realised)>0:
                register_mtm_realised_asof_bizdate(symbol=sym,strategy=new_strategy,mtm_realised=mtm_realised,biz_date=trn_cons["trn_date"],sess=sess)






