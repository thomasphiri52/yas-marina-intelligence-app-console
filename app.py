import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Yas Marina Marketing Intelligence Console", layout="wide")
st.title("YAS MARINA — Marketing Intelligence Stream Console")
st.caption("LIVE MARKETING COMMAND CENTER • Problem Detection • Gap Intelligence")

if "streaming" not in st.session_state:
    st.session_state.streaming = True

c1,c2,c3,c4=st.columns(4)
c1.metric("Visitors", "24,680", "+8.4%")
c2.metric("Campaigns", "87", "-3.2%")
c3.metric("Events", "14", "+12.1%")
c4.metric("Live Alerts", "4", "Needs attention")

st.divider()
st.subheader("🚨 Problem & Gap Intelligence")
gaps = [
    ("Visitor Conversion", "8.4%", "12%", "-3.6 pp", "CRITICAL"),
    ("Campaign Engagement", "4.9%", "6.0%", "-18%", "CRITICAL"),
    ("Event Registrations", "7,200", "10,000", "-2,800", "HIGH"),
    ("Customer Data Completeness", "62%", "90%", "-28 pp", "MEDIUM"),
]
st.table({"Area":[x[0] for x in gaps],"Actual":[x[1] for x in gaps],"Target":[x[2] for x in gaps],"Gap":[x[3] for x in gaps],"Severity":[x[4] for x in gaps]})

a,b=st.columns(2)
with a:
    st.subheader("🔎 Root-Cause Intelligence")
    st.write("• Campaign → Audience → Channel → Customer journey")
    st.write("• Compare performance by channel, audience and event")
    st.write("• Flag contributing signals for investigation")
with b:
    st.subheader("💡 Opportunity Intelligence")
    st.write("• 7 opportunities detected")
    st.write("• Identify high-performing audiences")
    st.write("• Highlight channels requiring attention")

st.divider()
st.subheader("⚡ Live Alerts")
for alert in [
    "Campaign performance below target",
    "Visitor conversion declining",
    "Event registration gap detected",
    "Customer data completeness below target",
]:
    st.warning(alert)

st.subheader("✅ Action & Measurement")
st.write("Investigate → Act → Measure → Resolve")
st.progress(0.72, text="Issues under investigation: 72% tracked")

st.sidebar.header("Control Room")
st.sidebar.success("● STREAMING" if st.session_state.streaming else "○ PAUSED")
if st.sidebar.button("Pause / Resume Stream"):
    st.session_state.streaming = not st.session_state.streaming
st.sidebar.divider()
st.sidebar.write("Modules")
for m in ["Live Dashboard","Problem & Gap Intelligence","Root-Cause Intelligence","Opportunity Intelligence","AI Insights","Campaign Intelligence","Event Intelligence","Alerts","Action Tracking","Executive Reporting","Admin"]:
    st.sidebar.write("• "+m)

st.caption("Updated console architecture: LIVE DATA → DETECT → EXPLAIN → ALERT → ACT → MEASURE → IMPROVE")
