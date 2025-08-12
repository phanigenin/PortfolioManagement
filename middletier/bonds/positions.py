def get_pos_all_open(sess=None):
    from PortfolioManagement.datamart.consts import TODAY
    return get_pos_asof_bizdate(TODAY,sess)

def get_pos_asof_bizdate(biz_date,sess=None):
    from PortfolioManagement.datamart.tables import PositionBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    import pandas as pd
    from PortfolioManagement.datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_

    sess = sess if sess else get_valid_session()
    qry  = sess.query(PositionBondIndia).filter(and_(PositionBondIndia.out_z>=THRU_Z_ETER,PositionBondIndia.from_z<=biz_date,PositionBondIndia.thru_z==THRU_Z_ETER))
    return pd.read_sql(qry.statement, sess.bind)

def get_pos_asof_bizdate_detail(biz_date,sess=None):
    from PortfolioManagement.datamart.tables import PositionBondIndia,InstrumentsBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    import pandas as pd
    from PortfolioManagement.datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_

    sess = sess if sess else get_valid_session()
    qry  = (
                sess.query(PositionBondIndia.isin,PositionBondIndia.from_z,PositionBondIndia.pos_user,PositionBondIndia.pos_source,InstrumentsBondIndia.coupon,
                           PositionBondIndia.open_qty,PositionBondIndia.pos_amt,
                           InstrumentsBondIndia.bond_type,InstrumentsBondIndia.issuer,InstrumentsBondIndia.descr)
                .join(InstrumentsBondIndia, PositionBondIndia.isin == InstrumentsBondIndia.isin)
                .filter(and_(PositionBondIndia.out_z>=THRU_Z_ETER,PositionBondIndia.from_z<=biz_date,PositionBondIndia.thru_z==THRU_Z_ETER))
           )

    return pd.read_sql(qry.statement, sess.bind)

def get_pos_asof_bizdate_detail_by_user(user,biz_date,sess=None):
    from PortfolioManagement.datamart.tables import PositionBondIndia,InstrumentsBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    import pandas as pd
    from PortfolioManagement.datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_

    sess = sess if sess else get_valid_session()
    qry  = (
                sess.query(PositionBondIndia.isin,PositionBondIndia.from_z,PositionBondIndia.pos_user,PositionBondIndia.pos_source,InstrumentsBondIndia.coupon,
                           PositionBondIndia.open_qty,PositionBondIndia.pos_amt,
                           InstrumentsBondIndia.bond_type,InstrumentsBondIndia.issuer,InstrumentsBondIndia.descr)
                .join(InstrumentsBondIndia, PositionBondIndia.isin == InstrumentsBondIndia.isin)
                .filter(and_(PositionBondIndia.out_z>=THRU_Z_ETER,PositionBondIndia.from_z<=biz_date,PositionBondIndia.thru_z==THRU_Z_ETER,PositionBondIndia.pos_user==user))
           )

    return pd.read_sql(qry.statement, sess.bind)

def get_pos_closed_asof_bizdate_detail(biz_date,sess=None):
    from PortfolioManagement.datamart.tables import PositionBondIndia,InstrumentsBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    import pandas as pd
    from PortfolioManagement.datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_

    sess = sess if sess else get_valid_session()
    qry  = (
                sess.query(PositionBondIndia.isin,PositionBondIndia.from_z,PositionBondIndia.pos_user,PositionBondIndia.pos_source,InstrumentsBondIndia.coupon,
                           PositionBondIndia.open_qty,PositionBondIndia.pos_amt,
                           InstrumentsBondIndia.bond_type,InstrumentsBondIndia.issuer,InstrumentsBondIndia.descr)
                .join(InstrumentsBondIndia, PositionBondIndia.isin == InstrumentsBondIndia.isin)
                .filter(and_(PositionBondIndia.out_z>=THRU_Z_ETER,PositionBondIndia.from_z<=biz_date,PositionBondIndia.thru_z<=biz_date))
           )

    return pd.read_sql(qry.statement, sess.bind)


def close_pos_asof_bizdate(isin,biz_date,sess=None):
    from PortfolioManagement.datamart.tables import PositionBondIndia
    from PortfolioManagement.datamart.access import get_valid_session
    from PortfolioManagement.datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_,update

    sess = sess if sess else get_valid_session()
    qry  = (update(PositionBondIndia).where(and_(PositionBondIndia.out_z>=THRU_Z_ETER,PositionBondIndia.from_z<=biz_date,PositionBondIndia.thru_z==THRU_Z_ETER,PositionBondIndia.isin==isin)).values({PositionBondIndia.thru_z:biz_date}))
    sess.execute(qry)
    sess.commit()

def register_pos_asof_bizdate(isin,biz_date,price,qty,amount,strategy,pos_source,pos_user,sess=None):
    from PortfolioManagement.datamart.tables import PositionBondIndia
    from PortfolioManagement.datamart.access import get_valid_session

    sess = sess if sess else get_valid_session()
    obj  = PositionBondIndia(isin=isin,open_price=price,open_qty=qty,biz_date=biz_date,strategy=strategy,pos_amt=amount,
                             pos_source=pos_source,pos_user=pos_user)
    sess.add(obj)
    sess.commit()

