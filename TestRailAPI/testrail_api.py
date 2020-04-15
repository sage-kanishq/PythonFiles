from pprint import pprint

from testrail import *

import requests

client = APIClient('')
client.user = ''
client.password = ''


def add_result_for_case(*, run_id: int, case_id: int, status: str, msg: str):
    """Add test case and update result

    """
    if status.lower() == "pass":
        result = client.send_post(
            'add_result_for_case/%d/%d' % (run_id, case_id),
            {'status_id': 1, 'comment': msg}
        )
        return result
    elif staus.lower() == "fail":
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


def get_run(run_id: int):
    run = client.send_get("get_run/%d" % (run_id))
    return run


def get_case(case_id: int):
    case = client.send_get("get_case/%d" % (case_id))
    return case
