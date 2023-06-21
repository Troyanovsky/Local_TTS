# Local_TTS
Local TTS GUI with Coqui TTS. With Local TTS, you can easily convert text to speech and save the output as a WAV file.

Models used: "tts_models/en/ljspeech/fast_pitch" & "vocoder_models/en/ljspeech/hifigan_v2"

## Installation
To use Local TTS, you need to have Python 3 installed on your computer. Tested with Pyton3.9. Does not work with Python3.11.

After installing Python 3, you can install the required dependencies by running the following command in your terminal:
```
pip install TTS
```

## Usage
To start Local TTS, run the following command in your terminal:
```python
python app.py
```
This will open the Local TTS GUI. To generate speech from text, enter the text in the input field and click the "Generate" button. You can choose the output folder by clicking the "Output Folder" button. If you don't choose a folder, the output file will be saved in the same directory as the app.

