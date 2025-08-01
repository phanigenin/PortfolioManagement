from enum import Enum
from datetime import date,datetime

OUT_Z_ETER  = datetime.strptime("20991231","%Y%m%d").date()
THRU_Z_ETER = datetime.strptime("20991231","%Y%m%d").date()
TODAY       = datetime.now().date()
ORIGIN      = datetime.strptime("19860309","%Y%m%d").date()
NOW         = datetime.now()