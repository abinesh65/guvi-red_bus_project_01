import streamlit as st
import pandas as pd
import numpy as np

rb_df = pd.read_csv('Red_bus_df.csv')

df_a = pd.read_csv('andhra_route_details.csv')
l_a=[]
for i in df_a['Route_name']:
    l_a.append(i)

df_g = pd.read_csv('goa_route_details.csv')
l_g=[]
for i in df_g['Route_name']:
    l_g.append(i)

df_h = pd.read_csv('himachalpradesh_route_details.csv')
l_h=[]
for i in df_h['Route_name']:
    l_h.append(i)

df_j = pd.read_csv('jammu_route_details.csv')
l_j=[]
for i in df_j['Route_name']:
    l_j.append(i)

df_k = pd.read_csv('kerala_route_details.csv')
l_k=[]
for i in df_k['Route_name']:
    l_k.append(i)

df_r = pd.read_csv('rajasthan_route_details.csv')
l_r=[]
for i in df_r['Route_name']:
    l_r.append(i)

df_s = pd.read_csv('southbengal_route_details.csv')
l_s=[]
for i in df_s['Route_name']:
    l_s.append(i)

df_t = pd.read_csv('telangana_route_details.csv')
l_t=[]
for i in df_t['Route_name']:
    l_t.append(i)

df_u = pd.read_csv('uttarpradesh_route_details.csv')
l_u=[]
for i in df_u['Route_name']:
    l_u.append(i)

df_w = pd.read_csv('westbengal_route_details.csv')
l_w=[]
for i in df_w['Route_name']:
    l_w.append(i)

sb = st.sidebar.radio(label="Choose your option",options=[":house: Home",":motorway: Book your ticket"])
# st.sidebar(":house: Home","Book your ticket")
st.write(sb)
if sb == ":house: Home":
    st.title(":rainbow[Welcome to Red Bus App] :bus:")
    st.header(":blue-background[App Description]",divider="blue")
    st.write("Plan your journey with ease! 🚍🛣️📍")
    st.markdown('''Red Bus App is designed to make your travel Seamless Travel Experience bus booking 
            and travel experience as smooth as possible. Whether you're planning a trip across 
            the city or a long-distance journey, Red Bus connects you with reliable 
            bus operators, ensuring a convenient, efficient, and affordable travel solution.''')
    
    st.header(':blue-background[Key Features]',divider="blue")
    st.subheader(":orange[Streamlit]")
    st.markdown('''interactive Streamlit application for data filtering.''')

    st.subheader(":orange[SQL Connector]")
    st.markdown('''The Python MySQL Connector is a robust library used to connect Python applications to 
                a MySQL database.It provides a seamless interface for executing SQL queries, 
                fetching data, and managing transactions directly from Python scripts. With support 
                for standard SQL features and secure connections, this connector simplifies database 
                interactions through Python code, offering efficient CRUD (Create, Read, Update, Delete)
                 operations. It also supports prepared statements, which enhance security by preventing
                 SQL injection. This connector is easy to use and highly suitable for building Python 
                applications that require MySQL database integration.''')
    st.subheader(":orange[Cashless Payments]")
    st.markdown('''Enjoy seamless transactions through multiple secure payment options including 
                credit/debit cards, UPI, and mobile wallets. No more cash hassles!''')
    st.subheader(":orange[24/7 Customer Support]")
    st.markdown('''Stuck somewhere? Our dedicated customer service team is available around the clock
                 to assist you with any queries, booking issues, or travel disruptions.''')
    st.subheader(":orange[Customised Trips]")
    st.markdown('''Our intuitive interface allows you to search, compare, and book bus tickets 
                with just a few taps. Choose from a wide range of routes, operators, and seating 
                options that best suit your preferences.''')
    
    st.header(':blue-background[Created by]',divider="blue")
    st.markdown(":rainbow[Abinesh]")

    
