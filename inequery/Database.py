import pandas as pd
from os.path import dirname, abspath
class DataBase():

    def __init__(self):
        path = dirname(dirname(abspath(__file__)))
        rel_path_data = "\data"
        filename = "\indicators.json"
        path = path + rel_path_data + filename
        self.df = pd.read_json(path)

    def get_all_themes(self):
        return self.df.theme.unique()
    
    def get_theme(self, theme):
        return self.df[self.df.theme == theme]
    
    def get_all_theme_subthemes(self, theme):
        return self.df.subtheme[self.df.theme == theme].unique()

    def get_subtheme(self, subtheme):
        return self.df[self.df.subtheme == subtheme]