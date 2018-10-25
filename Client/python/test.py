from zeep import Client
import datetime
#url = 'http://127.0.0.1:5000/soap/HelloWorldService?wsdl'
#url = 'https://flask-soap.herokuapp.com/soap/airService?wsdl'


from datetime import date, datetime
#from suds.client import Client

client = Client("http://url")
agenda = client.factory.create("{agenda}Agenda")
user = client.factory.create("{user}User")
user.Name = "Gabriel"