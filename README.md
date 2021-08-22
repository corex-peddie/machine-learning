# Folder Overview 📔
- **`/Data-Notebooks`** 
  - Contains the Jupyter Notebooks used for Data Analysis and ML Model Construction
- **`/ML-App`**
  - Contains source code for the [CoreX Analysis App](https://share.streamlit.io/corex-peddie/machine-learning/ML-App/app.py) (ML App Development)
# ML Model Construction 📈
Tools Used: Python, Jupyter Notebooks, Scikit-Learn, Numpy, Pandas, and Plotly
- `finance-forecast.ipynb` contains the two Linear Regression models used for predicting future profits and expenses
  - Data for this model was gained on Datalab and modified/cleaned for custom use 
- `website-visitors.ipynb` contains a RandomForestRegressor used to predict the performance of an E-Commerce website in the future
  - Data for this model was gained on Kaggle which used Google Analytics to obtain visitor data
- `/Models` contains all the models in the form of a saved file (used on the app)
# ML App Development 🖥
Tools Used: Python, Streamlit, and Joblib
- `/Data` contains CSV files for tables and the previously developed ML Models
- `/Components` contains pages for the app (finance analysis, seo analysis, and about)
- `app.py` contains the main section for the app such as navigation and page routing
- `multiapp.py` contains the code used to build multiple pages with Streamlit
- `requirements.txt` contains the libraries and packages needed to be installed when the app is hosted
