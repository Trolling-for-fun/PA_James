import requests
url = 'http://172.17.50.43/snow'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t*",r.status_code)
h = requests.head(url)
print("Header.")
print("**********")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("**********")
headers = {
    'User-Agent' : 'mobile'
}
url2 = 'http://172.17.50.43/snow'
rh = requests.get(url2, headers=headers)
print(rh.text)