import requests

fn = "images/pan.png"

with open(fn, "rb") as f:

  r = requests.post("http://127.0.0.1:5000/upload", files={"file": f})

print(r.status_code)

print(r.text)