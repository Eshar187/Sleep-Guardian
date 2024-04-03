import streamlit as st
import sklearn
import pickle
import numpy as np


st.image(r"Screenshot (91).png")

def forward():
    st.session_state.page = 'page2'

def backward():
    st.session_state.page = 'page1'

my_data=[]

def page1():
    st.title('Details')
    
    st.markdown("### Enter Your Name", unsafe_allow_html=True)
    Name=st.text_input('Your Name')

    st.markdown("<h3 style='text-align:side;'>Pick your Gender</h3>", unsafe_allow_html=True)
    Gender=st.radio("Your Gender",["Male","Female"])
    

    st.markdown("<h3 style='text-align:side;'>How old are you</h3>", unsafe_allow_html=True)
    Age=st.slider("Age",20,60)
    
    st.markdown("<h3 style='text-align:side;'>Occupation</h3>", unsafe_allow_html=True)
    Occupation=st.selectbox("What do you do? ",["Software Engineer","Doctor","Nurse","Lawyer","Teacher","Others"])
    
    
    st.markdown("<h3 style='text-align:side;'>Duration of sleep</h3>", unsafe_allow_html=True)
    Sleepduration=st.number_input("Sleep Duration",4.5,8.5,step=0.5)
    
    st.markdown("<h3 style='text-align:side;'>Sleep Quality</h3>", unsafe_allow_html=True)
    Sleepquality=st.slider("Rate yourself(1-10)",1,10)
    
    st.markdown("<h3 style='text-align:side;'>Pyhsical Activity</h3>", unsafe_allow_html=True)
    PhysicalActivity=st.number_input("Assuming minimum activity level be (10-100)",10,100)
    
    st.markdown("<h3 style='text-align:side;'>Stress Level</h3>", unsafe_allow_html=True)
    StressLevel=st.number_input("Select the level(1-10)",1,10)
    
    
    st.markdown("<h3 style='text-align:side;'>Body Mass Index (BMI)</h3>", unsafe_allow_html=True)
    BodyMI=st.selectbox("Select the category",["Normal","Overweight","Obese"])
    
    st.markdown("<h3 style='text-align:side;'>Blood Pressure</h3>", unsafe_allow_html=True)
    st.markdown("#### Systolic", unsafe_allow_html=True)
    HighBP=st.number_input("High Blood Pressure(90-180)",90,180)
    
    
    st.markdown("#### Diastolic")
    LowBP=st.number_input("Low Blood Pressure(60-90)",60,90)
    
    st.markdown("<h3 style='text-align:side;'>Current Heart Rate</h3>", unsafe_allow_html=True)
    Heartrate=st.slider("Select the Heart rate",60,100)
    
    
    st.markdown("<h3 style='text-align:side;'>Daily Steps</h3>", unsafe_allow_html=True)
    Dailysteps=st.slider("Steps till now",1000,10000)

    st.button(":navy[Submit]",type="primary",on_click=forward)
    user_input = {
        'Name': Name,
        'Gender': Gender,
        'Age': Age,
        'Occupation': Occupation,
        "Sleep Duration":Sleepduration,
        "Quality of Sleep":Sleepquality,
        "Physical Activity Level":PhysicalActivity,
        "Stress Level":StressLevel,
        "BMI Category":BodyMI,
        "Systolic":HighBP,
        "Diastolic":LowBP,
        "Heart Rate":Heartrate,
        "Daily Steps":Dailysteps
    }
    st.session_state.user_input = user_input
        # st.session_state.page = 'page2'


def page2():
    # st.title('Report')
    # user_input = st.session_state.user_input
    # st.write("Name:  ", user_input['Name'])
    # st.write("Gender:  ", user_input['Gender'])
    # st.write("Age:  ", user_input['Age'])
    # st.write("Occupation:  ", user_input['Occupation'])
    # st.write("Sleep Duration:  ", user_input['Sleep Duration'])
    # st.write("Quality of Sleep:  ", user_input['Quality of Sleep'])
    # st.write("Physical Activity Level:  ", user_input['Physical Activity Level'])
    # st.write("BMI Category:  ", user_input['BMI Category'])
    # st.write("Blood Pressure:  ", user_input['Systolic'],"/",user_input['Diastolic'])
    # # st.write("Diastolic:  ", user_input['Diastolic'])
    # st.write("Heart Rate:  ", user_input['Heart Rate'])
    # st.write("Daily Steps:  ", user_input['Daily Steps'])
    st.markdown("<h1 style='text-align:center;'>Report</h1>", unsafe_allow_html=True)
    user_input = st.session_state.user_input
    st.markdown(f"<h4 style='text-align:center;'> {user_input['Name']}</h4>", unsafe_allow_html=True)

    for i in range(0,2):
        st.write("")    
