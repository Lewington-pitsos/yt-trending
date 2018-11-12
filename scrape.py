import requests
from lxml import html
from scrape import parser, database

response = requests.get("https://www.youtube.com/feed/trending")

p = parser.Parser(html.fromstring(response.content))
p.parse()

db = database.DB()
for video in p.videos:
  print("saving video: {}".format(video["title"]))
  db.save_video(video)
