import streamlit as st
import redis
import time

st.title("🚛 LogiStream: Live Fleet Monitor")
r = redis.Redis(host='localhost', port=6379, db=0)

# Create two columns for the dashboard
col1, col2 = st.columns(2)

while True:
    with col1:
        t1 = r.get("temp:TRUCK-001")
        st.metric("Truck 001 Temp", f"{float(t1) if t1 else 0}°C")
    with col2:
        t2 = r.get("temp:TRUCK-002")
        st.metric("Truck 002 Temp", f"{float(t2) if t2 else 0}°C")
    
    time.sleep(1)
    st.rerun()