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
