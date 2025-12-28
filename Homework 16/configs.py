CATEGORIES = {
    "Books" : 'catalogue/category/books/travel_2/index.html'
}

def get_values(category):
    for key, values in  CATEGORIES.items():
        if key == category:
            return values
