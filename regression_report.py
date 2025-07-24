import streamlit as st
import plotly.graph_objects as go
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
st.markdown('<div class="section-header">Regression Analysis: Cost Next Quarter</div>', unsafe_allow_html=True)
# Regression Explanation (smaller font)
st.markdown("""
<div style="color:lightgray; font-size:14px">
<p>
Training data contains an <i>equal proportion of identified and unidentified plan members.</i> See <u>Model Card</u> for info on regression & modeling techniques<br>
</p>
</div>
""", unsafe_allow_html=True)

# Jack Scenario (font-size:16px to match bullet section)
st.markdown("""
<div style="color:lightgray; font-size:16px">
<p><b><u>Imagine a 32-year-old plan member named Jack, who changes age at will.</u></b><br>
Jack has <b>no OpioidRx-AI risk factors</b> and made <b>4 total medical/Rx transactions costing $250</b> to his insurer this quarter.<br>
<i>The model expects Jack's cost next quarter to be</i> <b><u>$295.98</u></b></p>
</div>

<ul style="color:lightgray; font-size:16px">
    <li>If Jack were flagged for <b><u>Opioid + Antipsychotic</u></b> his expected next cost (<b><u>$1,527.53</u></b>) raises about as much as becoming <u>60 years old and needing $700 more in healthcare this quarter</u></li>
    <li>If Jack were flagged for <b><u>2+ Opioid Pharmacies</u></b> his expected next cost (<b><u>$1,079.88</u></b>) raises about <u>3× as much as becoming younger than 2 years old.</u></li>
    <li>If Jack were flagged for <b><u>Opioid + Benzo</u></b> his expected next cost (<b><u>$892.36</u></b>) raises about as much as <u>aging 35 years and needing 11 more transactions before next quarter</u></li>
</ul>

<div style="color:lightgray; font-size:16px">
<br><p><b>OPCM outreach removes all risk factors from 53% of members within 1 quarter</b> with a 0.17% reidentification rate.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap='small')

with col1:
    fig = pio.read_json('cost_reg_coeffs_nolog.json')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = pio.read_json('risk_factor_removal.json')
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True)

    fig2 = pio.read_json('reg_cost_pmem.json')
    fig2.update_layout(height=350)
    st.plotly_chart(fig2, use_container_width=True)


# ─── Section 2 ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">Section 2</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Section 2 summary... </div>', unsafe_allow_html=True)

col3, col4 = st.columns([1, 1], gap='medium')

with col3:
    # fig = joblib.load('reg_cost_pmem.pkl')
    # st.plotly_chart(fig, use_container_width=True)
    st.markdown('Some text goes here...')

with col4:
    fig = pio.read_json('reg_sph.json')
    st.plotly_chart(fig, use_container_width=True)
