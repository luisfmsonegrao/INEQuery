import pandas as pd

class DataBase():

    def __init__(self):
        self.df = pd.read_json("..\data\indicators.json")

    def get_all_themes(self):
        return self.df.theme.unique()
    
    def get_theme(self, theme):
        return self.df[self.df.theme == theme]
    
    def get_all_theme_subthemes(self, theme):
        return self.df.subtheme[self.df.theme == theme].unique()
    
    def get_all_subthemes(self):
        return self.df.subtheme.unique()

    def get_subtheme(self, subtheme):
        return self.df[self.df.subtheme == subtheme]