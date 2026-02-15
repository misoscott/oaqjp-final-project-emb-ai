import requests, json
def emotion_detector(text_to_analyze):
    '''
    analyzes text for emotion
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)

    # collect values
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    dominant = max([anger,disgust,fear,joy,sadness])

    # which one is dominant?
    if dominant == anger:
        dname = 'anger'
    elif dominant == disgust:
        dname = 'disgust'
    elif dominant == fear:
        dname = 'fear'
    elif dominant == joy:
        dname = 'joy'
    else:
        dname = 'sadness'

    # construct dictionary for return value    ret = { 'anger': anger, 'disgust': disgust,
            'fear': fear, 'joy': joy, 'sadness': sadness,
        'dominant_emotion': dname}
    retuet
             
