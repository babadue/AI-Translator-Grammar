# for translation model
from transformers import MarianMTModel, MarianTokenizer

# Define the model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-zh"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Save the model and tokenizer to a local directory
local_directory = "C:/Users/userx/OneDrive/Desktop/AI/lab4/opus-mt-en-zh"
model.save_pretrained(local_directory)
tokenizer.save_pretrained(local_directory)

print(f"Model and tokenizer saved to {local_directory}")

# Define the model and tokenizer
model_name = "Helsinki-NLP/opus-mt-zh-en"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Save the model and tokenizer to a local directory
local_directory = "C:/Users/userx/OneDrive/Desktop/AI/lab4/opus-mt-zh-en"
model.save_pretrained(local_directory)
tokenizer.save_pretrained(local_directory)

print(f"Model and tokenizer saved to {local_directory}")

# for grammar correction

from transformers import T5ForConditionalGeneration, T5Tokenizer

# Model name
model_name = "vennify/t5-base-grammar-correction"

# Load the model and tokenizer from the Hub
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Specify the local directory where you want to save the model
local_directory = "C:/Users/userx/OneDrive/Desktop/AI/lab4/t5_base_grammar_correction"

# Save the model and tokenizer to the local directory
model.save_pretrained(local_directory)
tokenizer.save_pretrained(local_directory)

print(f"Model and tokenizer saved to {local_directory}")