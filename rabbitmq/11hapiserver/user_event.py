
import pika
from pika import PlainCredentials

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='10.155.78.221',credentials=PlainCredentials(username="cspmq", password="Juniper1")))
channel = connection.channel()

channel.exchange_declare(exchange='vnc_config.object-update',
                         type='topic')
routing_key = 'iamsvc.user'
message = '{"oper": "UPDATE", "uuid": "310033e0-106f-47da-af0d-d242f32db5b2", "request-id": "req-524fba73-05c0-479c-9b45-28b8fccc084b", "namespace": "iamsvc", "tenantid": "8e3b50ed97d748c6a3e3439d409035b2", "perms2": {"owner": "8e3b50ed97d748c6a3e3439d409035b2", "owner_access": 7, "global_access": 0, "share": []}, "request_id": "USXL9C", "type": "user", "obj_dict": {"fq_name": ["default-domain", "notify_test6"], "uuid": "310033e0-106f-47da-af0d-d242f32db5b2", "parent_type": "domain", "perms2": {"owner": "8e3b50ed97d748c6a3e3439d409035b2", "owner_access": 7, "global_access": 0, "share": []}, "id_perms": {"enable": true, "uuid": {"uuid_mslong": 3530879145299888090, "uuid_lslong": 12613969316324160946}, "created": "2017-05-02T05:56:20.437451", "creator": "admin", "user_visible": true, "last_modified": "2017-05-02T05:56:20.437451", "permissions": {"owner": "admin", "owner_access": 7, "other_access": 7, "group": "admin", "group_access": 7}, "description": null}, "display_name": "notify_test6"}}'

channel.basic_publish(exchange='vnc_config.object-update',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()