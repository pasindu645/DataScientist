import pandas as pd
import jsonlines  # Install this library: pip install jsonlines. this is very useful to read large datasets.

jsonl_file_path = 'french_books_reviews.jsonl'
csv_output_path = 'french_books_reviews.csv'

# Initialize lists to store data
book_title_title_list = []
author_list = []
reader_review_list = []
rating_list = []


# Open the JSONL file and read line by line
with jsonlines.open(jsonl_file_path, 'r') as reader:
    for item in reader:
        book_title_title_list.append(item.get('book_title', ''))
        author_list.append(item.get('author', ''))
        reader_review_list.append(item.get('reader_review',''))
        rating_list.append(item.get('rating',''))
        
        
            

# Create DataFrame
df = pd.DataFrame({
    'book_title': book_title_title_list,
    'author': author_list,
    'reader_review': reader_review_list,
    'rating': rating_list,
    
})

# Deal with missing values (example)
df = df.dropna()  # Remove rows with missing values

# Save to CSV
df.to_csv(csv_output_path, index=False)

# Display DataFrame info (columns, data types, etc.)
print(df.info())
