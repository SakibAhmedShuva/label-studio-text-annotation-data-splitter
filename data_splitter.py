import json
import random

# Load the JSON data with UTF-8 encoding
with open(fr'c:\Users\Sakib Ahmed\Documents\sample.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Shuffle the data
random.shuffle(data)

# Calculate split index
split_index = int(len(data) * 0.7)

# Split the data
train_data = data[:split_index]
validation_data = data[split_index:]

# Save the training data with UTF-8 encoding
with open('./train.json', 'w', encoding='utf-8') as train_file:
    json.dump(train_data, train_file, indent=4, ensure_ascii=False)

# Save the validation data with UTF-8 encoding
with open('./dev.json', 'w', encoding='utf-8') as validation_file:
    json.dump(validation_data, validation_file, indent=4, ensure_ascii=False)

print(f'Total data: {len(data)}')
print(f'Training data: {len(train_data)}')
print(f'Validation data: {len(validation_data)}')