import json
from pydub import AudioSegment

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def timestretch_audio(audio, target_length):
    # TODO: Implement this function to timestretch the audio to the target length
    # For now, we'll just return the original audio
    return audio

def process_audio():
    # Hardcoded filenames
    tts_audio_path = "input/generated_tts/output.mp3"
    tts_json_path = "input/generated_tts/output.json"
    bgm_audio_path = "input/music/byebye.mp3"
    bgm_json_path = "input/music/byebye.json"

    # Load JSON data
    tts_data = load_json(tts_json_path)
    bgm_data = load_json(bgm_json_path)

    # Load audio files
    tts_audio = AudioSegment.from_mp3(tts_audio_path) + 6
    bgm_audio = AudioSegment.from_mp3(bgm_audio_path) - 6

    # Get TTS duration
    tts_duration = tts_data['alignment']['character_end_times_seconds'][-1]

    # Get BGM drop timestamp
    drop_timestamp = bgm_data['drop_timestamp_in_seconds']

    # Check if TTS duration is longer than drop timestamp
    if tts_duration > drop_timestamp:
        # TODO: Implement timestretch function
        tts_audio = timestretch_audio(tts_audio, drop_timestamp)
        tts_duration = drop_timestamp

    # Calculate the start time for BGM
    bgm_start_time = drop_timestamp - tts_duration

    # Trim BGM to start at the correct time
    trimmed_bgm = bgm_audio[bgm_start_time * 1000:]

    # Ensure BGM is long enough (loop if necessary)
    # while len(trimmed_bgm) < len(tts_audio):
    #     trimmed_bgm += bgm_audio

    # Trim BGM to match TTS length
    # trimmed_bgm = trimmed_bgm[:len(tts_audio)]

    # Mix TTS and BGM
    mixed_audio = trimmed_bgm.overlay(tts_audio)

    # Export the final mix
    output_path = "output/mixed_audio1.mp3"
    mixed_audio.export(output_path, format="mp3")

    print(f"Mixed audio saved to {output_path}")

if __name__ == "__main__":
    process_audio()
