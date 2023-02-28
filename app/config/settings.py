import os
import importlib

mall_env = os.getenv('PLANT_ENV', 'dev')
module_name = f'app.config.setting_{mall_env}'

try:
    m = importlib.import_module(module_name)
    setting = m.setting
except ModuleNotFoundError as e:
    print(str(e))
    from app.config.setting_dev import setting
