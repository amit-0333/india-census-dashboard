<div align="center">

```
██╗███╗   ██╗██████╗ ██╗ █████╗      ██████╗███████╗███╗   ██╗███████╗██╗   ██╗███████╗
██║████╗  ██║██╔══██╗██║██╔══██╗    ██╔════╝██╔════╝████╗  ██║██╔════╝██║   ██║██╔════╝
██║██╔██╗ ██║██║  ██║██║███████║    ██║     █████╗  ██╔██╗ ██║███████╗██║   ██║███████╗
██║██║╚██╗██║██║  ██║██║██╔══██║    ██║     ██╔══╝  ██║╚██╗██║╚════██║██║   ██║╚════██║
██║██║ ╚████║██████╔╝██║██║  ██║    ╚██████╗███████╗██║ ╚████║███████║╚██████╔╝███████║
╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝
```

### 🇮🇳 India Census Analytics Dashboard

> An interactive geospatial dashboard exploring demographic, education, employment, and digital connectivity trends across Indian districts — built with Streamlit, Pandas, and Plotly.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

</div>

---

## 📌 About

This is my **India Census Analytics Dashboard** — an interactive geospatial data app built using Streamlit, exploring district-level census data across India.

The dashboard lets you filter by state, choose primary and secondary parameters, and visualise them on an interactive bubble map — alongside key summary metrics and a top-10 district leaderboard.

Built to practice:
- Geospatial visualisation with Plotly's scatter mapbox
- Building interactive, parameter-driven Streamlit dashboards
- Working with Indian census data (literacy rate, sex ratio, population, internet access, etc.)

---

## 🎬 Demo

https://github.com/amit-0333/india-census-dashboard/blob/main/dashbboard.mp4

---

## 📸 Screenshot

![Dashboard Overview](dashoard.png)

---

## 📊 Dashboard Features

- 🗺️ State selector — view Overall India or drill into a specific state
- 🔵 Interactive bubble map — bubble **size** and **color** mapped to user-selected parameters
- 📈 KPI cards — Districts count, Avg Literacy Rate, Avg Sex Ratio
- 🏆 Top 10 districts table by selected primary parameter
- 🎛️ 10 selectable metrics: Population, Male, Female, Literate, Households with Internet, Literacy Rate, Sex Ratio, Workers, Households with Computer, Total Power Parity

---

## 🗺️ Project Structure

```
india-census-dashboard/
│
├── 📄 app.py                    # Main Streamlit app
├── 📄 India_Dashboard_.csv      # Census dataset
├── 🎬 dashbboard.mp4            # Dashboard demo video
├── 🖼️ dashoard.png              # Dashboard screenshot
├── 📄 requirements.txt
└── 📄 README.md
```

---

## ⚙️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/amit-0333/india-census-dashboard.git

# 2. Navigate into the folder
cd india-census-dashboard

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python** | Core language |
| 🎈 **Streamlit** | Dashboard UI and interactivity |
| 🐼 **Pandas** | Data handling |
| 📊 **Plotly** | Interactive bubble maps |

---

## 👨‍💻 Author

**Amit Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-amit--0333-181717?style=flat&logo=github)](https://github.com/amit-0333)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/amit-kumar-a62a3640a/)

---

<div align="center">

> 📝 *Built as part of my Data Science and Python learning journey.*

⭐ **Star this repo if you found it useful!**

</div>
