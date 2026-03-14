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



# KPI'a

# Smoker 18 - 19 
smoker_18_19_subset = filtered_df[(filtered_df["smoker"] == "yes") & (filtered_df["age"].between(18,19))]

# 2. Werte sicher auslesen (counts.get verhindert Absturz bei 0 Treffern)
counts = smoker_18_19_subset["sex"].value_counts()
smoker_18_19_total = len(smoker_18_19_subset)
smoker_18_19_male = counts.get("male", 0)
smoker_18_19_female = counts.get("female", 0)


# Smokers 20 - 30
smoker_20_30_subset = filtered_df[ (filtered_df["smoker"] == "yes") & ( filtered_df["age"].between(20,30) )]

consts = smoker_20_30_subset["sex"].value_counts()
smoker_20_30_total = len(smoker_20_30_subset)
smoker_20_30_male = counts.get("male", 0)
smoker_20_30_female = counts.get("female", 0)


# Smokers 31 - 40
smoker_31_40_subset= filtered_df[ (filtered_df["smoker"] == "yes") & ( filtered_df["age"].between(31,40) )]

counts = smoker_31_40_subset["sex"].value_counts()
smoker_31_40_total = len( smoker_31_40_subset)
smoker_31_40_male = counts.get("male", 0)
smoker_31_40_female = counts.get("female", 0)


# # Smokers 41 - 50
smoker_41_50_subset =  filtered_df[ (filtered_df["smoker"] == "yes") & ( filtered_df["age"].between(41,50) )]

counts = smoker_41_50_subset["sex"].value_counts()
smoker_41_50_total = len( smoker_41_50_subset)
smoker_41_50_male = counts.get("male", 0)
smoker_41_50_female = counts.get("female", 0)

# # Smokers 51 - 60
smoker_51_60_subset = filtered_df[ (filtered_df["smoker"] == "yes") & ( filtered_df["age"].between(51,60) )]

counts = smoker_51_60_subset["sex"].value_counts()
smoker_51_60_total = len( smoker_51_60_subset)
smoker_51_60_male = counts.get("male", 0)
smoker_51_60_female = counts.get("female", 0)


# # Smokers 61 +
smoker_60_subset = filtered_df[ (filtered_df["smoker"] == "yes") & ( filtered_df["age"] >= 60 )]

counts = smoker_60_subset["sex"].value_counts()
smoker_60_total = len( smoker_60_subset)
smoker_60_male = counts.get("male", 0)
smoker_60_female = counts.get("female", 0)


# Beschreibungs
kpi_1, kpi_2, kpi_3 = st.columns(3)

kpi_1.write(f'<h4>All 18-19 Smoker: {smoker_18_19_total} </h4>' 
            f'<p> Male: {smoker_18_19_male}<b> | </b> Female: {smoker_18_19_female}</p>',
            unsafe_allow_html=True)


kpi_2.write(f'<h4>All 20-30  Smoker: {smoker_20_30_total} </h4>' 
            f'<p> Male: {smoker_20_30_male}<b> | </b> Female: {smoker_20_30_female}</p>',
            unsafe_allow_html=True)

kpi_3.write(f'<h4>All 31-40 Smoker: {smoker_31_40_total} </h4>' 
            f'<p> Male: {smoker_31_40_male} <b> | </b>  Female: {smoker_31_40_female}</p>',
            unsafe_allow_html=True)

st.write("##") # Erzeugt einen kleinen vertikalen Leerraum
# st.markdown("<br>", unsafe_allow_html=True)

kpi_4, kpi_5, kpi_6 = st.columns(3)

kpi_4.write(f'<h4>All 41-50 Smoker: {smoker_41_50_total} </h4>' 
            f'<p> Male: {smoker_41_50_male} <b> | </b>  Female: {smoker_41_50_female}</p>',
            unsafe_allow_html=True)


kpi_5.write(f'<h4>All 51-60 Smoker: {smoker_51_60_total} </h4>' 
            f'<p> Male: {smoker_51_60_male} <b> | </b>  Female: {smoker_51_60_female}</p>',
            unsafe_allow_html=True)

kpi_6.write(f'<h4>All 60+ Smoker: {smoker_60_total} </h4>' 
            f'<p> Male: {smoker_60_male} <b> | </b>  Female: {smoker_60_female}</p>',
            unsafe_allow_html=True)





# 1. Daten für das Diagramm zusammenstellen
chart_data = pd.DataFrame({
    "Age Group": ["18-19", "20-30", "31-40", "41-50", "51-60", "61+"],
    "Male": [smoker_18_19_male, smoker_20_30_male, smoker_31_40_male, smoker_41_50_male, smoker_51_60_male, smoker_60_male],
    "Female": [smoker_18_19_female, smoker_20_30_female, smoker_31_40_female, smoker_41_50_female, smoker_51_60_female, smoker_60_female]
})

# 2. Diagramm erstellen
fig = px.bar(
    chart_data, 
    x="Age Group", 
    y=["Male", "Female"], 
    barmode="group", # Balken nebeneinander statt übereinander
    title="Smokers by Age Group and Gender",
    labels={"value": "Count", "variable": "Gender"},
    color_discrete_map={"Male": "royalblue", "Female": "pink"} # Optionale Farben
)

# 3. In Streamlit anzeigen
st.plotly_chart(fig, use_container_width=True)


# Smokers
all_people = filtered_df["smoker"].value_counts().sum()
all_smoker = (filtered_df["smoker"] == "yes").sum()
no_smoker = filtered_df [ filtered_df["smoker"] == "no"].value_counts().sum()

col1, col2, col3 = st.columns( 3)


with col1:
    st.write(f'<h3> Smokers: <br> {all_smoker}</h3>', unsafe_allow_html= True)

with col2:
    st.write(f'<h3> No Smokers: <br> {no_smoker}</h3>', unsafe_allow_html= True)

with col3:
    st.write(f'<h3> All Data: <br> {all_people}</h3>', unsafe_allow_html= True)





# $smokers Histogram

fig_1 = px.pie(filtered_df, 
    names="smoker",   # Entspricht x="smoker" beim Histogramm
    color="smoker",   # Aktiviert die Farbtrennung
    title="Share of Smokers vs. Non-Smokers"
)
st.plotly_chart(fig_1, )






