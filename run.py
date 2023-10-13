from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Define the available choices for task prefixes
choices = {
    "1": "translate English to German:",
    "2": "cola sentence:",
    "3": "summarize:"
}

# Display the menu of choices to the user
print("Choose a task:")
for key, value in choices.items():
    print(f"{key}. {value}")

# Get the user's choice
user_choice = input("Enter the number of your choice: ")

# Check the user's choice and set the task_prefix accordingly
if user_choice in choices:
    task_prefix = choices[user_choice]
else:
    task_prefix = "Unknown task"

# Get the input sentences from the user
sentences = input("Enter the text to process: ")

# Tokenize the input sentences
input_text = f"{task_prefix}: {sentences}"
input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

# Generate the output based on the chosen task
output_ids = model.generate(input_ids, max_length=100, min_length=10, length_penalty=2.0, num_beams=4, early_stopping=True)

# Decode and print the output
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print("Generated Output:", output_text)