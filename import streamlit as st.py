import streamlit as st
import pandas as pd
import numpy as np

# Load CSVs
rb_df = pd.read_csv('Red_bus_df.csv')
df_a = pd.read_csv('andhra_route_details.csv')
l_a = df_a['Route_name'].tolist()
df_g = pd.read_csv('goa_route_details.csv')
l_g = df_g['Route_name'].tolist()
df_h = pd.read_csv('himachalpradesh_route_details.csv')
l_h = df_h['Route_name'].tolist()
df_j = pd.read_csv('jammu_route_details.csv')
l_j = df_j['Route_name'].tolist()
df_k = pd.read_csv('kerala_route_details.csv')
l_k = df_k['Route_name'].tolist()
df_r = pd.read_csv('rajasthan_route_details.csv')
l_r = df_r['Route_name'].tolist()
df_s = pd.read_csv('southbengal_route_details.csv')
l_s = df_s['Route_name'].tolist()
df_t = pd.read_csv('telangana_route_details.csv')
l_t = df_t['Route_name'].tolist()
df_u = pd.read_csv('uttarpradesh_route_details.csv')
l_u = df_u['Route_name'].tolist()
df_w = pd.read_csv('westbengal_route_details.csv')
l_w = df_w['Route_name'].tolist()

# Sidebar for app navigation
sb = st.sidebar.radio(label="Choose your option", options=[":house: Home", ":motorway: Book your ticket"])
st.write(sb)

if sb == ":house: Home":
    st.title(":rainbow[Welcome to Red Bus App] :bus:")
    st.header(":blue-background[App Description]", divider="blue")
    st.write("Plan your journey with ease! 🚍🛣️📍")
    st.markdown('''Red Bus App is designed to make your travel seamless and efficient.''')
    st.header(':blue-background[Created by]', divider="blue")
    st.markdown(":rainbow[Abinesh]")

elif sb == ":motorway: Book your ticket":
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        state = st.selectbox("Select State", options=['Andhra', 'Goa', 'Himachal Pradesh', 'Jammu', 'Kerala', 'Rajasthan', 'South Bengal', 'Telangana', 'Uttar Pradesh', 'West Bengal'])
    
    with col2:
        if state == 'Andhra':
            rn = st.selectbox("Route Name", options=l_a)
        elif state == 'Goa':
            rn = st.selectbox("Route Name", options=l_g)
        elif state == 'Himachal Pradesh':
            rn = st.selectbox("Route Name", options=l_h)
        elif state == 'Jammu':
            rn = st.selectbox("Route Name", options=l_j)
        elif state == 'Kerala':
            rn = st.selectbox("Route Name", options=l_k)
        elif state == 'Rajasthan':
            rn = st.selectbox("Route Name", options=l_r)
        elif state == 'South Bengal':
            rn = st.selectbox("Route Name", options=l_s)
        elif state == 'Telangana':
            rn = st.selectbox("Route Name", options=l_t)
        elif state == 'Uttar Pradesh':
            rn = st.selectbox("Route Name", options=l_u)
        elif state == 'West Bengal':
            rn = st.selectbox("Route Name", options=l_w)
        df = rb_df[rb_df['Route_name'] == rn]

    # Convert to numeric where necessary
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Depature_time'] = pd.to_datetime(df['Depature_time'], errors='coerce').dt.time

    # Handle missing data
    df = df.dropna(subset=['Rating', 'Price', 'Depature_time'])

    with col3:
        bus_ty = st.selectbox("Bus Type", options=df['Bus_type'].unique())
        df = df[df['Bus_type'] == bus_ty]

    with col4:
        r = st.selectbox('Select Rating', options=['1 to 2', '2 to 3', '3 to 4', '4 to 5'])
        if r == '1 to 2':
            df = df[(df['Rating'] >= 1) & (df['Rating'] <= 2)]
        elif r == '2 to 3':
            df = df[(df['Rating'] >= 2) & (df['Rating'] <= 3)]
        elif r == '3 to 4':
            df = df[(df['Rating'] >= 3) & (df['Rating'] <= 4)]
        elif r == '4 to 5':
            df = df[(df['Rating'] >= 4) & (df['Rating'] <= 5)]

    with col5:
        t = st.selectbox('Select Starting Time', options=['1:00 - 3:00', '3:00 - 6:00', '6:00 - 9:00', '9:00 - 12:00', '12:00 - 15:00', '15:00 - 18:00', '18:00 - 21:00', '21:00 - 24:00'])
        # Time filtering based on departure time
        # Add your time-based filtering here...

    with col6:
        p = st.selectbox("Select Price", options=['Below 200', '200 to 400', '400 to 600', '600 to 800', '800 to 1000', 'Above 1000'])
        if p == 'Below 200':
            df = df[df['Price'] <= 200]
        elif p == '200 to 400':
            df = df[(df['Price'] >= 200) & (df['Price'] <= 400)]
        # Add other price filters here...

    df = df.drop_duplicates()
    st.write(df)
