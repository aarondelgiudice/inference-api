# inference-api

## Install
Install required packages:
    ```shell
    python -m pip install -r requirements.txt
    ```

## Run
1. Activate the API
    ```shell
    python src/app.py
    ```

2. Send a request
    ```shell
    curl -X POST -H "Content-Type: application/json" -d '{"text": "hello world"}' http://localhost:5000/_inference
    ```

    Response:
        ```shell
        {
            "input": {
                "text": "hello world"
        },
            "message": "Received"
        }
        ```

