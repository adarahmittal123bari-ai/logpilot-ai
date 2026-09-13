import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="LogPilot AI", page_icon="🚀")
st.title("🚀 LogPilot: AI DevOps Assistant")
st.markdown("Paste cryptic server logs or terminal errors. AI will diagnose and fix them.")

api_key = st.text_input("Enter Gemini API Key:", type="password")
log_text = st.text_area("Paste Error Log Here:", height=200)

if st.button("Analyze & Fix Error"):
    if not api_key or not log_text:
        st.warning("⚠️ API Key aur Error Log dono daalna zaroori hai.")
    else:
        with st.spinner("Analyzing traceback..."):
            try:
                genai.configure(api_key=api_key)
                # IQ 200: Auto-detect working model
                available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                working_model = available_models[0]
                model = genai.GenerativeModel(working_model)
                
                prompt = f"Act as a DevOps Expert. Read this error: {log_text}. Give 1. Root Cause, 2. Step-by-step fix, 3. Terminal commands. Use clean markdown."
                response = model.generate_content(prompt)
                
                st.success("Analysis Complete!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"API Error: {e}")
