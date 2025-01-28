import requests
from utils import structured_extract


website_name = 'https://techmazone.com/'

jina = 'https://r.jina.ai/'
url = jina + website_name
response = requests.get(url)


text: str = response.text
json_result = structured_extract(text)
