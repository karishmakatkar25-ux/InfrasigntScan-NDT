TERRASCAN-NDT DASHBOARD — QUICK START

1. Extract app.py and requirements.txt into:
   C:\Users\karis\OneDrive\Desktop\datasets

2. Make sure these CSV files are in that folder (or a subfolder):
   gpr_anomaly_screening.csv
   terrascan_sensor_fusion_demo.csv
   terrascan_geotagged_demo.csv
   terrascan_integrated_demo_report.csv

3. Open VS Code terminal in the datasets folder and run:
   python -m pip install -r requirements.txt

4. Start the dashboard:
   python -m streamlit run app.py

5. Open the Local URL shown in the terminal if the browser does not open automatically.

Note: sensor values and GPS coordinates are simulated. GPR anomaly scores are statistical flags, not confirmed defects. YOLO metrics measure steel/pipe object detection, not leak detection.
