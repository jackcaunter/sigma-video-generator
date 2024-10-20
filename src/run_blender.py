import subprocess
import os

def run_blender_task(blender_script):
    # Get the directory of the current script (src folder)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the project root directory (one level up from src)
    project_root = os.path.dirname(current_dir)

    # Construct the path to the shell script
    shell_script = os.path.join(current_dir, "run_blender.sh")

    # Construct the path to the Blender script
    blender_script_path = os.path.join(current_dir, blender_script)

    # Run the shell script with the Blender script as an argument
    result = subprocess.run([shell_script, blender_script_path], capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode != 0:
        print(f"Error running Blender task: {result.stderr}")
    else:
        print(f"Blender task completed successfully: {result.stdout}")

# Main procedure
if __name__ == "__main__":
    # Run the Blender task
    run_blender_task("blender_scripts/create_turquoise_square_video_eevee.py")

    # Continue with the rest of the procedure
    print("Blender task finished. Continuing with the rest of the procedure...")
    # Add more code here as needed
