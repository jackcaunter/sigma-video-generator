import yaml
import os

def load_config():
    with open('config/settings.yaml', 'r') as file:
        return yaml.safe_load(file)

def list_video_clips(config):
    video_dir = config['directories']['background_videos_dir']
    for root, dirs, files in os.walk(video_dir):
        for file in files:
            if file.endswith('.mp4'):
                print(os.path.join(root, file))

def main():
    config = load_config()
    print("Listing available video clips:")
    list_video_clips(config)

if __name__ == "__main__":
    main()
