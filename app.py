from flask import Flask, render_template, request
from art import text2art

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = None
    if request.method == 'POST':
        user_text = request.form['text_input']
        selected_font = request.form['font_select']
        ascii_art = text2art(user_text, font=selected_font)
    return render_template('index.html', ascii_art=ascii_art)

if __name__ == '__main__':
    app.run(debug=True)