# Column 1
    col1, col2,col3 = st.columns(3)
    with col1:
        
        st.write("##### Gender:", user_input['Gender'])
        st.write("##### Age:", user_input['Age'])
        st.write("##### Occupation:", user_input['Occupation'])
        st.write("##### Sleep Duration:", user_input['Sleep Duration'])
        st.write("##### Quality of Sleep:", user_input['Quality of Sleep'])

# Column 3
        
    with col3:
        
        st.write("##### Physical Activity Level:  ", user_input['Physical Activity Level'])
        st.write("##### BMI Category:", user_input['BMI Category'])
        st.write("##### Blood Pressure:", user_input['Systolic'], "/", user_input['Diastolic'])
        st.write("##### Heart Rate:", user_input['Heart Rate'])
        st.write("##### Daily Steps:", user_input['Daily Steps'])
    
        
    st.button(":navy[Back]",type="primary",on_click=backward)
        # st.session_state.page = 'page1'


    gender=gender_num(user_input)
    bmi=bmi_num(user_input)

    my_data.extend([gender,user_input["Age"],user_input['Sleep Duration'],user_input['Quality of Sleep'],user_input['Physical Activity Level'],user_input["Stress Level"],bmi,user_input['Heart Rate'],user_input['Daily Steps'],user_input["Systolic"],user_input["Diastolic"],user_input['Occupation']])
    
    occ = my_data.pop()
    occ_list = ["Doctor", "Software Engineer", "Lawyer", "Nurse", "Teacher"]
    occupations=encode_occ(occ, occ_list)
    my_data.extend(occupations)

    # my_new_data=np.array(my_data).reshape(1,-1)
    my_new_data = np.array(my_data).reshape(1, -1) 
    # st.write(my_new_data)
    with open('Sleep_Dis232.pkl', 'rb') as f:
        model = pickle.load(f)
 
        prediction = model.predict(my_new_data) 
    # st.write("Prediction:", prediction)
        
# Column 2
    with col2:
        
        for i in range (0,15):
            st.write("")
        if prediction=="Fit":
            # st.markdown(f"<h4 style='text-align:center;'> {st.success("You are Fit")}</h4>", unsafe_allow_html=True)
            st.markdown("<div style='background-color: #21C3541A; padding:2px;  border-radius: 8px; text-align: center;'>"
    "<p style='color: #177233; padding-top:7px;'>Normal Sleep</p>""</div>", unsafe_allow_html=True)
            st.image(r"bwink_ppl_02_single_09.jpg")
        

        elif prediction=="Sleep Apnea":
            st.markdown("<div style='background-color: #FF2B2B17; padding:2px;  border-radius: 8px; text-align: center;'>"
    "<p style='color: #7D353B; padding-top:7px;'>Sleep Apnea</p>""</div>", unsafe_allow_html=True)
            st.image(r"4445829.jpg")


        else :
            # st.error(f"You have {prediction[0]}")
            st.markdown("<div style='background-color: #FF2B2B17; padding:2px;  border-radius: 8px; text-align: center;'>"
    "<p style='color: #7D353B; padding-top:7px;'>Insomania</p>""</div>", unsafe_allow_html=True)
            st.image(r"4436809.jpg")





def gender_num(user_input):
    if user_input['Gender']== "Male":
        user_input['Gender']=1
    else:
        user_input['Gender']=0
    return user_input['Gender']

def bmi_num(user_input):        
    if user_input['BMI Category']=="Normal":
        user_input['BMI Category']=0
    elif user_input['BMI Category']=="Overweight":
        user_input['BMI Category']=2
    else:
        user_input['BMI Category']=1
    return user_input['BMI Category']




def encode_occ(occ, occ_list):
    output = [0, 0, 0, 0, 0]
    if occ not in occ_list:
        return output
    else:
        index = occ_list.index(occ)
        output[index] = 1
        return output

# x=encode_occ("Doctor",["Doctor", "Software Engineer", "Lawyer", "Nurse", "Teacher"])
# print(x)

def main():
    page = st.session_state.get('page','page1')

    if page == 'page1':
        page1()
    elif page == 'page2':
        page2()

if __name__ == "__main__":
    main()