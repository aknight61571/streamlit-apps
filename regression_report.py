import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Dark Report Demo",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Custom Styles ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: white;
    }
    .section-text {
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 0.5rem;
    }
    .footnote {
        font-size: 13px;
        color: #cccccc;
        margin-top: 0.5rem;
    }
    .footnote b {
        color: #ffffff;
    }
    .footnote i {
        color: #aaaaaa;
    }
    .divider {
        margin: 3rem 0;
        border-top: 1px solid rgba(255, 255, 255, 0.2);
    }
    .summary-box {
        background-color: rgba(30, 144, 255, 0.1);
        border-left: 4px solid deepskyblue;
        padding: 1rem;
        margin-bottom: 2rem;
        border-radius: 0 4px 4px 0;
    }
    .summary-item {
        margin-bottom: 0.5rem;
        padding-left: 0.5rem;
    }
    .summary-box b {
        color: deepskyblue;
        display: block;
        margin-bottom: 0.75rem;
        font-size: 18px;
    }
    .summary-item a i {
        font-style: italic;
        text-decoration: underline;
        color: deepskyblue !important;
    }
    .summary-item a:hover i {
        color: lightskyblue !important;
    }
    .section-anchor {
        display: block;
        position: relative;
        top: -100px;
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ─── Summary Section ──────────────────────────────────────────────────────────
st.markdown("""
<div class="summary-box">
    <div class="section-text">
        <b>Summary</b>
    </div>
    <div class="summary-item">1. Opioid use causes stress, which degrades physical health and productivity. Construction workers are much more likely to use opioids.</div>
    <div class="summary-item">2. Interruption of OpioidRx-AI service increases frequency of opioid use among employees. <a href="#case-study"><i><u>Jump to 2</u></i></a></div>
    <div class="summary-item">3. OpioidRx-AI ameliorates risky behavior in both identified providers and members. <a href="#provider-outcomes"><i><u>Jump to 3</u></i></a></div>
    <div class="summary-item">4. Employees identified by OpioidRx-AI are expensive to insure. OPCM drastically lowers costs by the next quarter. <a href="#financial-cost"><i><u>Jump to 4</u></i></a></div>
</div>
""", unsafe_allow_html=True)

# ─── Purpose Section (Replaces Linear Regression Analysis Header) ─────────────
st.markdown("### Purpose")
st.markdown("""
<div class="section-text">
    OPCM esitmates 2% of a given healthcare plan's membership consists of high-risk opioid users and individuals going through withdrawal. 
    These members face health risks and soaring medical expenses. OPCM targets the providers of those members to ensure CDC adherence, 
    improve employee health, and reduce healthcare costs.
</div>
""", unsafe_allow_html=True)

# (Remaining code unchanged...)


# ─── Manual Scenario Builder ──────────────────────────────────────────────────

# New coefficients for log(y) ~ X model (no intercept)
data = {
    'Antipsychotic + Opioid': 0.662145,
    'Pain Med: WD': 0.531860,
    'Anxiolitic: WD': 0.381204,
    'Benzo + Opioid': 0.301535,
    '3+ Opioid Refills': 0.269436,
    '$300+ Plan Spend(This Quarter)': 0.233119,
    'Digestive/Miscellaneous: WD': 0.163909,
    '2+ Opioid Pharmacies': 0.106364,
    'Age': 0.090110,
    '50-100 mg Morphine Equivalent': 0.030856,
    'n Transactions(This Quarter)': 0.016391,
    '2+ Opioid Prescribers': 0.002064,
    'Plan Spend(This Quarter)': 0.000393
}
coef_series = pd.Series(data)

# Default values
defaults = {
    'Age': 32,
    'n Transactions(This Quarter)': 4,
    'Plan Spend(This Quarter)': 250,
    '$300+ Plan Spend(This Quarter)': 'No',
    '2+ Opioid Pharmacies': 'No',
    '3+ Opioid Refills': 'No',
    '2+ Opioid Prescribers': 'No',
    'Benzo + Opioid': 'No',
    'Antipsychotic + Opioid': 'No',
    'Pain Med: WD': 'No',
    'Anxiolitic: WD': 'No',
    'Digestive/Miscellaneous: WD': 'No',
    '50-100 mg Morphine Equivalent': 'No'
}

# Session state init for regressors
for var in coef_series.index:
    if var not in st.session_state:
        if var == 'Age':
            st.session_state[var] = 32
        elif var == 'n Transactions(This Quarter)':
            st.session_state[var] = 4
        elif var == 'Plan Spend(This Quarter)':
            st.session_state[var] = 250
        else:
            st.session_state[var] = 'No'

# Additional session state
if 'member_type' not in st.session_state:
    st.session_state['member_type'] = 'High Risk'
if 'member_toggle' not in st.session_state:
    st.session_state['member_toggle'] = None
if 'sort_by' not in st.session_state:
    st.session_state['sort_by'] = 'None'
if 'last_loaded_member' not in st.session_state:
    st.session_state['last_loaded_member'] = None

# Load datasets
@st.cache_data
def load_datasets():
    try:
        opc_data = pd.read_csv('reg_report_opc_rows_deets.csv')
        wd_data = pd.read_csv('reg_report_wd_rows_deets.csv')
        normal_data = pd.read_csv('reg_report_normal_rows_deets.csv')
        return {'High Risk': opc_data, 'Withdrawal': wd_data, 'Regular': normal_data}
    except Exception:
        empty_df = pd.DataFrame()
        return {'High Risk': empty_df, 'Withdrawal': empty_df, 'Regular': empty_df}

datasets = load_datasets()

# Helper lists
yes_no_fields = ['3+ Opioid Refills', '$300+ Plan Spend(This Quarter)', '2+ Opioid Prescribers',
                 'Benzo + Opioid', '2+ Opioid Pharmacies', 'Antipsychotic + Opioid',
                 'Pain Med: WD', 'Anxiolitic: WD', 'Digestive/Miscellaneous: WD',
                 '50-100 mg Morphine Equivalent']

# Define sort options based on member type
sort_options = {
    'Withdrawal': ['None', 'Pain Med: WD', 'Anxiolitic: WD', 'Digestive/Miscellaneous: WD'],
    'High Risk': ['None', 'Antipsychotic + Opioid', 'Benzo + Opioid', '3+ Opioid Refills', '2+ Opioid Pharmacies', '50-100 mg Morphine Equivalent'],
    'Regular': ['None', 'Age', 'n Transactions(This Quarter)', 'Plan Spend(This Quarter)']
}

# Get current sort options based on member type
current_member_type = st.session_state.get('member_type', 'High Risk')
current_sort_options = sort_options.get(current_member_type, ['None'])

# Reset sort_by if it's not in current options
if st.session_state.get('sort_by') not in current_sort_options:
    st.session_state['sort_by'] = 'None'

# Apply sorting to the current dataset based on sort_by selection
current_dataset = datasets.get(st.session_state.get('member_type', 'High Risk'), pd.DataFrame())
if not current_dataset.empty and st.session_state.get('sort_by') != 'None' and st.session_state.get('sort_by') in current_dataset.columns:
    sort_col = st.session_state['sort_by']
    
    # Check if the column is binary (contains only 0s and 1s, or Yes/No)
    unique_vals = current_dataset[sort_col].dropna().unique()
    is_binary = (set(unique_vals).issubset({0, 1, '0', '1'}) or 
                 set(unique_vals).issubset({'Yes', 'No'}) or
                 len(unique_vals) <= 2)
    
    if is_binary:
        # For binary columns, sort with 1s (or 'Yes') first
        if set(unique_vals).issubset({'Yes', 'No'}):
            current_dataset = current_dataset.sort_values(sort_col, key=lambda x: x.map({'Yes': 0, 'No': 1}))
        else:
            current_dataset = current_dataset.sort_values(sort_col, ascending=False)
    else:
        # For continuous columns, sort descending
        current_dataset = current_dataset.sort_values(sort_col, ascending=False)

# Make union list of toggles across all datasets (for Member dropdown)
if any(not d.empty for d in datasets.values()):
    all_toggles = pd.concat([d[['toggle']] for d in datasets.values() if not d.empty], ignore_index=True)['toggle']\
        .dropna().astype(str).unique().tolist()
    all_toggles = sorted(all_toggles)
else:
    all_toggles = []

# Update the member dropdown to show sorted toggles from current dataset
if not current_dataset.empty and 'toggle' in current_dataset.columns:
    current_toggles = current_dataset['toggle'].dropna().astype(str).tolist()
    # Keep the full list but prioritize current dataset's sorted order
    all_toggles = current_toggles + [t for t in all_toggles if t not in current_toggles]

# ─── Load selected member (by `toggle`) BEFORE computing prediction ──────────
member_row = None
actual_cost = 0.0
sel_toggle = st.session_state.get('member_toggle')
if sel_toggle is not None:
    for _name, df in datasets.items():
        if not df.empty and 'toggle' in df.columns:
            sub = df[df['toggle'].astype(str) == str(sel_toggle)]
            if not sub.empty:
                member_row = sub.iloc[0]
                break

# Only load member data if it's a new selection (prevents overwriting manual changes)
if member_row is not None and st.session_state.get('last_loaded_member') != sel_toggle:
    # Update the last loaded member tracker
    st.session_state['last_loaded_member'] = sel_toggle
    
    # Push member values into session_state
    for var in coef_series.index:
        if var in member_row.index:
            value = member_row[var]
            if var in yes_no_fields:
                st.session_state[var] = 'Yes' if value in [1, 'Yes', True] else 'No'
            else:
                st.session_state[var] = int(value) if pd.notna(value) else 0

# Always get actual cost if member is selected (for display purposes)
if member_row is not None and 'actual' in member_row.index and pd.notna(member_row['actual']):
    try:
        actual_cost = float(member_row['actual'])
    except Exception:
        actual_cost = 0.0

# Reset tracker when no member is selected
if sel_toggle is None:
    st.session_state['last_loaded_member'] = None

# Auto-set spend-related field based on $300+ threshold (after member load)
plan_spend_val = st.session_state.get('Plan Spend(This Quarter)', 250)
st.session_state['$300+ Plan Spend(This Quarter)'] = 'Yes' if plan_spend_val >= 300 else 'No'

# Build inputs from session state and compute prediction
user_inputs = {}
for v in coef_series.index:
    if v in yes_no_fields:
        user_inputs[v] = 1 if st.session_state.get(v, 'No') == 'Yes' else 0
    else:
        user_inputs[v] = st.session_state.get(v, 0)

log_predicted_cost = float(sum(user_inputs[v] * coef_series[v] for v in coef_series.index))
predicted_cost = float(np.expm1(log_predicted_cost))

# ─── Layout: Left = Filters + Costs + Graph | Right = Controls ───────────────
col1, col2 = st.columns([1.2, 0.8], gap='small')

with col1:
    # Filters and Member buttons in one row (tinted container)
    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    f1, f2, f3 = st.columns(3)
    with f1:
        st.selectbox("Rx-AI Criteria", options=['High Risk', 'Withdrawal', 'Regular'],
                     key='member_type', help="Choose the risk group")
    with f2:
        st.selectbox("Sort by", options=current_sort_options, key='sort_by')
    with f3:
        st.selectbox("Member", options=all_toggles, key='member_toggle',
                     help="Select by unique 'toggle' id (from any dataset)")
    st.markdown('</div>', unsafe_allow_html=True)

    # Expected & Actual cost (beneath filters, above graph)
    st.markdown(
        f"<div style='color:white; font-size:20px; margin-top:0.2rem;'><b><u>Expected Cost (Next FQ): ${predicted_cost:,.2f}</u></b></div>",
        unsafe_allow_html=True)
    st.markdown(
        f"<div style='color:lightblue; font-size:18px; margin-bottom:0.3rem;'><b>Actual Cost (Next FQ): ${actual_cost:,.2f}</b></div>",
        unsafe_allow_html=True)

    # Regression coefficients graph (colored by current param state)
    fig = pio.read_json('cost_reg_coeffs_nolog.json')
    if hasattr(fig.data[0], 'y'):
        var_names = fig.data[0].y
        colors = []
        for v in var_names:
            if v in yes_no_fields:
                colors.append('#1E3A5F' if st.session_state.get(v, 'No') == 'Yes' else 'lightskyblue')
            else:
                colors.append('#1E3A5F' if st.session_state.get(v, 0) != 0 else 'lightskyblue')
        fig.data[0].marker.color = colors
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Add spacing to align Regression Parameters header with Actual Cost line
    st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)
    
    # Parameter controls (right side)
    st.markdown('<div class="section-header">Regression Parameters</div>', unsafe_allow_html=True)

    # Numeric inputs
    ncol1, ncol2 = st.columns(2)
    with ncol1:
        st.number_input('Age', key='Age', step=1, format='%d', min_value=0)
    with ncol2:
        st.number_input('n Transactions(This Quarter)', key='n Transactions(This Quarter)', step=1, format='%d', min_value=0)

    ncol3, _ = st.columns(2)
    with ncol3:
        st.number_input('Plan Spend(This Quarter)', key='Plan Spend(This Quarter)', step=1, format='%d', min_value=0)

    # Yes/No fields (two per row) - rearranged to put empty space in bottom right
    # We have 10 yes/no fields, so we'll do 5 rows of 2 columns each
    yes_no_pairs = [
        ['3+ Opioid Refills', '$300+ Plan Spend(This Quarter)'],
        ['2+ Opioid Prescribers', 'Benzo + Opioid'],
        ['2+ Opioid Pharmacies', 'Antipsychotic + Opioid'],
        ['Pain Med: WD', 'Anxiolitic: WD'],
        ['Digestive/Miscellaneous: WD', '50-100 mg Morphine Equivalent']
    ]
    
    for pair in yes_no_pairs:
        row = st.columns(2)
        for j, var in enumerate(pair):
            with row[j]:
                st.selectbox(var, options=['No', 'Yes'], key=var)

# ─── Jack Scenario Bullets ───────────────────────────────────────────────────
st.markdown("""
<ul style="color:lightgray; font-size:16px">
    <li>If Jack were flagged for <b><u>Antipsychotic + Opioid</u></b> his expected next cost raises significantly due to the highest risk coefficient</li>
    <li>If Jack were flagged for <b><u>2+ Opioid Pharmacies</u></b> his expected next cost increases substantially</li>
    <li>If Jack were flagged for <b><u>Benzo + Opioid</u></b> his expected next cost shows moderate elevation</li>
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

# ─── Two Graphs ──────────────────────────────────────────────────────────────
col3, col4 = st.columns([1, 1], gap='small')
with col3:
    fig_a = pio.read_json('risk_factor_removal.json')
    st.plotly_chart(fig_a, use_container_width=True)
with col4:
    fig_b = pio.read_json('reg_cost_pmem.json')
    st.plotly_chart(fig_b, use_container_width=True)

