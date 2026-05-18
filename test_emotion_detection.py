# In this file, import the emotion_detector function from the EmotionDetection package.
# Also import the unittest library
from EmotionDetection.emotion_detection import emotion_detector
import unittest

# Create the unit test class. Let's call it TestEmotionDetection. 
# Define test_sentiment_analyzer as the function to run the unit tests.
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        
        # Test case for Statement I am glad this happened
        result_1 = emotion_detector('I am glad this happened') 
        self.assertEqual(result_1['dominant_emotion'], 'joy') 
        
        # Test case for Statement I am really mad about this
        result_2 = emotion_detector('I am really mad about this') 
        self.assertEqual(result_2['dominant_emotion'], 'anger') 
        
        # Test case for Statement I feel disgusted just hearing about this
        result_3 = emotion_detector('I feel disgusted just hearing about this') 
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        
        # Test case for Statement I am so sad about this
        result_4 = emotion_detector('I am so sad about this') 
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        
         # Test case for Statement I am really afraid that this will happen
        result_5 = emotion_detector('I am really afraid that this will happen') 
        self.assertEqual(result_5['dominant_emotion'], 'fear')
unittest.main()
