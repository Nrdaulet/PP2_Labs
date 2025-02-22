# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# Function 1: Check if a single movie has an IMDB score above 5.5
def is_high_score(movie):
    return movie["imdb"] > 5.5

# Function 2: Return a sublist of movies with an IMDB score above 5.5
def movies_above_threshold(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

# Function 3: Return movies under a specific category
def movies_by_category(movies, category_name):
    return [movie for movie in movies if movie["category"].lower() == category_name.lower()]

# Function 4: Compute the average IMDB score of a list of movies
def average_imdb(movies):
    if not movies:
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

# Function 5: Compute the average IMDB score for a specific category
def average_imdb_by_category(movies, category_name):
    category_movies = movies_by_category(movies, category_name)
    return average_imdb(category_movies)


# print(is_high_score({"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"}))  

# print("Next...")
# print(movies_above_threshold(movies)) 

# print("Next...")
# print(movies_by_category(movies, "Romance"))  

# print("Next...")
# print(average_imdb(movies)) 

print("Next...")
print(average_imdb_by_category(movies, "Romance"))  