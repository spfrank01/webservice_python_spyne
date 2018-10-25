from zeep import Client
import datetime
import random
url = 'http://127.0.0.1:5000/soap/HelloWorldService?wsdl'
#url = 'https://flask-soap.herokuapp.com/soap/airService?wsdl'

while(1):
    t = datetime.datetime.now()


    client_lis = Client(url)
    client_lis.service.insert_air_info(2116, (datetime.datetime.now()), (random.randint(20,30)), (random.randint(0,20)/10))
    print('.')

    print('dT : ', datetime.datetime.now()-t)
