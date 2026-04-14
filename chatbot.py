import streamlit as st

st.title("🏥 AI Health Chatbot")

st.write("Type your symptoms to get health advice.")

symptoms = st.text_input("Enter symptoms:")

def chatbot_response(text):
    text = text.lower()

    if "fever" in text:
        return "You may have a fever. Stay hydrated and consult a doctor if it persists."

    elif "headache" in text:
        return "It could be due to stress or dehydration. Take rest and drink water."

    elif "stomach pain" in text:
        return "Avoid spicy food and drink warm water. Consult a doctor if pain continues."

    elif "cold" in text or "cough" in text:
        return "You may have a cold. Drink warm fluids and take rest."

    elif "sore throat" in text:
        return "Gargle with warm salt water and avoid cold drinks."

    elif "vomiting" in text:
        return "Stay hydrated. Take small sips of water and avoid heavy food."

    elif "diarrhea" in text:
        return "Drink ORS and plenty of fluids. Consult a doctor if severe."

    elif "back pain" in text:
        return "Take rest, maintain good posture, and apply a hot compress."

    elif "chest pain" in text:
        return "This could be serious. Seek medical help immediately."

    elif "dizziness" in text:
        return "Sit or lie down and drink water. Could be due to low BP or dehydration."

    elif "skin rash" in text:
        return "Keep the area clean and avoid scratching. Use mild creams if needed."

    elif "allergy" in text:
        return "Avoid triggers and consider antihistamines if prescribed."

    elif "eye pain" in text:
        return "Avoid screen time and wash eyes with clean water."

    elif "tooth pain" in text:
        return "Rinse with warm salt water and consult a dentist."

    elif "ear pain" in text:
        return "Avoid inserting objects. Consult a doctor if pain persists."

    else:
        return "I'm here to help. Please describe your symptoms clearly."

if st.button("Get Advice"):
    if symptoms:
        result = chatbot_response(symptoms)
        st.success(result)
    else:
        st.warning("Please enter symptoms")