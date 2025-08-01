def register_mtm_realised_asof_bizdate(symbol,biz_date,mtm_realised,strategy,sess=None):
    from datamart.tables import MTMRealisedEquityIndia
    from datamart.access import get_valid_session
    import pandas as pd
    from datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_,update

    sess = sess if sess else get_valid_session()
    obj  = MTMRealisedEquityIndia(symbol=symbol,biz_date=biz_date,strategy=strategy,mtm_realised=mtm_realised)
    sess.add(obj)
    sess.commit()

def register_mtm_realised_asof_bizdate_equity_dividends(symbol,biz_date,mtm_realised,strategy,sess=None):
    from datamart.tables import MTMRealisedEquityIndiaDividends
    from datamart.access import get_valid_session
    import pandas as pd
    from datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_,update

    sess = sess if sess else get_valid_session()
    obj  = MTMRealisedEquityIndiaDividends(symbol=symbol,biz_date=biz_date,strategy=strategy,mtm_realised=mtm_realised)
    sess.add(obj)
    sess.commit()

def register_mtm_realised_asof_bizdate_equity_derivatives(symbol,biz_date,mtm_realised,strategy,sess=None):
    from datamart.tables import MTMRealisedEquityIndiaDerivatives
    from datamart.access import get_valid_session
    import pandas as pd
    from datamart.consts import TODAY,THRU_Z_ETER
    from sqlalchemy import and_,update

    sess = sess if sess else get_valid_session()
    obj  = MTMRealisedEquityIndiaDerivatives(symbol=symbol,biz_date=biz_date,strategy=strategy,mtm_realised=mtm_realised)
    sess.add(obj)
    sess.commit()