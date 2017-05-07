import movie

class DataMovies():
    """ Movie Class definy object to each item of list movies """
    def __init__(self):

        """
        create Toy History Object
        """
        toy_story = movie.Movie(
            "Toy Story",
            "A story of a boy the his tosy come to life",
            "images/toy_story.jpg",
            "https://www.youtube.com/watch?v=ZZv1vki4ou4"
        )

        """
        create Avatar Object
        """
        avatar = movie.Movie(
            "Avatar",
            "A marine on an alien planet",
            "images/avatar.jpg",
            "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
        )

        """
        create Last Samuray Object
        """
        last_samuray = movie.Movie(
            "The Last Samuray",
            " a formerly retired officer of the United States in Japan war",
            "images/the.last.samurai.jpg",
            "https://www.youtube.com/watch?v=T50_qHEOahQ"
        )

        """
        create a movie object list
        """
        self.data_movies_list = [
            toy_story,
            avatar,
            last_samuray
        ]
