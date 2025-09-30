import streamlit as st

# Set page config
st.set_page_config(page_title="Marketing Report", layout="wide")

# Apply dark theme background color
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
            background-color: #1E1E1E;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.5);
        }
        .box-text {
            font-weight: bold;
            margin-top: 10px;
        }
        .plus-sign {
            font-size: 32px;
            font-weight: bold;
            margin: 0px 10px;
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
st.markdown("<br>", unsafe_allow_html=True)  # spacing
st.markdown("<div class='section-header'>What Are OPCM Indicators?</div>", unsafe_allow_html=True)
st.write("Update this text later")

# --- FOUR BOXES ---
colA, colB, colC, colD = st.columns(4)

with colA:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.image("gray_pill_bottle.png", use_container_width=True)
    st.markdown("<div class='box-text'>50+ mg Morphine Equivalent</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with colB:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    img_cols = st.columns([1, 0.2, 1])
    with img_cols[0]:
        st.image("gray_pill_bottle.png", use_container_width=True)
    with img_cols[1]:
        st.markdown("<div class='plus-sign'>+</div>", unsafe_allow_html=True)
    with img_cols[2]:
        st.image("gray_pill_bottle.png", use_container_width=True)
    st.markdown("<div class='box-text'>Opioid + Benzo</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with colC:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    img_cols = st.columns([1, 0.2, 1])
    with img_cols[0]:
        st.image("gray_pill_bottle.png", use_container_width=True)
    with img_cols[1]:
        st.markdown("<div class='plus-sign'>+</div>", unsafe_allow_html=True)
    with img_cols[2]:
        st.image("gray_doctor.png", use_container_width=True)
    st.markdown("<div class='box-text'>2+ Opioid Prescribers</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with colD:
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    img_cols = st.columns([1, 0.2, 1])
    with img_cols[0]:
        st.image("gray_pill_bottle.png", use_container_width=True)
    with img_cols[1]:
        st.markdown("<div class='plus-sign'>+</div>", unsafe_allow_html=True)
    with img_cols[2]:
        st.image("gray_pharmacy.png", use_container_width=True)
    st.markdown("<div class='box-text'>2+ Opioid Pharmacies</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
