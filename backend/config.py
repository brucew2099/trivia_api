import dbconfig as cfg

# Connect to the database
USER = cfg.postgressql['user']
PASSWD = cfg.postgressql['passwd']
HOST = cfg.postgressql['host']
PORT = cfg.postgressql['port']
DB = cfg.postgressql['db']
DBTEST = cfg.postgressql['db_test']

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(USER, PASSWD, HOST, PORT, DB)
SQLALCHEMY_TEST_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(USER, PASSWD, HOST, PORT, DBTEST)
SQLALCHEMY_TRACK_MODIFICATIONS = False