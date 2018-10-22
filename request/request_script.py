import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--params_file", action='store', help='path to file with request parameters', required=True)
parser.add_argument("--log_file", action='store', help='path to logfile')
parser.add_argument("--write_log", action="store_true", help="add to write log, --log_file must be defined", )
arguments = parser.parse_args()


paramsFile = arguments.params_file
logFile = arguments.log_file
logNeed = arguments.write_log

request_params = dict


class Request:
    check_result = dict
    response = dict

    def request(self):
        if request_params['RequestMethod'] == "GET":
            request = requests.get(request_params['RequestUrl'], headers=request_params['Headers'])
        elif request_params['RequestMethod']== "POST":
            request = requests.post(request_params['RequestUrl'], data=request_params['PostData'])
        else:
            print("Unkown request method")
            exit(1)
        self.response = {
            "data": request.text,
            "status": request.status_code
        }

    def compare(self):
        # Check status code
        if request_params['StatusCode'] is not False:
            if self.response['status'] == request_params['StatusCode']:
                status_code = "OK"
            else:
                status_code = ['Not OK, actually {0}'.format(self.response['status'])]
        else:
            status_code = "Empty"
        # Check data
        if len(request_params['ExpectData']) > 0:
            if self.response['data'] == request_params['ExpectData']:
                expect_data = "OK"
            else:
                expect_data = ['Not OK, actually {0}'.format(self.response['data'])]
        else:
            expect_data = "Empty"
        self.check_result = {
            'data': expect_data,
            'code': status_code
        }

    def handle_results(self, log):
        if self.check_result is False:
            print('Check results empty')
            exit(1)
        # Check for success
        if ("Not" in self.check_result['data']) or ("Not" in self.check_result['code']):
            need_exit = True
        else:
            need_exit = False
        # Check for log needed
        if log is True:
            with open(logFile, 'a') as file:
                file.write("Status code: {0}, response data: {1}\n".format(self.check_result['code'], self.check_result['data']))
        # Check for need exit code
        if need_exit is True:
            exit(1)
        else:
            exit(0)


def get_params_from_file(params_file):
    with open(params_file, 'r') as f:
        json_params = f.read()
    params_result = json.loads(json_params)
    return params_result

app_requests = get_params_from_file(paramsFile)

for app in app_requests:
    request_params = app
    req = Request()
    req.request()
    req.compare()
    req.handle_results(logNeed)



