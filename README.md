# Fake News Detection

This project implements a Fake News Detection system that classifies news articles as either "Fake" or "True" using machine learning techniques. The model utilizes PassiveAggressiveClassifier to process text data and make predictions.

## Features
- **Text Input**: Users can input news text into a web form.
- **Real-time Predictions**: The system provides instant feedback on whether the news is classified as "Fake" or "True."
- **Machine Learning Model**: Uses a `PassiveAggressiveClassifier` trained on real and fake news datasets.
- **Text Preprocessing**: The project employs `TfidfVectorizer` for feature extraction from the text data.

## Tech Stack
- **Python**: Backend processing and machine learning model.
- **Flask**: Web framework for serving the application.
- **HTML/CSS**: Frontend for user interaction.
- **Scikit-learn**: Library for machine learning.

## How It Works
1. Users submit a news article in the input form.
2. The application preprocesses the news using `TfidfVectorizer`.
3. The pre-trained model predicts whether the news is fake or true.
4. The result is displayed on the webpage.

## Installation
To run the Fake News Detection system locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mohitkumhar/fake-news-detection.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd fake-news-detection
   
3. **Install the Required Dependencies**:
   Make sure you have Python and pip installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask Application**:
   ```bash
   python app.py
   ```
5. **Open the Application**:
   Navigate to `http://localhost:5000` in your web browser to access the Fake News Detection interface.

## Model Training
The model was trained using a dataset containing true and fake news articles. The data was split into training and testing sets, and the `PassiveAggressiveClassifier` was used for classification. The model achieved high accuracy and was saved for real-time predictions in the web app.

## Dataset
The dataset used consists of two parts:
- **True.csv**: Contains legitimate news articles.
- **Fake.csv**: Contains fake news articles.

## Future Improvements
- Integration of more advanced models like Logistic Regression, Random Forest, or Deep Learning techniques.
- Addition of features like credibility scoring and article source verification.
- Extension of the system to handle multilingual news detection.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right corner of this page.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make Your Changes**: Add your improvements or features.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add some feature"
   ```
5. **Push to the Branch**:
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Create a Pull Request**: Open a pull request on this repository and describe your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Scikit-learn](https://scikit-learn.org/stable/) for machine learning tools.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) for web application framework.
- Dataset sources for providing real and fake news articles.
