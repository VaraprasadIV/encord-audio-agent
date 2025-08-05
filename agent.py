
import whisper
from deep_translator import GoogleTranslator

class AudioTranslateAgent:
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe_and_translate(self, audio_path):
        result = self.model.transcribe(audio_path)
        segments = []
        for seg in result['segments']:
            text = seg['text'].strip()
            translated = GoogleTranslator(source='auto', target='hi').translate(text)
            segments.append({
                "start": seg['start'],
                "end": seg['end'],
                "original": text,
                "translated": translated
            })
        return segments
