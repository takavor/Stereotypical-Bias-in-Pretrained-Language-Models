from tqdm import tqdm
import json
from openai import OpenAI

client = OpenAI()

# load data
with open('data/data_copy.json') as file:
  data = json.load(file)

# function to generate similar sentences given context
def generate_similar_contexts(context, labels):
  
  prompt=f"Generate two sentences similar in meaning to: '{context}'\nThe sentences must also contain a 'BLANK' word, which could be replaced by the following words which are labeled as stereotype, anti-stereotype, or unrelated: {labels}."

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
    ]
  )
  
  response = completion.choices[0].message.content
  return response


for item in tqdm(data):
  response = generate_similar_contexts(item['context'], item['labels'])
  item['response'] = response

# save
with open('data/updated_data.json', 'w') as file:
  json.dump(data, file, indent=4)
  
  
  
