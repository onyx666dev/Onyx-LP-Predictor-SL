import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Linear Regression Predictor",
    page_icon="📊",
    layout="centered"
)

# Custom CSS for styling with button colors and height
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #333;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .signature {
        text-align: center;
        color: #999;
        font-size: 0.9em;
        font-style: italic;
        margin-top: 50px;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 1.5em;
        font-weight: bold;
        margin: 20px 0;
    }
    .success-box {
        background-color: #e8f5e9;
        color: #4CAF50;
    }
    .error-box {
        background-color: #ffebee;
        color: #f44336;
    }
    
    /* Standardize ALL button heights and styling */
    .stButton > button {
        height: 80px;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        white-space: pre-line;
    }
    
    /* Color each button by their key attribute */
    button[kind="secondary"] {
        color: white !important;
    }
    
    /* Target buttons by their position in the container */
    div[data-testid="column"] > div > div > div > div:nth-child(1) button {
        background-color: #4CAF50 !important;
        color: white !important;
    }
    
    div[data-testid="column"] > div > div > div > div:nth-child(3) button {
        background-color: #2196F3 !important;
        color: white !important;
    }
    
    div[data-testid="column"] > div > div > div > div:nth-child(5) button {
        background-color: #FF9800 !important;
        color: white !important;
    }
    
    /* Hover effects */
    div[data-testid="column"] > div > div > div > div:nth-child(1) button:hover {
        background-color: #45a049 !important;
    }
    
    div[data-testid="column"] > div > div > div > div:nth-child(3) button:hover {
        background-color: #0b7dda !important;
    }
    
    div[data-testid="column"] > div > div > div > div:nth-child(5) button:hover {
        background-color: #e68900 !important;
    }
</style>
""", unsafe_allow_html=True)

# Load models function
@st.cache_resource
def load_models():
    models = {}
    try:
        with open('simple.pkl', 'rb') as f:
            models['simple'] = pickle.load(f)
    except:
        models['simple'] = None
    
    try:
        with open('polynomial_transformer.pkl', 'rb') as f:
            models['poly_transformer'] = pickle.load(f)
        with open('linear_model.pkl', 'rb') as f:
            models['poly_lin_reg'] = pickle.load(f)
    except:
        models['poly_transformer'] = None
        models['poly_lin_reg'] = None
    
    try:
        with open('model.pkl', 'rb') as f:
            models['multiple'] = pickle.load(f)
    except:
        models['multiple'] = None
    
    return models

# Load all models
models = load_models()

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'menu'

# Navigation functions
def go_to_menu():
    st.session_state.page = 'menu'

def go_to_simple():
    st.session_state.page = 'simple'

def go_to_polynomial():
    st.session_state.page = 'polynomial'

def go_to_multiple():
    st.session_state.page = 'multiple'

# Main Menu Page
if st.session_state.page == 'menu':
    st.markdown('<div class="main-title">📊 Linear Regression Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Select a regression type to make predictions</div>', unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # Centered buttons with fixed width
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Button 1: Simple Linear Regression (GREEN)
        if st.button("🎓 Simple Linear Regression\n(Study Hours → Marks)", key="simple_btn", use_container_width=True):
            if models['simple'] is None:
                st.error("❌ simple.pkl model file not found!")
            else:
                go_to_simple()
                st.rerun()
        
        st.write("")
        
        # Button 2: Polynomial Regression (BLUE)
        if st.button("📈 Polynomial Regression\n(Level → Salary)", key="poly_btn", use_container_width=True):
            if models['poly_transformer'] is None or models['poly_lin_reg'] is None:
                st.error("❌ polynomial_transformer.pkl or linear_model.pkl file not found!")
            else:
                go_to_polynomial()
                st.rerun()
        
        st.write("")
        
        # Button 3: Multiple Linear Regression (ORANGE)
        if st.button("💼 Multiple Linear Regression\n(Startup Profit Prediction)", key="multiple_btn", use_container_width=True):
            if models['multiple'] is None:
                st.error("❌ model.pkl model file not found!")
            else:
                go_to_multiple()
                st.rerun()
    
    st.markdown('<div class="signature">@ ONYX PYTHON 2ND APP | 2025</div>', unsafe_allow_html=True)

# Simple Linear Regression Page
elif st.session_state.page == 'simple':
    st.markdown("### 🎓 Predict Marks from Study Hours")
    st.write("")
    
    hours = st.number_input("Study Hours (1-10):", min_value=1.0, max_value=10.0, value=5.0, step=0.1)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔮 Predict", key="predict_simple", use_container_width=True):
            if hours >= 1 and hours <= 10:
                marks = models['simple'].predict([[hours]])
                st.markdown(f'<div class="result-box success-box">Predicted Marks: {int(marks[0])}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="result-box error-box">Please enter hours between 1 and 10</div>', unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    if st.button("← Back to Menu", key="back_simple"):
        go_to_menu()
        st.rerun()

# Polynomial Regression Page
elif st.session_state.page == 'polynomial':
    st.markdown("### 📈 Predict Salary from Level")
    st.write("")
    
    level = st.number_input("Level:", min_value=1, max_value=20, value=5, step=1)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔮 Predict", key="predict_poly", use_container_width=True):
            try:
                level_poly = models['poly_transformer'].transform([[level]])
                predict_sal = models['poly_lin_reg'].predict(level_poly)
                st.markdown(f'<div class="result-box success-box">Predicted Salary: ${int(predict_sal[0]):,}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="result-box error-box">Error: {str(e)}</div>', unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    if st.button("← Back to Menu", key="back_poly"):
        go_to_menu()
        st.rerun()

# Multiple Linear Regression Page
elif st.session_state.page == 'multiple':
    st.markdown("### 💼 Startup Profit Prediction")
    st.write("")
    
    california = st.selectbox("California:", [0, 1], index=0)
    newyork = st.selectbox("New York:", [0, 1], index=0)
    florida = st.selectbox("Florida:", [0, 1], index=0)
    rd = st.number_input("R&D Spend ($):", min_value=0, value=100000, step=1000)
    admin = st.number_input("Administration Spend ($):", min_value=0, value=100000, step=1000)
    marketing = st.number_input("Marketing Spend ($):", min_value=0, value=100000, step=1000)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔮 Predict", key="predict_multiple", use_container_width=True):
            try:
                user_input = {
                    'california': california,
                    'newyork': newyork,
                    'florida': florida,
                    'rd': rd,
                    'admin': admin,
                    'marketing': marketing
                }
                
                user_data = pd.DataFrame(user_input, index=[0])
                prediction = models['multiple'].predict(user_data)
                
                st.markdown(f'<div class="result-box success-box">Predicted Profit: ${int(prediction[0]):,}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="result-box error-box">Error: {str(e)}</div>', unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    if st.button("← Back to Menu", key="back_multiple"):
        go_to_menu()
        st.rerun()
