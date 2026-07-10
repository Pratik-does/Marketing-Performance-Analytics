import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# STYLING
# =========================================================
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }

        .hero-box {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border: 1px solid #243244;
            border-radius: 22px;
            padding: 28px 28px 24px 28px;
            color: #ffffff;
        }

        .hero-kicker {
            font-size: 12px;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #93c5fd;
            font-weight: 800;
            margin-bottom: 10px;
        }

        .hero-title {
            font-size: 36px;
            line-height: 1.08;
            font-weight: 800;
            margin-bottom: 12px;
            color: #ffffff;
        }

        .hero-subtitle {
            font-size: 16px;
            line-height: 1.75;
            color: #dbe4f0;
            max-width: 980px;
        }

        .metric-card {
            background: #111827;
            border: 1px solid #243244;
            border-radius: 18px;
            padding: 18px 18px 16px 18px;
            min-height: 122px;
        }

        .metric-title {
            font-size: 13px;
            color: #93c5fd;
            font-weight: 800;
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        .metric-text {
            font-size: 14px;
            color: #e5e7eb;
            line-height: 1.6;
        }

        .section-title {
            font-size: 22px;
            font-weight: 800;
            color: #0f172a;
            margin-top: 0.35rem;
            margin-bottom: 0.8rem;
        }

        .soft-box {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 18px 20px;
        }

        .small-note {
            color: #64748b;
            font-size: 13px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# HERO SECTION
# =========================================================
st.markdown(
    """
    <div class="hero-box">
        <div class="hero-kicker">Power BI • SQL • Python • Streamlit</div>
        <div class="hero-title">Marketing Performance Analytics Dashboard</div>
        <div class="hero-subtitle">
            Executive-level analysis of spend, revenue, profit, ROI, platform performance,
            customer engagement, campaign outcomes, and monthly marketing trends.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# =========================================================
# PROJECT METRICS
# =========================================================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Dashboard Scope</div>
            <div class="metric-text">Executive marketing performance analysis across channels, countries, and time.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Core KPIs</div>
            <div class="metric-text">Spend, Revenue, Profit, ROI, Clicks, and Conversion Rate.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Visual Sections</div>
            <div class="metric-text">Trend analysis, platform analysis, country analysis, and campaign reporting.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Project Deliverables</div>
            <div class="metric-text">Power BI dashboard, business report, presentation, SQL scripts, and Streamlit app.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# =========================================================
# DASHBOARD PREVIEW
# =========================================================
dashboard_path = Path("dashboard") / "dashboard_view.png"

st.markdown('<div class="section-title">Executive Dashboard Preview</div>', unsafe_allow_html=True)
st.caption("Power BI dashboard screenshot used as the visual centerpiece of the portfolio.")

if dashboard_path.exists():
    image = Image.open(dashboard_path)
    st.image(image, use_container_width=True)
else:
    st.error("dashboard/dashboard_view.png not found.")

st.write("")

# =========================================================
# OVERVIEW + QUICK NAVIGATION
# =========================================================
left, right = st.columns([1.35, 1])

with left:
    st.markdown('<div class="section-title">Project Overview</div>', unsafe_allow_html=True)
    st.write(
        """
        This project analyzes multi-channel marketing campaign performance using Power BI,
        SQL, Python, and Streamlit.

        The dashboard is structured for executive review:
        - KPI summary at the top
        - Trend and platform analysis in the middle
        - Country and campaign analysis below
        """
    )

    st.write(
        """
        The analysis focuses on:
        - Best-performing campaigns
        - High-conversion channels
        - Customer engagement trends
        - Monthly analytics
        - Business recommendations
        """
    )

with right:
    st.markdown('<div class="section-title">Quick Navigation</div>', unsafe_allow_html=True)

    nav1, nav2 = st.columns(2)
    with nav1:
        st.page_link("pages/2_Business_Insights.py", label="💡 Business Insights", use_container_width=True)
        st.page_link("pages/4_Downloads.py", label="⬇ Downloads", use_container_width=True)

    with nav2:
        st.page_link("pages/3_Report.py", label="📄 Report", use_container_width=True)
        st.page_link("pages/5_About.py", label="👤 About", use_container_width=True)

    st.markdown(
    """
    <style>
        .dark-tip-box {
            margin-top: 14px;
            background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
            border: 1px solid #243244;
            border-radius: 16px;
            padding: 18px 20px;
            color: #e5e7eb;
            min-height: 120px;
        }
        .dark-tip-box .tip-title {
            color: #93c5fd;
            font-weight: 800;
            font-size: 16px;
            margin-bottom: 8px;
        }
        .dark-tip-box .tip-text {
            font-size: 14px;
            line-height: 1.7;
            color: #e5e7eb;
        }
    </style>

    <div class="dark-tip-box">
        <div class="tip-title">Quick Tip</div>
        <div class="tip-text">
            Use the sidebar to move between dashboard sections, business insights, report, downloads, and project background.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# =========================================================
# KEY FEATURES
# =========================================================
st.markdown('<div class="section-title">Key Features</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.info(
        """
        **KPI Tracking**
        - Total Spend
        - Total Revenue
        - Profit
        - ROI
        - Clicks
        - Conversion Rate
        """
    )

with f2:
    st.info(
        """
        **Visual Analysis**
        - Spend vs Revenue trend
        - Platform comparison
        - Country performance
        - Campaign summary table
        """
    )

with f3:
    st.info(
        """
        **Business Value**
        - Performance comparison
        - Budget efficiency
        - Optimization suggestions
        - Executive storytelling
        """
    )

st.write("")

# =========================================================
# TECHNOLOGY STACK
# =========================================================
st.markdown('<div class="section-title">Technology Stack</div>', unsafe_allow_html=True)

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.success("Power BI")
with t2:
    st.success("DAX")
with t3:
    st.success("SQL")
with t4:
    st.success("Python / Streamlit")

st.write("")

# =========================================================
# BUSINESS QUESTIONS
# =========================================================
st.markdown('<div class="section-title">Business Questions Answered</div>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
        .dark-q-box {
            background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
            border: 1px solid #243244;
            border-radius: 16px;
            padding: 18px 20px;
            color: #f8fafc;
            min-height: 170px;
        }
        .dark-q-box h4 {
            margin: 0 0 10px 0;
            color: #93c5fd;
            font-size: 16px;
        }
        .dark-q-box p {
            margin: 0;
            line-height: 1.7;
            color: #e5e7eb;
            font-size: 14px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

q1, q2 = st.columns(2)

with q1:
    st.markdown(
        """
        <div class="dark-q-box">
            <h4>Channel Performance</h4>
            <p>
                Which platforms generate the highest revenue?<br>
                Which channels convert the best?<br>
                Which platforms deserve more budget?
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with q2:
    st.markdown(
        """
        <div class="dark-q-box">
            <h4>Marketing Efficiency</h4>
            <p>
                How does spend compare with revenue?<br>
                Which countries perform best?<br>
                Which campaigns need optimization?
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )