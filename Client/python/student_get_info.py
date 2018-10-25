from zeep import Client, Settings
import xml.etree.ElementTree as et
import datetime
url = 'http://127.0.0.1:5000/soap/StudentService?wsdl'
#url = 'https://flask-soap.herokuapp.com/soap/airService?wsdl'

settings = Settings(strict=False, xml_huge_tree=True)
client_lis = Client(url, settings=settings)

with client_lis.settings(raw_response=True):
    response = client_lis.service.studentInfo()
    print('resp : ',response)

data = client_lis.service.studentInfo()
print(data)