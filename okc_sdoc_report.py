import streamlit as st

# Set page config
st.set_page_config(page_title="Marketing Report", layout="wide")

# Apply dark theme
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
            background-color: #4A4A4A; /* medium-light grey */
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.5);
            height: 100%;
        }
        .box img {
            max-width: 80px;  /* uniform scaling */
            height: auto;
        }
        .box .combo {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        .box-text {
            font-weight: bold;
            margin-top: 12px;
            font-size: 16px;
        }
        .plus-sign {
            font-size: 28px;
            font-weight: bold;
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
st.write("Update this text later")

# --- FOUR BOXES ---
colA, colB, colC, colD = st.columns(4)

with colA:
    st.markdown(
        """
        <div class="box">
            <img src="gray_pill_bottle.png" />
            <div class="box-text">50+ mg Morphine Equivalent</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with colB:
    st.markdown(
        """
        <div class="box">
            <div class="combo">
                <img src="gray_pill_bottle.png" />
                <div class="plus-sign">+</div>
                <img src="gray_pill_bottle.png" />
            </div>
            <div class="box-text">Opioid + Benzo</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with colC:
    st.markdown(
        """
        <div class="box">
            <div class="combo">
                <img src="gray_pill_bottle.png" />
                <div class="plus-sign">+</div>
                <img src="gray_doctor.png" />
            </div>
            <div class="box-text">2+ Opioid Prescribers</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with colD:
    st.markdown(
        """
        <div class="box">
            <div class="combo">
                <img src="gray_pill_bottle.png" />
                <div class="plus-sign">+</div>
                <img src="gray_pharmacy.png" />
            </div>
            <div class="box-text">2+ Opioid Pharmacies</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