if sb == ":motorway: Book your ticket":
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    # Three columns with different widths
    col1, col2, col3 = st.columns([2,2,2])
    col4, col5, col6 = st.columns([2,2,2])

    # Using 'with' notation:
    with col1:
        state = st.selectbox("Select State",options=['Andhra','Goa','Himachal Pradesh',
                                                     'Jammu','Kerala','Rajasthan','South Bengal',
                                                     'Telangana','Uttar Pradesh','West Bengal'])
        # st.write(state)
    with col2:
        if state == 'Andhra':
            rn = st.selectbox("Route Name",options=l_a)
        elif state == 'Goa':
            rn = st.selectbox("Route Name",options=l_g)
        elif state == 'Himachal Pradesh':
            rn = st.selectbox("Route Name",options=l_h)
        elif state == 'Jammu':
            rn = st.selectbox("Route Name",options=l_j)
        elif state == 'Kerala':
            rn = st.selectbox("Route Name",options=l_k)
        elif state == 'Rajasthan':
            rn = st.selectbox("Route Name",options=l_r)
        elif state == 'South Bengal':
            rn = st.selectbox("Route Name",options=l_s)
        elif state == 'Telangana':
            rn = st.selectbox("Route Name",options=l_t)
        elif state == 'Uttar Pradesh':
            rn = st.selectbox("Route Name",options=l_u)
        elif state == 'West Bengal':
            rn = st.selectbox("Route Name",options=l_w)
        df = rb_df[rb_df['Route_name'] == rn]
    
    with col3:
        ty = list(df['Bus_type'].unique())
        bus_ty = st.selectbox("Bus Type",options=ty)
        df = df[df['Bus_type']==bus_ty]
        # st.write(df['Rating'])
    
    with col4:
        r = st.selectbox('Select Rating',options=['1 to 2','2 to 3','3 to 4','4 to 5'],index=2)
        # st.write(r)
        if r == '1 to 2':
            df = df[(df['Rating']>=1) & (df['Rating']<=2)]
        elif r == '2 to 3':
            df = df[(df['Rating']>=2) & (df['Rating']<=3)]
        elif r == '3 to 4':
            df = df[(df['Rating']>=3) & (df['Rating']<=4)]
        elif r == '4 to 5':
            df = df[(df['Rating']>=4) & (df['Rating']<=5)]
    
    with col5:
        t = st.selectbox(label='Select starting time',options=['1:00 - 3:00','3:00 - 6:00',
                                                                 '6:00 - 9:00','9:00 - 12:00',
                                                                 '12:00 - 15:00','15:00 - 18:00',
                                                                 '18:00 - 21:00','21:00 - 24:00'])
        # st.write(df.dtypes)
        df['Depature_time'] = pd.to_datetime(df['Depature_time'], format='%H:%M').dt.time
        if t == '1:00 - 3:00':
            df = df[(df['Depature_time'] >= pd.to_datetime('01:00', format='%H:%M').time()) & 
        (df['Depature_time'] <= pd.to_datetime('03:00', format='%H:%M').time())]
        elif t == '3:00 - 6:00':
            df = df[(df['Depature_time'] >= pd.to_datetime('03:00', format='%H:%M').time()) & 
        (df['Depature_time'] <= pd.to_datetime('06:00', format='%H:%M').time())]
        elif t == '6:00 - 9:00':
            df = df[(df['Depature_time'] >= pd.to_datetime('06:00', format='%H:%M').time()) & 
        (df['Depature_time'] <= pd.to_datetime('09:00', format='%H:%M').time())]
        elif t == '9:00 - 12:00':
            df = df[(df['Depature_time'] >= pd.to_datetime('09:00', format='%H:%M').time()) & 
        (df['Depature_time'] <= pd.to_datetime('12:00', format='%H:%M').time())]
        elif t == '12:00 - 15:00':
            df = df[(df['Depature_time'] >= pd.to_datetime('12:00', format='%H:%M').time()) & 
        (df['Depature_time'] <= pd.to_datetime('15:00', format='%H:%M').time())]
        elif t == '15:00 - 18:00':
            df = df[(df['Depature_time'] >= pd.to_datetime('15:00', format='%H:%M').time()) & 
        (df['Depature_time'] <= pd.to_datetime('18:00', format='%H:%M').time())]
        elif t == '18:00 - 21:00':
            df = df[(df['Depature_time'] >= pd.to_datetime('18:00', format='%H:%M').time()) & 
        (df['Depature_time'] <= pd.to_datetime('21:00', format='%H:%M').time())]
        elif t == '21:00 - 24:00':
            df = df[(df['Depature_time'] >= pd.to_datetime('21:00', format='%H:%M').time()) & 
        (df['Depature_time'] <= pd.to_datetime('23:59', format='%H:%M').time())]
        # st.write(df)
    
    with col6:
        p = st.selectbox("Select price",options=['Below 200','200 to 400','400 to 600',
                                             '600 to 800','800 to 1000','Above 1000'],index=2)
        if p == 'Below 200':
            df = df[df['Price']<= 200]
        elif p == '200 to 400':
            df = df[(df['Price']>=200) & (df['Price']<=400)]
        elif p == '400 to 600':
            df = df[(df['Price']>=400) & (df['Price']<=600)]
        elif p == '600 to 800':
            df = df[(df['Price']>=600) & (df['Price']<=800)]
        elif p == '800 to 1000':
            df = df[(df['Price']>=800) & (df['Price']<=1000)]
        elif p == 'Above 1000':
            df = df[df['Price'] >= 1000]
    
    df = df.drop(columns=['Unnamed: 0'],axis=1).reset_index(drop=True)
    df = df.drop_duplicates()
    st.write(df)

