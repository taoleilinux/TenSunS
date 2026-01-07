from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_credentials.client import Client as CredClient
from alibabacloud_credentials.models import Config as CredConfig
from alibabacloud_domain20180129.client import Client as Domain20180129Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_domain20180129 import models as domain_20180129_models

import os,sys,json

class Domain:
    def __init__(self, ak, sk):
        self.config = {'type': 'access_key'}
        self.config['access_key_id'] = ak
        self.config['access_key_secret'] = sk
        self.config = CredConfig(**self.config)
        self.cred = CredClient(self.config)

    def create_client(self):
        config = open_api_models.Config(
            credential=self.cred
        )
        config.endpoint = f'domain.aliyuncs.com'
        return Domain20180129Client(config)

    def get_domain_info(self, domain_id):
        client = self.create_client()
        query_domain_by_instance_id_request = domain_20180129_models.QueryDomainByInstanceIdRequest(
            instance_id=domain_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            resp = client.query_domain_by_instance_id_with_options(query_domain_by_instance_id_request, runtime)
            return resp
        except Exception as error:
            logger.error(f'{error.message}')
            logger.error(f'诊断地址：{error.data.get("Recommend")}')
