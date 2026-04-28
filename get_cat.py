from conf import proxies
import requests


def get_cat(file_path):
  url = "https://api.thecatapi.com/v1/images/search"

  response = requests.get(url, proxies=proxies)
  response.raise_for_status()

  url2 = response.json()[0]['url']

  headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 [ip:81.56.37.76]'}

  response2 = requests.get(url2, proxies=proxies, headers=headers)
  response2.raise_for_status()

  with open(file_path, "wb") as my_file:
    my_file.write(response2.content)