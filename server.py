''' this is the module docstring '''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    ''' this is the doc string for emotion_detect '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return_str = "For the given statement, the system response is "
    for item in response:
        if item == "dominant_emotion":
            return_str += ". The dominant emotion is " + str(response[item]) + "."
            break
        return_str += "'" + item + "':" + str(response[item]) + ", "

    return return_str

@app.route('/')
def render_index_page():
    ''' this is the docstring for render_index_page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


