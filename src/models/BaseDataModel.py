from helpers.config import get_settings,Settings

class BaseDataModel:
    def __init__(self,df_client:object):
        self.db_client=self.db_client
        self.app_settings=get_settings()