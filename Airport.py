import AirportAtlas
import csv
from typing import Mapping,TypeVar,Iterable


class Airport:
    __airportDict={}
    airport_objs_dict={}
    

    def __init__(self, code, id, name, city, country, lat, long,airport_object):
        self.airport_object=airport_object
        self.code = code
        self.id = id
        self.name = name
        self.city = city
        self.country = country
        self.lat = float(lat)
        self.long = float(long)
        

    def createInstance(self,Code):
        
        with open('airportcsv.csv') as csvFile:
            reader = csv.reader(csvFile, delimiter=',')
            next(reader,None)
            for row in reader:
                
                self.__airportDict[row[4]] = {'Code':row[4], 'AirportID':row[0],
                    'AirportName':row[1],'Cityname':row[2], 'Country':row[3], 'lat':row[6],'long':row[7]}
        try:
            for i in self.__airportDict.items():
                    
                    self.airport_object=self.__airportDict[Code]
                    

                    self.code = str(self.airport_object['Code'])
                    self.lat  = float(self.airport_object['lat'])
                    self.long = float(self.airport_object['long'])
                    self.id = int(self.airport_object['AirportID'])
                    self.country = str(self.airport_object['Country'])
                    self.name = str(self.airport_object['AirportName'])
                    self.city = str(self.airport_object['Cityname'])
                    

                    
                  
                    return str(self.code),float(self.lat),self.long,self.id,self.country,self.name,self.city


        except KeyError:
            pass            

def getname(self):
    return self.name
test=Airport 
     
print(test.createInstance(test,''))
