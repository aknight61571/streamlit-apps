import streamlit as st
import base64
import plotly.io as pio

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
    OPCM's innovative <i>OpioidRx-AI</i> model is trained to evaluate opioid-related risk based on CDC-researched indicators.<br>
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

col1, col2, col3 = st.columns([47.5, 5, 47.5])

with col1:
    pio.read_json('risk_factor_removal.json')
with col2:
    st.image('okc_sdoc_savings.png')
