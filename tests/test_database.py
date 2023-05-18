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
    



