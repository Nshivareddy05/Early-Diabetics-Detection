import streamlit as st
from components.ui import render_metric_card
import config

def render(domains_data):
    st.title(f"{config.APP_ICON} Welcome to {config.APP_NAME}")
    st.markdown("""
        <p style='font-size: 1.2rem; color: var(--muted);'>
        Your ultimate guide to navigating the complex world of engineering careers. 
        Explore deep technical roadmaps, discover skill requirements, and find your perfect engineering domain.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Animated Stats Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        render_metric_card("Domains Covered", str(len(domains_data)) if domains_data else "12+", "Detailed Pathways", "📚")
    with col2:
        render_metric_card("Interactive Roadmaps", "3 Levels", "Beginner to Advanced", "🗺️")
    with col3:
        render_metric_card("Career Data", "Real-time", "Salary & Demand Trends", "📈")
        
    st.markdown("---")
    
    st.subheader("How to use this Hub")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class='glass-card'>
            <h4>🔍 Explore Domains</h4>
            <p style='color: var(--muted);'>Dive deep into specific engineering fields. View required skills, technologies, and step-by-step interactive learning roadmaps.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='glass-card'>
            <h4>⚖️ Compare Domains</h4>
            <p style='color: var(--muted);'>Can't decide between CS and IT? Or Mechanical vs Aerospace? Use our comparison tool to analyze salary, demand, and skill overlaps.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("""
        <div class='glass-card'>
            <h4>🤖 AI Recommendation</h4>
            <p style='color: var(--muted);'>Not sure where to start? Take our interactive quiz and let our recommendation engine find the perfect engineering discipline for your interests.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class='glass-card'>
            <h4>🎯 Skill Gap Analyzer</h4>
            <p style='color: var(--muted);'>Input your current skills and target role, and we'll tell you exactly what you need to learn next.</p>
        </div>
        """, unsafe_allow_html=True)
