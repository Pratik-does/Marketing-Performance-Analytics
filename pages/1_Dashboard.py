import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Marketing Performance Dashboard")

st.markdown(
"""
Explore the complete Power BI dashboard developed for marketing campaign analysis.
This page presents the executive dashboard along with a summary of the project's objectives and key capabilities.
"""
)

# ---------- Dashboard Image ----------

dashboard_path = Path("Dashboard") / "dashboard_view.png"

if dashboard_path.exists():
    image = Image.open(dashboard_path)
    st.image(
        image,
        caption="Marketing Performance Dashboard (Power BI)",
        width="stretch"
    )
else:
    st.error("Dashboard/dashboard_view.png not found.")

st.divider()

# ---------- Project Overview ----------

left, right = st.columns([2,1])

with left:
    st.subheader("Project Overview")

    st.write("""
This project analyzes multi-channel marketing campaign performance using Power BI.

The dashboard enables decision-makers to monitor:

- Marketing Spend
- Revenue
- Profit
- ROI
- Click Performance
- Conversion Performance
- Platform Analysis
- Country Analysis
- Campaign Performance
""")

with right:

    st.subheader("Technology Stack")

    st.success("Power BI")
    st.success("DAX")
    st.success("Power Query")
    st.success("SQL")
    st.success("Python")
    st.success("Streamlit")

st.divider()

st.subheader("Key Dashboard Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 KPI Cards")

    st.write("""
- Spend
- Revenue
- Profit
- ROI
- Clicks
- Conversion Rate
""")

with col2:
    st.info("📊 Visual Analysis")

    st.write("""
- Monthly Trends
- Platform Performance
- Country Analysis
- Campaign Overview
""")

with col3:
    st.info("💡 Business Insights")

    st.write("""
- Best Channels
- High Conversion Platforms
- Revenue Drivers
- Marketing Recommendations
""")