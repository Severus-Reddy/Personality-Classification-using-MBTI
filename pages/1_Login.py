import streamlit as st
import pandas as pd
import pickle
import base64
from pathlib import Path

st.set_page_config(page_title="Login/Register")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.pexels.com/photos/4067870/pexels-photo-4067870.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}"""
st.markdown(page_bg_img, unsafe_allow_html=True)



# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Login"""

	st.title("Login")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home Page")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				text_clf = pickle.load(open('mbti_svm_v2.sav', 'rb'))

				def get_img_as_base64(file):
				    with open(file, "rb") as f:
				        data = f.read()
				    return base64.b64encode(data).decode()


				img = get_img_as_base64("C:/Users/bobby/Downloads/py -m streamlit run Home.py/close-up-fresh-grass_1160-618.png")

				page_bg_img = f"""
				<style>
				[data-testid="stAppViewContainer"] > .main {{
				background-image: url("https://images.pexels.com/photos/4067870/pexels-photo-4067870.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
				background-size: 100%;
				background-position: top left;
				background-repeat: no-repeat;
				background-attachment: local;
				}}
				[data-testid="stHeader"] {{
				background: rgba(0,0,0,0);
				}}
				[data-testid="stToolbar"] {{
				right: 2rem;
				}}
				</style>
				"""

				st.markdown(page_bg_img, unsafe_allow_html=True)
				st.title("Personality Classification")

				text = st.text_area('Tell me something about yourself or something interesting about anything or something you want to share in 2 or 3 lines?')

				new_output = text_clf.predict([text])

				string = "".join(new_output)
				my_dict={'I':"INTROVERSION", 'E':"EXTRAVERSION",'S':"SENSING",'N':"INTUITION",'T':"THINKING",'F':"FEELING",'J':"JUDGING",'P':"PERCEIVING"}

				personalities = []

				for key in my_dict:
					if key in string:
						personalities.append(my_dict[key])

				dicta={'INTJ':"Imaginative and strategic thinkers, with a plan for everything.",
					'INTP':"Innovative inventors with an unquenchable thirst for knowledge.",
					'ENTJ':"Bold, imaginative and strong-willed leaders, always finding a way – or making one.",
					'ENTP':"Smart and curious thinkers who cannot resist an intellectual challenge.",
					'INFJ':"Quiet and mystical, yet very inspiring and tireless idealists.",
					'INFP':"Poetic, kind and altruistic people, always eager to help a good cause.",
					'ENFJ':"Charismatic and inspiring leaders, able to mesmerize their listeners.",
					'ENFP':"Enthusiastic, creative and sociable free spirits, who can always find a reason to smile.",      
					'ISTJ':"Practical and fact-minded individuals, whose reliability cannot be doubted.",
					'ISFJ':"Very dedicated and warm protectors, always ready to defend their loved ones.",
					'ESTJ':"Excellent administrators, unsurpassed at managing things – or people.",
					'ESFJ':"Extraordinarily caring, social and popular people, always eager to help.",
					'ISTP':"Bold and practical experimenters, masters of all kinds of tools.",
					'ISFP':"Flexible and charming artists, always ready to explore and experience something new.",
					'ESTP':"Smart, energetic and very perceptive people, who truly enjoy living on the edge.",
					'ESFP':"Spontaneous, energetic and enthusiastic people – life is never boring around them.",}
				st.markdown(string)

				for i in personalities:
					st.markdown("->" + i)

				st.markdown(dicta[string])
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()