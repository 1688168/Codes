# <p style="text-align: center"> <span style="color:Orange"> Https </span> </p>

> Resources
[fake json data](https://jsonplaceholder.typicode.com)

> how to know what are the request types that is supported by an URL?
```sh
resp, data = http.request(bin_url, method='OPTIONS')
```

> The http swagger
* [http swagger](http://www.httpbin.org)

> how to print the response from http.request 
* pprint(data.decode('UTF-8'))


> requests
```sh
!pip install requests --upgrade
data = resp.text # return in json format
data = json.loads(resp.text) # converts json to python dict

```

> python open webpage
```python
webbrowser.open(someURL)
```

> python put example
```pythob
resp = requests.post('https://jsonplaceholder.typicode.com/posts', data=post_data)

```