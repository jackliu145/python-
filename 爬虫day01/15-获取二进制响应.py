import requests

r = requests.get("https://github.com/favicon.ico")
exit() if not r.status_code == requests.codes['\\o/'] else print('Successfully!')
with open('favorite.ico', 'wb') as f:
    f.write(r.content)