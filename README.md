# ✋ Hand Gesture Recognition (Real-Time)

A real-time hand gesture recognition system using computer vision that detects hand gestures through a webcam and maps them to predefined actions like numbers and symbols.

---

## 🚀 Features

* 🎥 Real-time webcam-based gesture detection
* ✋ Recognizes multiple hand gestures
* ⚡ Lightweight and fast execution
* 🧠 Uses hand landmark-based logic for gesture classification
* 🖥️ Easy to set up and run locally

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 📁 Project Structure

```
hand-gesture-recognition/
│
├── hand_gesture.py      # Main script
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ShantanuPatil123/hand-gesture-recognition.git
cd hand-gesture-recognition
```

---

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate the virtual environment

#### Windows:

```bash
venv\Scripts\activate
```

#### Mac/Linux:

```bash
source venv/bin/activate
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the project

```bash
python hand_gesture.py
```

---

## ✋ Supported Gestures

| Gesture        | Description               |
| -------------- | ------------------------- |
| ✊ Fist         | All fingers closed        |
| ☝️ One         | Index finger up           |
| ✌️ Two         | Index + middle finger     |
| 🤟 Three       | Index + middle + ring     |
| 🖖 Four        | All except thumb          |
| 🖐️ Five       | Open palm                 |
| 👍 Thumbs Up   | Thumb pointing upward     |
| 👎 Thumbs Down | Thumb pointing downward   |
| 🤘 Rock        | Thumb + pinky             |
| 👌 OK          | Thumb + index form circle |

---

## ⚠️ Limitations

* Sensitive to lighting conditions
* Requires clear hand visibility
* Accuracy may vary with hand angle and background

---

## 🔮 Future Improvements

* Replace MediaPipe with custom computer vision / deep learning model
* Add support for full sign language recognition
* Improve accuracy using trained datasets
* Deploy as a web application

---

## 🙌 Acknowledgements

* OpenCV community
* MediaPipe by Google

---

## 👨‍💻 Author

**Shantanu Patil**
GitHub: https://github.com/ShantanuPatil123

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub!
