# inference-api

## Project Structure

```
├── README.md
├── requirements.txt
├── src
│   └── app.py
│   └── inference.py
└── test
    └── test_app.py
```

- `README.md`
: you are here.
- `requirements.txt`
: Install necessary dependencies: `python -m pip install -r requirements.txt`
- `src/`
: python source code for API routing and model inference.
    - `app.py`
    : python code for API routing.
    - `inference.py`
    : python code for model inference.
- `test/`
: `pytest` code for unit testing.


## Install
Install required packages:

```shell
python -m pip install -r requirements.txt
```

## Run
Activate the API:

```shell
python src/app.py
```

Send a request:

```shell
curl -X POST -H "Content-Type: application/json" -d '{"text": "hello, world!"}' http://localhost:5000/_inference
```

Response:

```shell
{
  "message": "Vector generated",
  "vector": [
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8
  ]
}
```

## Test
Run tests:

```shell
python -m pytest
```
