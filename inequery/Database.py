import pandas as pd
from os.path import dirname, abspath

module_path = dirname(dirname(abspath(__file__)))
database_relative_path = "\data\indicators.json"
database_path = module_path + database_relative_path

class DataBase():

    def __init__(self):
        self.df = pd.read_json(database_path)

    def get_all_themes(self):
        return self.df.theme.unique()
    
    def get_theme(self, theme):
        return self.df[self.df.theme == theme]
    
    def get_all_theme_subthemes(self, theme):
        return self.df.subtheme[self.df.theme == theme].unique()

    def get_subtheme(self, subtheme):
        return self.df[self.df.subtheme == subtheme]