import subprocess
import time
import sys

# Update this list with your NEW LogiStream filenames
scripts = ["truck_sensors.py", "stream_processor.py", "data_bridge.py"]
processes = []

print("🚀 Starting the LogiStream Lambda Pipeline...")

# 1. Start your standard Python scripts
for script in scripts:
    # 'sys.executable' ensures we use the same Python you are currently using
    p = subprocess.Popen([sys.executable, script])
    processes.append(p)
    print(f"✅ Started {script}")
    time.sleep(2) 

# 2. Start the Streamlit Dashboard (The Visualization Layer)
print("📈 Launching Dashboard...")
dash = subprocess.Popen([sys.executable, "-m", "streamlit", "run", "dashboard.py"])
processes.append(dash)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Shutting down LogiStream...")
    for p in processes:
        p.terminate()
    print("✅ System cleaned up.")