import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Dark Report Demo",
    layout="wide",
    initial_sidebar_state="collapsed"
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
st.components.v1.html("""
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
""", height=0)

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

# ─── Prepare Bar Chart: Overdose PMR by Occupation ───────────────────────────
bar_data = {
    "Occupation": [
        "Construction and Extraction",
        "Installation, Maintenance, and Repair",
        "Transportation and Material Moving",
        "Food Preparation and Serving Related",
        "Healthcare Support",
        "Production",
        "Building and Grounds Cleaning and Maintenance",
        "Sales and Related",
        "Office and Administrative Support",
        "Education, Training, and Library",
        "..."
    ],
    "PMR_mean": [162, 143, 130, 118, 112, 110, 109, 98, 91, 85, None],
    "PMR_lower": [158, 139, 126, 114, 108, 106, 105, 94, 87, 81, None],
    "PMR_upper": [165, 147, 134, 122, 116, 114, 113, 102, 95, 89, None]
}
df_bar = pd.DataFrame(bar_data)
df_main = df_bar[df_bar['Occupation'] != '...'].sort_values('PMR_mean', ascending=False)
df_dummy = df_bar[df_bar['Occupation'] == '...']
df_sorted = pd.concat([df_main, df_dummy], ignore_index=True)

fig_bar = px.bar(
    df_sorted,
    x='PMR_mean',
    y='Occupation',
    orientation='h',
    template='plotly_dark',
    title='<b>95% CI: Opioid Overdose Deaths per 100,000 People</b>',
    color_discrete_sequence=['lightskyblue']
)
fig_bar.update_traces(
    error_x=dict(
        type='data',
        array=df_sorted['PMR_upper'] - df_sorted['PMR_mean'],
        arrayminus=df_sorted['PMR_mean'] - df_sorted['PMR_lower'],
        color='#AAAAAA'
    )
)
fig_bar.update_layout(
    yaxis=dict(
        categoryorder='array',
        categoryarray=list(df_sorted['Occupation'])[::-1],
        title=dict(text='<b>Occupation</b>')
    ),
    xaxis=dict(
        title=dict(text='<b>Deaths per 100,000 Employees</b>')
    )
)

# ─── SECTION 0: Wellness Cost ──────────────────────────────────────────────────
st.markdown("### <span id='wellness'>Cost of Opioids: Wellness</span>", unsafe_allow_html=True)
st.markdown("""
<div class="section-text">
    Using the Kessler-6 (K6) Scale as a metric, recent studies have shown that those with access to an opioid 
    consistently grade in the most severe category of stress.<sup>1</sup> Individuals in this K6 category are 
    3.5× more likely to experience chronic diseases, such as diabetes, hypertension, and obesity,<sup>2</sup> 
    are absent an additional 6 days annually, and are 40% less productive in the workplace.<sup>3</sup> Construction workers are not 
    only nearly twice as likely to have a Substance Use Disorder (SUD), but also suffer the highest rate of 
    opioid overdose deaths of any occupation in the United States.<sup>4</sup>
    <u>Hover graphs for exact values.</u>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footnote">
    <b>1.</b> <i>National Library of Medicine</i>, 2024 <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11003197/" target="_blank" style="color: lightblue;">PMC11003197</a><br>
    <b>2.</b> <i>CDC Prevention Center</i>, 2014 <a href="https://www.cdc.gov/pcd/issues/2014/14_0211.htm" target="_blank" style="color: lightblue;">CDC PCD 2014;11</a><br>
    <b>3.</b> <i>American Psychological Association</i>, 2019 <a href='https://psycnet.apa.org/doiLanding?doi=10.1037%2Focp0000155' target="_blank" style="color: lightblue;">link</a><br>
    <b>4.</b> <i>National Library of Medicine</i>, 2023 <a href="https://pubmed.ncbi.nlm.nih.gov/37639452/" target="_blank" style="color: lightblue;">PMID 37639452</a>
</div>
""", unsafe_allow_html=True)

