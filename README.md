# Open Ai Whisper Wrapper for easy usage.

This project uses the Whisper model to transcribe or translate audio files to text. The transcription can include timestamps if desired.

## Requirements

- Python 3.x
- pip

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

The configuration for the files to be processed and the model to be used is specified in the `files.json` file. Below is an example configuration:

```json
{
  "MODEL": "tiny",
  "FILES": [
    {
      "FILE_PATH": "./input/sample.mp4",
      "FILE_LANGUAGE": "en",
      "TRANSLATE": false,
      "TIMESTAMP": true
    },
    {
      "FILE_PATH": "./input/sample2.mp4",
      "FILE_LANGUAGE": "da",
      "TRANSLATE": false,
      "TIMESTAMP": false
    }
  ]
}
```

- `MODEL`: The Whisper model to use (e.g., `tiny`, `base`, `small`, `medium`, `large`, `large-v2`, `large-v3`, `turbo`).
- `FILES`: A list of files to be processed.
    - `FILE_PATH`: The path to the audio file.
    - `FILE_LANGUAGE`: The language of the audio file.
    - `TRANSLATE`: Whether to translate the audio to English.
    - `TIMESTAMP`: Whether to include timestamps in the transcription.

## Usage

Run the `convert.py` script to process the files specified in `files.json`:

```sh
python convert.py
```

The transcriptions will be saved in the `output` directory with the same name as the input file, appended with `_transcription.txt`.

## Example

For the given `files.json` configuration, the following files will be generated:

- `./output/sample_transcription.txt` (with timestamps)
- `./output/sample2_transcription.txt` (without timestamps)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
