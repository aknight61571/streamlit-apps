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
    }
    .summary-item {
        margin-bottom: 0.5rem;
    }
    .jump-link {
        font-style: italic;
        text-decoration: underline;
        color: deepskyblue !important;
        cursor: pointer;
    }
    .jump-link:hover {
        color: lightskyblue !important;
    }
</style>
""", unsafe_allow_html=True)

# ─── JavaScript for Anchor Links ──────────────────────────────────────────────
st.markdown("""
<script>
// Workaround for Streamlit Cloud anchor links
document.addEventListener('DOMContentLoaded', function() {
    const jumpLinks = document.querySelectorAll('.jump-link');
    jumpLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('data-target');
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
                // Add temporary highlight
                targetElement.style.backgroundColor = 'rgba(30, 144, 255, 0.2)';
                setTimeout(() => {
                    targetElement.style.backgroundColor = '';
                }, 1000);
            }
        });
    });
});
</script>
""", unsafe_allow_html=True)

# ─── Summary Section ──────────────────────────────────────────────────────────
st.markdown("""
<div class="summary-box">
    <div class="section-text">
        <b>Summary</b>
    </div>
    <div class="summary-item">1. Opioid use causes stress, which degrades physical health and productivity. Construction workers are much more likely to use opioids.</div>
    <div class="summary-item">2. Interruption in OpioidRx-AI service increases frequency of opioid use among employees. <span class="jump-link" data-target="case-study">Jump to 2</span></div>
    <div class="summary-item">3. Employees first identified by OpioidRx-AI are expensive to insure. OPCM drastically lowers costs by the next quarter. <span class="jump-link" data-target="financial-cost">Jump to 3</span></div>
</div>
""", unsafe_allow_html=True)

# ─── [Rest of your existing code...] ─────────────────────────────────────────
# IMPORTANT: Add these ID attributes to your section headers:

# SECTION 1 HEADER (Case Study):
st.markdown("### <span id='case-study'>Case Study: OpioidRx-AI Interruption</span>", unsafe_allow_html=True)

# SECTION 2 HEADER (Financial Cost):
st.markdown("### <span id='financial-cost'>Cost of Opioids: Financial</span>", unsafe_allow_html=True)

# [Keep all your existing plot code and other sections exactly as is...]
)

st.plotly_chart(fig, use_container_width=True)
