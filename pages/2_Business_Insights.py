import streamlit as st

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

st.markdown(
    """
    <style>
        .insight-card {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border: 1px solid #243244;
            border-radius: 16px;
            padding: 18px 20px;
            color: #ffffff;
            min-height: 140px;
        }
        .insight-title {
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 8px;
            color: #93c5fd;
        }
        .insight-text {
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
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💡 Business Insights & Recommendations")
st.caption("Executive-level summary of campaign performance, channel efficiency, engagement trends, and optimization opportunities.")

st.markdown("### Executive Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="insight-card">
            <div class="insight-title">Best Overall Performer</div>
            <div class="insight-text">
                Google Search emerged as the strongest revenue-driving channel and also showed the highest engagement volume in the dashboard.
                It is the clearest candidate for sustained budget support.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="insight-card">
            <div class="insight-title">High Conversion Channel</div>
            <div class="insight-text">
                Google Search delivered the highest conversion rate, followed by LinkedIn and Meta.
                This indicates that search traffic is converting more efficiently than most awareness-led channels.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="insight-card">
            <div class="insight-title">Budget Efficiency</div>
            <div class="insight-text">
                Spend is concentrated in a few platforms, while the revenue response is uneven.
                This suggests that budget reallocation and tighter campaign targeting can improve return.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs([
    "Best-Performing Campaigns",
    "High-Conversion Channels",
    "Customer Engagement Trends",
    "Recommendations"
])

with tab1:
    st.subheader("Best-Performing Campaigns")
    st.write(
        """
        The best-performing campaigns are the ones that combine high revenue contribution,
        strong ROI, and efficient conversion behavior.

        Based on the dashboard and campaign overview:
        - Campaigns tied to **Google Search** consistently show the strongest performance.
        - Campaigns with a **lead or conversion objective** tend to perform better than broad awareness campaigns.
        - Higher-performing campaigns are typically concentrated in markets where intent is stronger and campaign targeting is more focused.
        """
    )

    st.markdown("#### Performance Pattern")
    st.info(
        "Campaigns with clear intent, tighter audience targeting, and strong search visibility are outperforming broad exposure campaigns."
    )

with tab2:
    st.subheader("High-Conversion Channels")
    st.write(
        """
        Conversion efficiency is strongest in the search-led and intent-driven channels.

        Channel-level interpretation:
        - **Google Search**: highest conversion rate and strongest revenue contribution.
        - **LinkedIn**: efficient for targeted professional audiences.
        - **Meta**: decent conversion support, but efficiency is lower than search.
        - **TikTok / Snapchat / Display**: better for reach and awareness, but weaker for direct conversion.
        """
    )

    st.markdown("#### Channel Insight")
    st.warning(
        "High reach does not automatically mean high conversion. The dashboard shows that intent-driven channels outperform awareness-heavy channels in conversion efficiency."
    )

with tab3:
    st.subheader("Customer Engagement Trends")
    st.write(
        """
        Engagement trends suggest that customer interaction is concentrated in a few dominant channels.

        Observations:
        - Click volume is highest in the platforms with the largest audience reach.
        - Conversion behavior is more selective and does not always follow click volume.
        - Monthly performance indicates visible variation across the reporting period, which suggests seasonality and campaign timing effects.
        - Some channels attract attention but do not convert at the same level, which points to a gap between engagement and final action.
        """
    )

    st.markdown("#### Trend Interpretation")
    st.success(
        "The dashboard suggests that engagement is strongest when campaign intent, message relevance, and channel choice are aligned."
    )

with tab4:
    st.subheader("Marketing Improvement Suggestions")

    st.write(
        """
        The analysis supports the following recommendations:
        """
    )

    rec1, rec2 = st.columns(2)

    with rec1:
        st.markdown("### Budget Reallocation")
        st.write(
            """
            Increase spend on channels with strong revenue and conversion performance,
            especially Google Search.
            Reduce budget on low-return channels unless their role is awareness-led.
            """
        )

        st.markdown("### Campaign Optimization")
        st.write(
            """
            Improve targeting, creative alignment, and bidding strategy for weaker platforms.
            Review campaign objectives and compare performance by platform-country combination.
            """
        )

    with rec2:
        st.markdown("### Engagement Improvement")
        st.write(
            """
            Test more personalized creatives, stronger calls to action, and audience segmentation.
            Use monthly performance tracking to identify when engagement starts to drop.
            """
        )

        st.markdown("### Measurement Upgrade")
        st.write(
            """
            Maintain a clear KPI framework for spend, revenue, clicks, conversion rate, and ROI.
            This ensures consistent performance review across future reporting cycles.
            """
        )

st.markdown("---")

st.subheader("Monthly Analytics Summary")

left, right = st.columns([1.2, 1])

with left:
    st.write(
        """
        Monthly analytics show that performance is not flat across the year.
        Revenue and spend fluctuate over time, which means campaign timing and seasonality are affecting outcomes.
        The business should treat monthly performance as a planning signal rather than a backward-looking report only.
        """
    )

with right:
    st.markdown(
        """
        <div class="section-box">
            <div class="insight-title">Key Takeaway</div>
            <div class="insight-text">
                Revenue concentration in a small number of channels indicates an opportunity to scale winning campaigns
                while reducing waste in lower-performing areas.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )