# Label Studio Data Splitter

This repository contains a Python script for splitting annotated data (JSON format) from Label Studio into training and validation sets. The data is shuffled before splitting, and the output is saved in separate files for easy training and validation.

## Features

- Splits annotated data exported from Label Studio in  JSON format into training and validation sets.
- Edit splitting ratio as you wish
- Saves the training and validation data into `train.json` and `dev.json` files.

## Requirements

- Python 3.x

## Usage

1. Export annotations in json format from label studio:

![{AE87331D-4AF1-4587-AD39-86A2748F41E1}](https://github.com/user-attachments/assets/008faf75-d7b9-4fe1-a227-0f88485f5b07)


2. Clone the Repository

   ```bash
   git clone https://github.com/SakibAhmedShuva/label-studio-text-annotation-data-splitter.git
   cd label-studio-data-splitter

3. Modify the input filepath and intended split ratio
Edit the split ratio (currently set to 0.7 for a 70%-30% training-validation split):
  
   ```bash
   split_index = int(len(data) * 0.7)  # Adjust 0.7 to your desired ratio

4. Run the script:
   ```bash
   python data_splitter.py

5. Example Output:
   ```bash
   Total data: 1000
   Training data: 700
   Validation data: 300
