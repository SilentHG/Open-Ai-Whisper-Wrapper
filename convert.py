import os
import json
import time

import torch
import whisper
import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)


def load_files():
    """Load file configuration from the JSON file."""
    with open('files.json') as f:
        data = json.load(f)
        return data


def convert_to_text(model, file_path, file_language, TRANSLATE, TIMESTAMP):
    """
    Transcribe or translate audio to text using Whisper and save the result.
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Perform transcription or translation
    if not TRANSLATE:
        print(f"Transcribing {file_path}...")
        result = model.transcribe(file_path, language=file_language)
    else:
        print(f"Translating {file_path} from {file_language} to English...")
        result = model.transcribe(file_path, language=file_language, task='translate')

    # Extract file name and prepare output path
    file_name = os.path.basename(file_path).split('.')[0]
    output_path = f'./output/{file_name}_transcription.txt'

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the transcription/translation to a text file
    if TIMESTAMP:
        with open(output_path, 'w', encoding='utf-8') as f:
            for segment in result['segments']:
                # Extract start time, end time, and text
                start_time = segment['start']
                end_time = segment['end']
                text = segment['text']
                # Format time as MM:SS
                formatted_start = f"{int(start_time // 60):02d}:{int(start_time % 60):02d}"
                formatted_end = f"{int(end_time // 60):02d}:{int(end_time % 60):02d}"
                # Write to file
                f.write(f"[{formatted_start} - {formatted_end}] {text}\n")
    else:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result['text'])

    print(f"Output with timestamps saved to: {output_path}")


def main():
    start_time = time.time()  # Record the start time

    load_file = load_files()
    files = load_file['FILES']
    model = load_file['MODEL']
    gpu = load_file['GPU']
    print(f"Using model: {model}")
    if gpu:
        device = "cuda"
    else:
        device = "cpu"
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    model = whisper.load_model(model, download_root="models").to(device)
    print(f"Loaded model to {device}")

    for file in files:
        convert_to_text(model, file['FILE_PATH'], file['FILE_LANGUAGE'], file['TRANSLATE'], file['TIMESTAMP'])

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f"Processing time: {elapsed_time:.2f} seconds")


if __name__ == '__main__':
    main()
