# Label Studio Data Splitter

This repository contains a Python script for splitting annotated data (JSON format) from Label Studio into training and validation sets. The data is shuffled before splitting, and the output is saved in separate files for easy training and validation.

## Features

- Splits JSON data exported from Label Studio into training (70%) and validation (30%) sets.
- Supports UTF-8 encoding to handle various languages and special characters.
- Shuffles the data to ensure randomness before splitting.
- Saves the training and validation data into `train.json` and `dev.json` files.

## Requirements

- Python 3.x

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/label-studio-data-splitter.git
cd label-studio-data-splitter

### 2. Modify input filepath as needed

### 3. Run the script:
   ```bash
   python data_splitter.py

Example Output:

```bash
Copy code
Total data: 1000
Training data: 700
Validation data: 300
