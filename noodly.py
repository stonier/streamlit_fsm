import streamlit as st


def show():
    st.write(
        """
        ## Noodle Counter
        """
    )
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    def increment():
        st.session_state.counter += 1

    st.write("Noodles:", st.session_state.counter)
    st.button("Plus one!", on_click=increment)

    if st.session_state.counter >= 50:
        st.success("King of counting there! Your trophy for reaching 50: 🏆")
    elif st.session_state.counter >= 10:
        st.warning("You have been blessed by the noodly appendages with 10 tickles!")
