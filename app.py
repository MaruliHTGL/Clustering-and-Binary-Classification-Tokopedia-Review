import streamlit as st
from ml_app import run_ml_app

def main():
    menu = ['Home', 'Review Analysis']
    choice = st.sidebar.radio("Menu", menu)

    if choice == 'Home':
        st.markdown(
            """
            <h1 style='text-align: center;'>Understand Sentiments, Elevate Experiences!</h1>
            <br>
            <p style='text-align: justify;'>
                Discover what users are saying about the <strong>Tokopedia</strong> app and transform their feedback into actionable insights that drive growth. With our powerful review analysis platform, you can go beyond the surface and truly understand your users' needs, preferences, and challenges.
            </p>
            <br>
            <h3 style='text-align: justify;'>Why Analyze User Reviews?</h3>
            <p style='text-align: justify;'> Every review holds valuable information. By analyzing user feedback, you can:</p>
            <ul>
                <li><strong>Discover Strengths:</strong> Identify what users love most about <strong>Tokopedia</strong> app to continue delivering what works.</li>
                <li><strong>Spot Areas for Improvement:</strong> Pinpoint recurring issues and address them before they impact your user base.</li>
                <li><strong>Uncover Trends:</strong> Stay ahead by recognizing emerging trends and changing customer expectations.</li>
                <li><strong>Make Informed Decisions:</strong> Use data-backed insights to prioritize updates and features that matter most.</li>
            </ul>
            <br>
            <p style='text-align: justify;'>
                <strong>Disclaimer:<strong> This tool is only to help analyze and may analyze reviews incorrectly. Perform further analysis to reduce analysis errors
            </p>
            <br>
            <p style='text-align: center;'><strong>Let your users guide your next big move!</strong></p>
            """, 
            unsafe_allow_html=True
        )

    elif choice == "Review Analysis":
        run_ml_app()

if __name__ == '__main__':
    main()
