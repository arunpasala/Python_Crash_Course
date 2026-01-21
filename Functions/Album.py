def make_album(artist_name, album_title, number_of_tracks=''):
    """Return a dictionary of information about a music album."""
    album = {'artist': artist_name, 'title': album_title}
    if number_of_tracks:
        album['tracks'] = number_of_tracks
    return album
album1 = make_album('pink floyd', 'the dark side of the moon')
print(album1)
album2 = make_album('metallica', 'ride the lightning', 8)
print(album2)