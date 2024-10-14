from langdetect import detect
from googletrans import Translator
from textblob import TextBlob

class code_nlp:

    def lang_detect(self,text):
        language = detect(text)

        return language
    def translation(self,text,dest):
        #language Translation
        translator = Translator()
        translated = translator.translate(text, dest=dest)
        response=translated.text

        return response
    
    def sentiment(self,text):
        blob = TextBlob(text)
        sentiment = blob.sentiment
        analysis=sentiment.polarity
        if analysis>0.5:
            result="Positive Comment"
        else:
            result="Negative Comment"

        return result