import webbrowser

class Movie():
    """ This class provides a way to store movie-related information """

    def __init__(self, movie_title, movie_poster_img_url,
                 movie_youtube_trailer_url):
        """ Turns parameters into instance variable"""
        self.title = movie_title
        self.poster_image_url = movie_poster_img_url
        self.trailer_youtube_url = movie_youtube_trailer_url

    def show_trailer(self):
        """ A function with target of self that uses the open function stored within webbrowser"""
        webbrowser.open(self.trailer_youtube_url)