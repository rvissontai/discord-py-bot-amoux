import pika
import json

class rabbitMQ:
    def __init__(self):
        pass

    def sendToQueue(self, model, queue):
        credentials = pika.PlainCredentials("user", "Z2Wx28yx5GG4")
        parameters = pika.ConnectionParameters(
            host="h-dtvm-queue-api-rabbitmq.vitreo.local",
            port=5672,
            credentials=credentials)

        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()

        channel.basic_publish(
            exchange='', 
            routing_key=queue, 
            body=json.dumps(model),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        print('enviada para fila')
        connection.close()
