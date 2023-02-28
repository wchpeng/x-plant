class Setting(dict):
    debug = True
    mall_env = 'dev'
    db_url_master = 'sqlite://./app/data/db.sqlite'
    db_url_slave = 'sqlite://./app/data/db.sqlite'


setting = Setting()
