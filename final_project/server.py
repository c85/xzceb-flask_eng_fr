from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/english_to_french/<english_text>")
def english_to_french(english_text):
    textToTranslate = request.args.get(english_text)
    translatedFrenchText = machinetranslation.translator.english_to_french(textToTranslate)
    return translatedFrenchText

@app.route("/french_to_english/<french_text>")
def french_to_english(french_text):
    textToTranslate = request.args.get(french_text)
    translatedEnglishText = machinetranslation.translator.french_to_english(textToTranslate)
    return translatedEnglishText

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
