
from urllib import request
import xmltodict
import time
import json


class DataLoader():

    host_url = 'https://www.ine.pt'
    
    def __init__(self, language, var_code):
        self.language = language
        self.var_code = var_code

    def get_metadata(self):
        url = DataLoader.host_url + '/ine/xml_indic.jsp?opc=1&varcd=' + self.var_code + '&lang=' + self.language
        metadata = request.urlopen(url)
        time.sleep(0.2)
        metadata = metadata.read()
        self.metadata = xmltodict.parse(metadata)
    
    def get_all_data(self):
        first_available = self.metadata['catalog']['indicator']['dates']['first_period_available']
        last_available = self.metadata['catalog']['indicator']['dates']['last_period_available']
        first_year = int(first_available.split('S7A')[1])
        last_year = int(last_available.split('S7A')[1])
        years = list(range(first_year, last_year))
        self.data = dict()
        for year in years:
            url = DataLoader.host_url + '/ine/json_indicador/pindica.jsp?op=2&varcd=' + self.var_code + '&Dim1=' + 'S7A' + str(year) + '&lang=' + self.language
            req = request.urlopen(url)
            time.sleep(0.2)
            data = req.read()
            data = json.loads(data)
            self.data[str(year)] = data
            
    


        

        


    