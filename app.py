
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Washroom Tracker",
    page_icon="🚻",
    layout="wide"
)

st.title("🚻 Washroom Tracker")
st.caption("Smart Washroom Management System")

if "records" not in st.session_state:
    st.session_state.records = []

st.subheader("Washroom Status")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Entries", len(st.session_state.records))

with col2:
    st.metric(
        "Available",
        sum(1 for r in st.session_state.records if r["status"] == "Available")
    )

st.divider()

st.subheader("Update Washroom Status")

with st.form("washroom_form"):
    washroom = st.selectbox(
        "Select Washroom",
        ["Washroom 1", "Washroom 2", "Washroom 3"]
    )

    status = st.selectbox(
        "Current Status",
        ["Available", "Occupied", "Cleaning Required"]
    )

    floor = st.selectbox(
        "Select Floor",
        ["Ground Floor", "First Floor", "Second Floor"]
    )

    submitted = st.form_submit_button("Update Status")

    if submitted:
        st.session_state.records.append({
            "washroom": washroom,
            "floor": floor,
            "status": status,
            "time": datetime.now().strftime("%d-%m-%Y %H:%M")
        })
        st.success("Washroom status updated successfully!")

st.divider()

st.subheader("Washroom Records")

if st.session_state.records:
    st.dataframe(
        st.session_state.records,
        use_container_width=True
    )
else:
    st.info("No records available yet.")

if st.button("Clear All Records"):
    st.session_state.records = []
    st.rerun()
