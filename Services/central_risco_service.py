from datetime import datetime
from rabbitMQ import rabbitMQ

import time
import json

class central_risco_service():
    def __init__(self):
        self.rabbit = rabbitMQ()
        self.fila = "CADM1"
        self.json1 = json.loads('{"MsgType":"ExecutionReport","Account":"32","AvgPx":"0","ClOrdID":"bb4f9b6e-f203-3484-97b9-b19885ca2441","CumQty":"0","ExecID":"52659a8c-3d4b-4f0f-98d0-54fc43205fbd","SecurityIDSource":"8","OrderID":"2021080514113293","OrderQty":"1","OrdStatus":"0","OrdType":"1","Price":"1005","SecurityID":"FUNDO4","Side":"1","Symbol":"4","TimeInForce":"1","TransactTime":"2019-02-22 16:47:37.836","TradeDate":"20190222","AllocAccount":"32","ExecType":"0","LeavesQty":"1","SecurityType":"FUND","SecurityExchange":"XBSP","MaturityDate":"20190222","ApplicationName":"FAST","BrokerID":"BVSP","OrderStrategy":"POSITION","PortID":"FUND","PortName":"PORTA FUNDOS","OrderTag":"POSITION.","IPAddress":"10.7.13.170","CurrentCumQty":"0","CurrentAvgPx":"0","SourceAddress":"10.10.1.10","ByPassClosedMarket":"N","EnteringTrader":"32","TimeSendQueue":"2019-02-22 16:47:37.852"}')
        self.json2 = json.loads('{"MsgType":"ExecutionReport","Account":"32","AvgPx":"1005","ClOrdID":"x","CumQty":"1","ExecID":"faf44455-ae15-4e51-a799-ad5429092a56","SecurityIDSource":"8","LastPx":"1005","LastQty":"1","OrderID":"2021080514113293","OrderQty":"1","OrdStatus":"2","OrdType":"2","OrigClOrdID":"x","Price":"1005","SecurityID":"FUNDO4","Side":"1","Symbol":"4","TimeInForce":"1","TransactTime":"2019-02-22 19:40:15.285","TradeDate":"20190222","AllocAccount":"32","ExecType":"F","LeavesQty":"0","SecurityType":"FUND","SecurityExchange":"XBSP","MaturityDate":"20190222","ApplicationName":"FAST","BrokerID":"BVSP","OrderStrategy":"POSITION","PortID":"FUND","PortName":"PORTA FUNDOS","OrderTag":"POSITION.","IPAddress":"10.7.13.170","IsStmOrder":"N","CurrentCumQty":"1","CurrentAvgPx":"1005","SourceAddress":"10.10.1.10","IsRelayReceived":"N","ByPassClosedMarket":"Y","UserCanCancel":"N","ExternalAccount":"CD32","ExecutingTrader":"32","EnteringTrader":"32","TimeSendQueue":"2019-02-22 19:40:15.303"}')

    
    def aprovar_ordem(self, id):
        orderID = datetime.now().strftime("%Y%m%d%H%M%S")
        print(orderID)
        print(self.json1)

        self.json1["ClOrdID"] = id
        self.json2["ClOrdID"] = id

        self.json1["OrderID"] = orderID
        self.json2["OrderID"] = orderID

        self.rabbit.sendToQueue(self.json1, self.fila)
        time.sleep(5)
        self.rabbit.sendToQueue(self.json2, self.fila)