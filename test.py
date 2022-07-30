
import requests, json

data =[('1', 'Tinky Winky', 't@gmail.com', 't123'),
(2, 'Dipsy', 'd@gmail.com', 'd123'),
(3, 'Laa-Laa', 'l@gmail.com', 'l123'),
(4, 'Po', 'p@gmail.com', 'p123'),
(5, 'rotem', 'r@gmail.com', 'r123')]

for _id, _username, _email, _password in data:

    url = "http://localhost:5000/insert_user"
    body = {
        "id": _id,
        "name": _username,
        "email": _email,
        "passwd": _password
    }

    header = {
        "Content-Type": "application/json"
    }

    res = requests.post(url=url, headers=header, data=json.dumps(body) )

    print(res)