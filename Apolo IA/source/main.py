import time
from classes.speech_to_text import SpeechModule
from classes.text_to_speech import VoiceRecognitionModule
from classes.chatbot_brain import ChatbotBrain

context = """Soy Apolo IA """

translation_artifacts_english = {"Disagreement": "Discord"}

translation_artifacts_spanish = {
    "pequenina": "Pequeñin",
    "osito de peluche": "Oso Teddy",
    "profesor": "Maestro",
}
chatbot = ChatbotBrain(
    context,
    translation_artifacts_english,
    translation_artifacts_spanish,
    "microsoft/DialoGPT-large",
    "microsoft/DialoGPT-large",
    True,
    True,
)

speech = SpeechModule()
recognition = VoiceRecognitionModule()

while True:
    text = recognition.recognize()

    if text:
        chatbot_text = chatbot.talk(text)
        speech.talk(chatbot_text)
    else:
        speech.talk("No te he entendido")
    time.sleep(1)
