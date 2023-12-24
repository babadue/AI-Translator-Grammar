from transformers import MarianMTModel, MarianTokenizer


def translate_to_chinese(text):
    # Load pre-trained model and tokenizer
    model_name = "Helsinki-NLP/opus-mt-en-zh"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    text_to_translate = text

    # Tokenize and translate
    input_ids = tokenizer.encode(text_to_translate, return_tensors="pt")

    # Generate translation
    translation_ids = model.generate(input_ids)
    translation = tokenizer.decode(translation_ids[0], skip_special_tokens=True)

    return translation

def translate_to_english(text):
    # Load pre-trained model and tokenizer
    model_name = "Helsinki-NLP/opus-mt-zh-en"  # Note the language code change
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    text_to_translate = text

    # Tokenize and translate
    input_ids = tokenizer.encode(text_to_translate, return_tensors="pt")

    # Generate translation
    translation_ids = model.generate(input_ids)
    translation = tokenizer.decode(translation_ids[0], skip_special_tokens=True)

    return translation

def english_to_chinese():
    # print("english to chinese original: ")
    # Prompt the user for input
    user_input = input("Enter English text to Chinese: ")
    translated_text = translate_to_chinese(user_input)
    print(f"Chinese Translation from user input: {translated_text}\n")

def chinese_to_english():
    # print("chinese to english original: ")
    user_input = input("Enter Chinese text to English: ")
    translated_text = translate_to_english(user_input)
    print(f"Chinese Translation from user input: {translated_text}\n")

def switch_case(user_key):
    switch_dict = {
        'c': english_to_chinese,
        'e': chinese_to_english,
        'q': 'This is case Q',
    }

    result = switch_dict.get(user_key)
    if callable(result):
        # print("callable")
        return result()
    # print("not a callable")
    return result

while True:
    # Prompt the user for a single keypress
    print("Press 'C' to Chinese or 'E' to English or 'Q' to quit: ")

    # Get a single character input
    user_key = input().lower()

    # Check the pressed key
    if user_key == 'q':
        print("Exiting the program.")
        break  # Break out of the loop to exit the program

    if user_key not in {'c', 'e'}:
        print("Invalid key. Please try again.")
        continue  # Continue to the next iteration without processing the invalid key

    # Process the key
    result = switch_case(user_key)
    # print("Result:", result)