def calc_pos_asof_bizdate(biz_date,sess=None):
    from PortfolioManagement.middletier.bonds.transactions import get_trn_bizdate,consolidate_trns
    from PortfolioManagement.middletier.bonds.mtm_realised import register_mtm_realised_asof_bizdate

    trn_asof = get_trn_bizdate(biz_date=biz_date,sess=sess)
    pos_asof = get_pos_asof_bizdate(biz_date=biz_date,sess=sess)
    print(pos_asof)


    all_syms = set(pos_asof["isin"].values).union( set(trn_asof["isin"].values) )
    add_objs,update_objs = [],[]
    for (isin,trn_user),group_df in trn_asof.groupby(["isin","trn_user"]):
        print("Calculating Position for ISIN :", isin)
        trn_cons     = consolidate_trns(isin,trn_user,group_df)
        if not len(trn_cons):
            print(" No new transaction impact ! skipping...")
            continue

        existing_pos = pos_asof[pos_asof["isin"]==isin]
        #register_pos_asof_bizdate(isin,biz_date,price,qty,amount,strategy,pos_source,pos_user
        #register_mtm_realised_asof_bizdate(isin,biz_date,mtm_realised,strategy,mtm_user
        mtm_realised = 0
        if not len(existing_pos):
            print("New position entered ! ")
            register_pos_asof_bizdate(isin=isin,strategy=trn_cons["strategy"],price=trn_cons["trn_price"],qty=trn_cons["trn_qty"],amount=trn_cons["trn_amt"],
                                      pos_source=trn_cons["trn_source"],pos_user=trn_cons["trn_user"],biz_date=trn_cons["trn_date"],sess=sess)
        else:
            print("netting with existing positions")

            old_pos_qty   = (existing_pos["open_qty"].values)[0]
            old_pos_price = (existing_pos["open_price"].values)[0]
            old_pos_strategy = (existing_pos["strategy"].values)[0]
            old_pos_amt      = (existing_pos["pos_amt"].values)[0]
            new_pos_price,new_pos_amt = 0,0
            print(old_pos_qty,old_pos_price,trn_cons["trn_qty"])
            if trn_cons["trn_buysell"] == "B":#additional buy
                new_pos_qty    = old_pos_qty + trn_cons["trn_qty"]
                new_pos_price  = (old_pos_price*old_pos_qty +  trn_cons["trn_qty"]*trn_cons["trn_price"])/new_pos_qty
                new_pos_amt    = old_pos_amt + trn_cons["trn_amt"]

            else:
                new_pos_qty    = old_pos_qty - trn_cons["trn_qty"]
                #new_pos_price  = (old_pos_price*old_pos_qty -  trn_cons["trn_qty"]*trn_cons["trn_price"])/new_pos_qty
                #if abs(new_pos_qty)>abs(old_pos_qty):# Sold more than existing
                #   new_pos_price = trn_cons["trn_price"]
                #else:
                #   new_pos_price = old_pos_price
                new_pos_price = trn_cons["trn_price"] if abs(new_pos_qty)>abs(old_pos_qty) else old_pos_price
                mtm_realised  = old_pos_price*old_pos_qty + trn_cons["trn_qty"]*trn_cons["trn_price"]
                new_pos_amt   = old_pos_amt - trn_cons["trn_amt"]
                #mtm_realised = abs(trn_cons["trn_qty"])*( - old_pos_price+trn_cons["trn_price"])
                print("matching sell... NewQty : {0} , OldQty : {1} , NewPrice : {2} , MtmRealised : {3} ".format( new_pos_qty, old_pos_qty, new_pos_price , mtm_realised) )

            strats = set([old_pos_strategy,trn_cons["strategy"]])
            new_strategy   = ','.join(strats)
            close_pos_asof_bizdate(isin=isin,biz_date=trn_cons["trn_date"],sess=sess)

            if abs(new_pos_qty)>0:
                print(" NET POSITION to be persisted !!",isin, trn_cons["trn_qty"],trn_cons["trn_amt"])

                register_pos_asof_bizdate(isin=isin, strategy=new_strategy, price=new_pos_price,
                                          qty=new_pos_qty, amount=new_pos_amt,
                                          pos_source=trn_cons["trn_source"], pos_user=trn_user,
                                          biz_date=trn_cons["trn_date"], sess=sess)

            if abs(mtm_realised)>0:
                print(" MTM Realised entry !!", isin, mtm_realised,trn_cons["trn_date"],trn_cons["trn_user"])
                register_mtm_realised_asof_bizdate(isin=isin,strategy=new_strategy,mtm_realised=mtm_realised,biz_date=trn_cons["trn_date"],mtm_user=trn_user,sess=sess)



