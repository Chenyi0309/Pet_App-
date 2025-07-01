import streamlit as st
import pandas as pd
import datetime

# Title
st.title("🐾 Pet Owner Insights Survey - Chicago")
st.markdown("Help us design the perfect pet care app! Your answers will help us better understand your needs.")

# Section 1: Basic Info
st.header("1. About You and Your Pet")
pet_type = st.radio("What kind of pet do you have?", ["Dog", "Cat", "Rabbit", "Bird", "Other"])
num_pets = st.slider("How many pets do you currently have?", 1, 10, 1)

# Section 2: App Usage
st.header("2. Your Current Tools")
current_apps = st.multiselect(
    "Which apps or websites do you currently use to help take care of your pet(s)?",
    ["Chewy", "Rover", "PetDesk", "Instagram", "Facebook Groups", "Reddit", "Google Calendar", "None", "Other"]
)

pain_points = st.multiselect(
    "What are the most frustrating parts of being a pet owner?",
    [
        "Remembering vaccines & vet appointments",
        "Finding trusted vets or groomers",
        "Shopping for the right food/toys",
        "No community or social features",
        "Hard to track health data",
        "Other"
    ]
)

# Section 3: Interest in New Features
st.header("3. Your Interest in New Features")
features_interest = st.multiselect(
    "Which features would you love to see in a pet care app?",
    [
        "Vaccination and medication reminders",
        "Online vet consultations",
        "Pet profile and health tracking",
        "Local pet services (grooming, sitting, walking)",
        "Pet community and sharing photos",
        "Pet product recommendations & shopping",
        "Event organization (pet meetups, competitions)"
    ]
)

pay_willingness = st.slider("How much would you be willing to pay monthly for a well-designed pet care app with the features above?", 0, 20, 0, step=1)

# Optional contact
st.header("4. Optional Contact")
email = st.text_input("Leave your email if you’d like to get updates about the app or participate in beta testing (optional):")

# Submit
if st.button("Submit Survey"):
    response = {
        "Timestamp": datetime.datetime.now(),
        "Pet Type": pet_type,
        "Number of Pets": num_pets,
        "Current Apps": ", ".join(current_apps),
        "Pain Points": ", ".join(pain_points),
        "Interested Features": ", ".join(features_interest),
        "Willingness to Pay": pay_willingness,
        "Email": email
    }
    df = pd.DataFrame([response])
    df.to_csv("pet_survey_responses.csv", mode='a', header=False, index=False)
    st.success("✅ Thank you for your input! Your response has been recorded.")
