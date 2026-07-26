"""
Mental Health Score Prediction System
--------------------------------------
A professional Streamlit frontend that consumes a FastAPI backend
(POST /predict) to predict a student's mental health score based on
social media usage and lifestyle habits.

Run with:
    pip install streamlit requests pandas
    streamlit run streamlit_app.py
"""

import streamlit as st
import requests
import pandas as pd

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="Mental Health Prediction System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# API endpoint
API_URL = "https://mental-health-score-ikoj.onrender.com/predict"

# ==========================================================
# CUSTOM CSS — Professional styling, gradients, cards, fonts
# ==========================================================
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        /* Hide default Streamlit branding for a cleaner look */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Hero / page header gradient banner */
        .hero-header {
            padding: 2.5rem 2rem;
            border-radius: 18px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            color: white;
            text-align: center;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.35);
            margin-bottom: 2rem;
        }
        .hero-header h1 {
            font-size: 2.6rem;
            font-weight: 800;
            margin-bottom: 0.4rem;
        }
        .hero-header p {
            font-size: 1.1rem;
            font-weight: 300;
            opacity: 0.95;
        }

        /* Generic content card */
        .info-card {
            background: #ffffff;
            border-radius: 16px;
            padding: 1.6rem 1.8rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
            border: 1px solid rgba(0,0,0,0.04);
            transition: transform 0.25s ease, box-shadow 0.25s ease;
            height: 100%;
            margin-bottom: 1rem;
        }
        .info-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 14px 30px rgba(0,0,0,0.14);
        }
        .info-card h3 {
            margin-top: 0;
            color: #4b2e83;
        }

        /* Feature card icon circle */
        .feature-icon {
            font-size: 2.4rem;
            margin-bottom: 0.6rem;
        }

        /* Result card after prediction */
        .result-card {
            background: linear-gradient(135deg, #43cea2 0%, #185a9d 100%);
            border-radius: 20px;
            padding: 2rem;
            color: white;
            text-align: center;
            box-shadow: 0 12px 30px rgba(24, 90, 157, 0.35);
            margin-top: 1.5rem;
        }
        .result-card h1 {
            font-size: 3.4rem;
            font-weight: 800;
            margin: 0.3rem 0;
        }
        .result-card p {
            font-size: 1.2rem;
            opacity: 0.95;
        }

        /* Recommendation card */
        .reco-card {
            background: #fff8e6;
            border-left: 6px solid #f7b733;
            border-radius: 10px;
            padding: 1.1rem 1.4rem;
            margin-top: 1.2rem;
            color: #5a4200;
            font-weight: 500;
        }

        /* Gradient buttons */
        div.stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: 600;
            border: none;
            border-radius: 12px;
            padding: 0.7rem 1.6rem;
            font-size: 1.05rem;
            transition: all 0.25s ease;
            box-shadow: 0 6px 18px rgba(102, 126, 234, 0.4);
        }
        div.stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 24px rgba(102, 126, 234, 0.55);
            color: white;
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1f1c2c 0%, #2b2540 100%);
        }
        section[data-testid="stSidebar"] * {
            color: #f0f0f0 !important;
        }

        /* Custom footer */
        .custom-footer {
            text-align: center;
            padding: 1.4rem;
            margin-top: 3rem;
            border-top: 1px solid rgba(0,0,0,0.08);
            color: #888;
            font-size: 0.9rem;
        }

        /* Metric card colors */
        .metric-box {
            border-radius: 14px;
            padding: 1.2rem;
            text-align: center;
            color: white;
            font-weight: 600;
            box-shadow: 0 6px 16px rgba(0,0,0,0.15);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================
with st.sidebar:
    st.markdown(
        "<h2 style='text-align:center;'>🧠 Mental Health<br>Prediction System</h2>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["🏠 Home", "📘 About Project", "🎯 Prediction", "👨‍💻 Developer"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; font-size:0.85rem; opacity:0.7;'>"
        "Powered by Machine Learning & FastAPI</p>",
        unsafe_allow_html=True,
    )

# ==========================================================
# REUSABLE FOOTER
# ==========================================================
def render_footer():
    st.markdown(
        """
        <div class="custom-footer">
            © 2026 Mental Health Prediction System | Built with ❤️ using Streamlit &amp; FastAPI
        </div>
        """,
        unsafe_allow_html=True,
    )

# ==========================================================
# HOME PAGE
# ==========================================================
if page == "🏠 Home":
    st.markdown(
        """
        <div class="hero-header">
            <h1>🧠 Mental Health Score Prediction</h1>
            <p>An AI-powered system that predicts a student's mental health score
            based on social media usage and lifestyle habits.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown(
            """
            <div class="info-card">
                <h3>📊 About This Tool</h3>
                <p style="color:#444; line-height:1.7;">
                This machine learning application analyzes a student's daily habits —
                social media usage, sleep, study hours, physical activity, and stress
                levels — to estimate a <b>Mental Health Score (0–10)</b>. The goal is
                to raise awareness about how digital habits and lifestyle choices
                impact overall wellbeing, and to encourage healthier routines among
                students.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="info-card" style="text-align:center;">
                <div style="font-size:5rem;">🧑‍🎓📱💤</div>
                <p style="color:#666;">Student Wellness • Digital Habits • Balance</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### ✨ Key Features")
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown(
            """
            <div class="info-card" style="text-align:center;">
                <div class="feature-icon">⚡</div>
                <h3>Fast Prediction</h3>
                <p style="color:#666;">Get instant mental health score predictions
                in real time through a lightweight API call.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with f2:
        st.markdown(
            """
            <div class="info-card" style="text-align:center;">
                <div class="feature-icon">🤖</div>
                <h3>Machine Learning Model</h3>
                <p style="color:#666;">Trained on real-world survey data using
                robust regression techniques for reliable predictions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with f3:
        st.markdown(
            """
            <div class="info-card" style="text-align:center;">
                <div class="feature-icon">💚</div>
                <h3>Student Mental Wellness</h3>
                <p style="color:#666;">Designed to promote awareness and healthier
                digital habits among students worldwide.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_footer()

# ==========================================================
# ABOUT PAGE
# ==========================================================
elif page == "📘 About Project":
    st.markdown(
        """
        <div class="hero-header">
            <h1>📘 About the Project</h1>
            <p>Understanding the purpose, data, and technology behind this system.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class="info-card">
                <h3>🎯 Project Objective</h3>
                <p style="color:#444;">To predict a student's mental health score
                using lifestyle and social media usage patterns, helping identify
                early signs of poor mental wellbeing and encouraging healthier
                habits.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="info-card">
                <h3>📂 Dataset</h3>
                <p style="color:#444;">The model is trained on a survey-based
                dataset capturing student demographics, social media platform
                usage, screen time, study patterns, sleep, physical activity,
                and self-reported stress levels across multiple countries.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="info-card">
                <h3>🧬 Features Used</h3>
                <p style="color:#444;">Age, Gender, Country, Academic Level,
                Most Used Platform, Purpose of Use, Average Daily Usage Hours,
                Daily Unlocks, Study Hours, Physical Activity Hours,
                Sleep Hours per Night, and Stress Level.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h3>🤖 Machine Learning Model</h3>
                <p style="color:#444;">A regression model (built with
                Scikit-Learn) trained on the processed dataset and serialized
                using Joblib for fast, production-ready inference.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="info-card">
                <h3>🚀 FastAPI Backend</h3>
                <p style="color:#444;">A lightweight, high-performance REST API
                built with FastAPI serves the trained model via a
                <code>/predict</code> endpoint, validating incoming data with
                Pydantic before inference.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="info-card">
                <h3>🎨 Streamlit Frontend</h3>
                <p style="color:#444;">This interactive Streamlit application
                provides a clean, modern interface for users to input their
                data and instantly view their predicted mental health score.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 🛠️ Tech Stack")
    tech_cols = st.columns(6)
    tech_stack = [
        ("🐍", "Python"),
        ("🐼", "Pandas"),
        ("📈", "Scikit-Learn"),
        ("⚡", "FastAPI"),
        ("🎈", "Streamlit"),
        ("📦", "Joblib"),
    ]
    for col, (icon, name) in zip(tech_cols, tech_stack):
        with col:
            st.markdown(
                f"""
                <div class="info-card" style="text-align:center; padding:1rem;">
                    <div style="font-size:2rem;">{icon}</div>
                    <p style="font-weight:600; color:#333; margin:0;">{name}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    render_footer()

# ==========================================================
# PREDICTION PAGE
# ==========================================================
elif page == "🎯 Prediction":
    st.markdown(
        """
        <div class="hero-header">
            <h1>🎯 Predict Your Mental Health Score</h1>
            <p>Fill in your details below to get an instant AI-based prediction.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📝 Enter Your Details")

    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)

        # ---------- Column 1 ----------
        with col1:
            age = st.number_input("🎂 Age", min_value=10, max_value=100, value=20, step=1)
            gender = st.selectbox("⚧ Gender", ["Male", "Female"])
            country = st.text_input("🌍 Country", value="India")
            academic_level = st.selectbox(
                "🎓 Academic Level", ["Undergraduate", "Graduate", "High School"]
            )

        # ---------- Column 2 ----------
        with col2:
            platform = st.selectbox(
                "📱 Most Used Platform",
                [
                    "Facebook", "LinkedIn", "Instagram", "Snapchat", "Twitter",
                    "YouTube", "TikTok", "LINE", "KakaoTalk", "VKontakte",
                    "WhatsApp", "WeChat",
                ],
            )
            purpose = st.selectbox(
                "🎯 Purpose of Use",
                ["Networking", "Education", "Entertainment", "News"],
            )
            avg_daily_usage = st.slider(
                "⏱️ Avg Daily Usage Hours", min_value=0.0, max_value=24.0, value=4.0, step=0.5
            )
            daily_unlocks = st.number_input(
                "🔓 Daily Unlocks", min_value=0, max_value=300, value=50, step=1
            )

        # ---------- Column 3 ----------
        with col3:
            study_hours = st.slider(
                "📚 Study Hours", min_value=0.0, max_value=24.0, value=5.0, step=0.5
            )
            physical_activity = st.slider(
                "🏃 Physical Activity Hours", min_value=0.0, max_value=24.0, value=1.0, step=0.5
            )
            sleep_hours = st.slider(
                "😴 Sleep Hours Per Night", min_value=0.0, max_value=24.0, value=7.0, step=0.5
            )
            stress_level = st.selectbox(
                "😰 Stress Level", ["Low", "Medium", "High", "Very High"]
            )

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🔮 Predict Score", use_container_width=True)

    # ------------------------------------------------------
    # HANDLE FORM SUBMISSION
    # ------------------------------------------------------
    if submitted:
        # Basic client-side validation
        if not country.strip():
            st.error("⚠️ Please enter a valid country name.")
        else:
            payload = {
                "Age": int(age),
                "Gender": gender,
                "Country": country.strip(),
                "Academic_Level": academic_level,
                "Most_Used_Platform": platform,
                "Purpose_Of_Use": purpose,
                "Avg_Daily_Usage_Hours": float(avg_daily_usage),
                "Daily_Unlocks": int(daily_unlocks),
                "Study_Hours": float(study_hours),
                "Physical_Activity_Hours": float(physical_activity),
                "Sleep_Hours_Per_Night": float(sleep_hours),
                "Stress_Level": stress_level,
            }

            try:
                with st.spinner("🔎 Analyzing your data..."):
                    response = requests.post(API_URL, json=payload, timeout=10)

                if response.status_code == 200:
                    result = response.json()
                    score = result.get("predicted_mental_health_score", None)

                    if score is None:
                        st.error("⚠️ Unexpected response format from the server.")
                    else:
                        score = round(float(score), 2)

                        # ---------------- Interpretation ----------------
                        if score < 3:
                            category = "Poor Mental Health"
                            color = "#e74c3c"
                            advice = (
                                "Your indicators suggest significant strain. Consider "
                                "reducing screen time, prioritizing sleep, and speaking "
                                "with a counselor or mental health professional."
                            )
                        elif score < 5:
                            category = "Below Average"
                            color = "#e67e22"
                            advice = (
                                "There's room for improvement. Try setting daily screen "
                                "time limits, increasing physical activity, and "
                                "maintaining a consistent sleep schedule."
                            )
                        elif score < 7:
                            category = "Moderate"
                            color = "#f1c40f"
                            advice = (
                                "You're doing okay, but small changes — more sleep, "
                                "regular exercise, and balanced social media use — "
                                "could further improve your wellbeing."
                            )
                        elif score < 8.5:
                            category = "Good"
                            color = "#2ecc71"
                            advice = (
                                "Great job! Keep maintaining your healthy study, "
                                "sleep, and activity balance."
                            )
                        else:
                            category = "Excellent"
                            color = "#27ae60"
                            advice = (
                                "Excellent mental wellbeing! Continue your current "
                                "lifestyle habits and encourage others to do the same."
                            )

                        # ---------------- Result Card ----------------
                        st.markdown(
                            f"""
                            <div class="result-card">
                                <p>Predicted Mental Health Score</p>
                                <h1>{score} / 10</h1>
                                <p style="font-size:1.4rem; font-weight:700;">{category}</p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

                        # ---------------- Progress bar (gauge-like) ----------------
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.markdown("#### 📊 Score Meter")
                        st.progress(min(int((score / 10) * 100), 100))

                        # ---------------- Metric row ----------------
                        m1, m2, m3 = st.columns(3)
                        with m1:
                            st.metric("🧠 Mental Health Score", f"{score}/10")
                        with m2:
                            st.metric("📈 Category", category)
                        with m3:
                            st.metric("😰 Reported Stress", stress_level)

                        # ---------------- Recommendation ----------------
                        st.markdown(
                            f"""
                            <div class="reco-card">
                                💡 <b>Recommendation:</b> {advice}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

                elif response.status_code == 422:
                    st.error("⚠️ Validation failed. Please check your input values and try again.")
                else:
                    st.error(f"⚠️ Server returned an error (status code {response.status_code}).")

            except requests.exceptions.ConnectionError:
                st.error("⚠️ Unable to connect to FastAPI server. Please make sure the backend is running at http://127.0.0.1:8000")
            except requests.exceptions.Timeout:
                st.error("⚠️ The request timed out. Please try again.")
            except Exception as e:
                st.error(f"⚠️ An unexpected error occurred: {e}")

    render_footer()

# ==========================================================
# DEVELOPER PAGE
# ==========================================================
elif page == "👨‍💻 Developer":
    st.markdown(
        """
        <div class="hero-header">
            <h1>👨‍💻 Developer Information</h1>
            <p>Meet the creator behind this project.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(
            """
            <div class="info-card" style="text-align:center;">
                <div style="font-size:5rem;">🧑‍💻</div>
                <h3>Yash Sitapara   </h3>
                <p style="color:#666;">Data Scientist &amp; ML Engineer</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="info-card">
                <h3>📌 Project Name</h3>
                <p style="color:#444;">Mental Health Prediction System</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="info-card">
                <h3>🛠️ Technologies Used</h3>
                <p style="color:#444;">Python, Pandas, Scikit-Learn, FastAPI, Streamlit, Joblib</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        link_col1, link_col2 = st.columns(2)
        with link_col1:
            st.markdown(
                """
                <div class="info-card" style="text-align:center;">
                    <h3>🔗 GitHub</h3>
                    <a href="https://github.com/yash11092005" target="_blank">github.com/yash11092005</a>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with link_col2:
            st.markdown(
                """
                <div class="info-card" style="text-align:center;">
                    <h3>💼 LinkedIn</h3>
                    <a href="https://www.linkedin.com/in/yash-sitapara-3ab434352/" target="_blank">linkedin.com/in/Yash Sitapara</a>
                </div>
                """,
                unsafe_allow_html=True,
            )

    render_footer()
