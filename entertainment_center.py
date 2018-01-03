import media
import index

maze_runner_3 = media.Movie("Maze Runner The Death Cure",
                        "Maze Runner: The Death Cure (also known simply as The Death Cure) is a 2018 American dystopian science fiction action film directed by Wes Ball and written by T.S. Nowlin, based on the novel The Death Cure written by James Dashner.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/e/eb/MazeRunnerDeathCureFinalPoster.jpeg/220px-MazeRunnerDeathCureFinalPoster.jpeg",
                        "https://www.youtube.com/watch?v=4-BTxXm8KSg")
star_wars = media.Movie("Star Wars: The Last Jedi",
                     "Star Wars: The Last Jedi (also known as Star Wars: Episode VIII – The Last Jedi) is a 2017 American epic space opera film written and directed by Rian Johnson.",
                     "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                     "https://www.youtube.com/watch?v=Q0CbN8sfihY")
greatest_showman = media.Movie("The Greatest Showman",
                         "The Greatest Showman is a 2017 American musical drama film directed by Michael Gracey in his directorial debut, written by Jenny Bicks and Bill Condon and starring Hugh Jackman, Zac Efron, Michelle Williams, Rebecca Ferguson, and Zendaya.",
                         "https://upload.wikimedia.org/wikipedia/en/1/10/The_Greatest_Showman_poster.png",
                         "https://www.youtube.com/watch?v=jr9QtXwC9vc")
justice_league = media.Movie("Justice League",
                         "Justice League is a 2017 American superhero film based on the DC Comics superhero team of the same name, distributed by Warner Bros. Pictures. It is the fifth installment in the DC Extended Universe (DCEU).",
                         "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
                         "https://www.youtube.com/watch?v=r9-DM9uBtVI")
murder_on_the_orient_express = media.Movie("Murder on the Orient Express",
                                   "Murder on the Orient Express is a 2017 American mystery drama film directed by Kenneth Branagh with a screenplay by Michael Green, based on the 1934 novel of the same name by Agatha Christie.",
                                   "https://upload.wikimedia.org/wikipedia/en/b/bd/Murder_on_the_Orient_Express_teaser_poster.jpg",
                                   "https://www.youtube.com/watch?v=Mq4m3yAoW8E")
jumanji = media.Movie("Jumanji: Welcome to the Jungle",
                              "Jumanji: Welcome to the Jungle is a 2017 American adventure comedy film[3][6] directed by Jake Kasdan and written by Chris McKenna, Erik Sommers, Scott Rosenberg, and Jeff Pinkner, from a story by McKenna.",
                              "https://upload.wikimedia.org/wikipedia/en/d/dc/Jumanji_Welcome_to_the_Jungle.png",
                              "https://www.youtube.com/watch?v=v_TJKwJwN0E")

movies=[star_wars,greatest_showman,justice_league,murder_on_the_orient_express,jumanji,maze_runner_3]
index.open_movies_page(movies)
