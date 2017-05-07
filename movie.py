import webbrowser

class Movie():

    """
    Class to create movie object
    """
    def __init__(
        self,
        title,
        story_line,
        poster_image_url,
        trailer_youtube_url
    ):

        """
        setup params movie descriptions
        """
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    """
    show trailer url in a box
    """
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
