import requests  
import json

def emotion_detector(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    """
    This function detects emotions. The text needs to be inpt as a string. The output is a string. 
    """
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    obj_json = { "raw_document": { "text": text_to_analyze } }    
    response = requests.post(url, json = obj_json, headers=headers) 
    di = json.loads(response.text) 
    if response.status_code == 400:
        emo = {'anger':None, 'disgust':None, 'fear':None, 'joy':None, 'sadness':None, 'dominant_emotion':None}
    else:
        emo = di['emotionPredictions'][0]['emotion']
        keymax = max(zip(emo.values(), emo.keys()))[1]
        emo['dominant_emotion'] = keymax

    return emo 
