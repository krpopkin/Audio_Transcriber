# Audio Transcriber

An audio transcription tool leveraging OpenAI Whisper and WhisperX for accurate and efficient transcriptions.

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  
- [Author](#author)

## About

Audio Transcriber is a Python-based command-line and scriptable tool for transcribing audio files into text. It integrates:

- **OpenAI Whisper** for baseline transcription.  
- **WhisperX** for forced alignment and improved timestamp accuracy.  
- Optional usage of **DeepSeek** or other transcription services.

The tool supports MP3 and MP4 input formats and outputs verbatim transcripts with timestamps.

## Features

- **High accuracy** with WhisperX forced alignment.  
- **Timestamped** transcriptions.  
- **Batch processing** of multiple audio files.  
- **Simple CLI** and Python API.  
- **Customizable** model selection and performance parameters.

- This repository contains an app built using Gradio that inputs audio and video files and creates a transcription.  The steps to create a transcription using this app are...

**Create a new transcription:**
1. Select the "Transcribe" tab
2. Enter the language spoken in the audio or video
3. Select an audio or video file on your local drive to upload
4. Select "Submit" to load the audio followed by "Transcribe" to begin the transcription
5. The results are displayed in the UI and written to an SQlite database.

**View Available Transcriptions:**
1. Select "View Transcriptions" tab
2. From the dropdown select the title of an audio or video
3. The transcripts results are displayed


## Prerequisites

- Python 3.8+  
- `pip` package manager  
- FFmpeg installed and available in your PATH.

## Installation

```bash
git clone https://github.com/krpopkin/Audio_Transcriber.git
cd Audio_Transcriber
pip install -r requirements.txt
```

## Usage

### Command-Line

```bash
python transcriber1.py --input /path/to/audio.mp3 --output transcript.txt
```

Common options:

- `--model`: Whisper model to use (e.g., `base`, `small`, `medium`, `large`).  
- `--align`: Enable WhisperX forced alignment.  
- `--language`: Specify language code (e.g., `en`, `es`).  
- `--batch-dir`: Process all audio files in a directory.

### Python API

```python
from transcriber1 import transcribe

result = transcribe(
    input_path="audio.mp3",
    model="small",
    align=True,
    language="en"
)
print(result.text)
```

## Configuration

Configuration options are set via command-line flags or environment variables:

- `WHISPER_MODEL`  
- `USE_WHISPERX`  
- `FFMPEG_PATH`

## Project Structure

```
Audio_Transcriber/
├── transcriber1.py           # Main transcription script
├── transcription_service.py  # Whisper and WhisperX integration
├── requirements.txt
├── examples/                 # Example audio files and usage
│   └── sample_audio.mp3
└── README.md                 # Project README (this file)
```
## Author

**Ken Popkin**  
*GitHub:* [@krpopkin](https://github.com/krpopkin)  
*Email:* krpopkin@gmail.com

