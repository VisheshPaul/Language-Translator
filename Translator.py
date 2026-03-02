from googletrans import Translator

translator = Translator()

language = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    "la": "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh-cn": "Chinese (Simplified)",
    "es": "Spanish"
}

# Language selection
while True:
    user_code = input(
        "\nEnter language code (type 'options' to see list): "
    ).lower()

    if user_code == "options":
        print("\nCode : Language")
        for code, lang in language.items():
            print(f"{code} => {lang}")
        print()
    elif user_code in language:
        print(f"You selected: {language[user_code]}")
        break
    else:
        print("Invalid language code!")

# Translation loop
while True:
    text = input("\nEnter text to translate (type 'close' to exit): ")

    if text.lower() == "close":
        print("Program closed. Have a nice day!")
        break

    try:
        translated = translator.translate(text, dest=user_code)

        print("\n----------------------------")
        print(f"Translated Text: {translated.text}")

        if translated.pronunciation:
            print(f"Pronunciation: {translated.pronunciation}")

        print(f"Detected Source Language: {translated.src}")
        print("----------------------------")

    except Exception as e:
        print("Translation failed:", e)