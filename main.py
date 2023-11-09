import streamlit as st
import joblib

clf = joblib.load("rf_model.sav")

st.title("Predict your next job level")
st.markdown('This is a simple app that can predict your job level with necessary information')

st.header("Answer the following")
col1, col2 = st.columns(2)

option1_li = ('Male', 'Female','Prefer not to say')
option2_li = ('Others',
	 'Computer Science',
	 'Economics',
	 'Accountancy',
	 'Mass Communication (Communication and Language Arts)',
	 'Electrical & Electronic Engineering',
	 'Business Administration',
	 'Biochemistry',
	 'Mechanical Engineering',
	 'Law',
	 'Microbiology',
	 'Political Science',
	 'History and International Studies',
	 'English and Literary Studies',
	 'Computer Engineering',
	 'Civil Engineering',
	 'Architecture',
	 'Chemical Engineering',
	 'Banking and Finance',
	 'Geography',
	 'Industrial Relations and Personnel Management',
	 'Physics and Astronomy',
	 'Medicine',
	 'Geology',
	 'Psychology',
	 'Estate Management',
	 'Statistics',
	 'Education & Economics',
	 'Mathematics',
	 'Sociology/Anthropology',
	 'Petroleum and Gas Engineering',
	 'Agricultural Economics',
	 'Philosophy',
	 'Food Science and Technology',
	 'Linguistics and Nigerian Languages',
	 'Pure and Industrial Chemistry',
	 'Business Management',
	 'Agricultural and Bioresources Engineering',
	 'Public Administration and Local Government',
	 'Management Information System',
	 'Marketing')
option3_li = ('Others',
	 'Covenant University Ota',
	 'University of Lagos',
	 'Obafemi Awolowo University,Ile-Ife',
	 'University of Ibadan',
	 'Babcock University,Ilishan-Remo',
	 'University of Benin',
	 'University of Ilorin',
	 'Others (For foreign trained students)',
	 'Lagos State University Ojo, Lagos.',
	 'University of Nigeria, Nsukka',
	 'University of Agriculture, Abeokuta.',
	 'Bowen University, Iwo',
	 'Ladoke Akintola University of Technology, Ogbomoso',
	 'University of Port-Harcourt',
	 'Ekiti State University',
	 'Olabisi Onabanjo University Ago-Iwoye',
	 'Federal University of Technology, Akure',
	 'Nnamdi Azikiwe University, Awka',
	 'Federal University of Technology, Owerri',
	 'Ahmadu Bello University, Zaria',
	 'Federal University of Technology, Minna.',
	 'Lagos State Polytechnic, Ikorodu, Ikeja, Lagos, Lagos State.',
	 'Adekunle Ajasin University, Akungba.',
	 'Imo State University, Owerri',
	 "Redeemer's University, Mowe",
	 'Delta State University Abraka',
	 'Osun State University, Oshogbo',
	 'Yaba College of Technology, Yaba, Lagos State.',
	 'Anambra State University of Science & Technology, Uli',
	 'Ebonyi State University, Abakaliki',
	 'Ambrose Alli University, Ekpoma,',
	 'Federal Polytechnic Nekede, Owerri, Imo State.',
	 'Abia State University, Uturu.',
	 'Landmark University,Omu-Aran.')
option4_li = ('Yes', 'No','Ongoing')

with col1:
	option1 = st.selectbox(
	    'What is your gender',
	    option1_li)
	option3 = st.selectbox(
	    'Polytechnic/University attended',
	    option3_li)


with col2:
	option2 = st.selectbox(
	    'Title of course studied',
	    option2_li)
	option4 = st.selectbox(
	    'Have you completed your NYSC?',
	    option4_li)


#st.button("Predict")

final = ['Entry level', 'Clerical and administrative','Experience/Professional','Managerial','Executive Director']
if st.button("Predict"):
	result = clf.predict([[option1_li.index(option1), option2_li.index(option2), option3_li.index(option3), option4_li.index(option4)]])
	st.text('Your next job level is '+final[result[0]])
	