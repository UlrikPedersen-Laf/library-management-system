class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_albums = []

    def display_info(self):
        print(f"ID: {self.member_id} | Name: {self.name} | Borrowed: {self.borrowed_albums}")
        
    def borrow_album(self, album):
        self.borrowed_albums.append(album)

    def return_album(self, album):
        self.borrowed_albums.remove(album)