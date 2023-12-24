from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from transformers import GenerationConfig

model_name='vennify/t5-base-grammar-correction'

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

def correct_sentence(sentence):
    inputs = tokenizer.encode("grammar: " + sentence, return_tensors="pt")
    outputs = model.generate(inputs, max_length=128, do_sample=True)
    corrected = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected


while True:
    # Prompt the user for input
    user_input = input("Enter text to check or just Q to quit: ")

    if user_input.lower() == 'q':
        print("Exiting the program.")
        break  # Break out of the loop to exit the program

    corrected_sentence = correct_sentence(user_input)
    print(f"Input sentence: {user_input}")
    print(f"Corrected sentence: {corrected_sentence}\n")
    continue
