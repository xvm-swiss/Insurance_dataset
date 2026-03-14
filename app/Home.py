import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# To run Streamlit: streamlit run app.py

# Page title
st.set_page_config(
    page_title= 'Dashboard',
    page_icon = ':bar_chart:',
    layout= 'wide'

)

df = pd.read_csv('data/cleaned data/cleaned_17_insurance.csv')



# Title 
st.markdown(
    "<h1 style='text-align: left; color: white; font-family: Times;font-size:35px'>Insurance KPI's</h1>",
    unsafe_allow_html=True
)




Age = st.sidebar.slider('Age:',
                        min_value= df["age"].min(),
                        max_value= df["age"].max(),
                        value= (df["age"].min(), df["age"].max())) 


Childrens = st.sidebar.slider('Childrens:',
                        min_value= df["children"].min(),
                        max_value= df["children"].max())


Sex = st.sidebar.multiselect( 'Sex: ',
                             options= df["sex"].unique(),
                             default= df['sex'].unique())


Smokers = st.sidebar.multiselect ('Smokers: ',
                                  options= df["smoker"].unique(),
                                  default= df["smoker"].unique())


# 1. Die gewünschte Reihenfolge festlegen
weight_order = ['Underweight', 'Normal weight', 'Overweight', 'xxl Overweight']

# 2. Nur diesen EINEN Multiselect verwenden (lösche den alten!)
Weights = st.sidebar.multiselect(
    "Weights:",
    options=weight_order,
    default=weight_order, 
)




# INfo age:
# Da der Slider für das Alter zwei Werte (Min und Max)
# in einem Tupel zurückgibt, musst du auf den Index
#  [0] und [1] zugreifen.

# Alle Filter kombiniert
filtered_df = df.query(
    'age >= @Age[0] and age <= @Age[1] and '
    'children >= @Childrens and '             # Falls du "ab X Kindern" meinst
    'sex in @Sex and '                        # 'in' für Multiselect-Listen
    'smoker in @Smokers and '
    '`Class_weights` in @Weights'
)




# ALL Unterweight
All_Underweight =filtered_df[ filtered_df["bmi"] < 18.5].value_counts().sum()

#  ALL Unterweight =  MALE
all_male_underweight = filtered_df[ filtered_df["bmi"] < 18.5] [df["sex"]=='male'].value_counts().sum()

# ALL Unterweight =  FEMALE
all_female_underweight = filtered_df[ filtered_df["bmi"] < 18.5] [df["sex"]=='female'].value_counts().sum()



# ALL Normal weight =  18.5 - 24.9 BMI
all_Normal_weight = filtered_df[ (filtered_df["bmi"] >= 18.5) & (filtered_df["bmi"] <= 24.9)] [df["sex"]== 'female'].value_counts().sum()

# Female Normal weight =  18.5 - 24.9 BMI
Normal_weight_female = filtered_df[ (filtered_df["bmi"] >= 18.5) & (df["bmi"] <= 24.9)] [df["sex"]== 'female'].value_counts().sum()

# Male Normal weight =  18.5 - 24.9 BMI
Normal_weight_male = df[ (filtered_df["bmi"] >= 18.5) & (df["bmi"] <= 24.9)] [df["sex"]== 'male'].value_counts().sum()



# All Overweight =  24.91 - 29.9 BMI
all_Overweight = filtered_df[ (df["bmi"] >= 24.91) & (df["bmi"] <= 29.9)].value_counts().sum()

# All Overweight  FEMALE =  24.91 - 29.9 BMI
all_Overweight_female = filtered_df[ (df["bmi"] >= 24.91) & (df["bmi"] <= 29.9)][df ["sex"] == 'female'].value_counts().sum()

# All Overweight MALE =  24.91 - 29.9 BMI
all_Overweight_male = filtered_df[ (df["bmi"] >= 24.91) & (df["bmi"] <= 29.9)][df ["sex"] == 'male'].value_counts().sum()



# All XXL Obesity =  > 29.91 BMI
all_XXL_Obesity = filtered_df[ (df["bmi"] > 29.91) ].value_counts().sum()

# XXL Obesity FEMALE =  > 29.91 BMI 
XXL_Obesity_female = filtered_df[ (df["bmi"] > 29.91) ][df ["sex"] == 'female'].value_counts().sum()

# XXL Obesity MALE =  > 29.91 BMI 
XXL_Obesity_male = filtered_df[ (df["bmi"] > 29.91) ][df ["sex"] == 'male'].value_counts().sum()



# All Together:
# all_bmi =  filtered_df["bmi"].value_counts().sum()
all_bmi = len(filtered_df)
all_female = filtered_df[ df["sex"] == "female"].value_counts().sum()
all_male = filtered_df[ df["sex"] == "male"].value_counts().sum()


# KPI

kpi_1, kpi_2, kpi_3 = st.columns(3)

kpi_1.write(f'<h4>Underweight:<br> {All_Underweight} </h4>'
            f'<p> Male: {all_male_underweight}<b> | </b> Female: {all_female_underweight}</p>',
            unsafe_allow_html= True)


kpi_2.write(f'<h4>Normalweight:<br> {all_Normal_weight} </h4>'
            f'<p> Male: {Normal_weight_male}<b> | </b> Female: {Normal_weight_female}</p>',
            unsafe_allow_html= True)

kpi_3.write(f'<h4>Overweight:<br> {all_Overweight} </h4>'
            f'<p> Male: {all_Overweight_male}<b> | </b> Female: {all_Overweight_female}</p>',
            unsafe_allow_html= True)



# Abstand
st.write('##')

kpi_4, kpi_5 , kpi_6= st.columns(3)

kpi_4.write(f'<h4>XXL Obesity:<br> {all_XXL_Obesity} </h4>'
            f'<p> Male: {XXL_Obesity_male}<b> | </b> Female: {XXL_Obesity_female}</p>',
            unsafe_allow_html= True)

kpi_5.write(f'<h4>XXL Obesity:<br> {all_bmi} </h4>'
            f'<p> Male: {all_male}<b> | </b> Female: {all_female}</p>',
            unsafe_allow_html= True)

# For Histogramm

# # 1. Underweight
# df.loc[df["bmi"] < 18.5, 'Class weights'] = 'Underweight'

# # 2. Normal weight
# df.loc[(df["bmi"] >= 18.5) & (df["bmi"] <= 24.9), 'Class weights'] = 'Normal weight'

# # 3. Overweight
# df.loc[(df["bmi"] >= 25.0) & (df["bmi"] <= 29.9), 'Class weights'] = 'Overweight'

# # 4. xxl Overweight or Adipositas
# df.loc[df["bmi"] >= 30.0, 'Class weights'] = 'xxl Overweight'


fig = px.histogram( filtered_df, x="Class_weights",color= "Class_weights",
                   title= "BMI: Unterweight, Normal weight, Overweight and XXL Overweight")

st.plotly_chart(fig, )


# # 1. Filtern
# filtered_df = df.query(
#     'age >= @Age[0] and age <= @Age[1] and '
#     'sex in @Sex and '
#     'smoker in @Smokers and '
#     '`Class_weights` in @Weights'
# )

# 2. Prüfen, ob Daten übrig sind
if filtered_df.empty:
    st.error("🚫 Keine Daten gefunden! Bitte passe deine Filter in der Sidebar an.")
else:
    # Hier kommen deine Diagramme oder Tabellen rein
    st.success(f"✅ {len(filtered_df)} Datensätze ausgewählt.")
    st.dataframe(filtered_df)

    # Beispiel für ein Chart (nur wenn Daten da sind!)
    # st.bar_chart(filtered_df['age'])
