import yaml
import requests
import json
import base64
from dotenv import load_dotenv
import os
import random
import datetime
import re

def load_config():
    with open('config/settings.yaml', 'r') as file:
        return yaml.safe_load(file)

def log_action(description):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    script_name = os.path.basename(__file__)
    log_entry = f"{timestamp} - {script_name}: {description}\n"
    with open('logs/logs.txt', 'a') as log_file:
        log_file.write(log_entry)

def get_random_text(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        raise ValueError("No files found in the specified directory")

    while True:
        random_file = random.choice(files)
        with open(os.path.join(directory, random_file), 'r', encoding='utf-8') as file:
            lines = file.readlines()
        non_empty_lines = [line.strip() for line in lines if line.strip()]
        if non_empty_lines:
            return random.choice(non_empty_lines)

def generate_filename(text, extension):
    # Take the first 5 words, remove non-alphanumeric characters, and join with underscores
    words = re.findall(r'\w+', text)[:5]
    filename = '_'.join(words).lower()
    return f"{filename[:50]}.{extension}"  # Limit filename length

config = load_config()
log_action("Configuration loaded")

load_dotenv()
log_action("Environment variables loaded")

VOICE_ID = "nPczCjzI2devNBz1zQrb"  # Brian
YOUR_XI_API_KEY = os.getenv("ELEVENLABS_API_KEY")

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps"

headers = {
  "Content-Type": "application/json",
  "xi-api-key": YOUR_XI_API_KEY
}

text_dir = config['directories']['generated_text_dir']
selected_text = get_random_text(text_dir)
log_action(f"Random text selected: {selected_text[:50]}...")

data = {
  "text": selected_text,
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.1,
    "similarity_boost": 0.75
  }
}

log_action("Sending request to ElevenLabs API")
response = requests.post(url, json=data, headers=headers)

if response.status_code != 200:
  error_message = f"Error encountered, status: {response.status_code}, content: {response.text}"
  log_action(error_message)
  print(error_message)
  quit()

log_action("Response received from ElevenLabs API")

json_string = response.content.decode("utf-8")
response_dict = json.loads(json_string)
audio_bytes = base64.b64decode(response_dict["audio_base64"])

tts_dir = config['directories']['generated_tts_dir']
audio_filename = generate_filename(selected_text, "mp3")
metadata_filename = generate_filename(selected_text, "json")

output_audio_file_path = os.path.join(tts_dir, audio_filename)
output_metadata_file_path = os.path.join(tts_dir, metadata_filename)

with open(output_audio_file_path, 'wb') as f:
  f.write(audio_bytes)
log_action(f"Audio file saved: {audio_filename}")

metadata = {
    "audio_filename": audio_filename,
    "full_text": selected_text,
    "alignment": response_dict['alignment']
}

with open(output_metadata_file_path, 'w') as f:
  json.dump(metadata, f, indent=2)
log_action(f"Metadata file saved: {metadata_filename}")

log_action("Script execution completed successfully")
