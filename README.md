🥛 **DAIRY PULSE**
**AI-Based Dairy Demand Prediction System**

---

## 📌 Project Overview

**DAIRY PULSE** is a machine learning–based web application that predicts the demand for dairy products.
It uses historical data, price information, and seasonality to classify demand as **High** or **Low**.
An AI language model also explains the prediction in simple terms for better understanding.

This project is built using **Python, Streamlit, Machine Learning, and Hugging Face LLMs**.

---

## 🚀 Features

* 📊 Predicts **High or Low demand** for dairy products
* 🗓 Considers **month (seasonality)**
* 🥛 Supports **multiple dairy products**
* 💰 Includes **price impact** on demand
* 🧠 Generates **AI-based explanation** using LLaMA model
* 🎨 Attractive UI with **custom background image**

---

## 🧠 Technologies Used

* Python
* Streamlit (Frontend & UI)
* NumPy
* Joblib
* Scikit-learn (Model & preprocessing)
* Hugging Face Inference API
* Meta LLaMA 3 – 8B Instruct
* Base64 (for background image)

---

## 📂 Project Structure

```
DAIRY_PULSE/
│
├── app.py                     # Main Streamlit application
├── demand_model.pkl           # Trained ML model
├── month_encoder.pkl          # Label encoder for months
├── product_encoder.pkl        # Label encoder for dairy products
├── price_scaler.pkl           # Scaler for price feature
├── dairy_bg.jpeg              # Background image
├── requirements.txt           # Required Python libraries
├── README.md                  # Project documentation
```

---

## ⚙ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/dairy-pulse.git
cd dairy-pulse
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Hugging Face API Setup

This project uses Hugging Face for AI explanations.

1. Create an account on **Hugging Face**
2. Generate an **API token**
3. Add the token to **Streamlit secrets**

Create a file:

```
.streamlit/secrets.toml
```

Add:

```toml
HF_TOKEN = "your_huggingface_api_token"
```

---

## ▶ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser.

---

## 📊 How the Prediction Works

User selects:

* Month
* Dairy product
* Price per unit

Inputs are:

* Encoded using **label encoders**
* Scaled using a **price scaler**

ML model predicts:

* **High Demand** or **Low Demand**

AI model explains:

* Seasonality effect
* Pricing influence
* Consumer behavior

---

## 🧪 Sample Output

**Prediction:** 📈 High Demand

**AI Explanation:**
Demand is high because this product is commonly consumed during this season. The price is affordable, which encourages more customers to buy it. Seasonal habits and regular household usage increase demand.

---

## 🎯 Use Cases

* Dairy supply chain planning
* Inventory management
* Pricing strategy analysis
* Student projects in AI & ML
* FMCG demand forecasting

---

## 🔮 Future Enhancements

* Add demand quantity prediction
* Include weather data
* Product-wise sales visualization
* Mobile-friendly UI
* Multi-language AI explanations

---

## 👩‍💻 Author

**R Fathima Sulfikkar**
Data Analytics | AI & ML Enthusiast

---

## 📜 License

This project is for educational and academic purposes.

---

