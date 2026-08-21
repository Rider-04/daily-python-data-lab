import pandas as pd
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")
def agent_effort(I):
    return 10*(1-np.exp(-I/400))
def agent_proba(eff):
    return 0.20(1-np.exp(-eff/5))
def rev(premium, probability, agent_prob, I):
    return premium * (probability + agent_prob)-I
data = pd.read_csv(r"C:\Users\lenovo\OneDrive\Desktop\Folder\daily-python-data-lab\04_machine_learning\Classification\train (2).csv")
data = data.drop(columns=["id","renewal"])
imputer = joblib.load("Simple_Imputer.pkl")
num_col = data.describe().columns
data[num_col]=imputer.transform(data[num_col])
data["Total_late"] =data['Count_3-6_months_late']+data['Count_6-12_months_late']+data['Count_more_than_12_months_late']
print(data.columns)

model = joblib.load("renewal_pipeline.pkl")
prediction=model.predict_proba(data[['perc_premium_paid_by_cash_credit', 'age_in_days', 'Income',
       'Total_late', 'application_underwriting_score','no_of_premiums_paid', 'premium', 'residence_area_type','sourcing_channel']])
print(prediction)

premium = list(data["premium"])

for j in range(len(premium)):
    pre=premium[i]
    base_prob=prediction[i][1]
    for i in range(500,5000,500):
        eff = agent_effort(i)
        prob = agent_proba(eff)
        revenue = rev(pre,base_prob,prob,i)

