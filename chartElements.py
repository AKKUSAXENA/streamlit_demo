import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly
import pydeck as pdk

# line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)
st.line_chart(chart_data)

# Area Chart

chart_Data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)
st.area_chart(chart_Data)

# Bar Chart

charts_Data = pd.DataFrame(
    np.random.randn(50,3),
    columns = ['a','b','c']
)
st.bar_chart(charts_Data)

# matplotlib

arr = np.random.normal(1,1, size =100 )
fig, ax = plt.subplots()
ax.hist(arr , bins = 20)

st.pyplot(fig)

# plotly 
import plotly.figure_factory as ff

# Add hsitogram data
x1 =  np.random.randn(200) - 2
x2 =  np.random.randn(200) 
x3 =  np.random.randn(200) + 2

# group data together
hist_data = [x1 , x2 ,x3]

group_labels = ["Group 1","Group 2","Group 3"]

# create  distplot with custom bin_size
fig  = ff.create_distplot(
    hist_data, group_labels , bin_size= [.1 , .25 , .5]
)

st.plotly_chart(fig , use_container_width= True)

# pydeck_chart
# Hers's a chart using a HexagonLayer and a ScatterplotLayeron top of the light map style:

df = pd.DataFrame(
    np.random.randn(1000,2)/[50,50] + [37.76 , -122.4],
    columns = ['lon','lat']
)

st.pydeck_chart(pdk.Deck(
    map_style = 'mapbox://styles/mapbox/light-v9',
    initial_view_state = pdk.ViewState(
        latitude= 37.76,
        longitude= -122.4,
        zoom = 11,
        pitch = 50,
    ),
    layers = [
        pdk.Layer(
            'HexagonLayer',
            data = df,
            get_position = '[lon,lat]',
            radius = 200,
            elevation_scale = 4,
            elevation_range = [0,1000],
            pickable = True,
            extruded = True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data =df,
            get_position = '[lon,lat]',
            get_color = '[200,30,0,160]',
            get_radius = 200,
        ),
    ],
))