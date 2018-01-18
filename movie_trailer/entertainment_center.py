import media
import fresh_tomatoes

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys that come to life",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=wsnMbDdhCe8")

coco = media.Movie("Coco",
                   "Coco is a 2017 American 3D computer-animated musical fantasy film produced by Pixar Animation Studios and released by Walt Disney Pictures",
                   "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=jjudmcSxzpc")

ratatouille = media.Movie("Ratatouille",
                          "A story of rad can cook",
                          "http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg",
                          "https://www.youtube.com/watch?v=-tNqfcZKn6k")

up = media.Movie("Up",
                 "Up is a 2009 American 3D computer-animated comedy-adventure film[3] produced by Pixar Animation Studios and released by Walt Disney Pictures",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")
car2 = media.Movie("Car2",
                   "Cars 2 is a 2011 American computer-animated action-adventure comedy film produced by Pixar Animation Studios for Walt Disney Pictures",
                   "https://i.jeded.com/i/cars-2.15102.jpg",
                   "https://www.youtube.com/watch?v=oFTfAdauCOo")

movies = [avatar, coco, ratatouille, up, car2]
fresh_tomatoes.open_movies_page(movies)