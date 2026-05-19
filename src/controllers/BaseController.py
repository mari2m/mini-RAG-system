from helpers.config import get_settings,Settings

class BaseController:
    def __init__(self):
        self.app_settings=get_settings()
        self.size_scale = 1024 * 1024
        