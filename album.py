class MediaItem:
    def __init__(self, item_id, title, copies):
        self.item_id = item_id
        self.title = title
        self.copies = copies

    def display_info(self):
        print("This method must be implemented by a subclass.")


class Album(MediaItem):
    def __init__(self, album_id, title, artist, copies):
        super().__init__(album_id, title, copies)
        self.artist = artist

    def display_info(self):
        print(f"ID: {self.item_id} | Title: {self.title} | Artist: {self.artist} | Copies: {self.copies}")


class Podcast(MediaItem):
    def __init__(self, podcast_id, title, host, copies):
        super().__init__(podcast_id, title, copies)
        self.host = host

    def display_info(self):
        print(f"ID: {self.item_id} | Title: {self.title} | Host: {self.host} | Copies: {self.copies}")