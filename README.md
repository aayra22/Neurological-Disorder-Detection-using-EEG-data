# **🧠 Neurological Disorder Detection Using EEG Data**

This project is a **Flask-based web application** that uses a **Convolutional Neural Network (CNN)** trained on EEG data to predict neurological disorders. Users can upload `.csv` EEG files, and the app displays the prediction results along with visual graphs.

---

## **📌 Features**

- 🧬 Deep learning-based EEG classification using CNN
- 📂 Upload `.csv` EEG data files for real-time predictions
- 📈 Visual output graph for prediction results
- 🌐 Clean and responsive frontend using HTML + CSS
- 🧠 Uses pre-trained models for both disorder and spindle detection

---

## **📂 Project Structure**

FLASK_PROJECT/
├── app.py # Main Flask app
├── model/ # Pretrained CNN models
│ ├── disorder_detection_model.h5
│ └── spindle_detection_model.h5
├── static/ # Static assets (CSS, images, uploads)
│ ├── style.css
│ ├── home_page.png
│ ├── upload_page.png
│ ├── sample_result.png
│ ├── Pi7_Tool_brain.jpg
│ └── prediction_graph.png
├── templates/ # HTML templates
│ ├── index.html
│ ├── upload.html
│ └── result.html
├── sample_1.csv to sample_6.csv # Sample EEG files
└── README.md # Project documentation

## ⚙️ Quick Setup

1. Clone the repo  
2. Create a virtual environment  
3. Install dependencies with `pip install -r requirements.txt`  
4. Run the app using `python app.py`  
5. Open `http://127.0.0.1:5000/` in your browser

📊 How It Works

Homepage: Introduces the application and its functionality.
Upload Page: Allows users to upload EEG .csv files.
Result Page: Shows predicted disorder and displays a graph.

🧠 Model Overview

Model Type: CNN (Convolutional Neural Network)
Framework: TensorFlow / Keras
Input: EEG data in CSV format
Output: Prediction (e.g., seizure, no disorder)

🧪 Tech Stack

- 🐍 Python — Backend & server logic  
- 🧠 TensorFlow/Keras — CNN model training and prediction  
- 🔬 Pandas & NumPy — Data processing and manipulation  
- 📈 Matplotlib — Visualization of results  
- 🌐 Flask — Web application framework  
- 🎨 HTML & CSS — Frontend design and styling  

### 🏠 Home Page  
![Home Page(home_screenshot.png)

### 📤 Upload Page  
![Upload Page](static/upload_screenshot.png)

### 📊 Result Page  
![Result Page](static/result_screenshot.png)



👩‍💻 Developed By

 Shivani Jadon
🎓 IT Student | 💻 Full Stack Developer | 🤖 Deep Learning Enthusiast
