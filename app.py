import streamlit as st
from menu import menu
# Set custom page title and other configurations
st.set_page_config(
    page_title="Mind-Set-Go",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)
def main():
    st.title("*Welcome to the Public Test Platform*")
    st.header("🩺Mind-Set-Go: A personalized mental health system using python.")
    st.write("Please use the sidebar to navigate to different tests.")
    st.warning("**Note:** Before going read the disclaimer!")
    disclaimer_content = """
    **Disclaimer:**
    The information provided in this platform is for educational and informational purposes only. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read on this platform.
    """
    # Create the dropdown with logo and warning
    with st.expander("ℹ️ **Disclaimer!**"):
        st.image("img3.png.crdownload", width=100)
        st.markdown(disclaimer_content)
    st.image('img1.jpg', caption='Save the Students from mental suffering!')
    st.subheader("About")
    st.markdown("""
    This platform mainly aims to make the students aware of their mental health problems like Depression, Low-Self Esteem, Social Anxiety, and lastly Insomnia and Sleep Problems. You can analyse the reports of your results and also check the overall statistics of our tests taken by all the students so far. Hope this platform contributes to the improvement of student mental health awareness!! Thank you for your valuable time to consider taking our tests. Happy Mental Well-being:)
    """)
    # st.balloons()
    st.snow()
    @st.dialog("Welcome!")
    def modal_dialog():
        st.write("Hello, Welcome to MindSetGo!")
    modal_dialog()
    
        

if __name__ == "__main__":
    menu()
    main()
