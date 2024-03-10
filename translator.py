from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        if 'file' not in request.files:
            raise Exception("No file part")

        file = request.files['file']
        if file.filename == '':
            raise Exception("No selected file")

        if file:
            translation = perform_translation(file)
            return render_template('index.html', translation=translation)

    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('index.html', error=error_message)

def perform_translation(file):
    from translate import Translator

    translator = Translator(to_lang="hi")
    text = file.read().decode('utf-8')
    translation = translator.translate(text)
    return translation

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
