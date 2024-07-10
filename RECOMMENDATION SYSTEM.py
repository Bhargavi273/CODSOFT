# Sample dataset of books with genres
books = {
    'book1': ['Fiction', 'Thriller'],
    'book2': ['Romance', 'Contemporary'],
    'book3': ['Fantasy'],
    'book4': ['Science Fiction', 'Adventure'],
    'book5': ['Self-Help', 'Motivational'],
    'book6': ['Mystery', 'Crime']
}

# Function to recommend books based on user preferences
def recommend_books(user_preferences):
    recommended_books = []
    for book, genres in books.items():
        if any(genre in genres for genre in user_preferences):
            recommended_books.append(book)
    
    return recommended_books

# Example user preferences for books
user_preferences = ['Fantasy', 'Motivational']

# Get recommended books
recommendations = recommend_books(user_preferences)

# Print recommended books based on preferences
if recommendations:
    print(f"Recommended books based on your preferences:")
    for book in recommendations:
        print(f"- {book}")
else:
    print("No books found based on your preferences.")
    