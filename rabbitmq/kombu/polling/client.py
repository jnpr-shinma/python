from kombu.pools import producers
from kombu import Exchange, Queue

# from queues import task_exchange
task_exchange = Exchange('csp-sse.poll-data', type='direct')

def send_as_task(connection , args=(), kwargs={}):
    payload = {  'args': args, 'kwargs': kwargs}
    routing_key="csp-sse.projectname.chassis"
    with producers[connection].acquire(block=True) as producer:
        producer.publish(payload,
                         exchange=task_exchange,
                         declare=[task_exchange],
                         routing_key=routing_key)

if __name__ == '__main__':
    from kombu import Connection

    connection = Connection('amqp://guest:guest@localhost:5672//')
    send_as_task(connection,  args=('Kombu', ), kwargs={})