st.plotly_chart(fig_bar, use_container_width=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─── SECTION 1: Case Study ────────────────────────────────────────────────────
st.markdown("### <span id='case-study'>Case Study: OpioidRx-AI Interruption</span>", unsafe_allow_html=True)
st.markdown("""
<div class="section-text">
    The advent of the COVID-19 pandemic in 2020 brought the rise of remote healthcare;
    temporarily closing brick-and-mortar facilities and interrupting non-patient accessibility
    to providers. A notable OPCM client witnessed soaring rates of opioid use during the
    third and fourth quarters due to diminished outreach.<sup>1</sup> The issue was quickly moderated
    as physical locations reopened in Q1 2023 and lack of outreach was resolved.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footnote">
    <b>1.</b> <i>Internal Reporting</i>, 2025
</div>
""", unsafe_allow_html=True)

# ─── Graph 1: Opioid Prescription Rates ───────────────────────────────────────
quarters_1 = ["Q1, 2020", "Q2, 2020", "Q3, 2020", "Q4, 2020",
              "Q1, 2021", "Q2, 2021", "Q3, 2021", "Q4, 2021"]
script_rates = [3.99, 3.88, 13.98, 18.23, 4.36, 4.68, 3.48, 3.33]

fig_scripts = px.line(
    x=list(range(len(quarters_1))),
    y=script_rates,
    title="Increased Opioid Access without OPCM",
    labels={"x": "Quarter", "y": "Opioid Scripts/100 Members"},
    markers=True,
    color_discrete_sequence=["orange"],
    template="plotly_dark"
)
fig_scripts.update_traces(line=dict(width=4))
fig_scripts.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=list(range(len(quarters_1))),
        ticktext=quarters_1,
        tickangle=-45
    ),
    height=400
)
fig_scripts.add_vline(x=1, line_dash="dash", line_color="lightgrey")
fig_scripts.add_vline(x=4, line_dash="dash", line_color="lightgrey")
fig_scripts.add_annotation(
    x=2.5,
    y=12,
    text="Service<br>Hindered",
    showarrow=False,
    font=dict(color="white", size=12),
    xanchor="center",
    align="center"
)

st.plotly_chart(fig_scripts, use_container_width=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─── SECTION 2: Financial Cost ────────────────────────────────────────────────
st.markdown("### <span id='financial-cost'>Cost of Opioids: Financial</span>", unsafe_allow_html=True)
st.markdown("""
<div class="section-text">
    Without regard to employee turnover, opioid abuse costs employers <b>$10 billion</b> per year from absenteeism
    and presenteeism alone.<sup>1</sup> In addition, the cost of replacing a worker is expected to be 50% of their annual salary.<sup>2</sup>
    Increased absenteeism among workers taking an Opioid is typically attributed to unexpected illness or injury- which can
    be costly. Between 2023 and 2025, Fargo Homebuilder's Association's quarterly health plan spend on members currently
    identified by <b><i>OpioidRx-AI</i></b> ranged from <b>$128,921</b> to <b>$512,688</b>. However, the plan spend on those
    same members during the sequential quarter ranged from <b>$29,535</b> to <b>$107,760</b>.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="font-size: 13px; margin-top: 10px;">
  <p><b>1.</b> <i>Providence Recovery Place</i>, 2023. <a href="https://providencerecoveryplace.org/opioid-addiction-cost-american-employers-between-10-25-billion-a-year/" target="_blank" style="color: lightblue;">link</a></p>
  <p><b>2.</b> <i>National Safety Council</i>, 2024. <a href="https://www.nsc.org/workplace/safety-topics/drugs-at-work/implications-of-drug-use-for-employers" target="_blank" style="color: lightblue;">link</a></p>
</div>
""", unsafe_allow_html=True)

# ─── Graph 2: Plan Spend Comparison ───────────────────────────────────────────
quarters_2 = ["Q1, 2023", "Q2, 2023", "Q3, 2023", "Q4, 2023",
              "Q1, 2024", "Q2, 2024", "Q3, 2024", "Q4, 2024"]
prev_spend = [512688, 351373, 161113, 498677, 400721, 128921, 264965, 278064]
curr_spend = [107760, 52793, 29871, 37936, 29535, 38199, 53114, 45638]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=quarters_2, y=prev_spend,
    mode='lines+markers',
    name='Previous Quarter Spend',
    line=dict(color='orange', width=4)
)
fig.add_trace(go.Scatter(
    x=quarters_2, y=curr_spend,
    mode='lines+markers',
    name='Current Quarter Spend',
    line=dict(color='deepskyblue', width=4),
    fill='tonexty',
    fillcolor='rgba(30, 144, 255, 0.2)'
))
for i in range(len(quarters_2)):
    fig.add_trace(go.Scatter(
        x=[quarters_2[i], quarters_2[i]],
        y=[curr_spend[i], prev_spend[i]],
        mode='lines',
        line=dict(width=0),
        fill='toself',
        fillcolor='rgba(255,165,0,0.25)',
        showlegend=False
    ))
fig.add_annotation(
    x=3.5,
    y=160000,
    text="Estimated Savings: $1,985,876",
    showarrow=False,
    font=dict(color="white", size=16),
    bgcolor="rgba(0,0,0,0.6)"
)
fig.update_layout(
    title="Plan Spend Comparison by Quarter",
    xaxis_title="Quarter",
    yaxis_title="Plan Spend ($)",
    template="plotly_dark",
    xaxis=dict(tickangle=-45),
    legend=dict(x=0.01, y=0.99),
    height=600
)

st.plotly_chart(fig, use_container_width=True)
