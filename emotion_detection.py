"""
Create an emotion detection application using the Watson NLP library
"""
import json # Import JSON library to handle HTTP requests
import requests # Import the requests library to handle HTTP requests

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):
    """
    Sends text to the Watson NLP Emotion Predict API and extracts the results.
    Args:
       text_to_analyse (str): The text document to be evaluated for sentiment.
    Returns:
        dict: A dictionary containing the sentiment 'label' and 'score'.
        Returns None for values if the server error occurs.
    """
    # URL of the sentiment analysis service
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    # Parse the response from the API
    formatted_response = json.loads(response.text)
    # Create a new dictionary "set of emotions"
    set_emotions =  formatted_response["emotionPredictions"][0]["emotion"]
    # Create the final result
    result = {
            "anger": set_emotions["anger"],
            "disgust": set_emotions["disgust"],
            "fear": set_emotions["fear"],
            "joy": set_emotions["joy"],
            "sadness": set_emotions["sadness"]
        }
    # Add to result dominant_emotion and return full result
    result["dominant_emotion"] = max(result, key=result.get)
    return result


    #    try:
#        # Send a POST request to the API with the text and headers
#        response = requests.post(url, json = myobj, headers=header, timeout=10)
#    except requests.exceptions.Timeout:
#        # Working with case whan Skills Network didn'r answer more then 10 second
#        return {"label": None, "score": None}
#    except requests.exceptions.RequestException:
#        # Working with case whan Skills Network had other errors
#        return {"label": None, "score": None}
#    # If the response status code is 200, extract the label and score from the response
#    if response.status_code == 200:
#        # Parse the response from the API
#        formatted_response = json.loads(response.text)
#        label = formatted_response['documentSentiment']['label']
#        score = formatted_response['documentSentiment']['score']
#    # If the response status code is 500, set label and score to None
#    elif response.status_code == 500:
#        label = None
#        score = None
#    # For any other unexpected status codes, set label and score to None
#    else:
#        label = None
#        score = None
#    # Return the label and score in a dictionary
#    return {'label': label, 'score': score}