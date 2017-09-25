import media
import fresh_tomatoes

# List of movies that will appear on a webpage
julia_michaels = media.Movie("Huh-ha",
                             "Rebound of Julia Michaels",
                             "https://upload.wikimedia.org/wikipedia/commons/2/29/Toy_Story_Midway_Mania.JPG",  # NOQA
                             "https://www.youtube.com/watch?v=9Ke4480MicU")

selena_gomez = media.Movie("Selena",
                           "Kygo, Selena Gomez",
                           "https://upload.wikimedia.org/wikipedia/commons/3/30/Selena_Gomez_2008.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=D5drYkLiLI8")

taylor_swift = media.Movie("Taylor",
                           "ZAYN, Taylor Swift",
                           "https://upload.wikimedia.org/wikipedia/commons/c/c0/Taylor_Swift.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=AY9blLYMKnI")

# List of movies
movies = [julia_michaels, selena_gomez, taylor_swift]

fresh_tomatoes.open_movies_page(movies)
