from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="TerraScan-NDT", page_icon="🛰️", layout="wide")
st.title("TerraScan-NDT Dashboard")
st.caption("GPR screening • YOLO baseline • Demo sensor fusion • Geo-tagging")

BASE = Path.cwd()

def locate(filename):
    direct = BASE / filename
    if direct.exists():
        return direct
    matches = list(BASE.rglob(filename))
    return matches[0] if matches else None

def load_csv(filename):
    path = locate(filename)
    if path is None:
        return None, None
    try:
        return pd.read_csv(path), path
    except Exception as exc:
        st.warning(f"Could not load {filename}: {exc}")
        return None, path

anomaly, anomaly_path = load_csv("gpr_anomaly_screening.csv")
fusion, fusion_path = load_csv("terrascan_sensor_fusion_demo.csv")
geo, geo_path = load_csv("terrascan_geotagged_demo.csv")
integrated, integrated_path = load_csv("terrascan_integrated_demo_report.csv")

st.warning(
    "Prototype only: YOLO detects steel/pipe objects, not leaks. GPR scores flag unusual "
    "image statistics, not confirmed defects. Acoustic/soil/magnetic scores and coordinates "
    "in the demo are simulated."
)

if anomaly is None:
    st.error("Could not find gpr_anomaly_screening.csv. Put app.py and your CSV outputs in the datasets folder.")
    st.stop()

with st.sidebar:
    st.header("Dashboard")
    st.write("Working folder:", str(BASE))
    flagged_only = st.checkbox("Show only images flagged for review", False)

overview, gpr_tab, fusion_tab, map_tab, reports_tab = st.tabs(
    ["Overview", "GPR Analysis", "Sensor Fusion", "Pipeline Map", "Reports"]
)

with overview:
    flagged = int(anomaly["flag_for_review"].fillna(False).astype(bool).sum()) if "flag_for_review" in anomaly else 0
    a, b, c = st.columns(3)
    a.metric("GPR images analyzed", len(anomaly))
    b.metric("Images flagged for review", flagged)
    c.metric("YOLO test images", 31)
    st.subheader("YOLO baseline test metrics")
    metrics = pd.DataFrame({
        "Class": ["Overall", "Steel", "Pipe"],
        "Precision": [0.428, 0.703, 0.152],
        "Recall": [0.454, 0.741, 0.167],
        "mAP@50": [0.437, 0.795, 0.0788],
        "mAP@50–95": [0.216, 0.405, 0.0276]
    })
    st.dataframe(metrics.style.format({k: "{:.1%}" for k in ["Precision", "Recall", "mAP@50", "mAP@50–95"]}), use_container_width=True, hide_index=True)
    st.error("Pipe detection is weak in this baseline. These are object-detection metrics, not leak-detection accuracy.")
    st.subheader("Found output files")
    for label, path in [("GPR screening", anomaly_path), ("Sensor fusion", fusion_path), ("Geo-tagging", geo_path), ("Integrated report", integrated_path)]:
        st.write(f"**{label}:** {path if path else 'Not found'}")

with gpr_tab:
    st.subheader("GPR statistical anomaly screening")
    data = anomaly.copy()
    if flagged_only and "flag_for_review" in data:
        data = data[data["flag_for_review"].fillna(False).astype(bool)]
    if "anomaly_score" in data:
        data = data.sort_values("anomaly_score", ascending=False)
        chart_data = data.head(20).sort_values("anomaly_score")
        fig = px.bar(chart_data, x="anomaly_score", y="image", orientation="h", title="Highest anomaly scores")
        st.plotly_chart(fig, use_container_width=True)
    st.dataframe(data, use_container_width=True, hide_index=True)
    if "image" in data and not data.empty:
        chosen = st.selectbox("Choose source GPR image", data["image"].dropna().astype(str).tolist())
        matches = [p for p in BASE.rglob(chosen) if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp"}]
        if matches:
            st.image(str(matches[0]), caption=chosen, use_container_width=True)
        else:
            st.caption("Source image not found in this folder; score details are still available.")

with fusion_tab:
    st.subheader("Sensor-fusion demo")
    if fusion is None:
        st.info("terrascan_sensor_fusion_demo.csv not found.")
    else:
        st.warning("Acoustic, soil-moisture, and magnetic values are simulated.")
        if "priority" in fusion:
            counts = fusion["priority"].value_counts().rename_axis("Priority").reset_index(name="Images")
            st.plotly_chart(px.bar(counts, x="Priority", y="Images", title="Demo priority counts"), use_container_width=True)
        st.dataframe(fusion, use_container_width=True, hide_index=True)

with map_tab:
    st.subheader("Geo-tagged demonstration map")
    if geo is None:
        st.info("terrascan_geotagged_demo.csv not found.")
    elif {"latitude", "longitude"}.issubset(geo.columns):
        st.warning("Map coordinates are simulated, not real pipeline GPS measurements.")
        coords = geo.copy()
        coords["latitude"] = pd.to_numeric(coords["latitude"], errors="coerce")
        coords["longitude"] = pd.to_numeric(coords["longitude"], errors="coerce")
        coords = coords.dropna(subset=["latitude", "longitude"])
        st.map(coords[["latitude", "longitude"]], use_container_width=True)
        st.dataframe(coords, use_container_width=True, hide_index=True)
    else:
        st.error("Latitude/longitude columns are missing.")

with reports_tab:
    st.subheader("Integrated report")
    if integrated is not None:
        st.dataframe(integrated, use_container_width=True, hide_index=True)
        st.download_button("Download integrated report", integrated.to_csv(index=False).encode(), "terrascan_integrated_demo_report.csv", "text/csv")
    else:
        st.info("Integrated report CSV not found.")
    for label, frame, filename in [
        ("GPR anomaly CSV", anomaly, "gpr_anomaly_screening.csv"),
        ("Sensor fusion CSV", fusion, "terrascan_sensor_fusion_demo.csv"),
        ("Geo-tagging CSV", geo, "terrascan_geotagged_demo.csv")
    ]:
        if frame is not None:
            st.download_button(f"Download {label}", frame.to_csv(index=False).encode(), filename, "text/csv", key=filename)

st.divider()
st.caption("TerraScan-NDT research prototype. Not a validated pipeline leak/defect diagnosis system.")
