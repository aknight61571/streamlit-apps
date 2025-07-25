import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(layout='wide', page_title='Opioid Cost Report', initial_sidebar_state='collapsed')
st.markdown("""
    <style>
        .element-container:has(.js-plotly-plot) + .element-container:has(.js-plotly-plot) {
            margin-top: -1rem; /* adjust this value as needed */
        }
    </style>
""", unsafe_allow_html=True)

# ─── Styling ──────────────────────────────────────────────────────────────────
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
        }
        .summary-header {
            font-size: 22px;
            font-weight: bold;
            border-bottom: 2px solid white;
            margin-bottom: 0.5rem;
        }
        .section-header {
            font-size: 20px;
            font-weight: bold;
            margin-top: 2rem;
        }
        .subtext {
            font-size: 14px;
            color: #cccccc;
            margin-bottom: 1rem;
        }
        .mini-header {
            font-size: 16px;
            font-weight: bold;
            margin-top: 0.5rem;
            margin-bottom: 0.25rem;
        }
        .mini-bullet {
            font-size: 14px;
            margin-left: 1rem;
            color: #cccccc;
        }
    </style>
""", unsafe_allow_html=True)

# ─── Summary ──────────────────────────────────────────────────────────────────
st.markdown('<div class="summary-header">Summary</div>', unsafe_allow_html=True)
col1, col2 = st.columns([3, 1], gap='medium')

with col1:
    st.markdown("""
    - Point 1: Something about cost trends  
    - Point 2: Something about member identification  
    """)
with col2:
    st.image("green_logo.png", use_container_width=True)

# ─── Section 1 ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">Linear Regression Analysis: Cost Next Quarter</div>', unsafe_allow_html=True)
# Regression Explanation (smaller font)
st.markdown("""
<div style="color:lightgray; font-size:14px">
<p>
Training data contains an <i>equal proportion of identified and unidentified plan members.<br>
Top and bottom 5% of costs removed to reduce skewness.</i> Adjusted R<sup>2</sup> indicates 68.3% of cost variation is explained by the model.
</p>
</div>
""", unsafe_allow_html=True)

# Jack Introduction (first part)
st.markdown("""
<div style="color:lightgray; font-size:16px">
<p><b>Linear Regression reveals the change in one variable associated with the change in other variables.</b><br><br>
<b><u>Imagine a 32-year-old plan member named Jack.</u></b><br>
Jack has <b>no OpioidRx-AI risk factors</b> and made <b>4 total medical/Rx transactions costing $250</b> to his insurer this quarter.<br>
<i>The model expects Jack's cost next quarter to be</i> <b><u>$298.71</u>. Update Jack's cost with cost indicators below.</b></p>
</div>
""", unsafe_allow_html=True)

# ─── Manual Scenario Builder ──────────────────────────────────────────────────

import pandas as pd

# Coefficients excluding removed vars
data = {
    'over_60': 124.2229,
    'under_2': 266.4056,
    'paid_300': 459.0998,
    'Paid Amount': 0.4311,
    'PharmaciesGT1': 783.9030,
    'RefillsGTEQ3': 380.9954,
    'PrescribersGT1': 523.5255,
    'BenzoCombo': 596.3844,
    'AntiPsychoticCombo': 1231.5529,
    'transaction_flag': 40.5988,
    'Age': 0.8920
}

rename = {
    'over_60': '60+ Years Old',
    'under_2': 'Under 2 Years Old',
    'paid_300': '$400+ Plan Spend (Current FQ)',
    'PharmaciesGT1': '2+ Opioid Pharmacies',
    'RefillsGTEQ3': '3+ Opioid Refills',
    'PrescribersGT1': '2+ Opioid Prescribers',
    'BenzoCombo': 'Opioid + Benzo',
    'AntiPsychoticCombo': 'AntiPsychotic + Opioid',
    'transaction_flag': '*n Transactions (Current FQ)',
    'Paid Amount': 'Paid Amount (Current FQ)',
    'Age': 'Age'
}

coef_series = pd.Series(data).rename(rename)

# Default values
defaults = {
    'Age': 32,
    '*n Transactions (Current FQ)': 4,
    'Paid Amount (Current FQ)': 250,
    '60+ Years Old': 'No',
    'Under 2 Years Old': 'No',
    '$400+ Plan Spend (Current FQ)': 'No',
    '2+ Opioid Pharmacies': 'No',
    '3+ Opioid Refills': 'No',
    '2+ Opioid Prescribers': 'No',
    'Opioid + Benzo': 'No',
    'AntiPsychotic + Opioid': 'No'
}

# Session state
for var in coef_series.index:
    if var not in st.session_state:
        st.session_state[var] = defaults.get(var, 0)

# Layout: Main graph on left (wider), interactive controls on right (narrower)
col1, col2 = st.columns([1.2, 0.8], gap='small')

with col1:
    fig = pio.read_json('cost_reg_coeffs_nolog.json')

    if hasattr(fig.data[0], 'y'):  # horizontal bar check
        var_names = fig.data[0].y
        colors = []
        for v in var_names:
            if v in ['60+ Years Old', 'Under 2 Years Old', '3+ Opioid Refills', 
                     '$400+ Plan Spend (Current FQ)', '2+ Opioid Prescribers', 
                     'Opioid + Benzo', '2+ Opioid Pharmacies', 'AntiPsychotic + Opioid']:
                # Binary variables - dark blue if Yes, light blue if No
                colors.append('#1E3A5F' if st.session_state.get(v, 'No') == 'Yes' else 'lightskyblue')
            else:
                # Numeric variables - dark blue if non-zero, light blue if zero
                colors.append('#1E3A5F' if st.session_state.get(v, 0) != 0 else 'lightskyblue')
        fig.data[0].marker.color = colors

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown('<div class="section-header">Interactive: Estimate Jack\'s Cost</div>', unsafe_allow_html=True)
    
    # Reset button
    if st.button("Reset Jack to Default"):
        for var, val in defaults.items():
            st.session_state[var] = val

    # Auto-update logic (before creating widgets)
    age = st.session_state.get('Age', 32)
    paid_amount = st.session_state.get('Paid Amount (Current FQ)', 250)
    
    # Auto-set age-related fields
    if age < 2:
        st.session_state['Under 2 Years Old'] = 'Yes'
    elif age >= 60:
        st.session_state['60+ Years Old'] = 'Yes'
    
    # Auto-set spend-related field
    if paid_amount >= 400:
        st.session_state['$400+ Plan Spend (Current FQ)'] = 'Yes'

    # Input layout: 2 inputs per row
    user_inputs = {}
    
    # Yes/No fields
    yes_no_fields = ['60+ Years Old', 'Under 2 Years Old', '3+ Opioid Refills', 
                     '$400+ Plan Spend (Current FQ)', '2+ Opioid Prescribers', 
                     'Opioid + Benzo', '2+ Opioid Pharmacies', 'AntiPsychotic + Opioid']
    
    # Integer fields (excluding Paid Amount which goes at the end)
    integer_fields = ['Age', '*n Transactions (Current FQ)']
    
    # Handle integer fields first (2 per row)
    for i in range(0, len(integer_fields), 2):
        cols = st.columns(2)
        for j, var in enumerate(integer_fields[i:i+2]):
            if i + j < len(integer_fields):
                with cols[j]:
                    st.number_input(var, key=var, step=1, format='%d')
                    user_inputs[var] = st.session_state[var]
    
    # Handle Yes/No fields (2 per row)
    for i in range(0, len(yes_no_fields), 2):
        cols = st.columns(2)
        for j, var in enumerate(yes_no_fields[i:i+2]):
            if i + j < len(yes_no_fields):
                with cols[j]:
                    st.selectbox(var, options=['No', 'Yes'], key=var)
                    user_inputs[var] = 1 if st.session_state[var] == 'Yes' else 0
    
    # Handle Paid Amount field at the bottom
    cols = st.columns(2)
    with cols[0]:
        st.number_input('Paid Amount (Current FQ)', key='Paid Amount (Current FQ)', step=1, format='%d')
        user_inputs['Paid Amount (Current FQ)'] = st.session_state['Paid Amount (Current FQ)']
    
    # Calculate prediction
    predicted_cost = sum(user_inputs[v] * coef_series[v] for v in coef_series.index)
    
    with cols[1]:
        # Display result next to Paid Amount field
        st.markdown(f"<div style='color:white; font-size:20px; margin-top:2rem;'><b><u>Expected Next Cost: ${predicted_cost:,.2f}</u></b></div>", unsafe_allow_html=True)

# Jack Scenario bullets (second part)
st.markdown("""
<ul style="color:lightgray; font-size:16px">
    <li>If Jack were flagged for <b><u>AntiPsychotic + Opioid</u></b> his expected next cost (<b><u>$1,530.27</u></b>) raises about as much as becoming <u>60 years old and needing $700 more in healthcare this quarter</u></li>
    <li>If Jack were flagged for <b><u>2+ Opioid Pharmacies</u></b> his expected next cost (<b><u>$1,082.62</u></b>) raises about <u>3× as much as becoming younger than 2 years old.</u></li>
    <li>If Jack were flagged for <b><u>Opioid + Benzo</u></b> his expected next cost (<b><u>$895.10</u></b>) raises about as much as <u>aging 35 years and needing 11 more transactions before next quarter</u></li>
</ul>

<div style="color:lightgray; font-size:16px">
<br><p><b>OPCM outreach removes all risk factors from 53% of members within 1 quarter</b> with a 0.17% reidentification rate</p>
</div>
""", unsafe_allow_html=True)

# ─── Provider Outreach Section ────────────────────────────────────────────────
st.markdown('<div class="section-header">Provider Outreach Prevents Exploding Costs</div>', unsafe_allow_html=True)
st.markdown("""
<div style="color:lightgray; font-size:16px">
<p>Opioid Clinical Management avoids contact with plan members in favor of direct contact with their high-risk providers.<br>
In the 6 fiscal quarters used, OPCM <u>removed all risk indicators after one quarter for <b>53%</b> of high-risk members.</u><br>
During the study, <b>99.83%</b> of flagged members remained low-risk after indicators were removed.</p>
</div>
""", unsafe_allow_html=True)

# Two graphs below, side by side at full size
col3, col4 = st.columns([1, 1], gap='small')

with col3:
    fig = pio.read_json('risk_factor_removal.json')
    st.plotly_chart(fig, use_container_width=True)

with col4:
    fig2 = pio.read_json('reg_cost_pmem.json')
    st.plotly_chart(fig2, use_container_width=True)
