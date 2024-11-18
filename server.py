"""
This module is important
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/emotionDetector')
def sent_analyzer():
    """
    This function detects emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    statem = "For the given statement, the system response is "
    for key, value in response.items():
        if key == 'dominant_emotion':
            statem += f"The dominant emotion is {value}. "
            break
        statem += f"'{key}': {value}, "
    return statem

@app.route('/')
def render_index_page():
    """
    This renders template
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
