import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Downloads",
    page_icon="⬇️",
    layout="wide"
)

st.title("⬇️ Project Downloads")
st.caption(
    "Download the complete project assets including datasets, Power BI dashboard, SQL scripts, report, presentation, and notebook."
)

# -------------------------------------------------------
# Helper functions
# -------------------------------------------------------

def find_first_file(folder: str, patterns: list[str]) -> Path | None:
    folder_path = Path(folder)
    if not folder_path.exists():
        return None

    for pattern in patterns:
        matches = sorted(folder_path.glob(pattern))
        if matches:
            return matches[0]

    return None


def download_file(title: str, filepath: str, mime: str, button_label: str | None = None):
    path = Path(filepath)

    st.markdown(f"#### {title}")

    if path.exists():
        with open(path, "rb") as file:
            st.download_button(
                label=button_label or f"📥 Download {path.name}",
                data=file,
                file_name=path.name,
                mime=mime,
                width="stretch"
            )
    else:
        st.error(f"{path.as_posix()} not found")


# =========================================================
# DATASETS
# =========================================================

st.header("📂 Datasets")

col1, col2 = st.columns(2)

with col1:
    download_file(
        "Raw Dataset",
        "data/raw/digital_marketing_dataset_30k.csv",
        "text/csv",
        "📥 Download Raw Dataset"
    )

with col2:
    download_file(
        "Cleaned Dataset",
        "data/processed/digital_marketing_cleaned.csv",
        "text/csv",
        "📥 Download Cleaned Dataset"
    )

st.divider()

# =========================================================
# POWER BI FILE
# =========================================================

st.header("📊 Power BI Dashboard")

pbix_file = find_first_file(
    "dashboard",
    ["*.pbix", "*.PBIX"]
)

if pbix_file:
    with open(pbix_file, "rb") as file:
        st.download_button(
            label="📥 Download Power BI (.pbix)",
            data=file,
            file_name=pbix_file.name,
            mime="application/octet-stream",
            width="stretch"
        )
else:
    st.error("Power BI file not found in the dashboard folder.")

st.divider()

# =========================================================
# DASHBOARD SCREENSHOT
# =========================================================

st.header("🖼 Dashboard Screenshot")

dashboard_image = find_first_file(
    "dashboard",
    ["dashboard_view.png", "*.png", "*.jpg", "*.jpeg", "*.webp"]
)

if dashboard_image:
    with open(dashboard_image, "rb") as file:
        st.download_button(
            label="📥 Download Dashboard Screenshot",
            data=file,
            file_name=dashboard_image.name,
            mime="image/png",
            width="stretch"
        )
else:
    st.error("Dashboard screenshot not found in the dashboard folder.")

st.divider()

# =========================================================
# REPORT AND PRESENTATION
# =========================================================

st.header("📑 Project Documents")

report_file = find_first_file(
    "report",
    ["*.pdf", "*.PDF"]
)

ppt_file = find_first_file(
    "presentation",
    ["*.pptx", "*.PPTX", "*.ppt", "*.PPT"]
)

left, right = st.columns(2)

with left:
    if report_file:
        with open(report_file, "rb") as file:
            st.download_button(
                label="📥 Download PDF Report",
                data=file,
                file_name=report_file.name,
                mime="application/pdf",
                width="stretch"
            )
    else:
        st.error("PDF report not found in the report folder.")

with right:
    if ppt_file:
        with open(ppt_file, "rb") as file:
            st.download_button(
                label="📥 Download Presentation",
                data=file,
                file_name=ppt_file.name,
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                width="stretch"
            )
    else:
        st.error("Presentation file not found in the presentation folder.")

st.divider()

# =========================================================
# NOTEBOOK
# =========================================================

st.header("📒 Jupyter Notebook")

notebook_file = find_first_file(
    "notebook",
    ["*.ipynb", "*.IPYNB"]
)

if notebook_file:
    with open(notebook_file, "rb") as file:
        st.download_button(
            label="📥 Download Notebook",
            data=file,
            file_name=notebook_file.name,
            mime="application/octet-stream",
            width="stretch"
        )
else:
    st.error("Notebook not found in the notebook folder.")

st.divider()

# =========================================================
# SQL FILES
# =========================================================

st.header("🗄 SQL Scripts")

sql_folder = Path("sql")
sql_files = sorted(sql_folder.glob("*.sql")) if sql_folder.exists() else []

if sql_files:
    st.success(f"Found {len(sql_files)} SQL script(s).")

    # show buttons in two columns
    cols = st.columns(2)

    for i, sql_file in enumerate(sql_files):
        with cols[i % 2]:
            with open(sql_file, "rb") as file:
                st.download_button(
                    label=f"📥 {sql_file.name}",
                    data=file,
                    file_name=sql_file.name,
                    mime="text/sql",
                    width="stretch"
                )
else:
    st.warning("No SQL files were found in the SQL folder.")

st.divider()

# =========================================================
# GITHUB REPOSITORY
# =========================================================

st.header("🌐 GitHub Repository")

st.write(
    """
    The complete source code, dashboard assets, SQL scripts, report files,
    dataset files, and Streamlit application are available in the GitHub repository.
    """
)

st.link_button(
    "🚀 Open GitHub Repository",
    "https://github.com/Pratik-does/Marketing-Performance-Analytics",
    width="stretch"
)

st.divider()

# =========================================================
# PROJECT SNAPSHOT
# =========================================================

st.header("📈 Repository Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Datasets", "2")

with c2:
    st.metric("SQL Scripts", str(len(sql_files)))

with c3:
    st.metric("Reports", "1")

with c4:
    st.metric("Presentation", "1")

st.divider()

# =========================================================
# PORTFOLIO NOTE
# =========================================================

st.header("💼 Portfolio Note")

st.write(
    """
    This repository demonstrates an end-to-end Marketing Performance Analytics project.
    It combines SQL analysis, Power BI dashboarding, business reporting, and Streamlit deployment
    into a recruiter-friendly portfolio presentation.
    """
)

st.success("Thank you for exploring the project!")
st.caption("© 2026 Pratik Bairagi | Marketing Performance Analytics Portfolio")