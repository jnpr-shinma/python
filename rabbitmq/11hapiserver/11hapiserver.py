    # def test_test(self):
    #     import json
    #


    # {"log_record_time": "2016-08-25 09:21:35.90", "node_source": "shinma-mbp", "region_name": null, "level": "DEBUG", "Thread_id": 4599197520, "process_id": 34956, "functionname": "on_event", "service_app_name": "data-view-central", "service_modulename": "message_manager", "request_id": "NO_REQUESTID_FOUND", "name": "app_cfg_server.handlers.message_manager", "type": "csp_logs", "message": "receive event{u'oper': u'CREATE', u'uuid': u'c811c5c9-da8c-4aef-927d-fa8533f192f1', u'request-id': u'req-daf7aea6-0d5c-4ad1-a745-3d59c2c1c3f1', u'namespace': u'ems-central', u'tenantid': None, u'type': u'template', u'obj_dict': {u'display_name': u'adsf1', u'perms2': {u'owner': None, u'owner_access': 7, u'global_access': 0, u'share': []}, u'fq_name': [u'adsf1'], u'id_perms': {u'enable': True, u'description': None, u'creator': None, u'created': u'2016-08-25T09:21:20.945069', u'uuid': {u'uuid_mslong': 14416521352935394031L, u'uuid_lslong': 10555868551635374833L}, u'user_visible': True, u'last_modified': u'2016-08-25T09:21:20.945069', u'permissions': {u'owner': u'cloud-admin', u'owner_access': 7, u'other_access': 7, u'group': u'cloud-admin-group', u'group_access': 7}}, u'uuid': u'c811c5c9-da8c-4aef-927d-fa8533f192f1'}}"}
# {"log_record_time": "2016-08-25 09:21:35.91", "node_source": "shinma-mbp", "region_name": null, "level": "DEBUG", "Thread_id": 4599197520, "process_id": 34956, "functionname": "on_event", "service_app_name": "data-view-central", "service_modulename": "message_manager", "request_id": "NO_REQUESTID_FOUND", "name": "app_cfg_server.handlers.message_manager", "type": "csp_logs", "message": "active objects ['customer', 'image', 'site', 'pop', 'vim', 'nfv-service-instance', 'device-profile', 'ems', 'device', 'nfv-service-profile']"}
# {"log_record_time": "2016-08-25 09:21:35.92", "node_source": "shinma-mbp", "region_name": null, "level": "DEBUG", "Thread_id": 4599197520, "process_id": 34956, "functionname": "on_event", "service_app_name": "data-view-central", "service_modulename": "message_manager", "request_id": "NO_REQUESTID_FOUND", "name": "app_cfg_server.handlers.message_manager", "type": "csp_logs", "message": "drop event, no subscriber handler {u'oper': u'CREATE', u'uuid': u'c811c5c9-da8c-4aef-927d-fa8533f192f1', u'request-id': u'req-daf7aea6-0d5c-4ad1-a745-3d59c2c1c3f1', u'namespace': u'ems-central', u'tenantid': None, u'type': u'template', u'obj_dict': {u'display_name': u'adsf1', u'perms2': {u'owner': None, u'owner_access': 7, u'global_access': 0, u'share': []}, u'fq_name': [u'adsf1'], u'id_perms': {u'enable': True, u'description': None, u'creator': None, u'created': u'2016-08-25T09:21:20.945069', u'uuid': {u'uuid_mslong': 14416521352935394031L, u'uuid_lslong': 10555868551635374833L}, u'user_visible': True, u'last_modified': u'2016-08-25T09:21:20.945069', u'permissions': {u'owner': u'cloud-admin', u'owner_access': 7, u'other_access': 7, u'group': u'cloud-admin-group', u'group_access': 7}}, u'uuid': u'c811c5c9-da8c-4aef-927d-fa8533f192f1'}}"}
import json

# a={u'oper': u'CREATE', u'uuid': u'e51b1898-9d1a-4a7f-8dad-6f0837294a73', u'request-id': u'req-0d95c7f5-0b83-41af-970d-b3118f4d914d', u'namespace': u'ems-central', u'tenantid': None, u'type': u'template', u'obj_dict': {u'display_name': u'adsf', u'perms2': {u'owner': None, u'owner_access': 7, u'global_access': 0, u'share': []}, u'fq_name': [u'adsf'], u'id_perms': {u'enable': True, u'description': None, u'creator': None, u'created': u'2016-08-25T06:57:32.379680', u'uuid': {u'uuid_mslong': 16508815902806526591L, u'uuid_lslong': 10208938011394656883L}, u'user_visible': True, u'last_modified': u'2016-08-25T06:57:32.379680', u'permissions': {u'owner': u'cloud-admin', u'owner_access': 7, u'other_access': 7, u'group': u'cloud-admin-group', u'group_access': 7}}, u'uuid': u'e51b1898-9d1a-4a7f-8dad-6f0837294a73'}}
# print json.dumps(a)
ddd={u'oper': u'CREATE', u'uuid': u'f8b2cdde-00b7-4df5-9ce2-3faddda173e1', u'request-id': u'req-6053de53-9a57-4caa-b1d8-f8743bf1368c', u'namespace': u'ems-central', u'tenantid': u'5c77fda2860b4ef58612cd0168fecc0e', u'type': u'device', u'obj_dict': {u'fq_name': [u'default-domain', u'ucpe-tenant', u'ucpe-site-NFX-250'], u'uuid': u'f8b2cdde-00b7-4df5-9ce2-3faddda173e1', u'region': u'regional', u'parent_type': u'project', u'system_info': {u'serial_number': u'DD0516AF0008', u'host_name': u'default_host'}, u'perms2': {u'owner': u'5c77fda2860b4ef58612cd0168fecc0e', u'owner_access': 7, u'global_access': 7, u'share': []}, u'id_perms': {u'enable': True, u'uuid': {u'uuid_mslong': 17920612220639071733L, u'uuid_lslong': 11304668030633604065L}, u'created': u'2016-08-20T03:56:03.764991', u'description': None, u'creator': None, u'user_visible': True, u'last_modified': u'2016-08-20T03:56:03.764991', u'permissions': {u'owner': u'admin', u'owner_access': 7, u'other_access': 7, u'group': u'admin', u'group_access': 7}}, u'device_family_refs': [{u'to': [u'default-domain', u'juniper-nfx'], u'uuid': u'60465774-e602-40ab-bb53-0d6e2fcadf98'}], u'management_state': u'EXPECTED', u'unique_id': u'DD0516AF0008', u'display_name': u'ucpe-site-NFX-250'}}
print json.dumps(ddd)
