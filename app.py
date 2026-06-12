import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('India_Dashboard_.csv')

metrics = [
    'Population',
    'Male',
    'Female',
    'Literate',
    'Households_with_Internet',
    'literacy_rate',
    'sex_ratio',
    'Workers',
    'Households_with_Computer',
    'Total_Power_Parity'
]

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.title('India Census Analytics Dashboard')
st.markdown('Explore demographic, education, employment, and digital connectivity trends across Indian districts.')

st.sidebar.title('India Census Analytics')

selected_state = st.sidebar.selectbox('Select a state',list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter',metrics)

secondary = st.sidebar.selectbox('Select Secondary Parameter',metrics)

plot = st.sidebar.button('Plot Graph')

if plot:

    st.info(f'Bubble Size = {primary} | Bubble Color = {secondary}')

    if selected_state == 'Overall India':

        col1,col2,col3 = st.columns(3)

        col1.metric('Districts',len(df))
        col2.metric('Avg Literacy Rate',f"{df['literacy_rate'].mean():.1f}%")
        col3.metric('Avg Sex Ratio',f"{df['sex_ratio'].mean():.0f}")

        fig = px.scatter_mapbox(
            df,
            lat='Latitude',
            lon='Longitude',
            size=primary,
            color=secondary,
            zoom=4,
            size_max=35,
            mapbox_style='carto-positron',
            width=1200,
            height=700,
            hover_name='District',
            hover_data=['Population','literacy_rate','sex_ratio']
        )

        st.plotly_chart(fig,use_container_width=True)

        st.subheader(f'Top 10 Districts by {primary}')

        top10 = df.sort_values(primary,ascending=False)[['District',primary]].head(10)

        st.dataframe(top10,use_container_width=True)

    else:

        state_df = df[df['State'] == selected_state]

        col1,col2,col3 = st.columns(3)

        col1.metric('Districts',len(state_df))
        col2.metric('Avg Literacy Rate',f"{state_df['literacy_rate'].mean():.1f}%")
        col3.metric('Avg Sex Ratio',f"{state_df['sex_ratio'].mean():.0f}")

        fig = px.scatter_mapbox(
            state_df,
            lat='Latitude',
            lon='Longitude',
            size=primary,
            color=secondary,
            zoom=6,
            size_max=35,
            mapbox_style='carto-positron',
            width=1200,
            height=700,
            hover_name='District',
            hover_data=['Population','literacy_rate','sex_ratio']
        )

        st.plotly_chart(fig,use_container_width=True)

        st.subheader(f'Top 10 Districts in {selected_state} by {primary}')

        top10 = state_df.sort_values(primary,ascending=False)[['District',primary]].head(10)

        st.dataframe(top10,use_container_width=True)