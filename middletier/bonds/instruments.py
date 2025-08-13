def register_instrument(isin,instr_payload,sess=None):
    '''
    Register a new BOND instrument

    :param isin:
    :param instr_payload:
    :param sess:
    :return:
    '''
    from datamart.tables import InstrumentsBondIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess    = sess if sess else get_valid_session()
    trn_obj = InstrumentsBondIndia(isin=isin,**instr_payload)
    print("adding transaction : {0}".format(str(trn_obj)))
    sess.add(trn_obj)
    sess.commit()

def get_instruments(sess=None):
    '''
    GET all bond instruments registered in the system

    :param sess:
    :return:
    '''
    from datamart.tables import InstrumentsBondIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess    = sess if sess else get_valid_session()
    qry = sess.query(InstrumentsBondIndia)
    return pd.read_sql(qry.statement, sess.bind)

def get_instrument_by_isins(isins,sess=None):
    '''
    GET all bond instruments registered in the system, given LIST of isins

    :param isins:
    :param sess:
    :return:
    '''
    from datamart.tables import InstrumentsBondIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess    = sess if sess else get_valid_session()
    qry = sess.query(InstrumentsBondIndia).filter(InstrumentsBondIndia.isin.in_(isins))
    return pd.read_sql(qry.statement, sess.bind)

def get_instrument_by_issuers(issuers,sess=None):
    from datamart.tables import InstrumentsBondIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess    = sess if sess else get_valid_session()
    qry = sess.query(InstrumentsBondIndia).filter(InstrumentsBondIndia.issuer.in_(issuers))
    return pd.read_sql(qry.statement, sess.bind)