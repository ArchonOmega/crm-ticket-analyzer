\# 📊 CRM Support Ticket Analyzer



!\[Streamlit](https://img.shields.io/badge/Live%20App-Online-success?style=flat-square\&logo=streamlit\&color=brightgreen)



\*\*🔗 Live App:\*\* \[https://yourusername.streamlit.app](https://yourusername.streamlit.app)  

\*\*🔗 GitHub Repo:\*\* \[https://github.com/ArchonOmega/crm-ticket-analyzer](https://github.com/ArchonOmega/crm-ticket-analyzer)



---



A lightweight web app to help support teams visualize, track, and flag customer support tickets from any CRM system.



\### 💡 Features



\- 📁 Upload CSV ticket exports from Zoho, Salesforce, etc.

\- 📊 View tickets by Category, Priority, and Status

\- 🚩 Auto-flag unresolved high-priority tickets

\- 📈 Interactive visual charts (Pie + Bar) with Plotly

\- 🌐 Built using Streamlit and ready to deploy anywhere



\### 🗂️ Sample CSV Format



```csv

TicketID,Subject,Description,Category,Priority,Status,CreatedDate,ResolvedDate

1001,Login Error,User cannot login to account,Login,High,Open,2025-07-01,

...



Tech Stack

Python 3.10+



Streamlit



Pandas



Plotly



Run Locally:
git clone https://github.com/ArchonOmega/crm-ticket-analyzer.git

cd crm-ticket-analyzer

pip install -r requirements.txt

streamlit run app.py



