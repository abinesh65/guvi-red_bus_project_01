import streamlit as st
import pandas as pd
import pymysql

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
    st.header(':blue-background[Project details]',divider="blue")
    st.subheader(":green[Project title]")
    st.markdown("**Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit**")
    st.subheader(":green[Skills take away From This Project]")
    st.markdown("**Web Scraping using Selenium, Python, Streamlit , SQL**")
    st.subheader(":green[Domain]")
    st.markdown("**Transportation**")
    st.header(':blue-background[Created by]',divider="blue")
    st.markdown(":rainbow[**ANESHA NAGARAJAN**]")

if sb == ":motorway: Book your ticket":
    st.title("Book your ticket")
    myconnection = pymysql.connect(host='localhost',user='root',password='@neSre11',database='redbus')
    cursor = myconnection.cursor()
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
    # Three columns with different widths
    col1, col2, col3 = st.columns([2,2,2])
    col4, col5, col6 = st.columns([2,2,2])
    col7, col8, col9 = st.columns([2,2,2])

    with col1:
        state = st.selectbox("Select State",options=['Andhra','Goa','Himachal Pradesh',
                                                     'Jammu','Kerala','Rajasthan','South Bengal',
                                                     'Telangana','Uttar Pradesh','West Bengal'])
        
    with col2:
        if state == 'Andhra':
            s = st.selectbox("Select Route Name",options=l_a)
        elif state == 'Goa':
            s = st.selectbox("Select Route Name",options=l_g)
        if state == 'Himachal Pradesh':
            s = st.selectbox("Select Route Name",options=l_h)
        if state == 'Jammu':
            s = st.selectbox("Select Route Name",options=l_j)
        if state == 'Kerala':
            s = st.selectbox("Select Route Name",options=l_k)
        if state == 'Rajasthan':
            s = st.selectbox("Select Route Name",options=l_r)
        if state == 'South Bengal':
            s = st.selectbox("Select Route Name",options=l_s)
        if state == 'Telangana':
            s = st.selectbox("Select Route Name",options=l_t)
        if state == 'Uttar Pradesh':
            s = st.selectbox("Select Route Name",options=l_u)
        if state == 'West Bengal':
            s = st.selectbox("Select Route Name",options=l_w)

    with col3:
        ty = ['AC','Non AC']
        bus_ty = st.selectbox("Bus Type",options=ty)
        if bus_ty == 'AC':
            typ1 = "NOT like '%NON%'"
            typ2 = "NOT like '%Non%'"
        elif bus_ty == 'Non AC':
            typ1 = "like '%NON%'"
            typ2 = "like '%Non%'"

    with col4:
        r = st.slider(label="Choose Rating",min_value=1,max_value=5)
        # r = st.selectbox('Select Rating',options=['1 to 2','2 to 3','3 to 4','4 to 5'],index=2)
        if r == 1:
            rate = 'between 1 and 5'
        elif r == 2:
            rate = 'between 2 and 5'
        elif r == 3:
            rate = 'between 3 and 5'
        elif r == 4:
            rate = 'between 4 and 5'

    with col5:
        t = st.selectbox(label='Select starting time',options=['1:00 - 3:00','3:00 - 6:00',
                                                                 '6:00 - 9:00','9:00 - 12:00',
                                                                 '12:00 - 15:00','15:00 - 18:00',
                                                                 '18:00 - 21:00','21:00 - 24:00'])
        if t == '1:00 - 3:00':
            d_t = "between '00:00' and '03:00'"
        elif t == '3:00 - 6:00':
            d_t = "between '03:00' and '06:00'"
        elif t == '6:00 - 9:00':
            d_t = "between '06:00' and '09:00'"
        elif t == '9:00 - 12:00':
            d_t = "between '09:00' and '12:00'"
        elif t == '12:00 - 15:00':
            d_t = "between '12:00' and '15:00'"
        elif t == '15:00 - 18:00':
            d_t = "between '15:00' and '18:00'"
        elif t == '18:00 - 21:00':
            d_t = "between '18:00' and '21:00'"
        elif t == '21:00 - 24:00':
            d_t = "between '21:00' and '23:59'"


    with col6:
        p = st.selectbox("Select price",options=['Below 200','200 to 400','400 to 600',
                                             '600 to 800','800 to 1000','Above 1000'],index=2)
        if p == 'Below 200':
            pr = '<=200'
        elif p == '200 to 400':
            pr = 'Between 200 and 400'
        elif p == '400 to 600':
            pr = 'Between 400 and 600'
        elif p == '600 to 800':
            pr = 'Between 600 and 800'
        elif p == '800 to 1000':
            pr = 'Between 800 and 1000'
        elif p == 'Above 1000':
            pr = '>=1000'

        query = f'''select * from bus_routes where route_name = "{s}" and (bus_type {typ1} or
                    bus_type {typ2}) and star_rating {rate} and departing_time {d_t} and price {pr}'''
        cursor.execute(query)
        output = cursor.fetchall()
        # op = myconnection.query(query, ttl=600)
        
        df = pd.DataFrame(output,columns=['ID','Route Name','Route Link','Bus Name','Bus Type',
                                        'Depature Time','Duration','Reaching Time','Rating','Price',
                                        'Seat Availability'])
        df=df.drop(columns=['ID'])
   
    # with col8:
    #     sub = st.button("Submit")
    # if sub:
    st.write(df)
        