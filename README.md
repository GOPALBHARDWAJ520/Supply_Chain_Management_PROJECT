# 🏭 Supply Chain Management: ML / FA / DA Project

## 📌 Project Overview
This project aims to develop a **Demand Forecasting Model** using machine learning techniques to optimize supply chain operations for a fashion and beauty startup. The project leverages data analytics and forecasting to improve efficiency, reduce stockouts, and manage inventory more effectively.

---

## 📂 Tools & Technologies
- Python
- Machine Learning (TensorFlow / Keras)
- SQL
- Microsoft Excel
- Streamlit (for dashboard visualization)

---

## 📊 Dataset
The dataset includes real-world supply chain data from a fashion and beauty startup. It consists of features like:

- Product Type, SKU, Price, Availability
- Number of Products Sold, Revenue Generated
- Customer Demographics
- Stock Levels, Lead Times, Order Quantities
- Shipping Times, Costs, Carriers, Routes
- Supplier Name, Location
- Manufacturing Lead Time & Costs
- Defect Rates, Inspection Results
- Transportation Modes and Sustainability Metrics

🔗 [Download Dataset](https://drive.google.com/file/d/1LzRgcmiPu-D1e1sPNIDvkr57C4mGzdLH/view?usp=sharing)

<br>
<img width="1844" height="773" alt="image" src="https://github.com/user-attachments/assets/f5966305-a910-42ee-b181-33b643bda098" />
<br><br>

---

## 🧠 Project Steps

### 1️⃣ Data Preprocessing
- Handled missing values and cleaned the dataset
- Feature Engineering (e.g., extracting Month, DayOfWeek, Quarter from date)
- One-hot encoding for categorical features
- Standardization using `StandardScaler`
- Train-test split for model training

### 2️⃣ Model Building
A Neural Network model was built using Keras:

```python
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=[X_train_scaled.shape[1]]),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)
])
```

- Optimizer: Adam
- Loss Function: Mean Squared Error (MSE)
- Trained for 50 epochs with 20% validation split

### 3️⃣ Model Evaluation
- Evaluated using MSE on test set
- Visualized predictions vs actual sales
- Example prediction using new data

### 4️⃣ Model Deployment
- Model saved as `demand_forecasting_model.h5`
- Demonstrated how to load and predict with new input

---

## 📈 Exploratory Data Analysis (EDA)
- Descriptive stats, bar plots, and line charts for key metrics
- Revenue vs. Cost, Stock Levels, Transportation Costs
- Visualizations for Shipping Carriers, Routes, Supplier-wise Costs

### 📊 Dashboard
An interactive **Streamlit Dashboard** was created for real-time visualization and monitoring.

🔗 [Explore Streamlit Dashboard](https://analyticsforfashionsupplymanagement.streamlit.app/)

---





## ✅ Key Outcomes
- Built a predictive model to forecast future product demand
- Improved understanding of supply chain KPIs
- Developed visual tools to support data-driven decision-making
- Enabled better inventory and resource planning

---

## 📎 References
- GitHub: [Supply Chain ML Project](https://github.com/RILUCK/Supply-Chain-Management-Machine-Learning)
- Dashboard Code Sample: [Kaggle Notebook](https://www.kaggle.com/code/yaminh/supply-chain-analysis-with-dashboard)

---

## 📌 Conclusion
This project demonstrates how machine learning can be applied to real-world supply chain challenges. With the demand forecasting model and visual dashboards, companies can enhance operational efficiency, lower costs, and improve customer satisfaction.

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/supply-chain-ml-project.git
   cd supply-chain-ml-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run Jupyter Notebook or Python scripts to preprocess data and train model.

4. Launch the Streamlit dashboard (optional):
   ```bash
   streamlit run dashboard.py
   &
   python--m-streamlit-run-advanced_dashboard.py
   ```

---

## ✍️ Author
**Gopal Bhardwaj**  
Domain: Data Analyst | Machine Learning | Supply Chain  
