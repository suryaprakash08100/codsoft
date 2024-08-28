movies = [
    {"title": "Inception", "genres": ["Action", "Sci-Fi", "Thriller"]},
    {"title": "The Matrix", "genres": ["Action", "Sci-Fi"]},
    {"title": "The Godfather", "genres": ["Crime", "Drama"]},
    {"title": "The Shawshank Redemption", "genres": ["Drama"]},
    {"title": "Pulp Fiction", "genres": ["Crime", "Drama"]},
    {"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"]},
    {"title": "Interstellar", "genres": ["Sci-Fi", "Drama"]},
    {"title": "Forrest Gump", "genres": ["Drama", "Romance"]},
]

def recommend_movies(preferences):
    recommended = []
    preferences = set(preferences)  
    
    for movie in movies:
        if preferences.intersection(movie["genres"]):
            recommended.append(movie["title"])
    return recommended

def main():
    user_input = input("Enter your preferred genres (comma-separated): ")
    preferences = [genre.strip().title() for genre in user_input.split(",")]
    recommendations = recommend_movies(preferences)
    
    if recommendations:
        print("We recommend the following movies based on your preferences:")
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print("Sorry, we couldn't find any movies matching your preferences.")

if __name__ == "__main__":
    main()
