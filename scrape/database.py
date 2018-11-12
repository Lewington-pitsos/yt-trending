import psycopg2

conn_str = "dbname='yt_trending' user='postgres'" # Might want to change this

# def truncate(value: str, length: int) -> str:
#     if len(value) > length:
#         return value[:length] + "..."
    
#     return value

class DB:
    def __init__(self):
        self.connection = psycopg2.connect(conn_str)
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()
    
    def rollback(self):
        self.connection.rollback()
    
    def save_video(self, data: dict):
      self.cursor.execute("""
      INSERT INTO trending (title, summary, thumbnail, link)
      VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING;
      """, (
        data["title"], 
        data["summary"],
        data["thumbnail"],
        data["link"]
      ))
      self.commit()