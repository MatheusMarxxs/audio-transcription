# WhatsApp Audio Transcription

This code was created to transcribe WhatsApp audio messages for legal purposes.

## Description

The code utilizes the following libraries and tools:
- `os` for file and folder operations
- `speech_recognition` for speech recognition functionality
- `pydub` for audio file manipulation and splitting
- `subprocess` for executing the Opus to WAV conversion using ffmpeg

The main functions in the code are:
- `convert_opus_to_wav(opus_file)`: Converts Opus audio files to WAV format.
- `transcribe_audio(wav_file)`: Transcribes WAV audio files using the Google Speech Recognition API.
- The main script transcribes all Opus audio files in the "audios" folder and writes the transcriptions to text files.

## Installation

### Prerequisites

Before running the code, you need to have `ffmpeg` installed on your system. `ffmpeg` is a command-line tool used for audio and video processing, and it is required for converting Opus audio files to WAV format. Please follow the instructions below to install `ffmpeg` based on your operating system:

#### macOS

You can install `ffmpeg` on macOS using Homebrew. Open a terminal and run the following command:


```shell
brew install ffmpeg
```

#### Linux

On most Linux distributions, you can install ffmpeg using the package manager. Open a terminal and run the appropriate command for your package manager:

For Ubuntu/Debian-based systems:

```shell
sudo apt-get install ffmpeg
```

For Fedora/RHEL-based systems:

```shell
sudo dnf install ffmpeg
```

#### Windows

For Windows, you can download a static build of `ffmpeg` from the official website:

1. Go to the [ffmpeg download page](https://ffmpeg.org/download.html).
2. Scroll down to the "Windows" section.
3. Under "Get the packages", click on "Static Builds".
4. Download the latest static build of `ffmpeg` for your architecture (32-bit or 64-bit).
5. Extract the downloaded ZIP file to a directory of your choice.
6. Add the directory containing the `ffmpeg` executable to your system's PATH environment variable. This will allow you to use `ffmpeg` from any location in the command prompt.

### Python Dependencies

To install the required Python dependencies, you can use `pip`. Open a terminal and navigate to the root directory of the project (where the `requirements.txt` file is located), then run the following command:

```shell
pip install -r requirements.txt
```

This will install the necessary libraries with the specified versions.

## Usage

1. Place Opus audio files to be transcribed in the "audios" folder.
2. Run the script, and it will convert Opus files to WAV format and transcribe them.
3. Transcriptions will be saved as text files in the "textos" folder.

## License

Fell free to use, improve, share it :)
