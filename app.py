import google.generativeai as genai
import gradio as gr
import pickle
import pandas as pd
import PyPDF2
import re
import plotly.express as px
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)
# Load model
model = pickle.load(open("power_model.pkl", "rb"))
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------
# PDF Bill Analyzer
# -------------------------
def analyze_bill(pdf_file):

    try:
        text = ""

        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        units = re.findall(r"\d+\s*kWh", text)

        return f"""
📄 Electricity Bill Summary

Units Consumed:
{units[0] if units else "Not Found"}

Suggestions:
• Reduce AC usage
• Switch off unused devices
• Use LED lights
"""

    except Exception as e:
        return str(e)


# -------------------------
# Dashboard Graph
# -------------------------
def create_graph():

    df = pd.read_csv("dataset.csv")

    fig = px.scatter(
        df,
        x="TMAX",
        y="daily_consumption",
        title="Temperature vs Energy Consumption"
    )

    return fig


# -------------------------
# AI Assistant
# -------------------------
def ai_assistant(question):

    try:

        prompt = f"""
You are PowerGuard AI, an intelligent assistant for:

• Electricity consumption
• Power cut prediction
• Energy saving
• Renewable energy
• WFH and student productivity during outages

Rules:
1. Answer naturally like a chatbot.
2. Give concise and practical answers.
3. If the question is unrelated to electricity or energy, answer normally but briefly.
4. Use bullet points whenever appropriate.

User Question:
{question}

Answer:
"""

        response = gemini_model.generate_content(prompt)

        return response.text

    except Exception as e:
        return str(e)
# =========================
# Gradio App
# =========================

def predict_consumption(awnd, prcp, tmax, tmin):

    input_df = pd.DataFrame({
        "AWND":[awnd],
        "PRCP":[prcp],
        "TMAX":[tmax],
        "TMIN":[tmin]
    })

    prediction = model.predict(input_df)[0]

    return f"Predicted Consumption: {prediction:.2f} kWh"
with gr.Blocks() as demo:

    gr.Markdown("""
# ⚡ PowerGuard AI

### Smart Energy Consumption Prediction System
""")

    # Prediction Tab
    with gr.Tab("⚡ Prediction"):

        gr.Markdown("""
### 📌 Input Parameter Guide

- 🌬️ Wind Speed (AWND) → Average wind speed in m/s.
- 🌧️ Rainfall (PRCP) → Amount of rainfall in mm.
- 🌡️ Maximum Temperature (TMAX) → Highest temperature of the day in °C.
- ❄️ Minimum Temperature (TMIN) → Lowest temperature of the day in °C.
""")

        awnd = gr.Number(label="🌬️ Wind Speed (AWND)")
        prcp = gr.Number(label="🌧️ Rainfall (PRCP)")
        tmax = gr.Number(label="🌡️ Maximum Temperature (TMAX)")
        tmin = gr.Number(label="❄️ Minimum Temperature (TMIN)")
        awnd = gr.Number(
            label="🌬️ Wind Speed (AWND)",
            info="Average wind speed in m/s"
        )

        prcp = gr.Number(
            label="🌧️ Rainfall (PRCP)",
            info="Amount of rainfall in mm"
        )

        tmax = gr.Number(
            label="🌡️ Maximum Temperature (TMAX)",
            info="Highest temperature of the day in °C"
        )

        tmin = gr.Number(
            label="❄️ Minimum Temperature (TMIN)",
            info="Lowest temperature of the day in °C"
        )

        predict_btn = gr.Button("Predict")
        output1 = gr.Textbox(label="Prediction Result")

        predict_btn.click(
            predict_consumption,
            inputs=[awnd, prcp, tmax, tmin],
            outputs=output1
        )

    # Bill Analyzer Tab
    with gr.Tab("📄 Bill Analyzer"):

        pdf_input = gr.File(label="Upload Electricity Bill PDF")
        analyze_btn = gr.Button("Analyze")
        output2 = gr.Textbox(label="Bill Summary")

        analyze_btn.click(
            analyze_bill,
            inputs=pdf_input,
            outputs=output2
        )

    # Dashboard Tab
    with gr.Tab("📊 Dashboard"):

        graph_btn = gr.Button("Show Graph")
        graph_output = gr.Plot()

        graph_btn.click(
            create_graph,
            outputs=graph_output
        )

    # AI Assistant Tab
    with gr.Tab("🤖 AI Assistant"):

        question = gr.Textbox(label="Ask PowerGuard AI")
        ask_btn = gr.Button("Ask")
        answer = gr.Textbox(label="Response")

        ask_btn.click(
            ai_assistant,
            inputs=question,
            outputs=answer
        )

demo.launch(share=True)