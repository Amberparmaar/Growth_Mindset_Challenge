import streamlit as st

# Page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="⭐", layout="wide")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Reflection", "Achievements", "About"])

# Home Page
if page == "Home":
    st.markdown('<h1 style="color: purple;">🌱 Growth Mindset Challenge by Amber Parmaar</h1>', unsafe_allow_html=True)
    st.header("Welcome to a journey of growth, resilience, and endless possibilities! 🚀")
    st.write("*Every challenge is a chance to grow. Learn from mistakes, embrace new experiences, and build a mindset for success!*")

    st.markdown("---")

    # Quote Section
    st.markdown('<h1 style="color: green;">🌑 Today Wisdom on Personal Growth</h1>', unsafe_allow_html=True)
    st.write("*🔥 Your strength lies not in the outcome, but in your will to grow and improve.- Unknown*")

    st.markdown("---")

    st.header("💪 How are you challenging yourself today?")
    user_input = st.text_area("Share your goals and progress below.")

    if user_input:
        st.success(f"You are facing: {user_input}. Keep pushing forward toward your goals! 🚀")
    else:
        st.warning("Tell us about your challenge to get started! 🌟")

# Reflection Page
elif page == "Reflection":
    st.markdown('<h1 style="color: orange;">📖 Reflect on Your Progress</h1>', unsafe_allow_html=True )
    st.write("Take a moment to reflect on your progress and what you've learned from your experiences.")

    reflection = st.text_area("What have you learned from your challenges today?")

    if reflection:
        st.success(f"Great insight! You've learned: {reflection} 🌟")
    else:
        st.info("Share your reflection to continue growing! 🌱")

# Achievements Page
elif page == "Achievements":
    st.markdown('<h1 style="color: blue;">🏆 Celebrate Your Achievements</h1>', unsafe_allow_html=True)
    achievement = st.text_area("What have you accomplished today?")

    if achievement:
        st.success(f"Congratulations on your achievement: {achievement} 🎉")
    else:
        st.info("Share your achievements to celebrate your growth! 🌟")

# About Page
elif page == "About":
    st.markdown('<h1 style="color: rgb(252, 3, 102);">📌 About This Project</h1>', unsafe_allow_html=True)
    st.write("This project is designed to help you build a growth mindset by setting challenges, reflecting on your progress, and celebrating achievements.")
    
    st.write("Keep up the great work! 🌟")
    st.markdown("---")
    st.write("**Created with ❤️ by Amber Parmaar**")
    st.write("Find me on [LinkedIn](https://www.linkedin.com/in/amber-shoukat-19724a293/)")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("🚀 Keep growing and learning!")
