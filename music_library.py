from album import Album
from member import Member

class MusicLibrary:
    def __init__(self):
        self.albums = {}
        self.members = {}

    def add_album(self, album):
        self.albums[album.album_id] = album
        print(f"Album '{album.title}' added.")

    def display_albums(self):
        for album in self.albums.values():
            album.display_info()
    
    def remove_album(self, album_id):
        if album_id in self.albums:
            removed = self.albums.pop(album_id)
            print(f"Album '{removed.title}' removed.")
        else:
            print(f"Album with ID '{album_id}' not found.")

    def update_album(self, album_id, title=None, artist=None, copies=None):
        if album_id in self.albums:
            if title:
                self.albums[album_id].title = title
            if artist:
                self.albums[album_id].artist = artist
            if copies:
                self.albums[album_id].copies = copies
            print(f"Album '{album_id}' updated.")
        else:
            print(f"Album with ID '{album_id}' not found.")

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Member '{member.name}' added.")

    def remove_member(self, member_id):
        if member_id in self.members:
            removed = self.members.pop(member_id)
            print(f"Member '{removed.name}' removed.")
        else:
            print(f"Member with ID '{member_id}' not found.")

    def display_members(self):
        for member in self.members.values():
            member.display_info()
    
    def issue_album(self, album_id, member_id):
        if album_id not in self.albums:
            print(f"Album with ID '{album_id}' not found.")
        elif member_id not in self.members:
            print(f"Member with ID '{member_id}' not found.")
        elif self.albums[album_id].copies <= 0:
            print(f"No copies available for '{self.albums[album_id].title}'.")
        else:
            self.albums[album_id].copies -= 1
            self.members[member_id].borrow_album(album_id)
            print(f"Album '{self.albums[album_id].title}' issued to '{self.members[member_id].name}'.")

    def return_album(self, album_id, member_id):
        if member_id not in self.members:
            print(f"Member with ID '{member_id}' not found.")
        elif album_id not in self.members[member_id].borrowed_albums:
            print(f"Member '{self.members[member_id].name}' has not borrowed this album.")
        else:
            self.albums[album_id].copies += 1
            self.members[member_id].return_album(album_id)
            print(f"Album '{self.albums[album_id].title}' returned by '{self.members[member_id].name}'.")