import requests

inference_request = {
    "dataframe_split": {
        "columns": [
            "fixed acidity",
            "volatile acidity",
            "citric acid",
            "residual sugar",
            "chlorides",
            "free sulfur dioxide",
            "total sulfur dioxide",
            "density",
            "pH",
            "sulphates",
            "alcohol",
        ],
        "data": [[7.0,	0.27,	0.36,	20.7,	0.045,	45.0,	170.0,	1.001,	3.0,	0.45,	8.8]]
    }
}

endpoint = "http://localhost:5232/invocations"
response = requests.post(endpoint, json=inference_request)

response.json()