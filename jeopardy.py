# Import necessary libraries and display csv format in environment
import pandas as pd
pd.set_option('display.max_colwidth', None)

jeopardy = pd.read_csv('jeopardy.csv')

# Annoying space before all column names in original file. Used rename method to re-format
jeopardy = jeopardy.rename(columns = {
    ' Show Number': 'Show Number',
    ' Air Date': 'Air Date',
    ' Round': 'Round',
    ' Category': 'Category',
    ' Value': 'Value',
    ' Question': 'Question',
    ' Answer': 'Answer'
})

# Function designed to filter out specific words in the dataset.
def filtered_df(data, words):
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    return data.loc[data['Question'].apply(filter)]
                    
# Example function call 
filtered_questions = filtered_df(jeopardy, ['sports', 'science'])
print(filtered_questions['Question'].head())
    
# Add float value column to perform aggregate statistics    
jeopardy['Float_Values'] = jeopardy['Value'].apply(lambda x: float(x[1:].replace(',', '') if x != 'None' else 0))

# Example equation
mean_difficulty = filtered_df(jeopardy, ['sports'])
print(mean_difficulty['Float_Values'].mean())


#function that returns the count of unique answers in datset
def unique_answers(data):
    return data['Answer'].value_counts()
# Get answer counts
print(unique_answers(filtered_questions))



                





