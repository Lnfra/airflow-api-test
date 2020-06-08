import requests
import json

AIRFLOW_PORT = 8080

class AirflowAPI:
    def __init__(self):
        self.ip = self.get_ip()

    def get_ip(self):
        return "localhost"

    def get_airflow_url(self):
        return "http://%s:%s/api/experimental" % (self.ip, AIRFLOW_PORT)

    def unpause_dag(self, dag_id):
        return requests.get(
            "%s/dags/%s/paused/false" % (self.get_airflow_url(), dag_id))

    def pause_dag(self, dag_id):
        return requests.get(
            "%s/dags/%s/paused/true" % (self.get_airflow_url(), dag_id))

    def trigger_dag(self, dag_id, execution_date):
        url = "%s/dags/%s/dag_runs" % (self.get_airflow_url(), dag_id)
        body = {"execution_date": execution_date}

        triggered_response = requests.post(url=url, json=body)
        print("url", url)
        print("body", body)
        print("response",  triggered_response)
        if triggered_response.status_code != 200:
            raise Exception("Please, wait for airflow web server to start.")

    def dag_state(self, dag_id, execution_date):
        return requests.get(
            "%s/dags/%s/dag_runs/%s" % (
                self.get_airflow_url(), dag_id, execution_date))

    def clear_dag(self, dag_id, execution_date):
        return requests.get(
            "%s/admin/rest_api/api?api=clear&dag_id=%s&execution_date=%s" % (
                self.get_airflow_url(), dag_id, execution_date))

    def is_dag_running(self, dag_id, execution_date):
        response = self.dag_state(dag_id, execution_date)
        json_response = json.loads(response.text)
        print("In is_dag_running", json_response)
        if "state" in json_response and json_response["state"] == "running":
            return True
        elif "state" in json_response and json_response["state"] == "success":
            return False
        elif "error" in json_response:
            return False

    def get_dag_status(self, dag_id, execution_date):
        response = self.dag_state(dag_id, execution_date)
        json_response = json.loads(response.text)
        print("In get_dag_status", json_response)
        if "state" in json_response:
            return json_response["state"]
        if "error" in json_response:
            return json_response["error"]
        else:
            return "Not Defined"
