import requests

class Retriever():
  def get(self, image_link: str) -> bytes:
    body = requests.get(image_link).content
    print("Response received for: {}".format(image_link))
    return body
