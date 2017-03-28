
# job_upd_exchange = kombu.Exchange('vnc_config.object-update', 'topic',
#                                       durable=False)


#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='vnc_config.object-update',
                         type='topic')

routing_key = 'sse.polling.device'
message = '{"oper": "UPDATE", "uuid": "f8b2cdde-00b7-4df5-9ce2-3faddda173e1", "request-id": "req-6053de53-9a57-4caa-b1d8-f8743bf1368c", "namespace": "polling", "tenantid": "5c77fda2860b4ef58612cd0168fecc0e", "type": "polling", "obj_dict": {"parent_type": "project", "perms2": {"owner": "5c77fda2860b4ef58612cd0168fecc0e", "owner_access": 7, "global_access": 7, "share": []}, "device_family_refs": [{"to": ["default-domain", "juniper-nfx"], "uuid": "60465774-e602-40ab-bb53-0d6e2fcadf98"}], "management_state": "EXPECTED", "display_name": "ucpe-site-NFX-250", "fq_name": ["default-domain", "ucpe-tenant", "ucpe-site-NFX-250"], "uuid": "f8b2cdde-00b7-4df5-9ce2-3faddda173e1", "region": "regional", "system_info": {"serial_number": "DD0516AF0008", "host_name": "default_host"}, "id_perms": {"enable": true, "uuid": {"uuid_mslong": 17920612220639071733, "uuid_lslong": 11304668030633604065}, "last_modified": "2016-08-20T03:56:03.764991", "created": "2016-08-20T03:56:03.764991", "permissions": {"owner": "admin", "owner_access": 7, "other_access": 7, "group": "admin", "group_access": 7}, "creator": null, "user_visible": true, "description": null}, "unique_id": "DD0516AF0008"}}'

channel.basic_publish(exchange='vnc_config.object-update',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()