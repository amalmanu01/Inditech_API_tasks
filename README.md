I have used Visual Code Studio

Install dependencies:
pip install requests

check python version
python --version
If it is Python < 3.10.xx is good ,if not install

API=http://api.petpooja.com/V1/orders/get_sales_data/?app_key=srd2neaq1xg7bzc6uyk5jmwv98o4tpfh&app_secret=fd08934c5224af4c975015e599d60a74bf857b4a&access_token=0442e1ee9899bc3806f1a40be490af4ec5c6602a&restID=51wok2zxnsad&from_date=2025-01-20%2000:00:00&to_date=2025-01-20%2023:59:59

i have changed the api code as above due to some space issues in from and to date (YYYY-MM-DD HH:MM:SS)
fetch_data.py file is basically connects to the Petpooja API and converts the JSON response to Python
fetch_task2.py file created the sales_data.db and properly stored the data form the API 
