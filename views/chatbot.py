import streamlit as st
import utils.state_manager as state_manager

def render(domains_data):
    st.title("🤖 AI Chatbot Assistant")
    st.markdown("<p style='color: var(--muted);'>Ask me anything about engineering domains, salaries, or what skills you need to learn!</p>", unsafe_allow_html=True)
    
    # Display chat messages from history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # Chat input
    if prompt := st.chat_input("E.g., What is the salary for a data scientist?"):
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # Generate Rule-based Response
        response = generate_response(prompt.lower(), domains_data)
        
        # Add assistant message
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

def generate_response(query, domains_data):
    # Very simple keyword matching
    if "salary" in query or "pay" in query:
        for domain, data in domains_data.items():
            if domain.lower() in query:
                s = data.get("salary_trends", {})
                return f"The salary for {domain} typically ranges from **{s.get('Entry')}** for entry-level, up to **{s.get('Senior')}** for senior roles."
        return "Which domain's salary are you interested in? (e.g., Computer Science, Mechanical)"
        
    if "skill" in query or "learn" in query:
        for domain, data in domains_data.items():
            if domain.lower() in query:
                skills = ", ".join(data.get("skills", [])[:5])
                return f"To succeed in {domain}, you should focus on learning: **{skills}**."
        return "I can tell you the skills needed for any domain. Just ask 'What skills do I need for Data Science?'"
        
    if "hi" in query or "hello" in query:
        return "Hello! How can I assist you with your engineering roadmap today?"
        
    return "I'm a simple rule-based assistant currently. Try asking me about the **salary** or **skills** for a specific engineering domain!"
