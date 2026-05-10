import streamlit as st
import config

def render_metric_card(title, value, subtitle="", icon=""):
    st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 10px;">{icon}</div>
            <h3 style="margin:0; font-size: 1.2rem; color: var(--muted);">{title}</h3>
            <h2 style="margin:10px 0; font-size: 2rem; color: var(--primary);">{value}</h2>
            <p style="margin:0; font-size: 0.9rem; color: var(--muted);">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)

def render_skill_tags(skills):
    tags_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
    st.markdown(f"<div>{tags_html}</div><br>", unsafe_allow_html=True)

def render_resource_link(title, url, type_icon="🔗"):
    st.markdown(f"""
        <a href="{url}" target="_blank" class="resource-link">
            <span style="font-size: 1.5rem; margin-right: 15px;">{type_icon}</span>
            <div style="flex-grow: 1;">
                <h4 style="margin:0; font-size: 1.1rem;">{title}</h4>
                <p style="margin:0; font-size: 0.8rem; color: var(--muted);">Click to open resource</p>
            </div>
            <span style="color: var(--primary);">→</span>
        </a>
    """, unsafe_allow_html=True)
