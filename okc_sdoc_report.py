import streamlit as st
import base64
import plotly.io as pio
import pandas as pd
import numpy as np
# Page config
st.set_page_config(page_title="Marketing Report", layout="wide")

# Dark theme + box styles
st.markdown(
    """
    <style>
        body {
            background-color: #0E1117;
            color: white;
        }
        .section-header {
            font-size: 28px;
            font-weight: bold;
            border-bottom: 2px solid white;
            padding-bottom: 5px;
            margin-bottom: 10px;
        }
        .bullet-list li {
            font-size: 18px;
            margin-bottom: 5px;
        }
        .box {
            background-color: #4A4A4A;  /* medium-light grey */
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 220px;
        }
        .box img {
            max-width: 80px;
            height: auto;
        }
        .combo {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
        }
        .box-text {
            font-weight: bold;
            margin-top: 15px;
            font-size: 16px;
            text-align: center;
        }
        .plus-sign {
            font-size: 28px;
            font-weight: bold;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HEADER SECTION ---
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("<div class='section-header'>Objective</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <ul class='bullet-list'>
            <li>Explain OPCM Indicators</li>
            <li>Explain Provider Outreach</li>
            <li>Explain Benefits</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.image("green_logo.png", use_container_width=True)

# --- FIRST TEXT SECTION ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>What Are OPCM Indicators?</div>", unsafe_allow_html=True)

# --- FOUR BOXES ---
colA, colB, colC, colD = st.columns(4)

# Add this function at the top of your file
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Then use it like this:
with colA:
    pills_base64 = get_base64_image("gray_pill_bottle.png")
    st.markdown(
        f"""
        <div class="box">
            <img src="data:image/png;base64,{pills_base64}" />
            <div class="box-text">50+ mg Morphine Equivalent</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with colB:
    st.markdown(
        f"""
        <div class="box">
            <div class="combo">
                <img src="data:image/png;base64,{pills_base64}" />
                <div class="plus-sign">+</div>
                <img src="data:image/png;base64,{pills_base64}" />
            </div>
            <div class="box-text">Opioid + Benzodiazepine</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with colC:
    doc_base64 = get_base64_image("gray_doctor.png")
    st.markdown(
        f"""
        <div class="box">
            <div class="combo">
                <img src="data:image/png;base64,{doc_base64}" />
                <div class="plus-sign">+</div>
                <img src="data:image/png;base64,{doc_base64}" />
            </div>
            <div class="box-text">2+ Opioid Prescribers</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with colD:
    pharm_base64 = get_base64_image("gray_pharmacy.png")
    st.markdown(
        f"""
        <div class="box">
            <div class="combo">
                <img src="data:image/png;base64,{pharm_base64}" />
                <div class="plus-sign">+</div>
                <img src="data:image/png;base64,{pharm_base64}" />
            </div>
            <div class="box-text">2+ Opioid Pharmacies</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown(
    """
    <br>
    <br>
    OPCM's innovative <i>OpioidRx-AI</i> model is trained to evaluate opioid-related risk based on CDC-researched indicators including, but not limited to, those above.<br>
    When risk reaches a pre-set threshold, OPCM pharmacist contact their precribers directly. <br><br>
    Such members exceeding the threshold(flagged) carry direct financial impacts due to coverage expense and delayed financial impacts due to abenteeism and presenteeism.
    <br> <u>Outlier threshold is the maximum cost without being considered a financial outlier.</u>
    <br><br>""",
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([16.5, 67, 16.5])
with col2:
    st.image("okc_cost_of_ident.png", use_container_width=True)

st.header("OPCM Outreach")

col1, col2, col3 = st.columns([5, 90, 5])
with col2:
    st.image("Flowchart.svg", use_container_width=True)

st.write("""All prescribers who wrote an opioid Rx for a plan member identified by OpioidRx-Ai receive communication from OPCM pharmacists.
<li>Prescribers for members with <90 continuous days of an opioid recieve a letter stating the employer has adopted CDC prescribing guidelines for opioid prescriptions.
<li> Prescribers for members with >90 continuous days of an opioid recieve a personal call in addition to this letter, informing them of current CDC guidelines and verifying their intent to adhere.

The quality of OPCM's outreach ensures that a large portion of high-risk cohorts are considered low-risk by the following fiscal quarter..
""")

col1, col2 = st.columns([67, 33])
with col1:
    fig = pio.read_json('risk_factor_removal.json')
    st.plotly_chart(fig,use_container_width=True)
with col2:
    st.header('Why is OPCM an Ongoing Service?')
    st.write('''Unfortunately, it's not as simple as contacting providers once to resolve the issue.
    <br><br>Even under OPCM supervision, roughly <b>40% of a quarterly identified cohort is made of newly identified members.</b><br><br>
    This is due to a number of reasons, including:
    <li> Naturally arising conditions warranting extended opioid use
    <li> Appearance of new providers not following CDC guidelines
    <br>
    ''',unsafe_allow_html=True
    )        
col1, col2 = st.columns([33, 67])
with col2:
    st.image('qident_qafter.png',use_container_width=True)

with col1:
    st.header('Exploding Costs in High-Risk Members')
    st.write('''
    <li>Without OPCM, the median cost of an identified member <b>increases by <b>196%</b> the next quarter.
    <li>With OPCM, the median cost <b>decreases by 27%</b>
    <li>In FQ after identification, ~12% of members exceed outlier threshold with/without supervision
    <li> Those members have a median cost of $8,804.04 without supervison, but $5,321.71 with supervision.
    <br><br>
    With a 2% ID rate, 12% being outliers:''', unsafe_allow_html=True)
    
    # User input for plan size
    plan_size = st.number_input('Enter Plan Size:', min_value=1000, value=10000, step=1000)
    
    # Calculate values
    flagged_total = 0.02 * plan_size
    flagged_non_outlier = 0.88 * flagged_total
    flagged_outlier = 0.12 * flagged_total
    
    # Cost per member values
    cost_non_outlier_opcm = 228.93
    cost_non_outlier_no_super = 505.03
    cost_outlier_opcm = 5321.71
    cost_outlier_no_super = 8804.08
    
    # Calculate Total (Annual)
    total_annual_no_super = (4 * cost_non_outlier_no_super * flagged_non_outlier) + (4 * cost_outlier_no_super * flagged_outlier)
    total_annual_opcm = (4 * cost_non_outlier_opcm * flagged_non_outlier) + (4 * cost_outlier_opcm * flagged_outlier)
    
    # Calculate Savings (Annual)
    savings_annual = total_annual_no_super - total_annual_opcm
    
    # Create HTML table
    html_table = f"""
    <table style="width:100%; border-collapse: collapse;">
        <thead>
            <tr>
                <th style="text-align: left; padding: 8px; border-bottom: 2px solid #ddd;"></th>
                <th style="text-align: right; padding: 8px; border-bottom: 2px solid #ddd;">No Supervision</th>
                <th style="text-align: right; padding: 8px; border-bottom: 2px solid #ddd;">OPCM Supervision</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding: 8px; border-bottom: 1px solid #ddd;">Flagged<br>(FQ, non-outlier)</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">{flagged_non_outlier:,.0f}</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">{flagged_non_outlier:,.0f}</td>
            </tr>
            <tr>
                <td style="padding: 8px; border-bottom: 1px solid #ddd;">Flagged<br>(FQ, outlier)</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">{flagged_outlier:,.0f}</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">{flagged_outlier:,.0f}</td>
            </tr>
            <tr>
                <td style="padding: 8px; border-bottom: 1px solid #ddd;">Cost Next FQ<br>(non-outlier, per member)</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">${cost_non_outlier_no_super:,.2f}</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">${cost_non_outlier_opcm:,.2f}</td>
            </tr>
            <tr>
                <td style="padding: 8px; border-bottom: 1px solid #ddd;">Cost Next FQ<br>(outlier, per member)</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">${cost_outlier_no_super:,.2f}</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">${cost_outlier_opcm:,.2f}</td>
            </tr>
            <tr>
                <td style="padding: 8px; border-bottom: 1px solid #ddd;">Total (Annual)</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">${total_annual_no_super:,.2f}</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">${total_annual_opcm:,.2f}</td>
            </tr>
            <tr>
                <td style="padding: 8px; border-bottom: 1px solid #ddd;">Savings (Annual)</td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;"></td>
                <td style="text-align: right; padding: 8px; border-bottom: 1px solid #ddd;">${savings_annual:,.2f}</td>
            </tr>
        </tbody>
    </table>
    """
    
    st.markdown(html_table, unsafe_allow_html=True)
#    Due to not recieving quarterly claims until the beginning of the subsequent quarter,<br>
#   OPCM has minimal control of costs during the quarter of identification.
