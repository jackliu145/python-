import requests
import base64
def parse_ssr(ssr_content):
    data = {
        'ssrlink': ssr_content
    }
    try:
        response = requests.post('https://xiaohutong.org/api/resolve', data=data)
        return response.text
    except expression as identifier:
        return None

headers = {
    "content-type": "application/x-www-form-urlencoded",
    "User-Agent": "PostmanRuntime/7.11.0",
}

try:
    response = requests.post('https://lncn.org/api/ssr', headers=headers, data='code=LTc4MTIwMTI2OTc0NDU%3D')
    ssrs = response.json().get('ssrs')
    r = base64.b64decode(ssrs)
    print(r)
except BaseException as e:
    print(e)


