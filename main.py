# This is a project about sentiment sense of the text
# --------------------------------------------
# © 2023 Jose Rey | All rights reserved.     #
# This code is for personal use only.        #
# --------------------------------------------

# import the necessary modules
import datetime
import sys
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from nltk.sentiment import SentimentIntensityAnalyzer


# function for the main program
class SentimentSense(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        try:
            loadUi("./assets/ui/sentimentsense.ui", self)
            self.setWindowTitle("Sentiment Sense")
            self.setWindowIcon(QIcon("./assets/images/logo.png"))
            self.greeting_time_now()
            self.errorMessage.setVisible(False)
            self.btnAnalyze.clicked.connect(self.analyze_text)
            self.inputText.textChanged.connect(self.on_text_changed)
        except Exception as e:
            print(f"Failed to load UI file: {e}")

    def greeting_time_now(self):
        # Get the current time
        current_time = datetime.datetime.now().time()

        # Define time ranges for greetings
        time_ranges = {
            (datetime.time(6, 0), datetime.time(12, 0)): "Good Morning!",
            (datetime.time(12, 0), datetime.time(18, 0)): "Good Afternoon!",
        }

        # Check the current time and print the corresponding greeting
        greeting = next((msg for (start, end), msg in time_ranges.items() if start <= current_time < end),
                        "Good Evening!")
        self.lblText.setText(greeting)

    def on_text_changed(self):
        if self.inputText.text() != "":
            self.errorMessage.setVisible(False)

    def analyze_text(self):
        # get the text input from the field
        textAnalyze = self.inputText.text()

        try:
            if textAnalyze == "":
                self.errorMessage.setText("Please enter a text to analyze.")
                self.errorMessage.setVisible(True)
            else:
                # Create a SentimentIntensityAnalyzer object
                analyzer = SentimentIntensityAnalyzer()

                # Perform sentiment analysis
                sentiment_scores = analyzer.polarity_scores(textAnalyze)
                sentiment_polarity = sentiment_scores["compound"]

                # Determine emotion level based on sentiment polarity
                if sentiment_polarity > 0:
                    emotion_level = "Positive"
                    path = "./assets/images/positive.png"
                    color = "color: #2EC000"
                elif sentiment_polarity < 0:
                    emotion_level = "Negative"
                    path = "./assets/images/negative.png"
                    color = "color: #FD7700"
                else:
                    emotion_level = "Neutral"
                    path = "./assets/images/neutral.png"
                    color = "color: #434343"

                pixmap = QPixmap(path)
                self.lblText.setStyleSheet(color)
                self.lblEmotion.setPixmap(pixmap)
                self.lblText.setText(emotion_level)

        except Exception as e:
            print("Error: ", e)


if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window
    window = SentimentSense()
    window.show()

    # Start the event loop
    sys.exit(app.exec())

# --------------------------------------------
# © 2023 Jose Rey | All rights reserved.     #
# This code is for personal use only.        #
# --------------------------------------------
