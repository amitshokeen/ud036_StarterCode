import webbrowser

class Movie():
    '''This class is used to store movie related information'''
    #class variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #class variable
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
