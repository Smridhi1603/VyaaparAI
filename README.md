# 🧠 Vyaapar AI - Inventory & Demand Forecasting for Cosmetics

**Vyaapar AI** is an AI-powered solution designed for retailers and businesses to forecast demand and optimize inventory for cosmetic products such as skincare, bodycare, and haircare items. It uses XGBoost-based machine learning models trained on historical sales data to generate accurate future insights, detect sales trends, and automate inventory alerts.

---

## ✨ Key Features

- 🔮 **Demand Forecasting** using XGBoost
- 📈 **Visual Insights** for trends, seasonality, and product-level analytics
- ⚡ **Quick Insights** into sales performance and future predictions
- 📦 **Inventory Logs** for stock alerts, reorder levels, and demand gaps
- 🧠 Smart feature engineering with time-aware lag features
- ✅ Simple to use and extensible for more product categories

---

## 📂 Project Structure

FORECASTING_SYSTEM/
│
├── .streamlit/                      # Streamlit config folder
├── jupyter file/                    # Notebooks for data exploration and modeling
│   ├── cosmetic_bodycare_...ipynb
│   ├── month_forecasting.ipynb
│
├── pages/                           # Streamlit pages
│   ├── cosmetic_bodycare_...xlsx    # Dataset in Excel format
│   ├── Inventory_Log.py             # Stock risk detection and alerts
│   ├── Quick_Forecast.py            # Forecasting insights (text-based)
│   ├── Visual_Insights.py           # Forecasting insights (graphs and visuals)
|   ├── Vyaapar_Bot.py               # AI-powered assistant using RAG
|
├── Home.py                          # Streamlit landing page
├── pic.jpg                          # Optional image asset
├── README.md          