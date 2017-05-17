from kombu import Connection
from kombu import Exchange
from kombu import Queue
#
job_upd_exchange = Exchange('vnc_config.object-update', 'topic', durable=False)
import kombu

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
queue=Queue(qname, job_upd_exchange, bindings=default_bindings,
                    durable=True,
                    queue_arguments=queue_arguments)
urls='amqp://cspmq:Juniper1@10.102.93.212:5672//'
# connection = kombu.Connection(urls, heartbeat=cfg.CONF.rabbit_heart_beat)
connection = kombu.Connection(urls, heartbeat=100)
with kombu.connections[connection].acquire() as conn:
# with Connection() as conn:
    simple_queue = conn.SimpleQueue('cc6b0bc3-2f2c-3b49-907e-d62e93803660')
    message = simple_queue.get(block=True, timeout=1)
    print("Received: %s" % message.payload)
    message.ack()
    simple_queue.close()

    # with Connection('amqp://cspmq:Juniper1@10.102.93.212:5672//') as conn:
    #     simple_queue = conn.SimpleQueue('cc6b0bc3-2f2c-3b49-907e-d62e93803660')
    #     message = simple_queue.get(block=True, timeout=1)
    #     print("Received: %s" % message.payload)
    #     message.ack()
    #     simple_queue.close()
