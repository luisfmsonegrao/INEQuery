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
    
    def get_all_subtheme_indicators(self, subtheme):
        return self.df.title[self.df.subtheme == subtheme].unique()
    
    def get_indicator(self, theme, subtheme, indicator):
        return self.df[(self.df.theme == theme) & (self.df.subtheme == subtheme) & (self.df.title == indicator)]
    
    def get_indicator_code(self, theme, subtheme, indicator):
        return self.df.code[(self.df.theme == theme) & (self.df.subtheme == subtheme) & (self.df.title == indicator)]#Sometimes there is more than one code for same theme-subtheme-indicator. What do do?
    
    def get_indicator_by_code(self, code):
        return self.df[self.df.code == code].iloc[[0]]
    
    def get_indicator_data_url(self, code):
        ind = self.get_indicator_by_code(code)
        return ind.json_dataset.iloc[0]
    
    def get_indicator_metadata_url(self, code):
        ind = self.get_indicator_by_code(code)
        return ind.json_metainfo.iloc[0]
    
    def get_first_available(self, code):
        ind = self.get_indicator_by_code(code)
        return ind.first_period_available.iloc[0]
    
    def get_last_available(self, code):
        ind = self.get_indicator_by_code(code)
        return ind.last_period_available.iloc[0]
    
    def get_themes(self, *args):
        return self.df[self.df.theme.isin(args)]
    
    def get_indicators(self, theme, subtheme, *args):
        return self.df[(self.df.theme == theme) & (self.df.subtheme == subtheme) & (self.df.title.isin(args))]

    def get_periodicity(self, code):
        df = self.get_indicator_by_code(code)
        return df.periodicity.iloc[0].strip()
    
    def get_indicator_time_prefix(self, code):
        df = self.get_indicator_by_code(code)
        first = df.first_period_available.iloc[0]
        prefix = first.split('A')[0] + 'A'
        return prefix

