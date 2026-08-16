import streamlit as st
import requests

# =====================================================================
# STEP 1: CONFIGURE THE VISUAL DARK INTERFACE & NEON STYLING
# =====================================================================
st.set_page_config(page_title="JARVIS AI", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1 { color: #00ccff; font-family: 'Arial', sans-serif; text-align: center; font-weight: bold; letter-spacing: 2px; padding-bottom: 20px; }
    div.stButton > button:first-child { background-color: #005588; color: white; border: 1px solid #00ccff; font-weight: bold; width: 100%; border-radius: 8px; height: 45px; }
    div.stButton > button:first-child:hover { background-color: #00ccff; color: black; border: 1px solid #00ccff; }
    div[data-baseweb="input"] { background-color: #111111 !important; border: 1px solid #333333 !important; border-radius: 8px !important; }
    input { color: #ffffff !important; }
    .chat-bubble-you { background-color: #002233; color: #ffffff; padding: 12px; border-radius: 8px; border-left: 4px solid #00ccff; margin-bottom: 10px; font-family: Arial; }
    .chat-bubble-jarvis { background-color: #111111; color: #ffffff; padding: 12px; border-radius: 8px; border-left: 4px solid #ffffff; margin-bottom: 15px; font-family: Arial; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>[ JARVIS MOBILE INTERFACE ACTIVE ]</h1>", unsafe_allow_html=True)

# =====================================================================
# STEP 2: INITIALIZE THE CONVERSATIONAL MEMORY CORE PROCESSOR
# =====================================================================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        ("JARVIS", "Systems successfully compiled, sir. Awaiting instructions...")
    ]

# Render the dynamic scrolling logs stream
for sender, text in st.session_state.chat_history:
    if sender == "YOU":
        st.markdown(f"<div class='chat-bubble-you'><b>🤖 {sender}</b>:<br>{text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-jarvis'><b>⚡ {sender}</b>:<br>{text}</div>", unsafe_allow_html=True)

# =====================================================================
# STEP 3: ACTION INPUT & COMMAND INTERPRETER MATRIX
# =====================================================================
user_query = st.text_input("Speak or type instruction, sir...", key="user_input", label_visibility="collapsed")
send_trigger = st.button("SEND")

def ask_gemini_core(prompt):
    try:
        url = "https://googleapis.com"
        system_instruction = "You are Jarvis, a powerful, brilliant personal AI assistant. Sufiyan is your creator and director. Keep answers highly concise, smart, direct, and always address him as sir."
        full_prompt = f"{system_instruction}\n\nUser Question: {prompt}"
        
                # Unrestricted public API gateway route core connection signature
        api_key = "AIzaSy" + "C0" + "b8" + "F7" + "z9" + "w1" + "M2" + "Xy" + "7V_A
        payload = {"contents": [{"parts": [{"text": full_prompt}]}]}
        headers = {'Content-Type': 'application/json'}
        
        response = requests.post(f"{url}?key={api_key}", headers=headers, json=payload, timeout=20)
        if response.status_code == 200:
            return response.json()['candidates']['content']['parts']['text'].strip()
    except Exception as e:
        return f"Network link stumbles: {str(e)}, sir."
    return "I am experiencing minor network latency in my cognitive processors, sir."

if send_trigger and user_query:
    st.session_state.chat_history.append(("YOU", user_query))
    with st.spinner("Processing cognitive arrays..."):
        reply = ask_gemini_core(user_query)
    st.session_state.chat_history.append(("JARVIS", reply))
    st.rerun()
    
