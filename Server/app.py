from werkzeug.wsgi import DispatcherMiddleware
from spyne.server.wsgi import WsgiApplication
from spyne import Iterable, Integer, Unicode, srpc, rpc, Application, DateTime
from spyne.model.primitive import String, Double, Integer, Time, AnyXml, AnyDict
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from spyne.protocol.xml import XmlDocument
from spyne.model.complex import ComplexModel, XmlAttribute
from spyne.model.complex import Array
from flask import Flask

import xml.etree.ElementTree as et
import csv

app = Flask(__name__)

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

application = Application([AirService],
    tns='spyne.examples.cctv',
    in_protocol=Soap11(validator='lxml'),
     out_protocol=Soap11())

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/soap': WsgiApplication(application)
})

if __name__ == '__main__':
    app.run()