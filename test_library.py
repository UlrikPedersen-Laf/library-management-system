from album import Album, Podcast
from member import Member
from music_library import MusicLibrary


def test_add_album():
    lib = MusicLibrary()
    album = Album("A001", "Thriller", "Michael Jackson", 3)
    lib.add_album(album)
    assert "A001" in lib.albums


def test_remove_album():
    lib = MusicLibrary()
    album = Album("A001", "Thriller", "Michael Jackson", 3)
    lib.add_album(album)
    lib.remove_album("A001")
    assert "A001" not in lib.albums


def test_add_member():
    lib = MusicLibrary()
    member = Member("M001", "Ulrik")
    lib.add_member(member)
    assert "M001" in lib.members


def test_issue_album():
    lib = MusicLibrary()
    lib.add_album(Album("A001", "Thriller", "Michael Jackson", 3))
    lib.add_member(Member("M001", "Ulrik"))
    lib.issue_album("A001", "M001")
    assert lib.albums["A001"].copies == 2
    assert "A001" in lib.members["M001"].borrowed_albums


def test_return_album():
    lib = MusicLibrary()
    lib.add_album(Album("A001", "Thriller", "Michael Jackson", 3))
    lib.add_member(Member("M001", "Ulrik"))
    lib.issue_album("A001", "M001")
    lib.return_album("A001", "M001")
    assert lib.albums["A001"].copies == 3
    assert "A001" not in lib.members["M001"].borrowed_albums


def test_no_copies_available():
    lib = MusicLibrary()
    lib.add_album(Album("A001", "Thriller", "Michael Jackson", 0))
    lib.add_member(Member("M001", "Ulrik"))
    lib.issue_album("A001", "M001")
    assert "A001" not in lib.members["M001"].borrowed_albums


def test_polymorphism():
    album = Album("A001", "Thriller", "Michael Jackson", 3)
    podcast = Podcast("P001", "Lex Fridman", "Lex Fridman", 1)
    assert album.item_type() if hasattr(album, "item_type") else album.title == "Thriller"
    assert podcast.host == "Lex Fridman"