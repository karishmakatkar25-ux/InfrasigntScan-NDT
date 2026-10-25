# InfrasightScan-NDT
### AI-Powered Multi-Sensor Screening Prototype for Buried Pipeline Inspection

## 1. Project Overview

InfrasightScan-NDT is an AI-powered pipeline inspection prototype designed to support the screening and prioritization of potential anomalies in buried water pipelines. The project explores the use of Ground Penetrating Radar (GPR) imagery, computer vision, anomaly screening, multi-sensor data fusion, and geospatial visualization to assist pipeline inspection workflows.

Underground water pipelines are difficult to inspect because they are concealed beneath soil and may be affected by leakage, corrosion, structural deterioration, or other defects. Conventional inspection can require significant time, specialized equipment, and field investigation. This project investigates how AI-assisted analysis and integrated sensor information could help identify areas that deserve further inspection.

The current implementation demonstrates the software workflow using an available GPR image dataset, a YOLO-based object-detection model, statistical anomaly screening, simulated auxiliary sensor readings, and demonstration geospatial coordinates.

## 2. Problem Statement

Buried water pipeline networks require reliable inspection and maintenance, but locating and prioritizing potential problem areas can be challenging. Large volumes of inspection data may require manual interpretation, and information from different sensing technologies can be difficult to analyze together.

The objective of this project is to develop a prototype that processes GPR images, highlights unusual image patterns, combines screening results with additional sensor-related inputs, and presents the outputs through an interactive dashboard for easier interpretation.

## 3. Proposed Solution

The proposed workflow combines computer vision, statistical anomaly screening, sensor-fusion scoring, and map-based visualization.

- **GPR Image Analysis:** Uses a YOLO-based object-detection model to identify the dataset's annotated classes, including steel and pipe.
- **Anomaly Screening:** Extracts image characteristics such as grayscale intensity, intensity variation, and edge density to flag unusual images for review.
- **Confidence Scoring:** Reports YOLO detection confidence scores to help users understand the model's confidence in its predicted objects.
- **Sensor-Fusion Demonstration:** Combines GPR anomaly scores with simulated acoustic, soil-moisture, and magnetic scores to demonstrate how multiple inputs could be used to prioritize inspection.
- **Geospatial Visualization:** Displays demonstration locations to illustrate how inspection priorities could be represented geographically.
- **Interactive Dashboard:** Presents analysis outputs, model evaluation metrics, anomaly screening results, fusion scores, and reports in one interface.

## 4. Technology Stack

- **Programming Language:** Python
- **Computer Vision:** OpenCV
- **Object Detection:** Ultralytics YOLO
- **Model Framework:** PyTorch
- **Data Processing:** Pandas and NumPy
- **Dashboard:** Streamlit
- **Visualization:** Plotly and Folium, where used
- **Development Environment:** Visual Studio Code and Jupyter Notebook
- **Version Control:** Git and GitHub

## 5. Project Workflow

1. Load and inspect the available GPR image dataset.
2. Prepare the dataset configuration and annotations for object detection.
3. Train and evaluate a YOLOv8n baseline model.
4. Generate predictions and extract object-detection confidence scores.
5. Calculate statistical anomaly-screening scores from GPR image characteristics.
6. Demonstrate sensor fusion using GPR anomaly scores and simulated auxiliary sensor values.
7. Associate selected demonstration results with simulated coordinates.
8. Visualize outputs and reports through the Streamlit dashboard.
9. Store the source code, notebook, configuration, and selected output files in GitHub.

## 6. Model Evaluation

The initial YOLOv8n baseline was trained for five epochs and evaluated on the available test set.

Reported overall evaluation metrics:

- **Precision:** 0.428
- **Recall:** 0.454
- **mAP@50:** 0.437
- **mAP@50–95:** 0.216

Performance varied considerably between classes. The model performed better on the steel class than on the pipe class. These results represent object detection on the supplied dataset and should not be interpreted as verified pipeline-leak detection accuracy.

The anomaly-screening component is a statistical heuristic. Its flagged images are candidates for further investigation, not confirmed defects.

## 7. Dashboard Features

The dashboard provides a consolidated interface for exploring the prototype's outputs, including:

- Project overview and available analysis summaries
- GPR anomaly-screening results
- Object-detection evaluation metrics
- Sensor-fusion demonstration scores and priority categories
- Geospatial demonstration visualization
- Downloadable or reviewable analysis reports, depending on the generated files

## 8. Current Limitations

This repository contains a research and demonstration prototype rather than a validated field-deployed pipeline inspection system.

- Auxiliary acoustic, soil-moisture, and magnetic values used in the fusion demonstration are simulated.
- The demonstration coordinates are simulated and are not actual GPS measurements.
- Statistical anomaly scores do not directly establish the presence of a leak, crack, or corrosion.
- YOLO confidence values represent model confidence in predicted objects; they are not calibrated probabilities of pipeline defects.
- The current model has limited performance on the pipe class and requires further dataset preparation, training, and validation.
- Actual sensor integration, field trials, and independent ground-truth verification are required before making operational claims.

## 9. Future Scope

Potential future improvements include:

- Integration of real GPR, acoustic, magnetic, and soil-related sensor measurements
- Collection of accurately labeled pipeline defect and non-defect data
- Improved model training and class-specific performance
- Sensor-fusion methods calibrated against real inspection outcomes
- Real GPS integration and GIS-based pipeline mapping
- Field validation and evaluation against verified inspection results
- Deployment of a more robust interface for inspection teams

## 10. Repository Contents

The repository contains the project files that were selected for version control, including the analysis notebook, dashboard application, supporting configuration files, and available generated reports.

Large raw datasets and trained model weights may be excluded from the GitHub repository and may need to be obtained or generated separately.

## 11. Running the Dashboard

1. Install Python and Git.
2. Clone the repository:

   `git clone https://github.com/karishmakatkar25-ux/InfrasigntScan-NDT.git`

3. Open the cloned folder in Visual Studio Code.
4. Install the dashboard dependencies using the provided requirements file:

   `python -m pip install -r requirements.txt`

5. Start the dashboard:

   `python -m streamlit run app.py`

6. Open the local URL displayed in the terminal.

Ensure the required CSV reports are available in the expected project folders. If the notebook, dataset, or model weights are needed for a particular workflow, provide those separately and update the relevant file paths.

## 12. Conclusion

InfrasightScan-NDT demonstrates a potential software workflow for AI-assisted screening and visualization of buried pipeline inspection data. By combining GPR image analysis, statistical anomaly screening, object-detection confidence, simulated multi-sensor fusion, and geospatial presentation, the prototype provides a foundation for further research into intelligent pipeline inspection.

The next stage is to integrate real sensor measurements, improve the detection model, and validate the complete workflow against verified field data.

**Project Status:** Prototype / Research Demonstration  
**Repository:** https://github.com/karishmakatkar25-ux/InfrasigntScan-NDT
