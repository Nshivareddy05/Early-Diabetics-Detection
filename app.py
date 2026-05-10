import streamlit as st
from streamlit_option_menu import option_menu
from utils.css_loader import load_css
from utils.data_loader import load_domains_data, load_roadmaps_data, load_resources_data
import config

# Import Pages
from views import home, domain_explorer, compare_domains, ai_recommendation, skill_gap, daily_planner, dashboard, career_prep, chatbot, resource_hub
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
resources_data = load_resources_data()

# Sidebar Navigation
with st.sidebar:
    st.markdown(f"""
        <div style='text-align: center; margin-bottom: 2.5rem; padding-top: 1rem;'>
            <h1 style='color: var(--primary); font-size: 2.2rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 0;'>{config.APP_ICON} Hub</h1>
            <p style='color: var(--muted); font-size: 0.75rem; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; margin-top: -5px;'>Engineering Nexus</p>
        </div>
    """, unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["Overview", "Dashboard", "Domain Explorer", "Resource Library", "Career Track", "Compare Specs", "AI Advisor", "Skill Analytics", "Daily Planner", "AI Assistant"],
        icons=["house", "grid", "compass", "collection", "briefcase", "arrow-left-right", "cpu", "pie-chart", "calendar-check", "chat-square-text"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": config.THEME_COLORS['secondary'], "font-size": "1.1rem"}, 
            "nav-link": {
                "font-size": "0.95rem", 
                "text-align": "left", 
                "margin": "0.4rem 0", 
                "padding": "0.75rem 1rem",
                "border-radius": "8px",
                "font-weight": "500",
                "font-family": "'Inter', sans-serif",
                "color": "rgba(255,255,255,0.8)",
                "--hover-color": "rgba(255,255,255,0.05)",
                "transition": "all 0.2s ease-in-out"
            },
            "nav-link-selected": {
                "background": "rgba(255,255,255,0.08)", 
                "color": "#fff",
                "border-left": f"3px solid {config.THEME_COLORS['primary']}",
                "font-weight": "600"
            },
        }
    )
    
    st.markdown("<div style='margin-top: 6rem;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.05); opacity: 0.7;'>
            <p style='color: var(--muted); font-size: 0.7rem; font-family: "Inter", sans-serif; letter-spacing: 0.5px;'>
                <strong>NEXUS HUB v2.0</strong><br>
                Empowering the future of engineering
            </p>
        </div>
    """, unsafe_allow_html=True)

# Routing
if selected == "Overview":
    home.render(domains_data)
elif selected == "Dashboard":
    dashboard.render(domains_data, roadmaps_data)
elif selected == "Domain Explorer":
    domain_explorer.render(domains_data, roadmaps_data)
elif selected == "Resource Library":
    resource_hub.render(resources_data)
elif selected == "Career Track":
    career_prep.render(domains_data)
elif selected == "Compare Specs":
    compare_domains.render(domains_data)
elif selected == "AI Advisor":
    ai_recommendation.render(domains_data)
elif selected == "Skill Analytics":
    skill_gap.render(domains_data)
elif selected == "Daily Planner":
    daily_planner.render(domains_data)
elif selected == "AI Assistant":
    chatbot.render(domains_data)
