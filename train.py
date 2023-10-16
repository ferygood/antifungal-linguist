from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load your fine-tuned T5 model and tokenizer
# model_name = "your-fine-tuned-model-directory"
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# User input
user_question = "What is the capital of France?"

# Generate rationale
rationale_context = "the capital is the city that has the most population in a country"
input_text = f"Rationale: {user_question} Context: {rationale_context} "
input_ids = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)["input_ids"]
rationale_output_ids = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Generate label
label_context = "Paris"
input_text = f"Label: {user_question} Context: {label_context} "
input_ids = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)["input_ids"]
label_output_ids = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decode and print the rationale and label responses
rationale_response = tokenizer.decode(rationale_output_ids[0], skip_special_tokens=True)
label_response = tokenizer.decode(label_output_ids[0], skip_special_tokens=True)

print("Rationale Response:", rationale_response)
print("Label Response:", label_response)