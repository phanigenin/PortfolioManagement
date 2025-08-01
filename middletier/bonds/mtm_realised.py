def register_mtm_realised_asof_bizdate(isin,biz_date,mtm_realised,strategy,mtm_user,sess=None):
    from datamart.tables import MTMRealisedBondIndia
    from datamart.access import get_valid_session
    import pandas as pd
    from datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_,update

    sess = sess if sess else get_valid_session()
    obj  = MTMRealisedBondIndia(isin=isin,biz_date=biz_date,strategy=strategy,mtm_realised=mtm_realised,mtm_user=mtm_user)
    sess.add(obj)
    sess.commit()
