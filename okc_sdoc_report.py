import streamlit as st
import base64
import plotly.io as pio
import pandas as pd

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
    <br> Outlier threshold is the maximum cost without being considered a financial outlier.
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

st.write("Update this later")

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
    st.write('''OPCM's provider outreach is imperative to avoid the exploding costs of opioid misuse:
    <li>Without OPCM, the median cost of an identified member <b>increases by <b>196%</b> the next quarter.
    <li>With OPCM, the median cost <b>decreases by 27%</b>
    <br><br>
    Doing the math, we see:''', unsafe_allow_html=True)
    
    # User input for plan size
    plan_size = st.number_input('Enter Plan Size:', min_value=1000, value=10000, step=1000)
    
    # Calculate values
    flagged_per_quarter = 0.02 * plan_size
    cost_next_quarter_no_supervision = flagged_per_quarter * 171.55 * 2.96
    cost_next_quarter_opcm = flagged_per_quarter * 311.60 * 0.73
    savings_annual = (cost_next_quarter_no_supervision - cost_next_quarter_opcm) * 4
    
    # Create dataframe for the table
    data = {
        'No Supervision': [
            plan_size,
            flagged_per_quarter,
            '+196%',
            cost_next_quarter_no_supervision,
            cost_next_quarter_no_supervision * 4,
            np.nan
        ],
        'OPCM Supervision': [
            plan_size,
            flagged_per_quarter,
            '-27%',
            cost_next_quarter_opcm,
            cost_next_quarter_opcm * 4,
            savings_annual
        ]
    }
    
    df_table = pd.DataFrame(data, index=['Plan Size', 'Flagged per Quarter', '% Cost Increase', 'Cost Next Quarter', 'Total (Annual)', 'Savings (Annual)'])
    
    # Format the table
    formatted = df_table.style.format({
        'No Supervision': lambda x: f'{x:,.0f}' if isinstance(x, (int, float)) and not pd.isna(x) else '',
        'OPCM Supervision': lambda x: f'{x:,.0f}' if isinstance(x, (int, float)) and not pd.isna(x) else ''
    }, subset=pd.IndexSlice[['Plan Size', 'Flagged per Quarter'], :])
    
    formatted = formatted.format({
        'No Supervision': lambda x: f'${x:,.2f}' if isinstance(x, (int, float)) and not pd.isna(x) else '',
        'OPCM Supervision': lambda x: f'${x:,.2f}' if isinstance(x, (int, float)) and not pd.isna(x) else ''
    }, subset=pd.IndexSlice[['Cost Next Quarter', 'Total (Annual)', 'Savings (Annual)'], :])
    
    st.dataframe(formatted)
#    Due to not recieving quarterly claims until the beginning of the subsequent quarter,<br>
#   OPCM has minimal control of costs during the quarter of identification.
