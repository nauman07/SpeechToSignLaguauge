# 🤟 Speech to Sign Language Converter

A Python-based accessibility tool that **converts spoken speech into American Sign Language (ASL)** gestures in real time, designed to improve communication for the deaf and hard-of-hearing community.

---

## 📖 About

Communication barriers between hearing and non-hearing individuals remain a significant challenge. This project addresses that by building a system that listens to spoken words and displays the corresponding sign language gestures — making communication more inclusive and accessible.

---

## 📂 Repository Structure

```
SpeechToSignLaguauge/
├── SpeechToSignLanguage.py     # Main conversion script
└── README.md
```

---

## ✨ Features

- 🎙️ **Real-time speech recognition** — Captures and transcribes spoken words
- 🤲 **Sign language rendering** — Displays corresponding ASL gestures for each recognized word/letter
- 🔄 **Continuous listening** — Keeps running to capture ongoing speech
- ♿ **Accessibility-focused** — Designed to aid communication for the deaf community

---

## 📦 Dataset

The sign language gesture images are sourced from the **WLASL (Word-Level American Sign Language)** dataset, available on Kaggle.

🔗 Search: *"WLASL"* or *"ASL Alphabet"* on [Kaggle](https://www.kaggle.com)

---

## 🛠️ Tech Stack

| Library | Purpose |
|--------|---------|
| `SpeechRecognition` | Converting speech to text |
| `OpenCV` | Displaying sign language images/animations |
| `NumPy` | Array operations |
| `Pygame` / `PIL` | Rendering gesture visuals |

---

## 🚀 Getting Started

### Install Dependencies

```bash
pip install SpeechRecognition opencv-python numpy Pillow pyaudio
```

> **Note:** For `pyaudio` on Windows:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

### Setup Dataset

Download the WLASL dataset from Kaggle and organize gesture images in a folder structure:
```
signs/
├── A.jpg
├── B.jpg
├── hello.jpg
├── thank_you.jpg
...
```

### Run the Converter

```bash
git clone https://github.com/nauman07/SpeechToSignLaguauge.git
cd SpeechToSignLaguauge
python SpeechToSignLanguage.py
```

Speak clearly into your microphone and the corresponding sign language gesture will be displayed.

---

## 🎯 Use Cases

- Classrooms with deaf students
- Healthcare settings for patient communication
- Public kiosks and information systems
- Learning ASL with audio input

---

## 🤝 Contributing

Contributions to extend vocabulary, add video animations, or improve accuracy are very welcome. Open an issue or submit a pull request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
