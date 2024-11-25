from flask import Flask
from prometheus_client import start_http_server, Counter, Gauge
import random
import time

app = Flask(__name__)

# Метрики Prometheus
REQUEST_COUNT = Counter('request_count', 'Total number of requests')
IN_PROGRESS = Gauge('in_progress_requests', 'Number of in-progress requests')

@app.route('/')
@IN_PROGRESS.track_inprogress()
def hello_world():
    REQUEST_COUNT.inc()
    return 'Hello, World!'

if __name__ == '__main__':
    # Запуск сервера метрик на порту 8000
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)

