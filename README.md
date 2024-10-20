# Sigma Video Generator

Automatically generate sigma brainrot YouTube shorts with one click!

## Description

The Sigma Video Generator is an automated system that procedurally creates "engaging" "short-form" "video" "content". It combines generated text, text-to-speech audio, background music, and video manipulation and editing techniques to produce complete .mp4 files ready for upload to platforms like YouTube Shorts.

## Features

- Text generation using a local LLM (via Ollama or similar)
- Text-to-speech conversion using ElevenLabs API
- Background music integration
- Audio mixing with Pydub
- Video compositing and manipulation using Blender

## Installation

(Add installation instructions here, including setting up the virtual environment and installing dependencies)

## Input
Place input files in the appropriate subdirectories under the input/ directory:

background_videos/: MP4 files for background videos
generated_text/: Text files for input to TTS
generated_tts/: JSON and MP3 files from TTS API
images/: Image files for video composition
inspiration/: Additional text input files (e.g., topics.txt)
music/: Background music files with metadata about BPM and when the song drops

## Usage

To generate a video:

1. Ensure all input files are in place (background videos, music, etc.)
2. Run the main script:

```bash
python src/main.py
```

3. The generated video will be saved in the `output/` directory.

## Dependencies

- Python 3.x
- Ollama (or alternative local LLM)
- ElevenLabs API
- Blender
- Pydub
- (List any other major dependencies)

## Configuration

Adjust settings in `config/settings.yaml`.
Put your own videos in `input/background_videos`.

## Contributing

(Add instructions for contributing to the project)

## License

(Specify the license under which this project is released)

## Acknowledgements

- ElevenLabs for text-to-speech API
- Blender for 3D rendering and video compositing
- Peter Wan
- (Add any other acknowledgements or credits)
