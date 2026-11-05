#Movies.py
movies = {
    "action": ["John Wick", "Extraction"],
    "comedy": ["The Mask", "Home Alone"],
    "sci-fi": ["Interstellar", "Inception"]
}
genre = input("Enter movie genre: ").lower()
import random
print("Recommended Movie:", random.choice(movies[genre]))