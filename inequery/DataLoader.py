
from urllib import request
import xmltodict
import time
import json
from . import Database


class DataLoader():

    database = Database.DataBase()

    def __init__(self):
        self.data = dict()

    def get_all_indicator_data(self, code):
        years = get_available_years(self, code)
        self.data = dict()
        for year in years:
            self.data[year] = self.get_yearly_indicator_data(code, year)  

    def get_yearly_indicator_data(self, code, year):
        if not(year in get_available_years(self, code)):
            print("Series does not have data available for year " + year)
            return
        data_url = self.database.get_indicator_data_url(code)
        prefix = self.database.get_indicator_time_prefix(code)
        url_parts = data_url.split('&lang')
        data_url = url_parts[0] + '&Dim1=' + prefix + year + '&lang' + url_parts[1]
        data_req = request.urlopen(data_url)
        time.sleep(0.1)
        data = data_req.read()
        return json.loads(data)
        




def get_available_years(dl, code):
    first = int(dl.database.get_first_available(code).split('A')[1])
    last = int(dl.database.get_last_available(code).split('A')[1])
    periodicity = dl.database.get_periodicity(code)
    step = convert_periodicity(periodicity)
    available_years = list(range(first, last+1, step))
    return [str(year) for year in available_years]

def convert_periodicity(periodicity):
    if periodicity == "Anual":
        return 1
    elif periodicity == "Decenal":
        return 10




        

        


    