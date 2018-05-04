import csv
from Currency import Currency

#getcurrency = Currency



class Countrycurrency:

    __CountryDict={}

    def __init__(self, currency_name, currency_alphabetic_code,currency_country_name,euro_to_currency):
        self.currency_name = currency_name
        self.currency_alphabetic_code = currency_alphabetic_code
        self.currency_country_name = currency_country_name
        self.euro_to_currency=euro_to_currency
  

    def createInstance(self,code):
        try:
            with open('countrycurrency.csv') as csvFile:
                reader = csv.reader(csvFile, delimiter=',')
          
                for row in reader:
                   
                    self.__CountryDict[row[14]] = {'currency_alphabetic_code':row[14],'currency_name':row[-3],
                    'currency_country_name':row[-5]}
                   

                   
                    
                    self.country_currency_object=self.__CountryDict
                    
                    #print(self.__CountryDict)
                    currencyrate_object =  Currency
                    self.euro_to_currency=currencyrate_object.FindConversion(currencyrate_object,self.currency_alphabetic_code)
                                        
                    self.currency_name = str(self.country_currency_object['currency_name'])
                    self.currency_alphabetic_code  = str(self.country_currency_object['currency_alphabetic_code'])
                    self.currency_country_name=str(self.country_currency_object['currency_country_name'])
                    #print(self.country_currency_object)
                    return (self.currency_name,self.currency_alphabetic_code,self.currency_country_name)
                    
        except KeyError:
            pass
                    
                    
                   





    def FindCurrencyCode(self,currency_alphabetic_code):

        try:  
            currency_alphabetic_code = Countrycurrency.createInstance(self,currency_alphabetic_code)
            print(currency_alphabetic_code[2])
            
            currency_country_code=(currency_alphabetic_code[1])
            #print(currency_country_name)
            return currency_country_code


        except:TypeError
        pass

       
    
 

          
#C=Currency
#D=Currency
#C = Currency.createInstance(C,'ZAR')
#D = Currency.FindConversion(D,'ZMW')
#print(D)


#D=Countrycurrency.createInstance(D,'EURO')
#X=Countrycurrency.FindCountry(X,'EURO')
#print(D)

#print(X)





