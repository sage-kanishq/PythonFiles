from pprint import pprint
import json
from testrail import APIClient,APIError

import requests

client = APIClient('')
client.user = ''
client.password = ''

class TestRailClient:
    def add_result(self,test_id,status:str):
        _ = client.send_post(f'add_result/{test_id}',{"status_id":5})
    def add_result_for_case(self,run_id: int, case_id: int, status: str, msg: str):
        """Add test case and update result

        """
        if status.lower() == "pass":
            result = client.send_post(
                'add_result_for_case/%d/%d' % (run_id, case_id),
                {'status_id': 1, 'comment': msg}
            )
            return result
        elif status.lower() == "fail":
            result = client.send_post(
                'add_result_for_case/%d/%d' % (run_id, case_id),
                {'status_id': 5, 'comment': msg}
            )
            return result
        elif status.lower() == "block":
            result = client.send_post(
                'add_result_for_case/%d/%d' % (run_id, case_id),
                {'status_id': 3, 'comment': msg}
            )
            return result
        elif status.lower() == "retest":
            result = client.send_post(
                'add_result_for_case/%d/%d' % (run_id, case_id),
                {'status_id': 4, 'comment': msg}
            )
            return result

        else:
            raise Exception("Not a valid status")


    def get_run(self,run_id: int):
        run = client.send_get("get_run/%d" % (run_id))
        return run

    def get_case(self,case_id: int):
        case = client.send_get("get_case/%d" % (case_id))
        return case


    def get_results(self,test_id):
        results = client.send_get("get_results/%d"%(test_id))
        
        return results

    def get_results_for_case(self,run_id,case_id):
        result = client.send_get(f"get_results_for_case/{run_id}/{case_id}")
        return result


print("")
a = TestRailClient()


