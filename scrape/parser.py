from scrape import retriever

class Parser():
  def __init__(self, body):
    self.body = body
    self.videos = []
    self.retriever = retriever.Retriever()
  
  def parse(self):
    for video in self.get_videos():
      try:
        self.videos.append({
          "thumbnail": self.get_thumbnail(video),
          "title": self.get_title(video),
          "summary": self.get_summary(video),
          "link": self.get_link(video),
        })
      except Exception as e:
        print(e)

  def get_videos(self):
    videos = self.body.xpath("//div[contains(@class, 'yt-lockup-dismissable')]")
    print("Number of videos: {}".format(len(videos)))
    return videos
  
  def get_title(self, element) -> str:
    return element.xpath(".//h3[contains(@class, 'yt-lockup-title')]/a")[0].text_content()
  
  def get_summary(self, element) -> str:
    return element.xpath(".//div[contains(@class, 'yt-lockup-description')]")[0].text_content()
  
  def get_link(self, element) -> str:
    return element.xpath(".//h3[contains(@class, 'yt-lockup-title')]/a/@href")[0]
  
  def get_thumbnail(self, element) -> bytes:
    img_link = element.xpath(".//img/@src")[0]
    if ".gif" in img_link:
      img_link = element.xpath(".//img/@data-thumb")[0]
    
    return self.retriever.get(img_link)
    

