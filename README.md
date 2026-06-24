# ⚡ PowerGuard AI

## Smart Energy Consumption Forecasting and Alert System

PowerGuard AI is an intelligent energy consumption prediction system that helps users estimate daily electricity consumption based on weather conditions and historical patterns. The system promotes efficient energy usage and supports sustainable development goals.

---

## 🌍 Sustainable Development Goals (SDGs)

- ✅ SDG 7 – Affordable and Clean Energy
- ✅ SDG 9 – Industry, Innovation and Infrastructure
- ✅ SDG 11 – Sustainable Cities and Communities

---

## 🚀 Features

- ⚡ Daily Energy Consumption Prediction
- 🌡 Weather-based Forecasting
- 📊 Consumption Status Classification
- 🟢 Low Consumption
- 🟡 Moderate Consumption
- 🔴 High Consumption
- 📈 Interactive Web Interface using Gradio
- 🤖 Machine Learning Model using Random Forest Regressor

---

## 🛠 Tech Stack

### Frontend
- Gradio

### Backend
- Python

### Machine Learning
- Scikit-Learn
- Random Forest Regressor

### Data Processing
- Pandas
- NumPy

### Visualization
- Matplotlib
- Plotly

### Development Environment
- Google Colab

---

## 📁 Project Structure

```text
PowerGuard_AI
│
├── data
│     dataset.csv
│
├── model
│     power_model.pkl
│
├── notebook
│     powercut_web.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── images
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/PowerGuard_AI.git
```

Move into the project directory:

```bash
cd PowerGuard_AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## 📊 Input Parameters

| Feature | Description |
|-----------|------------|
| AWND | Wind Speed |
| PRCP | Precipitation |
| TMAX | Maximum Temperature |
| TMIN | Minimum Temperature |
| Year | Current Year |
| Month | Month |
| Day | Day |
| DayOfWeek | Day of Week |

---

## 📈 Output

Predicted Daily Consumption (kWh)

Consumption Status:

- 🟢 Low Consumption
- 🟡 Moderate Consumption
- 🔴 High Consumption

---

## 🤖 Machine Learning Model

Model Used:

Random Forest Regressor

Evaluation Metric:

R² Score

---

## 🔮 Future Enhancements

- 📄 PDF Bill Upload and Analysis
- 🔍 Entity Extraction
- 📝 Automatic Summarization
- 🧠 Retrieval-Augmented Generation (RAG)
- 📊 Advanced Analytics Dashboard
- 🌐 Deployment using Hugging Face Spaces

---

## 👨‍💻 Author

Developed using Python, Gradio and Machine Learning.

---

## ⭐ If you like this project, don't forget to star the repository!