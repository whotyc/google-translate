from googletrans import Translator

translator = Translator()
print('Enter the text you want to translate:')
text_to_translate = input()
translated_text = translator.translate(text_to_translate, src = 'ru', dest = 'en')
print('Your translated text:', translated_text.text)
