import requests
url='https"//jsonplaceholder.typicode.com/posts'
data={
    'title':'Hi Students',
    'body':'Wipro Geeks',
    'userId':1
}
response=requests.post(url,json=data)
print(rseponse.status_code)
print(response.json())