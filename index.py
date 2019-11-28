import requests
import json

headers = {"Authorization": "Bearer ACCESS_TOKEN"}


def run_query(query, variables):
    request = requests.post('https://gqlv2.nexpie.io/',
                            json={'query': query, 'variables': variables}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))

deviceid = "DEVICEID"
value = {
    "trigger": [
        {
            "action": "LINENOTIFY",
            "event": "SHADOW.UPDATED",
            "condition": "$.temp > 0",
            "msg": "temp is {{$.temp}}",
            "option": {
                "url": "https://notify-api.line.me/api/notify"
            }
        },
        {
            "action": "JSON",
            "event": "SHADOW.UPDATED",
            "condition": "$.temp > 0",
            "msg": "{\"hello\": \"test\"}",
            "option": {
                "url": "https://en0k41mwcnnj9i.x.pipedream.net/"
            }
        },
    ],
    "enabled": True
}

query = """
mutation($deviceid: String!, $value: JSON) {
    updateTrigger(deviceid: $deviceid, value: $value) {
        id
        deviceid
        value
    }
}
"""

variables = {
    "deviceid": deviceid,
    "value": json.dumps(value)
}

result = run_query(query, variables)  # Execute the query
print(result)
