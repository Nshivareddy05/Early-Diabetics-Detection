import streamlit as st
import config

def load_css():
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Inter:wght@400;500;700&display=swap');
        
        /* Base styles */
        :root {{
            --primary: {config.THEME_COLORS['primary']};
            --secondary: {config.THEME_COLORS['secondary']};
            --bg: {config.THEME_COLORS['background']};
            --card-bg: {config.THEME_COLORS['card_bg']};
            --text: {config.THEME_COLORS['text']};
            --muted: {config.THEME_COLORS['muted']};
        }}
        
        .stApp {{
            background-color: var(--bg);
            color: var(--text);
            font-family: 'Inter', sans-serif;
            letter-spacing: 0.02em;
        }}
        
        /* Headers */
        h1, h2, h3, h4, h5 {{
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }}
        
        /* Metric Cards */
        div[data-testid="metric-container"] {{
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(0, 242, 254, 0.2);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }}
        
        div[data-testid="metric-container"]::before {{
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 50%; height: 100%;
            background: linear-gradient(to right, transparent, rgba(255,255,255,0.1), transparent);
            transform: skewX(-20deg);
            transition: all 0.5s;
        }}
        
        div[data-testid="metric-container"]:hover::before {{
            left: 150%;
        }}
        
        div[data-testid="metric-container"]:hover {{
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 10px 20px rgba(0, 242, 254, 0.2);
            border-color: var(--primary);
        }}
        
        /* Custom UI Elements */
        .glass-card {{
            background: rgba(30, 41, 59, 0.6);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 24px;
            margin-bottom: 24px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        }}
        .glass-card:hover {{
            border-color: rgba(0, 242, 254, 0.5);
            box-shadow: 0 8px 32px 0 rgba(0, 242, 254, 0.2);
            transform: translateY(-2px);
        }}
        
        /* Skill tags */
        .skill-tag {{
            display: inline-block;
            padding: 6px 14px;
            margin: 4px;
            background: linear-gradient(135deg, rgba(0,242,254,0.1), rgba(79,172,254,0.1));
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 20px;
            font-size: 0.9em;
            color: var(--primary);
            transition: all 0.3s ease;
            cursor: default;
        }}
        .skill-tag:hover {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: var(--bg);
            transform: scale(1.05);
            box-shadow: 0 0 10px rgba(0,242,254,0.5);
        }}
        
        /* Resource Links */
        .resource-link {{
            display: flex;
            align-items: center;
            padding: 12px 16px;
            background: var(--card-bg);
            border-radius: 8px;
            margin-bottom: 12px;
            text-decoration: none !important;
            color: var(--text) !important;
            border: 1px solid rgba(255,255,255,0.05);
            transition: all 0.3s ease;
        }}
        .resource-link:hover {{
            background: rgba(255,255,255,0.05);
            border-color: var(--secondary);
            transform: translateX(5px);
        }}
        
        /* Hide default Streamlit elements */
        header {{visibility: hidden;}}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        
        /* Buttons */
        div.stButton > button:first-child {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: var(--bg);
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }}
        
        div.stButton > button:first-child:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 242, 254, 0.4);
            color: var(--bg);
        }}
        
        /* Streamlit Tabs */
        button[data-baseweb="tab"] {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.02em;
            color: var(--muted);
            background-color: transparent;
            padding-bottom: 12px;
        }}
        
        button[data-baseweb="tab"]:hover {{
            color: var(--primary);
        }}
        
        button[data-baseweb="tab"][aria-selected="true"] {{
            color: var(--primary);
            border-bottom-color: var(--primary) !important;
        }}
        
        button[data-baseweb="tab"][aria-selected="true"] p {{
            color: var(--primary) !important;
            font-weight: 800 !important;
        }}
    </style>
    """, unsafe_allow_html=True)
