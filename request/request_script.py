import requests
import json

paramsFile = "e:\\temp\\params.json"


class Request():
    requestUrl = str
    statusCode = int
    expectData = str
    headers = dict
    requestType = str

    def set_params(self, **kwargs):
        self.requestUrl = kwargs['requestUrl']
        self.statusCode = kwargs['statusCode']
        self.expectData = kwargs['expectData']
        self.headers = kwargs['headers']
        self.requestType = kwargs['requestType']

    def exec_request(self)
        if self.requestType == 'GET':
            request = requests.get(self.requestUrl, headers=self.headers)
            data, status = request.request, request.status_code
sstatus_codestatus_codestatus_code



def get_params_from_file(self, paramsFile):
    with open(paramsFile, 'r') as f:
        jsonParams = f.read()
    params = json.loads(jsonParams)