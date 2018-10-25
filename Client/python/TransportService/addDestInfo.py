from zeep import Client, Settings
import xml.etree.ElementTree as et
import datetime
url = 'http://127.0.0.1:5000/soap/StudentService?wsdl'
#url = 'https://flask-soap.herokuapp.com/soap/airService?wsdl'

client_lis = Client(url)
name = 'ABC'
address = '1521 asda Bangkok 10000'
weight = 1
client_lis.service.addDestinationInfo(name, address, weight)
#print(data)