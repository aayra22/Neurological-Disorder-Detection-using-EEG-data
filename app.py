import matplotlib.pyplot as plt

from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import tensorflow as tf
import numpy as np
import os




app = Flask(__name__)

# Load your trained deep learning model
MODEL_PATH = "model\disorder_detection_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400  # Bad Request if no file is uploaded
        
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400  # Bad Request if no file is selected

        if file:
            filepath = os.path.join("static", "uploaded_file.csv")
            file.save(filepath)
            return redirect(url_for('result'))  # Redirect to result page after saving

    return render_template('upload.html')


# @app.route('/result')
# @app.route('/result', methods=['GET', 'POST'])

# def result():
#     # Load the uploaded CSV file
#     file_path = os.path.join("static", "uploaded_file.csv")
#     data = pd.read_csv(file_path)

#     # Preprocess the data (Modify this according to your model's input format)
#     input_data = np.array(data.iloc[:, :-1])  # Adjust based on features
#     predictions = model.predict(input_data)

#     # Convert predictions to a readable format
#     result_text = ["Positive" if pred > 0.5 else "Negative" for pred in predictions]

#     return render_template('result.html', predictions=result_text)

# number 1
# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     file_path = os.path.join("static", "uploaded_file.csv")
    
#     # Load the CSV file
#     data = pd.read_csv(file_path)

#     # Ensure the number of columns match the model input
#     input_data = np.array(data.iloc[:, :5])  # Adjust column selection based on model requirement

#     # Generate model predictions
#     predictions = model.predict(input_data)
    
#     # Convert predictions to numerical values for graphing
#     predicted_values = predictions.flatten()

#     # Create a graph
#     plt.figure(figsize=(8, 5))
#     plt.plot(predicted_values, marker='o', linestyle='-', color='b', label='Predicted Values')
#     plt.xlabel('Sample Index')
#     plt.ylabel('Prediction Value')
#     plt.title('Neurological Disorder Predictions')
#     plt.legend()
    
#     # Save the graph as an image
#     graph_path = "static/prediction_graph.png"
#     plt.savefig(graph_path)
#     plt.close()

#     return render_template('result.html', image_path=graph_path)

@app.route('/result', methods=['GET', 'POST'])
def result():
    file_path = os.path.join("static", "uploaded_file.csv")
    
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Ensure the number of columns match the model input
    input_data = np.array(data.iloc[:, :5])  # Adjust column selection based on model requirement

    # Generate model predictions
    predictions = model.predict(input_data)
    
    # Convert predictions to numerical values for graphing
    predicted_values = predictions.flatten()

    # Calculate accuracy (Example: if you have actual labels, replace with real data)
    actual_values = np.random.randint(0, 2, size=predicted_values.shape)  # Dummy actual values
    accuracy = np.mean((predicted_values > 0.5) == actual_values) * 100

    # Create a graph
    plt.figure(figsize=(8, 5))
    plt.plot(predicted_values, marker='o', linestyle='-', color='b', label='Predicted Values')
    plt.xlabel('Sample Index')
    plt.ylabel('Prediction Value')
    plt.title('Neurological Disorder Predictions')
    plt.legend()
    
    # Save the graph as an image
    graph_path = "static/prediction_graph.png"
    plt.savefig(graph_path)
    plt.close()

    return render_template('result.html', image_path=graph_path, accuracy=accuracy)


if __name__ == '__main__':
    app.run(debug=True)


