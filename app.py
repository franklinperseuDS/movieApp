import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'UserId': "1",   
                            'MovieId': "68646",   
                            'Rating': "3",   
                            'Timestamp': "1381620027",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/88cee1267b3f4781be5764f390ed1fa2/services/13bef76ee21148a6ba961ad4bdd6f0fa/execute?api-version=2.0&format=swagger'
api_key = 'v+QeyVdnxNfouQJzkktiNd28qIAksKkhvll+qAppwOtFlrbNzGK7XJM8RzGO+vGRrlxQdAjDJmYWut/wcTakCg=='
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))