from kombu.mixins import ConsumerMixin
from kombu.log import get_logger
from kombu import Exchange
from kombu import Queue
import kombu



logger = get_logger(__name__)


class Worker(ConsumerMixin):

    def __init__(self, connection):
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        job_upd_exchange = Exchange('vnc_config.object-update', 'topic', durable=False)

        default_bindings = [
            kombu.binding(job_upd_exchange, routing_key='ems-central.#'),
            kombu.binding(job_upd_exchange, routing_key='fmpm-provider.#'),
            kombu.binding(job_upd_exchange, routing_key='topology-service.#'),
            kombu.binding(job_upd_exchange, routing_key='tssm.#'),
            kombu.binding(job_upd_exchange, routing_key='vim.#'),
            kombu.binding(job_upd_exchange, routing_key='data-view-central.#')
        ]
        qname="default-hapi-consume"
        queue_arguments=None
        task_queues=Queue(qname, job_upd_exchange, bindings=default_bindings,
                            durable=True,
                            queue_arguments=queue_arguments)
        return [Consumer(queues=task_queues,
                         accept=['pickle', 'json'],
                         callbacks=[self.process_task])]

    def process_task(self, body, message):
        print "=========================="
        print body
        print message
        print "=========================="
        message.ack()

if __name__ == '__main__':
    from kombu import Connection
    from kombu.utils.debug import setup_logging
    # setup root logger
    setup_logging(loglevel='INFO', loggers=[''])
    urls='amqp://cspmq:Juniper1@10.102.93.212:5672//'
    # connection = kombu.Connection(urls, heartbeat=cfg.CONF.rabbit_heart_beat)
    connection = kombu.Connection(urls, heartbeat=100)
    with kombu.connections[connection].acquire() as conn:
    # with Connection('amqp://guest:guest@localhost:5672//') as conn:
        try:
            worker = Worker(conn)
            worker.run()
        except KeyboardInterrupt:
            print('bye bye')