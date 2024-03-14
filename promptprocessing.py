import json

# function to split the data into 2 copies, each copy containing a sentence generated
def split_data(data):
    
    split_data_1 = []
    split_data_2 = []
    
    for item in data:
        item_1 = item.copy()
        item_2 = item.copy()
        
        responses = item['response'].split('\n')
        
        item_1['response'] = responses[0]
        item_2['response'] = responses[1]
        
        split_data_1.append(item_1)
        split_data_2.append(item_2)
        
    return split_data_1, split_data_2

# function to process sentences (remove square brackets, newlines, etc.)
def process_sentences(data):
    
    modified = []
    
    for item in data:
        modified_item = item.copy()
        modified_item['context'] = modified_item['context'].replace('[BLANK]', 'BLANK')
        modified_item['response'] = modified_item['response'].replace('[BLANK]', 'BLANK').strip()
        modified.append(modified_item)
        
    return modified

# function to format the data in the original format
def format_data(data):
    pass

# load data
with open('data/data_gpt4.json') as file:
  data = json.load(file)
  
# run functions on gpt4 data
data_1, data_2 = split_data(data)

# process data
data_1, data_2 = process_sentences(data_1), process_sentences(data_2)

# write to files
with open('data/data_gpt4_1.json', 'w') as file_1:
    json.dump(data_1, file_1, indent=4)
    
with open('data/data_gpt4_2.json', 'w') as file_2:
    json.dump(data_2, file_2, indent=4)