import csv
class Currency:

    __currencyRatesDict={}
    def __init__(self, name, code , euro_to_currency,currency_to_euro):
        
        self.name = name
        self.code = code
        self.currency_to_euro = float(currency_to_euro)
        self.euro_to_currency = float(euro_to_currency)
        
  

    def createInstance(self,code):
        
            with open('currencyrates.csv') as csvFile:
                reader = csv.reader(csvFile)
                
                for row in reader:
                   self.__currencyRatesDict[row[1]] = { 'code':row[1],'name':row[0],
                    'euro_to_currency':row[2],'currency_to_euro':row[3]}

                   #print(self.__currencyRatesDict) 
            try:
                for i in self.__currencyRatesDict.items():
                    
                    
                    
                    self.currency_object=self.__currencyRatesDict[code]
                    
                    #print(self.__currencyRatesDict)
                    self.name = str(self.currency_object['name'])
                    self.code  = str(self.currency_object['code'])
                    self.euro_to_currency = float(self.currency_object['euro_to_currency'])
                    self.currency_to_euro = float(self.currency_object['currency_to_euro'])
                   
                    

                    
                  
                    return (self.name,str(self.code),self.euro_to_currency,self.currency_to_euro)

            except KeyError:

                pass


    def FindConversion(self,code):

        try:  
            code = Currency.createInstance(self,code)
            #print(code)
            #print ("the conversion rate for", code[0], "with code", code[1], "is :",code[2])
            convert=float(code[2])
            return float(convert) 
        except:TypeError
        pass

            

#TESTS
#C=Currency
#D=Currency

#D = Currency.FindConversion(D,'EUR')
#C = Currency.FindConversion(C,'ZWD')
#print(D*10)
#print(C)

