import pandas as pd
import jsonlines  # Install this library: pip install jsonlines. this is very useful to read large datasets.

jsonl_file_path = 'D:/projects/data scientist/dev.jsonl'
csv_output_path = 'devTest.csv'

# Initialize lists to store data
document_title_list = []
question_text_list = []
example_id_list = []
long_answer_candidates_list = []


# Open the JSONL file and read line by line
with jsonlines.open(jsonl_file_path, 'r') as reader:
    for item in reader:
        document_title_list.append(item.get('document_title', ''))
        question_text_list.append(item.get('question_text', ''))
        example_id_list.append(item.get('example_id',''))
        long_answer_candidates_list.append(item.get('long_answer_candidates',''))
        
        

# Create DataFrame
df = pd.DataFrame({
    'document_title': document_title_list,
    'question_text': question_text_list,
    'example_id': example_id_list,
    'long_answer_candidates': long_answer_candidates_list,
    
})

# Deal with missing values (example)
df = df.dropna()  # Remove rows with missing values

# Save to CSV
df.to_csv(csv_output_path, index=False)

# Display DataFrame info (columns, data types, etc.)
print(df.info())
