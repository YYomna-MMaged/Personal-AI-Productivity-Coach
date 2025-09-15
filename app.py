import streamlit as st
from scr.server_model import analyze_day_report, analyze_tasks
from automation import send_telegram_message

def clean_output(text: str, sentance) -> str:
    if sentance in text:
        text = text.split(sentance, 1)[1]
    for phrase in [
        "You are a helpful", 
        "You are an expert", 
        "ONLY output", 
        "Do NOT include",
        "**",
        "AI Feedback",
        "AI Suggestions",
        "Next line should be: Empathetic Efficiency ❤️📈",
        "Productivity Report",
        "After that, you should continue writing the report directly without any other headers."
    ]:
        text = text.replace(phrase, "")
    text = sentance + text
    return text.strip()


st.set_page_config(page_title="Personal AI Productivity Coach", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
    .big-title {
        font-size: 40px !important;
        text-align: center;
        color: #ff69b4;
    }
    .funny-subtitle {
        font-size: 20px !important;
        text-align: center;
        color: #6a5acd;
        margin-bottom: 20px;
    }
    /* Center the tabs */
    div[data-baseweb="tab-list"] {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <h1 style='text-align: center; color: white; font-size: 40px; font-weight: bold;'>
        🌟 Personal AI Productivity Coach 🌟
    </h1>
    """,
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs(["📝 Daily Report", "✅ Task Manager"])

with tab1:
    st.title("📝 Daily Report Analysis")
    st.write("Spill the green mint about your day 🍵 and I’ll give you magical insights 💫")

    user_text = st.text_area("Tell me about your day, buddy:")

    if st.button("Analyze My Day 🎯"):
        if user_text.strip():
            with st.spinner("Hold on... sipping anise while analyzing your day 🍵..."):
                try:
                    raw_response = analyze_day_report(user_text)
                    response = clean_output(raw_response, "Productivity Report")
                    st.success("✅ Boom! Got your analysis!")
                    st.write("### ✨ Here’s what I think about your day:")
                    st.write(response)

                    if send_telegram_message(response):
                        st.info("📩 Report sent to Telegram successfully!")
                    else:
                        st.warning("⚠️ Failed to send report to Telegram.")

                except Exception as e:
                    st.error(f"Oops! Error: {e}")
        else:
            st.warning("Don’t be shy 😅, tell me something first!")

with tab2:
    st.title("✅ Task Organization")
    st.write("Drop your tasks here 📝, and I’ll turn chaos into order 🪄✨")

    tasks_text = st.text_area("Write your tasks (one per line):")

    if st.button("Organize My Tasks 🤹‍♀️"):
        if tasks_text.strip():
            with st.spinner("Juggling your tasks... don’t worry I got skills 🤹‍♂️..."):
                try:
                    raw_response = analyze_tasks(tasks_text)
                    response = clean_output(raw_response, "Tasks Suggestion")
                    st.success("✅ Tasks organized, like a boss!")
                    st.write("### 💡 Here’s your new plan:")
                    st.write(response)

                    if send_telegram_message(response):
                        st.info("📩 Tasks sent to Telegram successfully!")
                    else:
                        st.warning("⚠️ Failed to send tasks to Telegram.")
                
                except Exception as e:
                    st.error(f"Oops! Error: {e}")
        else:
            st.warning("Give me at least one task, lazybones 😜")
