import pickle
import streamlit as st

text_clf = pickle.load(open('mbti_svm_v2.sav', 'rb'))

text = st.text_area('Enter the text')

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
for i in personalities:
    st.markdown("->" + i)

st.markdown(dicta[string])

