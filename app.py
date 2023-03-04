import requests
import json

api_url = "http://localhost:8083/connectors/source-csv-spooldir-00/config"
headers = {
    "Content-Type": "application/json"
}
data={
        "connector.class": "com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnector",
        "topic": "orders_spooldir_00",
        "input.path": "/csv/unprocessed",
        "finished.path": "/csv/processed",
        "error.path": "/csv/error",
        "input.file.pattern": ".*\\.csv",
        "schema.generation.enabled":"true",
        "csv.first.row.as.header":"true"
        }
response = requests.put(api_url,data=json.dumps(data),headers=headers)
