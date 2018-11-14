from werkzeug.wsgi import DispatcherMiddleware
from spyne.server.wsgi import WsgiApplication
from spyne import Iterable, Integer, Unicode, srpc, rpc, Application, DateTime
from spyne.model.primitive import String, Double, Integer, Time, AnyXml, AnyDict, Float
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from spyne.protocol.xml import XmlDocument
from spyne.model.complex import ComplexModel, XmlAttribute
from spyne.model.complex import Array
from flask import Flask

import xml.etree.ElementTree as et
import csv
import bcrypt

app = Flask(__name__)
password = b"selecttopic"
password_hash = bcrypt.hashpw(password, bcrypt.gensalt())

class AirService(ServiceBase):
    @srpc(_returns=Iterable(String))
    def query_air_info():
        tree = et.parse('food.xml')
        #yield tree.getroot()
        with open('airdata.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                yield str(row)

    @srpc(Integer, Time, Double, Double, _returns=Iterable(String))
    def insert_air_info(room, time, temp, humidity):
        rowData = [room, time, temp, humidity]
        with open('airdata.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(rowData)
        csvFile.close()

    @srpc()
    def delete_db():
        f = open("airdata.csv", "w")
        f.truncate()
        f.close()

    @srpc(String, _returns=Iterable(String))
    def test_query_air_info(password):
        if bcrypt.checkpw(password.encode('utf8'), password_hash) == False:
            return None
        tree = et.parse('food.xml')
        #yield tree.getroot()
        with open('airdata.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                yield str(row)
                
class Student(ComplexModel):
    __namespace__ = "student"

    username = String
    userid = Integer
    fovorite1 = String
    fovorite2 = String

class StudentService(ServiceBase):
    @srpc(_returns=Student)
    def studentInfo():
        sName = 'Phutthinan Setnoi'
        sNumber = 5801012630149
        sFovorite = ['reading novel', 'reading a book']
        student_info = [sName, sNumber, sFovorite[0], sFovorite[1]]
        return student_info

class TransportInfo(ComplexModel):
    __namespace__ = "transportInfo"

    name = String
    dest = String
    weight = Float
    status = String

class TransportService(ServiceBase):
    @srpc(String, String, Double)
    def addDestinationInfo(name, address, weight):
        destInfo = [name, address, weight, 'sending']
        with open('transportInfo.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(destInfo)
        csvFile.close()

    @srpc(String)
    def destinationSent(name):
        name = "'"+name+"'"
        status = 'sent'
        all_row = []
        with open('transportInfo.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if len(row) < 4:
                    continue
                data = []
                for each in row:
                    data.append(each)
                if data[0]==name:
                    data[3] = status
                all_row.append(data)
            csv_file.close()

        f = open("transportInfo.csv", "w")
        f.truncate()
        f.close()

        with open('transportInfo.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            for row in all_row:
                writer.writerow(row)
            csvFile.close()

    @srpc(String ,_returns=TransportInfo)
    def transportStatus(name=None):
        with open('transportInfo.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:                
                if len(row) < 4:
                    continue
                data = []
                for each in row:
                    data.append(each)
                if data[0]==name or data[0]=="'"+name+"'":
                    return row
application = Application([AirService, StudentService, TransportService],
    tns='spyne.examples.cctv',
    in_protocol=Soap11(validator='lxml'),
     out_protocol=Soap11())



app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/soap': WsgiApplication(application)
})

if __name__ == '__main__':
    app.run()