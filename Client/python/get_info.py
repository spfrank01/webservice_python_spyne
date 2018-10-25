from zeep import Client
import datetime
url = 'http://127.0.0.1:5000/soap/HelloWorldService?wsdl'
#url = 'https://flask-soap.herokuapp.com/soap/airService?wsdl'

while(1):
    t = datetime.datetime.now()
    client_lis = Client(url)
    data = client_lis.service.test()
    print(data)
    print('dT : ', datetime.datetime.now()-t)
