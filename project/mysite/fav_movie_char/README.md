This application is a poll app where you get a list of main characters from a specific movie. 
When you pick your favourite character from all movies, you can submit a form.
App should: 
  - Check if all movies do have a selected choice. 
  - Update vote numbers after submiting the form.
  - Show a result page with number of votes that each character has.
  - Sort the result page by the amount of votes.

Example Usage:
python manage.py shell
Python 3.8.3 (default, Jul  2 2020, 16:21:59)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.16.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from fav_movie_char.models import Movie, Character

In [2]: Movie(title="Titanic").save()

In [3]: character = Movie.character_set.get(title="Titanic")

In [4]: movie = Movie.objects.get(title="Titanic")

In [5]: movie.character_set.create(char_name="Rose DeWitt Bukater")
Out[5]: <Character: Character object (1)>

In [6]: exit 

python manage.py runserver

And now on the http://localhost:8000/movies the poll should appear
