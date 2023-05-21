from pandas import DataFrame
from inequery.DataLoader import DataLoader, get_available_years, convert_periodicity
from inequery.Database import DataBase

dl = DataLoader()

def test_dataloader_constructor():
    assert type(dl.data) == dict
    assert len(dl.data) == 0
    assert type(dl.database) == DataBase

def test_get_available_years():
    theme = dl.database.df.theme.unique()[0]
    subtheme = dl.database.get_all_theme_subthemes(theme)[2]
    indicator = dl.database.get_all_subtheme_indicators(subtheme)[20]
    code = dl.database.get_indicator_code(theme, subtheme, indicator).iloc[0]
    df = dl.database.get_indicator_by_code(code)
    first = int(df.first_period_available.iloc[0].split('A')[1])
    last = int(df.last_period_available.iloc[0].split('A')[1])
    periodicity = convert_periodicity(dl.database.get_periodicity(code))
    years = list(range(first, last+1,periodicity))
    years = [str(year) for year in years]
    assert get_available_years(dl, code) == years

def test_convert_periodicity():
    assert convert_periodicity("Anual") == 1
    assert convert_periodicity("Decenal") == 10

def test_get_yearly_indicator_data():
    theme = dl.database.df.theme.unique()[0]
    subtheme = dl.database.get_all_theme_subthemes(theme)[2]
    indicator = dl.database.get_all_subtheme_indicators(subtheme)[20]
    code = dl.database.get_indicator_code(theme, subtheme, indicator).iloc[0]
    years = get_available_years(dl, code)
    data_year1 = dl.get_yearly_indicator_data(code, years[0])
    ind_keys = ['IndicadorCod', 'IndicadorDsg', 'MetaInfUrl', 'DataExtracao', 'DataUltimoAtualizacao', 'UltimoPref', 'Dados', 'Sucesso']
    assert type(data_year1) == list
    assert len(data_year1) == 1
    assert [key in data_year1[0].keys() for key in ind_keys]

def test_get_all_indicator_data():
    theme = dl.database.df.theme.unique()[0]
    subtheme = dl.database.get_all_theme_subthemes(theme)[2]
    indicator = dl.database.get_all_subtheme_indicators(subtheme)[20]
    code = dl.database.get_indicator_code(theme, subtheme, indicator).iloc[0]
    dl.get_all_indicator_data(code)
    years = get_available_years(dl, code)
    assert type(dl.data) == dict
    assert len(dl.data) == len(years)
    assert [year in dl.data.keys() for year in years]
    

