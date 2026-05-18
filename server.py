''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the all needed emotions from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    # Return a formatted string with the all needed emotions and the dominant emotion
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # function should simply run the render_template function on the HTML template, index.html
    return render_template("index.html")

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    # File execution, run the application on host: 0.0.0.0 (or localhost) on port number 5000.
    app.run(host = "0.0.0.0", port = 5000)