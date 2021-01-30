This application is a poll app where you get a list of main characters from a specific movie. 
When you pick your favourite character from all movies, you can submit a form.
App should: 
  - Check if all movies do have a selected choice. 
  - Update vote numbers after submiting the form.
  - Show a result page with number of votes that each character has.
  - Sort the result page by the amount of votes.

Example Usage:

python manage.py shell

In [1]: from fav_movie_char.models import Movie, Character

In [2]: Movie(title="Titanic").save()

In [3]: movie = Movie.objects.get(title="Titanic")

In [4]: movie.character_set.create(char_name="Rose DeWitt Bukater")
Out[4]: <Character: Character object (1)>

In [5]: exit 

python manage.py runserver

And now under the http://localhost:8000/movies/ address the poll should appear
