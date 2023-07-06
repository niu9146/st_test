import streamlit as st

if 'story' not in st.session_state:
    st.session_state.story = ""

options = [
    "Option 1: Eric decides to intervene directly, using his powers to disarm the robbers and save the hostages.",
    "Option 2: Eric takes a more cautious approach and uses his powers to stealthily gather information about the robbers' plans before alerting the authorities.",
    "Option 3: Eric decides to observe the situation from a safe distance, trying to analyze the criminals' weaknesses and come up with a strategic plan of action.",
    "Option 4: Overwhelmed by the gravity of the situation, Eric hesitates and struggles to decide on the best course of action.",
    "Option 5: Eric realizes that his powers are not yet fully developed, so he chooses to retreat and seek guidance from someone who can help him understand and control his abilities."
]

story_intro = """in the bustling city of Metroville, there lived an ordinary 17-year-old boy named Eric. \n
Little did everyone know, Eric possessed extraordinary superpowers that he had yet to fully understand and master. \n
From a young age, he had dreamed of becoming a superhero and using his abilities to protect the innocent and fight for justice. \n
One sunny day, as Eric walked home from school, he noticed a commotion in the distance. Curiosity piqued, he hurried toward the source of the disturbance. \n
To his surprise, he stumbled upon a bank robbery in progress.The robbers were armed and threatening the innocent bank employees and customers. \n
Now faced with a pivotal moment, Eric had to make a choice. How would he use his burgeoning powers to confront the criminals and bring them to justice? \n"""

story_end = "What path will Eric choose? The decision is yours to make. \n"

st.session_state.story = st.session_state.story + story_intro

st.session_state.story = st.session_state.story + story_end

text_col, img_col = st.columns(2)

with text_col:
    storyBox = st.write(st.session_state.story)
with img_col:
    st.image("https://picsum.photos/200")

for option in options:
    if option.startswith("Option 1"):
        text_col.markdown(f"<span style='color: Thistle'>{option}</span>", unsafe_allow_html=True)
    elif option.startswith("Option 2"):
        text_col.markdown(f"<span style='color: Thistle'>{option}</span>", unsafe_allow_html=True)
    elif option.startswith("Option 3"):
        text_col.markdown(f"<span style='color: Thistle'>{option}</span>", unsafe_allow_html=True)
    elif option.startswith("Option 4"):
        text_col.markdown(f"<span style='color: Thistle'>{option}</span>", unsafe_allow_html=True)
    elif option.startswith("Option 5"):
        text_col.markdown(f"<span style='color: Thistle'>{option}</span>", unsafe_allow_html=True)
