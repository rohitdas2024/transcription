import whisper
import warnings

warnings.filterwarnings("ignore", category=UserWarning, message="FP16 is not supported on CPU; using FP32 instead")

model=whisper.load_model("base")
result=model.transcribe("recording.wav")


with open("transcription.txt","w") as f:
    f.write(result["text"])