import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="About",
    page_icon="👤",
    layout="wide"
)

st.markdown(
    """
    <style>
        .about-card {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border: 1px solid #243244;
            border-radius: 16px;
            padding: 18px 20px;
            color: #ffffff;
            min-height: 150px;
        }
        .about-title {
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 8px;
            color: #93c5fd;
        }
        .about-text {
            font-size: 14px;
            line-height: 1.6;
            color: #e5e7eb;
        }
        .section-box {
            background: #111827;
            border: 1px solid #243244;
            border-radius: 16px;
            padding: 20px;
            margin-top: 12px;
        }
        .small-note {
            color: #9ca3af;
            font-size: 13px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("👤 About This Project")
st.caption("Professional portfolio project showcasing marketing analytics, dashboarding, business insights, and deployment.")

st.markdown("### Project Summary")

left, right = st.columns([1.4, 1])

with left:
    st.markdown(
        """
        <div class="about-card">
            <div class="about-title">Marketing Performance Analytics Dashboard</div>
            <div class="about-text">
                This project analyzes multi-channel marketing data to evaluate spend efficiency, revenue contribution,
                customer engagement, and conversion performance across platforms, countries, objectives, and time periods.
                It combines Power BI analysis with a Streamlit portfolio deployment to present the work in a recruiter-friendly format.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        """
        <div class="about-card">
            <div class="about-title">Project Outcome</div>
            <div class="about-text">
                The final deliverable includes a professional Power BI dashboard, a business insights report,
                SQL analysis, and a deployable Streamlit portfolio application.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown("### What This Project Covers")

c1, c2, c3 = st.columns(3)

with c1:
    st.info(
        """
        **Data Preparation**
        - Cleaning
        - Transformation
        - Feature engineering
        - SQL-ready dataset creation
        """
    )

with c2:
    st.info(
        """
        **Analytics & BI**
        - KPI analysis
        - Platform comparison
        - Country performance
        - Monthly trends
        """
    )

with c3:
    st.info(
        """
        **Business Storytelling**
        - Executive summary
        - Insights
        - Recommendations
        - Portfolio presentation
        """
    )

st.divider()

st.markdown("### Project Metrics")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Main Dashboard", "1")

with m2:
    st.metric("Insight Pages", "4+")

with m3:
    st.metric("Core KPIs", "6")

with m4:
    st.metric("Tools Used", "5+")

st.divider()

st.markdown("### Tools & Technologies")

tools_left, tools_right = st.columns(2)

with tools_left:
    st.markdown(
        """
        <div class="section-box">
            <div class="about-title">Core Tools</div>
            <div class="about-text">
                • Power BI Desktop<br>
                • DAX<br>
                • Power Query<br>
                • SQL<br>
                • Python
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with tools_right:
    st.markdown(
        """
        <div class="section-box">
            <div class="about-title">Portfolio Stack</div>
            <div class="about-text">
                • Streamlit<br>
                • GitHub<br>
                • Pandas<br>
                • NumPy<br>
                • Plotly / Image assets
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown("### Business Focus Areas")

focus1, focus2 = st.columns(2)

with focus1:
    st.markdown(
        """
        <div class="section-box">
            <div class="about-title">Insights Generated</div>
            <div class="about-text">
                • Best-performing campaigns<br>
                • High-conversion channels<br>
                • Customer engagement trends<br>
                • Monthly analytics reports<br>
                • Campaign performance summary
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with focus2:
    st.markdown(
        """
        <div class="section-box">
            <div class="about-title">Recommendations Delivered</div>
            <div class="about-text">
                • Budget reallocation guidance<br>
                • Channel optimization suggestions<br>
                • Engagement improvement actions<br>
                • Better campaign targeting<br>
                • Reporting and measurement improvements
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown("### Repository & Files")

repo_col1, repo_col2 = st.columns(2)

with repo_col1:
    st.link_button(
        "🚀 Open GitHub Repository",
        "https://github.com/Pratik-does/Marketing-Performance-Analytics",
        width="stretch"
    )

with repo_col2:
    st.markdown(
        """
        <div class="section-box">
            <div class="about-title">Included Assets</div>
            <div class="about-text">
                • Power BI dashboard (.pbix)<br>
                • Executive report (PDF)<br>
                • Presentation deck<br>
                • SQL scripts<br>
                • Dataset files<br>
                • Streamlit pages
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.markdown("### Project Workflow")

st.write(
    """
    1. Data was cleaned and prepared in Python and SQL  
    2. Analytical views and KPI measures were created in Power BI  
    3. The dashboard was designed for executive-level reporting  
    4. Business insights and recommendations were documented  
    5. The project was packaged into a Streamlit portfolio application
    """
)

st.info(
    "This portfolio is designed to show end-to-end analytics skills: data preparation, BI modeling, storytelling, and deployment."
)

st.markdown("---")
st.markdown(
    "<p class='small-note'>© 2026 Pratik Bairagi | Marketing Performance Analytics Portfolio</p>",
    unsafe_allow_html=True
)