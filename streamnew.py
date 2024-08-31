import streamlit as st
import pymysql
import pandas as pd
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Malar@1976#",
    database='sri'
)
mycursor = mydb.cursor()

st.title("SRI REDBUS")
st.markdown("""**See your desired buses**""")
st.text("After selecting STATE click \"SAVE STATE\" then selct your desired ROUTE\n click \"SHOW BUSES\"")

form = st.form(key='registration_form')
country = form.selectbox("Select \" STATE\" ", ["kaac","westbengal","jksrctc","ktcl","bihar","north bengal","pepsu","chandighar","astc","hrtc"])
button1 = st.button("SHOW BUSES")
st.text("jksrtc-jammu kashmir ; ktcl-kadamba\npepsu-punjab ;astc-assam\nhrtc-himachal ;kaac-karbi analogue(assam)")
#st.text("0-busid;1-state;2-route;3-link of busroute;4-busname;5-bustype;6arrival time;\n7-travel time;8-departure time;9-star rating;10-price;11-available seats")
r1={'kaac': ['Diphu to Guwahati', 'Guwahati to Diphu', 'Bokolia (assam) to Guwahati', 'Dokmoka to Guwahati', 'Guwahati to Dokmoka', 'Guwahati to Bokolia (assam)', 'Langhin (assam) to Guwahati', 'Diphu to Hamren', 'Guwahati to Langhin (assam)', 'Guwahati to Manja (assam)','Manja (assam) to Guwahati', 'Hamren to Diphu'], 'westbengal': ['Kolkata to Digha', 'Digha to Kolkata', 'Mandarmani to Kolkata', 'Kolkata to Mandarmani', 'Kolkata to Bakkhali'], 'jksrctc': ['Jammu (j and k) to Srinagar', 'Delhi to Srinagar', 'Srinagar to Jammu (j and k)', 'Jammu (j and k) to Haridwar', 'Jammu (j and k) to Delhi', 'Delhi to Jammu (j and k)', 'Katra (jammu and kashmir) to Jammu (j and k)', 'Jammu (j and k) to Katra (jammu and kashmir)', 'Mendhar (J & K) to Jammu (j and k)', 'Jammu (j and k) to Poonch','Haridwar to Jammu (j and k)', 'Chandigarh to Jammu (j and k)', 'Jammu (j and k) to Kishtwar', 'Jammu (j and k) to Mendhar (J & K)', 'Jammu (j and k) to Amritsar', 'Ajmer to Jammu (j and k)'],'ktcl': ['Pune to Goa', 'Goa to Pune', 'Mumbai to Goa', 'Goa to Mumbai', 'Pandharpur to Goa', 'Bangalore to Goa', 'Goa to Pandharpur', 'Belagavi to Goa', 'Goa to Bangalore', 'Solapur to Goa', 'Goa to Kolhapur(Maharashtra)', 'Goa to Solapur', 'Goa to Sangola (Solapur)', 'Sangola (Solapur) to Goa', 'Calangute (goa) to Goa Airport', 'Goa to Sangli', 'Calangute (goa) to Mopa Airport', 'Mopa Airport to Calangute (goa)', 'Ponda to Belagavi', 'Goa to Miraj', 'Goa Airport to Calangute (goa)', 'Marcel to Belagavi', 'Shivamogga to Goa', 'Goa to Mopa Airport', 'Goa to Satara', 'Belagavi to Marcel', 'Mopa Airport to Goa', 'Shirdi to Goa', 'Goa to Shivamogga', 'Goa to Shirdi', 'Goa to Goa Airport', 'Margao to Mopa Airport', 'Goa Airport to Goa', 'Mopa Airport to Margao', 'Belagavi to Saquelim', 'Panaji to Mopa Airport', 'Saquelim to Belagavi', 'Calangute (goa) to Goa', 'Calangute (goa) to Panaji', 'Goa Airport to Panaji'], 'bihar': ['Patna (Bihar) to Bettiah', 'Gopalganj (Bihar) to Delhi', 'Patna (Bihar) to Motihari', 'Delhi to Motihari', 'Bettiah to Patna (Bihar)', 'Motihari to Delhi', 'Patna (Bihar) to Balmiki Nagar (bihar)', 'Balmiki Nagar (bihar) to Patna (Bihar)', 'Patna (Bihar) to Kathmandu', 'Patna (Bihar) to Katihar', 'Patna (Bihar) to Purnea', 'Patna (Bihar) to Hazaribagh', 'Ranchi to Patna (Bihar)', 'Hazaribagh to Patna (Bihar)', 'Patna (Bihar) to Raxaul', 'Muzaffarpur (Bihar) to Kathmandu', 'Patna (Bihar) to Ranchi', 'Muzaffarpur (Bihar) to Ranchi', 'Kathmandu to Patna (Bihar)', 'Ranchi to Muzaffarpur (Bihar)', 'Motihari to Lucknow', 'Lucknow to Motihari', 'Motihari to Kathmandu', 'Agra to Motihari', 'Patna (Bihar) to Janakpur (Nepal)', 'Muzaffarpur (Bihar) to Hazaribagh', 'Purnea to Patna (Bihar)', 'Patna (Bihar) to Araria (Bihar)', 'Darbhanga to Patna (Bihar)', 'Patna (Bihar) to Saharsa', 'Motihari to Agra', 'Hajipur (Bihar) to Kathmandu', 'Kathmandu to Motihari', 'Patna (Bihar) to Forbesganj', 'Ranchi to Hajipur (Bihar)', 'Lucknow to Gopalganj (Bihar)'], 'north bengal': ['Kolkata to Siliguri', 'Siliguri to Kolkata', 'Siliguri to Darjeeling', 'Kolkata to Raiganj', 'Raiganj to Kolkata', 'Kolkata to Malda', 'Cooch Behar (West Bengal) to Berhampore (West Bengal)', 'Kolkata to Cooch Behar (West Bengal)', 'Malda to Kolkata', 'Berhampore (West Bengal) to Cooch Behar (West Bengal)', 'Cooch Behar (West Bengal) to Kolkata', 'Kolkata to Balurghat', 'Berhampore (West Bengal) to Siliguri', 'Siliguri to Berhampore (West Bengal)', 'Kolkata to Gangarampur', 'Siliguri to Kalimpong', 'Cooch Behar (West Bengal) to Malda', 'Malda to Cooch Behar (West Bengal)', 'Balurghat to Kolkata', 'Kolkata to Jalpaiguri', 'Kolkata to Islampur (West Bengal)', 'Falakata (west bengal) to Berhampore (West Bengal)', 'Kolkata to Falakata (west bengal)', 'Cooch Behar (West Bengal) to Raiganj', 'Siliguri to Cooch Behar (West Bengal)', 'Raiganj to Krishnanagar (West Bengal)', 'Raiganj to Siliguri', 'Kolkata to Buniadpur', 'Gangarampur to Kolkata', 'Siliguri to Ranaghat', 'Siliguri to Krishnanagar (West Bengal)', 'Falakata (west bengal) to Kolkata', 'Kolkata to Farakka', 'Siliguri to Raiganj', 'Kolkata to Dhupguri (West Bengal)', 'Falakata (west bengal) to Malda', 'Kolkata to Gazole', 'Berhampore (West Bengal) to Falakata (west bengal)', 'Balurghat to Siliguri', 'Siliguri to Barasat (West Bengal)', 'Kolkata to Maynaguri (West Bengal)', 'Kolkata to Itahar (West Bengal)', 'Cooch Behar (West Bengal) to Krishnanagar (West Bengal)', 'Cooch Behar (West Bengal) to Omarpur (West Bengal)', 'Berhampore (West Bengal) to Jalpaiguri', 'Malda to Siliguri', 'Raiganj to Ranaghat', 'Cooch Behar (West Bengal) to Farakka', 'Cooch Behar (West Bengal) to Siliguri'], 'pepsu': ['Patiala to Delhi', 'Delhi to Patiala', 'Ludhiana to Delhi', 'Delhi to Ludhiana', 'Phagwara to Delhi', 'Jalandhar to Delhi', 'Delhi to Jalandhar', 'Patiala to Delhi Airport', 'Jalandhar to Delhi Airport', 'Ludhiana to Delhi Airport', 'Phagwara to Delhi Airport', 'Delhi Airport to Ludhiana', 'Delhi to Phagwara', 'Delhi to Amritsar', 'Amritsar to Delhi', 'Delhi Airport to Patiala', 'Amritsar to Delhi Airport', 'Kapurthala to Delhi', 'Delhi Airport to Jalandhar', 'Chandigarh to Bathinda', 'Chandigarh to Faridkot', 'Chandigarh to Patiala'], 'chandighar': ['Chandigarh to Delhi', 'Delhi to Chandigarh', 'Yamuna Nagar to Chandigarh', 'Chandigarh to Shimla', 'Chandigarh to Vrindavan', 'Chandigarh to Yamuna Nagar', 'Chandigarh to Sujanpur (himachal pradesh)', 'Ludhiana to Chandigarh', 'Hamirpur (Himachal Pradesh) to Chandigarh', 'Vrindavan to Chandigarh', 'Chandigarh to Hamirpur (Himachal Pradesh)', 'Sujanpur (himachal pradesh) to Chandigarh', 'Shimla to Chandigarh', 'Chandigarh to Ludhiana', 'Chandigarh to Dharamshala (Himachal Pradesh)', 'Chandigarh to Dehradun', 'Chandigarh to Baijnath', 'Pathankot to Chandigarh', 'Chandigarh to Haridwar', 'Chandigarh to Pathankot', 'Talwara to Chandigarh', 'Dehradun to Chandigarh', 'Amritsar to Chandigarh', 'Chandigarh to Rishikesh', 'Chandigarh to Talwara', 'Chandigarh to Dinanagar (punjab)', 'Dinanagar (punjab) to Chandigarh', 'Rishikesh to Chandigarh', 'Chandigarh to Amritsar', 'Chandigarh to Agra', 'Dharamshala (Himachal Pradesh) to Chandigarh', 'Chandigarh to Katra (jammu and kashmir)', 'Hisar (Haryana) to Chandigarh', 'Rohtak to Chandigarh', 'Chandigarh to Una (Himachal Pradesh)', 'Chandigarh to Jammu (j and k)', 'Chandigarh to Rohtak', 'Chandigarh to Manali', 'Chandigarh to Haldwani', 'Jawala Ji to Chandigarh', 'Agra to Chandigarh', 'Jammu (j and k) to Chandigarh', 'Chandigarh to Hisar (Haryana)', 'Chandigarh to Kathgodam', 'Haridwar to Chandigarh', 'Katra (jammu and kashmir) to Chandigarh', 'Baijnath to Chandigarh', 'Narnaul to Chandigarh', 'Chandigarh to Jawala Ji'], 'astc': ['Tezpur to Guwahati', 'Guwahati to Tezpur', 'Nagaon (Assam) to Guwahati', 'Guwahati to Nagaon (Assam)', 'Goalpara to Guwahati', 'Jorhat to North Lakhimpur', 'Dhubri to Guwahati', 'Guwahati to Dhubri', 'North Lakhimpur to Sibsagar', 'North Lakhimpur to Jorhat', 'Dhekiajuli to Guwahati', 'Jorhat to Dibrugarh', 'Jorhat to Dhemaji', 'Sibsagar to North Lakhimpur', 'Dhemaji to Jorhat', 'Tezpur to Dibrugarh', 'Haflong to Guwahati', 'North Lakhimpur to Dibrugarh', 'Jorhat to Tinsukia', 'Dibrugarh to Tezpur', 'Guwahati to Biswanath Charali', 'Guwahati to Haflong', 'Dibrugarh to North Lakhimpur', 'Nagaon (Assam) to Haflong', 'Tezpur to Moran', 'Dibrugarh to Jorhat', 'Guwahati to Silchar', 'Bihpuria to Dibrugarh', 'Haflong to Nagaon (Assam)', 'North Lakhimpur to Tezpur', 'Biswanath Charali to Guwahati', 'Biswanath Charali to Dibrugarh', 'Tinsukia to Jorhat', 'Moran to Tezpur', 'Jorhat to Gogamukh', 'Dibrugarh to Biswanath Charali', 'Gohpur to Guwahati', 'Tinsukia to Tezpur', 'North Lakhimpur to Golaghat', 'Golaghat to North Lakhimpur', 'Silchar to Guwahati', 'Bokakhat to Dibrugarh', 'North Lakhimpur to Moran', 'Tezpur to North Lakhimpur', 'Tezpur to Tinsukia', 'Dibrugarh to Bihpuria'], 'hrtc': ['Delhi to Shimla', 'Shimla to Delhi', 'Manali to Chandigarh', 'Chandigarh to Manali', 'Delhi to Manali', 'Hamirpur (Himachal Pradesh) to Chandigarh', 'Delhi to Hamirpur (Himachal Pradesh)', 'Delhi to Chandigarh', 'Manali to Delhi', 'Hamirpur (Himachal Pradesh) to Delhi', 'Chandigarh to Hamirpur (Himachal Pradesh)', 'Shimla to Manali', 'Delhi to Dharamshala (Himachal Pradesh)', 'Shimla to Chandigarh', 'Chandigarh to Dharamshala (Himachal Pradesh)', 'Delhi to Baddi (Himachal Pradesh)', 'Dharamshala (Himachal Pradesh) to Chandigarh', 'Chamba (Himachal Pradesh) to Chandigarh', 'Delhi to Dalhousie', 'Delhi to Chamba (Himachal Pradesh)', 'Dalhousie to Delhi', 'Solan to Delhi', 'Delhi to Palampur', 'Dharamshala (Himachal Pradesh) to Delhi', 'Delhi to Solan', 'Chandigarh to Reckong Peo (Himachal Pradesh)', 'Manali to Shimla', 'Palampur to Delhi', 'Chandigarh to Kullu', 'Kangra to Chandigarh', 'Kullu to Chandigarh', 'Delhi to Kangra', 'Chamba (Himachal Pradesh) to Delhi', 'Palampur to Chandigarh', 'Chandigarh to Shimla', 'Chandigarh to Kangra', 'Delhi to Nalagarh', 'Baddi (Himachal Pradesh) to Delhi', 'Kangra to Delhi', 'Ghumarwin to Delhi', 'Delhi to Sarkaghat']}
submit_button = form.form_submit_button(label='SAVE STATE')
route = form.selectbox("Select \"ROUTES\" ", r1[country])


if button1:
    query = f"SELECT * FROM redbusfinal WHERE state = '{country}' AND route = '{route}';"
    mycursor.execute(query)
    data = mycursor.fetchall()
    #st.table(data)   

    column_names = ["Bus ID", "State", "Route", "Link of Bus Route", "Bus Name", "Bus Type", "Arrival Time", 
                    "Travel Time", "Departure Time", "Star Rating", "Price", "Available Seats"]
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=column_names)
    
    # Display as a table
    st.table(df)  # Display the DataFrame as a table with headers