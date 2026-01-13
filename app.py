import streamlit as st
import joblib
import numpy as np
import base64
from huggingface_hub import InferenceClient

# ==========================
# Background image function
# ==========================
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ==========================
# Apply background
# ==========================
set_bg("Dairyplus.bg.png.jpg")

# ==========================
# Load ML artifacts
# ==========================
demand_model = joblib.load("demand_model.pkl")
month_encoder = joblib.load("month_encoder.pkl")
product_encoder = joblib.load("product_encoder.pkl")
price_scaler = joblib.load("price_scaler.pkl")

# ==========================
# Hugging Face LLM Client
# ==========================
hf_client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=st.secrets["HF_TOKEN"]
)

# ==========================
# UI
# ==========================
st.set_page_config(page_title="DAIRY PULSE", layout="centered")

st.title("🥛 DAIRY PULSE")
st.markdown(
    "<h4 style='color:white;'>AI-based Dairy Demand Prediction System</h4>",
    unsafe_allow_html=True
)

# ==========================
# Sidebar Inputs
# ==========================
st.sidebar.header("Input Parameters")

month = st.sidebar.selectbox(
    "Select Month",
    month_encoder.classes_.tolist()
)

product = st.sidebar.selectbox(
    "Select Dairy Product",
    product_encoder.classes_.tolist()
)

price = st.sidebar.slider(
    "Price per Unit (₹)",
    min_value=10,
    max_value=500,
    value=50
)

# ==========================
# Prediction + LLM Explanation
# ==========================
if st.sidebar.button("Predict Demand"):

    # Encode inputs
    month_encoded = month_encoder.transform([month])[0]
    product_encoded = product_encoder.transform([product])[0]
    price_scaled = price_scaler.transform([[price]])[0][0]

    X_input = np.array([[month_encoded, product_encoded, price_scaled]])

    # ML prediction
    prediction = demand_model.predict(X_input)[0]
    demand_label = "High" if prediction == 1 else "Low"

    # Display result
    st.subheader("📊 Prediction Result")
    if demand_label == "High":
        st.success("📈 High Demand")
    else:
        st.warning("📉 Low Demand")

    # ==========================
    # LLM Explanation Prompt
    # ==========================
    prompt = f"""
    A dairy demand prediction system predicted {demand_label.lower()} demand.

    Month: {month}
    Dairy product: {product}
    Price per unit: ₹{price}

    Explain the demand prediction in 3 to 4 simple sentences.
    Consider seasonality, pricing, and consumer behavior.
    Use clear and student-friendly language.
    """

    with st.spinner("Generating AI explanation..."):
        response = hf_client.chat_completion(
            messages=[
                {"role": "system", "content": "You are a friendly AI assistant that explains demand predictions in simple language."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=120,
            temperature=0.6
        )

    explanation = response.choices[0].message["content"]

    st.subheader("🧠 AI Explanation")
    st.info(explanation)