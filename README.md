
# Real-Time Speech Translator for PowerPoint Presentations

The **RT_SpeechTranslator** is a real-time speech translation tool that enables seamless translation of spoken English into Italian during PowerPoint presentations. It leverages machine learning and modern UI frameworks to deliver a smooth and accessible user experience.

## Features

- **Real-Time Translation**: Converts spoken English into Italian instantly.
- **Tkinter UI Integration**: Displays translations in a modern and minimalist user interface.
- **Audio Handling**: Uses `sounddevice` for high-quality audio recording.
- **Multithreading**: Processes speech recognition and translation in a separate thread for responsiveness.
- **Automatic Speech Recognition (ASR)**: Utilizes Google's ASR for speech-to-text conversion.
- **Hugging Face Transformer**: Employs the `Helsinki-NLP/opus-mt-en-it` model for high-quality translations.

---

## Installation

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/Altricch/RealTime_SpeechTranslator_for_Presentations
   cd RT_SpeechTranslator
   ```

2. **Install Dependencies**:  
   Ensure Python is installed (>= 3.8). Then, install the required libraries:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Model Files** (Optional):  
   The required Hugging Face model, `Helsinki-NLP/opus-mt-en-it`, will be downloaded automatically when running the script.

---

## Usage

1. **Run the Translator**:  
   Start the script from your terminal:  
   ```bash
   python RT_SpeechTranslator.py
   ```

2. **Configure Input and Output**:  
   - Ensure your microphone is properly set up.
   - Translated text will be displayed in a full-screen Tkinter window.

3. **During the Presentation**:  
   - Run the PowerPoint slideshow.
   - Minimize or position the translation display window for better visibility.

---

## Requirements

- **Operating System**: Windows/macOS/Linux
- **Python**: Version 3.8 or higher
- **Dependencies**:  
  - `speech_recognition`
  - `sounddevice`
  - `transformers`
  - `scipy`
  - `numpy`
  - `tkinter`

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Configuration

- **Translation Model**:  
   By default, the tool uses `Helsinki-NLP/opus-mt-en-it` for English-to-Italian translation. To support additional languages, integrate other models in the `translator` pipeline.

- **Microphone Input**:  
   Verify that the system's default microphone is correctly set in your audio settings.

- **UI Customization**:  
   Adjust the Tkinter UI settings in the script (e.g., font size, window dimensions, colors) to meet your presentation needs.

---

## Roadmap

Future improvements include:
- Adding support for multiple languages.
- Enhancing UI for more interactive audience engagement.
- Reducing CPU usage through advanced threading or multiprocessing techniques.
- Optimizing translation speed for larger phrases.

---

## Contributing

We welcome contributions! Please:
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes.
4. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

This project uses:
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for ASR.
- [Hugging Face Transformers](https://huggingface.co/) for machine translation.
- [sounddevice](https://python-sounddevice.readthedocs.io/) for audio recording.
- Tkinter for UI rendering.

For feedback or inquiries, contact [altric@usi.ch](mailto:altric@usi.ch). 
