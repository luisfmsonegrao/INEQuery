from pandas import DataFrame
from inequery.Database import DataBase
db = DataBase()

def test_constructor():
    assert len(db.__dict__.keys()) == 1
    assert list(db.__dict__)[0] == 'df'
    assert type(db.df) == DataFrame

def test_get_all_themes():
    themes = db.df.theme.unique()
    assert all(db.get_all_themes() == themes)

def test_get_theme():
    theme = db.df.theme.unique()[0]
    assert all(db.get_theme(theme) == db.df[db.df.theme == theme])

def test_get_all_theme_subthemes():
    theme = db.df.theme.unique()[1]
    subthemes = db.df.subtheme[db.df.theme == theme].unique()
    assert all(db.get_all_theme_subthemes(theme) == subthemes)

def test_get_subtheme():
    subtheme = db.df.subtheme.unique()[0]
    assert all(db.get_subtheme(subtheme) == db.df[db.df.subtheme == subtheme])

def test_get_all_subtheme_indicators():
    subtheme = db.df.subtheme.unique()[0]
    indicators = db.df.title[db.df.subtheme == subtheme].unique()
    assert all(db.get_all_subtheme_indicators(subtheme) == indicators)

def test_get_indicator():
    theme = db.df.theme.unique()[0]
    subtheme = db.get_all_theme_subthemes(theme)[2]
    indicator = db.get_all_subtheme_indicators(subtheme)[20]
    indicator_df = db.df[(db.df.theme == theme) & (db.df.subtheme == subtheme) & (db.df.title == indicator)]
    assert all(db.get_indicator(theme, subtheme, indicator) == indicator_df)
    
def test_get_indicator_code():
    theme = db.df.theme.unique()[0]
    subtheme = db.get_all_theme_subthemes(theme)[2]
    indicator = db.get_all_subtheme_indicators(subtheme)[20]
    indicator_df = db.get_indicator(theme, subtheme, indicator)
    code = indicator_df.code
    assert all(db.get_indicator_code(theme, subtheme, indicator) == code)

def test_get_indicator_data_url():
    theme = db.df.theme.unique()[0]
    subtheme = db.get_all_theme_subthemes(theme)[2]
    indicator = db.get_all_subtheme_indicators(subtheme)[20]
    indicator_df = db.get_indicator(theme, subtheme, indicator)
    code = indicator_df.code.iloc[0]
    url = indicator_df.json_dataset.iloc[0]
    print(url)
    print(db.get_indicator_data_url(code))
    assert db.get_indicator_data_url(code) == url

def test_get_first_available():
    theme = db.df.theme.unique()[0]
    subtheme = db.get_all_theme_subthemes(theme)[2]
    indicator = db.get_all_subtheme_indicators(subtheme)[20]
    indicator_df = db.get_indicator(theme, subtheme, indicator)
    code = indicator_df.code.iloc[0]
    first_available = indicator_df.first_period_available.iloc[0]
    assert db.get_first_available(code) == first_available

def test_get_last_available():
    theme = db.df.theme.unique()[0]
    subtheme = db.get_all_theme_subthemes(theme)[2]
    indicator = db.get_all_subtheme_indicators(subtheme)[20]
    indicator_df = db.get_indicator(theme, subtheme, indicator)
    code = indicator_df.code.iloc[0]
    last_available = indicator_df.last_period_available.iloc[0]
    assert db.get_last_available(code) == last_available

def test_get_themes():
    theme1 = db.df.theme.unique()[0]
    theme2 = db.df.theme.unique()[0]
    theme3 = db.df.theme.unique()[0]
    themes_df = db.df[(db.df.theme == theme1) | (db.df.theme == theme2) | (db.df.theme == theme3)]
    assert all(db.get_themes(theme1, theme2, theme3) == themes_df)

def test_get_indicators():
    theme = db.df.theme.unique()[0]
    subtheme = db.get_all_theme_subthemes(theme)[2]
    indicator1 = db.get_all_subtheme_indicators(subtheme)[10]
    indicator2 = db.get_all_subtheme_indicators(subtheme)[20]
    indicator3 = db.get_all_subtheme_indicators(subtheme)[30]
    indicators_df = db.df[(db.df.theme == theme) & (db.df.subtheme == subtheme) & ((db.df.title == indicator1) | (db.df.title == indicator2) | (db.df.title == indicator3))]
    assert all(db.get_indicators(theme, subtheme, indicator1, indicator2, indicator3) == indicators_df)


def test_get_periodicity():
    theme = db.df.theme.unique()[0]
    subtheme = db.get_all_theme_subthemes(theme)[2]
    indicator = db.get_all_subtheme_indicators(subtheme)[20]
    code = db.get_indicator_code(theme, subtheme, indicator).iloc[0]
    periodicity = db.df.periodicity[(db.df.theme == theme) & (db.df.subtheme == subtheme) & (db.df.title == indicator) & (db.df.code == code)].iloc[0].strip()
    assert db.get_periodicity(code) == periodicity

def test_get_indicator_time_prefix():
    theme = db.df.theme.unique()[0]
    subtheme = db.get_all_theme_subthemes(theme)[2]
    indicator = db.get_all_subtheme_indicators(subtheme)[20]
    code = db.get_indicator_code(theme, subtheme, indicator).iloc[0]
    prefix = db.get_first_available(code).split('A')[0] + 'A'
    assert db.get_indicator_time_prefix(code) == prefix