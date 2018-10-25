from zeep import Client, Settings
import xml.etree.ElementTree as et
import datetime
url = 'http://127.0.0.1:5000/soap/StudentService?wsdl'
#url = 'https://flask-soap.herokuapp.com/soap/airService?wsdl'

client_lis = Client(url)
name = 'ABC'
client_lis.service.destinationSent(name)
#print(data)