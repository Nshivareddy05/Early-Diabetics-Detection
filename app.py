import streamlit as st
from streamlit_option_menu import option_menu
from utils.css_loader import load_css
from utils.data_loader import load_domains_data, load_roadmaps_data
import config

# Import Pages
from views import home, domain_explorer, compare_domains, ai_recommendation, skill_gap, daily_planner, dashboard, career_prep, chatbot
import utils.state_manager as state_manager

# Page Configuration MUST be the first Streamlit command
st.set_page_config(
    page_title=config.APP_NAME,
    page_icon=config.APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
state_manager.init_session_state()

# Load global CSS
load_css()

# Load Data
domains_data = load_domains_data()
roadmaps_data = load_roadmaps_data()

# Sidebar Navigation
with st.sidebar:
    st.markdown(f"<h2 style='text-align: center; color: var(--primary);'>{config.APP_ICON} Hub</h2>", unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Dashboard", "Domain Explorer", "Career Prep", "Compare", "AI Recommend", "Skill Gap", "Daily Planner", "Chatbot"],
        icons=["house", "speedometer2", "compass", "briefcase", "arrow-left-right", "robot", "tools", "calendar", "chat-dots"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": config.THEME_COLORS['secondary'], "font-size": "18px"}, 
            "nav-link": {
                "font-size": "15px", 
                "text-align": "left", 
                "margin": "4px 0px", 
                "padding": "10px",
                "border-radius": "8px",
                "font-weight": "500",
                "letter-spacing": "0.02em",
                "--hover-color": config.THEME_COLORS['card_bg']
            },
            "nav-link-selected": {
                "background-color": config.THEME_COLORS['card_bg'], 
                "color": config.THEME_COLORS['primary'],
                "border-left": f"4px solid {config.THEME_COLORS['primary']}"
            },
        }
    )
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: var(--muted); font-size: 0.8rem;'>Engineering Roadmap Hub v2.0<br>Built with Streamlit</p>", unsafe_allow_html=True)

# Routing
if selected == "Home":
    home.render(domains_data)
elif selected == "Dashboard":
    dashboard.render(domains_data, roadmaps_data)
elif selected == "Domain Explorer":
    domain_explorer.render(domains_data, roadmaps_data)
elif selected == "Career Prep":
    career_prep.render(domains_data)
elif selected == "Compare":
    compare_domains.render(domains_data)
elif selected == "AI Recommend":
    ai_recommendation.render(domains_data)
elif selected == "Skill Gap":
    skill_gap.render(domains_data)
elif selected == "Daily Planner":
    daily_planner.render(domains_data)
elif selected == "Chatbot":
    chatbot.render(domains_data)
