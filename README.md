# LogiStream: Cold-Chain Logistics Monitoring (Lambda Architecture)
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/0271da20-dc26-413e-8679-54e85bfd0fb1" />



## 1. Project Overview
**LogiStream** is a real-time data engineering pipeline designed to monitor **cold-chain logistics** for perishable goods across Kenya. The system is built using a **Lambda Architecture**, combining real-time responsiveness with long-term accuracy.

This approach balances:
- **Sub-second emergency alerts** (Speed Layer)  
- **100% accurate historical audits** (Batch Layer)  

The result is a resilient system capable of preventing spoilage *and* supporting long-term operational analytics.

---

## 2. Problem Statement
In cold-chain logistics, a single refrigeration failure in a truck transporting **milk, flowers, or vaccines**—for example from **Naivasha to Mombasa**—can result in **millions of shillings in losses**.

Traditional batch-only systems detect failures **after delivery**, when it’s already too late.

**LogiStream solves this by:**
- Detecting **temperature spikes in milliseconds** to trigger immediate alerts.
- Persisting **every sensor reading** for fuel efficiency analysis, driver behavior auditing, and compliance reporting.

---

## 3. Tech Stack & Infrastructure
- **Ingestion:** Python (Simulated IoT Truck Sensors)  
- **Message Broker:** Apache Kafka (Event Streaming Backbone)  

### Lambda Architecture Layers
- **Speed Layer (Real-Time):** Redis  
  - In-memory storage for sub-second alerts and dashboard updates  
- **Batch Layer (Historical):** PostgreSQL  
  - Relational storage for long-term auditing and the single source of truth  

### Supporting Tools
- **Orchestration:** Docker Compose & Python Subprocess  
- **Visualization:**  
  - Streamlit (Operational Monitoring Dashboard)  
  - pgAdmin 4 (Database Management & Auditing)

---

## 4. System Architecture
LogiStream operates through **three coordinated layers**, each with a distinct responsibility:

### Ingestion Layer
- **`truck_sensors.py`**  
  - Simulates IoT sensors on refrigerated trucks  
  - Continuously emits telemetry data including:
    - Temperature  
    - Fuel Levels  
    - GPS Location  
  - Publishes events to Kafka topics

### Speed Layer (Real-Time Intelligence)
- **`stream_processor.py`**  
  - Consumes events from Kafka in real time  
  - Applies business rules (e.g., temperature > **7°C**)  
  - Instantly updates Redis to:
    - Trigger alerts  
    - Power live dashboards  

### Batch Layer (Historical Truth)
- **`data_bridge.py`**  
  - Acts as a persistent Kafka consumer  
  - Archives every raw event into PostgreSQL  
  - Enables:
    - Regulatory compliance  
    - Fuel consumption analysis  
    - Long-term performance reporting  

---

## 5. Why Lambda Architecture?
- **Speed Layer:** Saves the cargo *now*  
- **Batch Layer:** Explains *why* it happened later  

By separating immediate decision-making from long-term analytics, LogiStream delivers both **operational safety** and **data integrity**, making it ideal for mission-critical logistics systems.
