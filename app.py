import urllib.request
import json
import streamlit as st

st.title("Web Data Reccomendation Movies") 


UserId = st.text_input("User Id", key="UserId", value="1")
MovieId = st.text_input("Movie Id", key="MovieId", value="68646")
Rating = st.text_input("Rating ", key="Rating", value="0")
Timestamp = st.text_input("Time stamp", key="Timestamp", value="1381620027")

# inserindo um botão na tela
btn_predict = st.button("Realizar Previsão")


if btn_predict:
    data = {
            "Inputs": {
                    "input1":
                    [
                        {
                                'UserId': UserId,   
                                'MovieId': MovieId,   
                                'Rating': Rating,   
                                'Timestamp': Timestamp,   
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
        parsed_json = (json.loads(result))
        y = json.loads(json.dumps(parsed_json, indent=4, sort_keys=True))
        x = y['Results']
        z = x['output1']
        m = z[0]
    # except urllib.error.HTTPError as error:
    #     print("The request failed with status code: " + str(error.code))

    #     # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    #     print(error.info())
    #     print(json.loads(error.read().decode("utf8", 'ignore')))