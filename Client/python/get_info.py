from zeep import Client
import datetime
import time
url = 'http://127.0.0.1:5000/soap/HelloWorldService?wsdl'
#url = 'https://flask-soap.herokuapp.com/soap/airService?wsdl'
client_lis = Client(url)
while(1):
    t = datetime.datetime.now()
    
    data = client_lis.service.test_query_air_info('selecttopic')
    print(data)
    print('dT : ', datetime.datetime.now()-t)
    time.sleep(1)
