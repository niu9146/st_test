import time
import streamlit as st


@st.cache_data(show_spinner=True)
def get_answer_to_life_universe_and_everything():
    time.sleep(5)
    return 42


def main():
    data = get_answer_to_life_universe_and_everything()
    st.markdown(f"The Answer to the Ultimate Question of Life, The Universe, and Everything is **{data}**")
    if st.button("Clear cache"):
        st.cache_data.clear()


if __name__ == "__main__":
    main()
