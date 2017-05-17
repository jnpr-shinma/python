from urllib3 import PoolManager
import logging
from logging import StreamHandler
import json

logger = logging.getLogger(__name__)


def init_log():
    logger.setLevel(logging.DEBUG)
    ch = StreamHandler()
    ch.setLevel(logging.DEBUG)
    format = logging.Formatter(
        "%(asctime)s %(levelname)-8s %(threadName)s %(name)-20s %(filename)s[line:%(lineno)d]   %(message)s")
    ch.setFormatter(format)
    logger.addHandler(ch)


def insert_data():
    an = Analysis()
    url = "http://127.0.0.1:8082/ems-central/device/"
    body = {
        "device": {
            "device_family_refs": [
                {
                    "attr": None,
                    "uri": "/ems-central/device-family/60465774-e602-40ab-bb53-0d6e2fcadf98",
                    "uuid": "60465774-e602-40ab-bb53-0d6e2fcadf98",
                    "to": [
                        "default-domain",
                        "default-project",
                        "juniper-nfx"
                    ]
                }
            ],
            "name": "site-2043-0-NFX-250",
            "uuid": "d53c6be3-25c5-4df7-a01f-36cb4a8ad30c",
            "fq_name": [
                "default-domain",
                "cust2043",
                "site-2043-0-NFX-250"
            ],

            "topology_uuid": "c79e8d0a-1814-43bb-8a64-cda5a4adb976",
            "display_name": "site-2043-0-NFX-250",
            "parent_type": "project",
            "parent_uuid": "55d0ac8d-4894-4b0f-a50c-28fef22c1edd",
            "region": "regional",
            "connection_type": "CSP_INITIATED",
            "uri": "/ems-central/device/d53c6be3-25c5-4df7-a01f-36cb4a8ad30c",
            "unique_id": "PORTER10.222.63.219",
            "abstract_configs": [
                {
                    "uri": "/ems-central/abstract-config/2d715349-3569-4e71-9200-e1ef951853fd",
                    "uuid": "2d715349-3569-4e71-9200-e1ef951853fd",
                    "to": [
                        "default-domain",
                        "cust2043",
                        "site-2043-0-NFX-250",
                        "stageone_config"
                    ]
                }
            ],

            "system_info": {
                "serial_number": "PORTER10.222.63.219",
                "host_name": "default_host"
            },
            "management_state": "EXPECTED"
        }
    }
    an.create_object(url, body)


class Analysis():
    def __init__(self):
        self.manager = PoolManager(10)

    def create_object(self, url, body):
        self.manager.request("POST", url=url, headers={'Content-Type': 'application/json'}, body=json.dumps(body))


if __name__ == '__main__':
    insert_data()
