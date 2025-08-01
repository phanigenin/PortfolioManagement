def register_instrument(isin,instr_payload,sess=None):
    from datamart.tables import InstrumentsBondIndia
    from datamart.access import get_valid_session
    import pandas as pd

    sess    = sess if sess else get_valid_session()
    trn_obj = InstrumentsBondIndia(isin=isin,**instr_payload)
    print("adding transaction : {0}".format(str(trn_obj)))
    sess.add(trn_obj)
    sess.commit()