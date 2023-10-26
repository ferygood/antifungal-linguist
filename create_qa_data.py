import pandas as pd
#from datasets import Dataset, DatasetDict

file = "data/train.csv"
df = pd.read_csv(file)

print(df.iloc[0,0])

# Replace 'train_dataset.csv' and 'test_dataset.csv' with your file paths
""" train_csv_file = 'train_dataset.csv'
test_csv_file = 'test_dataset.csv'
 """
""" # Read the CSV files into Pandas DataFrames
train_df = pd.read_csv(train_csv_file)
test_df = pd.read_csv(test_csv_file)

# Convert DataFrames into datasets
train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

# Rename columns if needed
train_dataset = train_dataset.rename_column("question", "input_text")
train_dataset = train_dataset.rename_column("answer", "target_text")

test_dataset = test_dataset.rename_column("question", "input_text")
test_dataset = test_dataset.rename_column("answer", "target_text")

# Create a DatasetDict with both "train" and "test" partitions
toy_dataset = DatasetDict({"train": train_dataset, "test": test_dataset})

# Print dataset information
print(toy_dataset)


 """