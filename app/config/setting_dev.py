class Setting(dict):
    debug = True
    mall_env = 'dev'
    db_url_master = 'sqlite://data/db_data/db.sqlite'
    db_url_slave = 'sqlite://data/db_data/db.sqlite'


setting = Setting()
