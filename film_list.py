import fresh_tomatoes
import film

#Movie is a class within the film file
film_1 = film.Movie("My Neighbor Totoro",
                    "https://upload.wikimedia.org/wikipedia/en/0/02/My_Nei"
                    + "ghbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.j"
                    + "pg",
                    "https://www.youtube.com/watch?v=92a7Hj0ijLs")
film_2 = film.Movie("Howl's Moving Castle",
                    "https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-"
                    + "moving-castleposter.jpg",
                    "https://www.youtube.com/watch?v=iwROgK94zcM")
film_3 = film.Movie("Spirited Away",
                    "https://upload.wikimedia.org/wikipedia/en/3/30/Spirit"
                    + "ed_Away_poster.JPG",
                    "https://www.youtube.com/watch?v=ByXuk9QqQkk")
film_4 = film.Movie("Princess Mononoke",
                    "https://upload.wikimedia.org/wikipedia/en/2/24/Prince"
                    + "ss_Mononoke_Japanese_Poster_%28Movie%29.jpg",
                    "https://www.youtube.com/watch?v=4OiMOHRDs14")
film_5 = film.Movie("Castle in the Sky",
                    "https://upload.wikimedia.org/wikipedia/en/4/40/Castle"
                    + "_in_the_Sky_%28Movie_Poster%29.jpg",
                    "https://www.youtube.com/watch?v=8ykEy-yPBFc")
film_6 = film.Movie("Kiki's Delivery Service",
                    "https://upload.wikimedia.org/wikipedia/en/0/07/Kiki%2"
                    + "7s_Delivery_Service_%28Movie%29.jpg",
                    "https://www.youtube.com/watch?v=piIdiZ44zzU")

movies = [film_1, film_2, film_3, film_4, film_5, film_6]

fresh_tomatoes.open_movies_page(movies)
