import json

# load data
with open('data/llama_preliminary_1.json') as file_1:
  data_1 = json.load(file_1)
  
with open('data/llama_preliminary_2.json') as file_2:
  data_2 = json.load(file_2)


from metrics import get_metrics
lms_1, ss_1, icat_1 = get_metrics(data_1)
lms_2, ss_2, icat_2 = get_metrics(data_2)

print('Data 1')
print(f'LMS: {lms_1}')
print(f'SS: {ss_1}')
print(f'iCAT: {icat_1}')
print('---')
print('Data 2')
print(f'LMS: {lms_2}')
print(f'SS: {ss_2}')
print(f'iCAT: {icat_2}')