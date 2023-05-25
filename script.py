import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import subprocess


def convert_opus_to_wav(opus_file):
    wav_file = os.path.splitext(opus_file)[0] + ".wav"

    # Use ffmpeg to convert Opus to WAV
    subprocess.run(["ffmpeg", "-y", "-i", opus_file, "-ar", "16000", wav_file])

    return wav_file


def transcribe_audio(wav_file):
    # Load the WAV file
    audio = AudioSegment.from_file(wav_file, format="wav")

    # Split audio on silent parts
    chunks = split_on_silence(
        audio,
        min_silence_len=500,    # Minimum silence length in milliseconds
        silence_thresh=-40       # Adjust this threshold according to your audio
    )

    transcriptions = []

    # Initialize the speech recognition recognizer
    recognizer = sr.Recognizer()

    # Process each audio chunk
    for i, chunk in enumerate(chunks):
        # Export chunk as WAV for compatibility with the speech recognition library
        chunk.export("temp.wav", format="wav")

        # Load the WAV file
        with sr.AudioFile("temp.wav") as source:
            # Read the audio data from the file
            audio_data = recognizer.record(source)

            try:
                # Perform speech recognition
                text = recognizer.recognize_google(audio_data, language="pt-PT")  # Adjust language if needed
                transcriptions.append(text)
            except sr.UnknownValueError:
                # Handle unknown value error
                transcriptions.append("<Unrecognized>")
            except sr.RequestError:
                # Handle request error (e.g., no internet connection)
                transcriptions.append("<RequestError>")

    # Write transcriptions to file
    output_file = os.path.join("texts", os.path.splitext(os.path.basename(wav_file))[0] + ".txt")
    with open(output_file, "w") as file:
        file.write("\n".join(transcriptions))

    print(f"Transcriptions written to {output_file}")


# Get a list of all files in the "audios" folder
folder_path = "audios"
audio_files = [file for file in os.listdir(folder_path) if file.endswith(".opus")]

# Transcribe each audio file
for file in audio_files:
    opus_file = os.path.join(folder_path, file)
    print(f"Transcribing {opus_file}:")
    wav_file = convert_opus_to_wav(opus_file)
    transcribe_audio(wav_file)
