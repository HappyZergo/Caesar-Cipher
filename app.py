from flask import Flask, request, render_template
from CaesarCipher import cipher, cracked, cryptoanalyse, check

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['encode']
        shift = request.form['shift']
        if shift == '':
            shift = 0

        if shift == 0 or None:
            decoded = cracked(text.upper())
            decodedtext = decoded[0]
            shift = decoded[1]
            frequence = cryptoanalyse(text)
            freq = frequence[0]
            item = frequence[1]
            return render_template("index.html", encode=text, shift=shift, decode=decodedtext, number= freq, labels = item)
        else:
            decoded = cipher(shift,text)
            frequence = cryptoanalyse(text)
            freq = frequence[0]
            item = frequence[1]
            return render_template("index.html", encode=text, shift=shift, decode=decoded, number= freq,  labels = item)
    else:
        return render_template("index.html", encode='', shift='', decode='', number= [])


if __name__ == '__main__':
    app.run()
