import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Executive Analytics Report")
st.caption("Professional business report for marketing performance analysis.")

report_path = Path("report") / "market analytics report.pdf"

st.markdown("### Report Summary")
st.write(
    """
    This report presents a professional review of the marketing performance dashboard,
    covering campaign performance, platform efficiency, customer engagement, monthly trends,
    and actionable business recommendations.
    """
)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("### What this report includes")
    st.write(
        """
        - Executive summary
        - Best-performing campaigns
        - High-conversion channels
        - Customer engagement trends
        - Monthly analytics summary
        - Marketing improvement suggestions
        - Campaign performance overview
        """
    )

    st.markdown("### Business value")
    st.success(
        "The report converts dashboard outputs into clear business insights for recruiters, managers, and stakeholders."
    )

with col2:
    st.markdown("### Download Report")
    if report_path.exists():
        with open(report_path, "rb") as file:
            st.download_button(
                label="Download PDF Report",
                data=file,
                file_name="Marketing_Performance_Analytics_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.error("Report PDF not found in the report folder.")

st.divider()

st.markdown("### Report Highlights")
a, b, c = st.columns(3)

with a:
    st.info("Best campaigns identified from revenue, ROI, and engagement patterns.")

with b:
    st.info("Channel performance compared across platform, clicks, and conversion rates.")

with c:
    st.info("Optimization actions based on spend efficiency and performance concentration.")