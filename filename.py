import streamlit as st
import time

#This section will set the title and headers instructing
#the user how to navigate the form.

st.title("Procedure Cost Lookup")
st.header("Use this to estimate your real cost for care at any given facility. Compare prices and select the provider of highest value to you.")
st.subheader("Please enter your details below.")

'''

'''

#This section asks for the user to enter their zip-code to find
#hospitals near them.

procedure = st.text_input("Enter your zip code:","")
st.write("Your zip code is: ", procedure)



#This section asks for a radius around the zip code they have entered.

radius = st.slider("Select the radius: ", 10,100)

st.text('Selected radius: {} miles.'.format(radius))


#This section asks for the user to enter the name of 
#the procedure they would like to have performed.

procedure = st.text_input("Enter the procedure name:","E.g. Gastric Bypass Surgery")
st.write("Your have entered: ", procedure)




#This section prompts the user to select a hospital from
#the dropdown.

hospital = st.selectbox("Hospital: ",
                        ['Wesley Medical Center','Via Christi St. Joseph'])
st.write("Your hospital is: ", hospital)




#This section will control the button actions.

if(st.button("Run Cost Estimate")):
    st.text("Submitting form details...")
    time.sleep(3)
    st.text("Your information has been submitted.")
    st.balloons()












