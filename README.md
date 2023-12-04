# Whisper ASR Transcription

## Overview

This Python script utilizes the Whisper ASR (Automatic Speech Recognition) library to transcribe an audio recording. The Whisper model named "base" is loaded, and the transcription of the provided audio file ("recording.wav") is saved to a text file ("transcription.txt"). The script includes a warning filter to suppress a specific UserWarning related to FP16 not being supported on CPU.

## Prerequisites

Python 3.x
Whisper library (pip install whisper)

Install the required dependencies:
```
pip install whisper
```
## File Descriptions

main.py: The main Python script containing the transcription code.
recording.wav: Audio file to be transcribed.
transcription.txt: Output file containing the transcribed text.

## Notes
Ensure that the audio file ("recording.wav") is in the same directory as the script, or provide the correct path to the audio file.
Run the script:
Also ensure that the Whisper model "base" is available for loading. If not, download and specify the correct model.

## Author
Rohit Das
