import streamlit as st

# Configure page with dark theme
st.set_page_config(
    page_title="OPCM Marketing Report",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark theme and styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .objectives-title {
        color: #ffffff;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .divider-line {
        border-top: 2px solid #ffffff;
        margin: 10px 0 20px 0;
    }
    .bullet-point {
        color: #ffffff;
        font-size: 18px;
        margin: 10px 0;
        padding-left: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Create container for header section
header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    # Objectives section
    st.markdown('<div class="objectives-title">Objectives</div>', unsafe_allow_html=True)

with header_col2:
    # Logo in top right
    try:
        st.image("green_logo.png", width=200)
    except:
        st.info("Logo: green_logo.png")

# Full-width divider line
st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)

# Bullet points
st.markdown('<div class="bullet-point">• Explain OPCM Member Identification</div>', unsafe_allow_html=True)
st.markdown('<div class="bullet-point">• Explain OPCM Provider Outreach</div>', unsafe_allow_html=True)
st.markdown('<div class="bullet-point">• Explain Benefits: Employee Wellbeing & Costs</div>', unsafe_allow_html=True)

# Spacing
st.markdown("<br>", unsafe_allow_html=True)

# New section header
st.markdown('<div class="objectives-title">What Are OPCM Indicators?</div>', unsafe_allow_html=True)
st.markdown('<div class="bullet-point">Update this text later</div>', unsafe_allow_html=True)
