import sys
from tests.airflow_api import AirflowAPI
import unittest
import time
from datetime import datetime, timedelta

class TestTriggerDag(unittest.TestCase):
    """Integration test for airflow DAG"""

    def setUp(self):
        self.airflow_api = AirflowAPI()

    def test_trigger_dag(self):
        """dag should run successfully"""
        execution_date = datetime.utcnow().replace(microsecond=0).isoformat()

        dag_id = "tutorial"
        self.airflow_api.trigger_dag(dag_id, execution_date)
        is_running = True
        while is_running:
            is_running = self.airflow_api.is_dag_running(dag_id, execution_date)
            # sleep x number of seconds before polling again
            time.sleep(15)

        self.assertEqual(is_running, False)
        self.assertEqual(self.airflow_api.get_dag_status(dag_id, execution_date), "success")


if __name__ == '__main__':
    unittest.main()
