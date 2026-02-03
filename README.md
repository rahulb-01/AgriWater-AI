# AgriWater AI – Smart Irrigation and Water Monitoring System 🌱

## About
AgriWater AI is an intelligent, AI-driven irrigation and water monitoring system designed to optimize water usage in agriculture. The system uses Machine Learning to analyze soil moisture, temperature, and humidity data and predict whether irrigation is required. By providing data-driven irrigation recommendations, AgriWater AI helps reduce water wastage, improve crop health, and promote sustainable farming practices.

The platform is built as a web-based application using Django and Machine Learning models. It includes secure user authentication, a real-time dashboard for sensor data input, and analytics for monitoring soil moisture trends. Currently, sensor data is simulated through manual input, allowing the system to function without physical hardware. The architecture is designed to support future integration with real IoT sensors for practical deployment.

AgriWater AI aims to bridge the gap between traditional irrigation methods and modern smart agriculture by combining AI intelligence with scalable web technologies.

---

## Features
- AI-based irrigation prediction using Machine Learning  
- Secure user authentication (Login and Registration)  
- Dashboard for real-time sensor data input and irrigation decision  
- Analytics and visualization of soil moisture trends  
- Storage of historical sensor data for monitoring and analysis  
- Modular and scalable system architecture  
- Future-ready design for IoT sensor integration  

---

## Requirements

### Operating System
- Windows 10/11 or Linux

### Development Environment
- Python 3.9 or higher  
- Virtual environment (recommended)

### Frameworks and Libraries
- Django  
- Scikit-learn  
- Joblib  
- Pandas  
- NumPy  

### Frontend Technologies
- HTML  
- CSS  
- Chart.js  

### Database
- SQLite (used for development and testing)

### Tools
- VS Code or PyCharm  
- Git and GitHub for version control  

---

## System Architecture

### Current Workflow (Simulation Phase)
### Future Workflow (IoT Integration)
## Outputs

### Output 1 – User Authentication (Login & Register)
The system provides secure user authentication through login and registration modules. New users can register with valid credentials, and existing users can securely log in to access the dashboard and analytics features. Authentication ensures that sensor data and analytics are user-specific and protected.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/262faeba-e233-4286-bf30-6b45e2901adf" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/5f76623a-968d-4e99-8646-3e29baacc9e1" />


### Output 2 – Dashboard & Irrigation Prediction
The dashboard allows authenticated users to input soil moisture, temperature, and humidity values. Based on these inputs, the integrated machine learning model predicts whether irrigation is required, providing real-time decision support.
<img width="1919" height="1078" alt="image" src="https://github.com/user-attachments/assets/374484e6-aff0-4a30-aa18-3f7a155cf9e7" />

### Output 3 – Analytics Visualization
The analytics module displays soil moisture trends over time using graphical charts. This visualization helps users understand historical sensor data patterns and supports better irrigation planning.
<img width="1919" height="1078" alt="image" src="https://github.com/user-attachments/assets/5c1b953e-51e2-4a79-a305-9343cce1d713" />

### Output 4 – Data Storage
All sensor readings, predictions, and timestamps are securely stored in the database. This enables historical monitoring, analytics generation, and future data-driven improvements.
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/1fcfec9a-4d7f-44a5-9114-49de4b1efc5a" />


## System Output Summary
AgriWater AI generates intelligent irrigation recommendations based on machine learning predictions. The system stores sensor data securely, provides real-time visualization, and supports scalable expansion for real-world agricultural applications.

---

## Note
The current implementation simulates sensor data through manual input and is intended for academic and prototype purposes. The system provides decision support and is not an automated irrigation controller. Real-world deployment requires physical IoT sensors and field calibration.

## Future Scope
- Integration with real IoT soil moisture, temperature, and humidity sensors  
- Automatic irrigation control using actuators  
- Weather API integration for enhanced prediction accuracy  
- Cloud deployment for large-scale agricultural monitoring  

---

## Results and Impact
The development of AgriWater AI demonstrates the effective application of Machine Learning in smart agriculture. Testing and simulations show accurate irrigation predictions and meaningful analytics, highlighting the system’s potential to reduce water wastage, improve crop yield, and support sustainable farming practices.

--- 

## Articles Published / References

[1] FAO, “Water Use in Agriculture and Sustainable Irrigation Practices,” Food and Agriculture Organization of the United Nations, 2021.

[2] Kamilaris, A., Kartakoullis, A., & Prenafeta-Boldú, F. X., “A Review on the Practice of Big Data Analysis in Agriculture,” Computers and Electronics in Agriculture, 2017.

[3] Liakos, K. G., Busato, P., Moshou, D., Pearson, S., & Bochtis, D., “Machine Learning in Agriculture: A Review,” Sensors, 2018.

[4] World Health Organization (WHO), “Artificial Intelligence in Sustainable Development,” WHO Publications, 2021.
