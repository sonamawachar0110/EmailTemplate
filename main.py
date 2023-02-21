import requests
api_url=http://localhost:8083/connectors/source-csv-spooldir-00/config
response= requests.get(api_url)
response.json()
##{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
response.status_code=200
response.headers["Content-Type"]
'application/json'
