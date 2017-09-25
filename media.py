import webbrowser


class Movie:
    """A model of a movie"""
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):  # NOQA
        """Initialize title,storyline , image and a youtube link"""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def openTrailor(self):
        """Opening the browser with the specified link"""
        webbrowser.open(self.trailer_youtube_url)
