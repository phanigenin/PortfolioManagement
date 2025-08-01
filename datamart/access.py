PATH_WIDOWS     = "F:\\PortfolioManagement\\"
PATH_LINUX      = "/External/Store/PortfolioManagement/"

REP_PATH_WINDOWS ="sqlite:///F:\\PortfolioManagement\\portfolio.db"
REP_PATH_LINUX =  "sqlite:////External/Store/PortfolioManagement/portfolio.db"

#CONTENT_PATH_WIDOWS     = "F:\\PortfolioManagement\\ArticleContent"

def get_valid_session():
    from datamart.tables import get_database_session
    from utils import is_windows

    path = REP_PATH_WINDOWS if is_windows() else REP_PATH_LINUX
    eng,session = get_database_session(repository_path=path)
    return session

def get_valid_engine():
    from datamart.tables import get_database_session
    from utils import is_windows

    path = REP_PATH_WINDOWS if is_windows() else REP_PATH_LINUX
    eng,session = get_database_session(repository_path=path)
    return eng
