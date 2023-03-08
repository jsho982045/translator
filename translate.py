import openai
import json

openai.api_key = "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"

text = input("Please enter the text to be translated: ")
language = input("Please enter the language you want to translate to: ")

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"Translate '{text}' to {language}.",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

translation = response.choices[0].text.strip()

if translation:
    try:
        translation_dict = json.loads(translation)
        if "translation" in translation_dict:
            translated_text = translation_dict["translation"]
            pronunciation = translation_dict.get("pronunciation")
            print(f"\nTranslated text ({language}): {translated_text}")
            if pronunciation:
                print(f"Pronunciation: {pronunciation}")
        else:
            print(f"\nTranslation failed. Response: {translation}")
    except json.JSONDecodeError as e:
        print(f"\nTranslation failed. Response: {translation}. Error: {e}")
else:
    print(f"\nTranslation failed. Response: {translation}")


