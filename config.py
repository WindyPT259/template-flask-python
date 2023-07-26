from urllib.parse import quote_plus

# APIURL
API_URL = "http://127.0.0.1:5000"

# Connect DB
database = "mysql"
# MYSQL
connection_string = (
    "DRIVER= MySQL ODBC 8.0 ANSI Driver;"
    "SERVER=localhost;"
    "PORT=3306;"
    "DATABASE=sampleapp;"
    "UID=root;"
    "PWD=250997;"
    "charset=utf8mb4;"
)
# # Microsoft SQL Server
# connection_string = (
#     "DRIVER=SQL Server Native Client 11.0;"
#     "SERVER=LTPTHAO\\SQL_THAO;"
#     "DATABASE=sampleapp;"
#     "UID=sa;"
#     "PWD=12345678x@X;"
#     "charset=utf8mb4;"
# )
params = quote_plus(connection_string)
# SQLAlchemy URI
SQLALCHEMY_DATABASE_URI = f"{database}+pyodbc:///?odbc_connect=%s" % params

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_TIMEOUT = 20
DEBUG = True

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Auto reload templates
TEMPLATES_AUTO_RELOAD = True

# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
