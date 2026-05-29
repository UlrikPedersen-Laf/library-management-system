class Album:
    def __init__(self, album_id, title, artist, copies):
        self.album_id = album_id
        self.title = title 
        self.artist = artist
        self.copies = copies
    def display_info(self):
        print(f"ID: {self.album_id} | Title: {self.title} | Artist: {self.artist} | Copies: {self.copies}")
        