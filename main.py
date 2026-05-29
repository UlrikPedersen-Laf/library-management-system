from album import Album, Podcast
from member import Member
from music_library import MusicLibrary

def main():
    lib = MusicLibrary()

    while True:
        print("\n--- Music Library ---")
        print("1. Add Album")
        print("2. Add Podcast")
        print("3. Display all items")
        print("4. Add Member")
        print("5. Display all members")
        print("6. Issue album to member")
        print("7. Return album from member")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            album_id = input("Album ID: ")
            title = input("Title: ")
            artist = input("Artist: ")
            copies = int(input("Copies: "))
            lib.add_album(Album(album_id, title, artist, copies))

        elif choice == "2":
            podcast_id = input("Podcast ID: ")
            title = input("Title: ")
            host = input("Host: ")
            copies = int(input("Copies: "))
            lib.add_album(Podcast(podcast_id, title, host, copies))

        elif choice == "3":
            lib.display_albums()

        elif choice == "4":
            member_id = input("Member ID: ")
            name = input("Name: ")
            lib.add_member(Member(member_id, name))

        elif choice == "5":
            lib.display_members()

        elif choice == "6":
            album_id = input("Album ID: ")
            member_id = input("Member ID: ")
            lib.issue_album(album_id, member_id)

        elif choice == "7":
            album_id = input("Album ID: ")
            member_id = input("Member ID: ")
            lib.return_album(album_id, member_id)

        elif choice == "0":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()