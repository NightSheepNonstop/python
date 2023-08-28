def make_album(artist_name, album_name, album_num=None):
    album = {'artist_name': artist_name, 'album_name': album_name}
    if album_num:
        album['album_num'] = album_num
    return album


album1 = make_album('Lorde', 'Melodrama')
album2 = make_album('LanaDelRey', 'Norman Fucking Rockwell')
album3 = make_album('Beyoncé', 'Lemonade', 7)
print(album1, album2, album3)
