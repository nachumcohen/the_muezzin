import whisper
from loging.logger import Logger

logger = Logger.get_logger()
def convert_audio_to_text(file):

    try:
        model = whisper.load_model("base")
        result = model.transcribe(file)
        return result["text"]

    except Exception as e:
        logger.error(e)
