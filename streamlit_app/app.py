import streamlit as st
import requests
import time

st.set_page_config(
    page_title="TechSage Crew — AI Research Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

API_URL = "http://127.0.0.1:8000/run-crew"

st.title("🤖 TechSage Crew")
st.caption("🧠 TechSage Crew autonomously researches emerging technologies and generates detailed, reader-friendly articles based on real-time insights.")

st.markdown("### ✍️ Enter a topic to research:")
topic = st.text_input("Example: AI in Healthcare", placeholder="Type your topic here...")

if st.button("Run CrewAI"):
    if not topic.strip():
        st.warning("⚠️ Please enter a valid topic before running the Crew.")
    else:
        st.info("⏳ Running the CrewAI pipeline... please wait.")
        start_time = time.time()

        try:
            response = requests.post(API_URL, json={"topic": topic})

            if response.status_code == 200:
                data = response.json()
                elapsed = round(time.time() - start_time, 2)

                if data.get("result") and data["result"].strip() != "None":
                    st.success(f"✅ CrewAI completed successfully in {elapsed}s!")
                    st.markdown("### 🧠 **Generated Report:**")
                    output_text = data["result"]
                    replacements = {
                        "#": "",
                        "*": "",
                        "- ": "",
                        ">": "",
                        "`": "",
                    }
                    for key, val in replacements.items():
                        output_text = output_text.replace(key, val)
                    st.write(output_text)


                else:
                    st.error("⚠️ CrewAI returned no result. Please check the backend logs.")
            else:
                st.error(f"❌ API Error {response.status_code}: {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("⚠️ Could not connect to the FastAPI backend. Is it running on port 8000?")
        except Exception as e:
            st.error(f"💥 Unexpected error: {e}")

st.sidebar.header("About TechSage Crew")
st.sidebar.markdown("""
**TechSage Crew** is a collaborative AI framework powered by:
- 🧠 **CrewAI** for agent orchestration  
- 🗞️ **Gemini 2.0 Flash** for reasoning & writing  
- 🌐 **Serper Search Tool** for real-time data retrieval  
- ⚡ Integrated via FastAPI + Streamlit  
---
**Developer:** Md. Reyad Hossain  
📧 reyadhasan7254@gmail.com  
""")
