import streamlit as st
import time

# Set page configuration at the very top
st.set_page_config(page_title="FABRICE'S E-PORTIFOLIO", page_icon="💩", layout="wide")

# Apply default white theme styling
st.markdown("""
    <style>
        .main {background-color: #ffffff; color: black;}
        .stSidebar {background-color: #f0f0f0; color: black;}
        .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
        .stExpander {background-color: #ffffff; color: black;}
        .stProgress {background-color: #D5D8DC;}
        .stSidebar .css-1d391kg, .stSidebar .css-1v3fvcr, .stSidebar .css-1v3fvcr a {color: black;} /* Navigation bar text color */
        .stSidebar .css-1v3fvcr {color: black;} /* Navigation bar text color */
    </style>
""", unsafe_allow_html=True)

# Streamlit app title
st.title("🎓 Welcome to the Student Portfolio App")
st.write("Explore student achievements and projects.")

# Sidebar navigation
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Settings", "Contact", "Testimonials"])

# Initialize session state variables if they don't exist
if 'name' not in st.session_state:
    st.session_state.name = "NIYOMUFASHA Junior"
if 'location' not in st.session_state:
    st.session_state.location = "Musanze, Rwanda" 
if 'bio' not in st.session_state:
    st.session_state.bio = "I am a passionate AI engineer, Data Analytics and Business Enterprenuer!"

# Home section
if page == "Home":
    st.title("🧑‍🎓 Student Profile")
    st.image("5.jpeg", width=150, caption="Default image")

    # Display profile details
    st.subheader("📌 Personal Details")
    st.markdown(f"*📍 Location:* {st.session_state.location}")
    
    # About Me (Short introduction)
    st.subheader("🔹 About Me")
    st.write(st.session_state.bio)

    # If "Customize Profile" is clicked, allow editing
    if st.session_state.get('editing_profile', False):
        st.session_state.name = st.text_input("Name:", st.session_state.name)
        st.session_state.location = st.text_input("Location:", st.session_state.location)
        st.session_state.bio = st.text_area("Short introduction about myself:", st.session_state.bio)

        # Save and update profile
        if st.button("Save Profile Changes"):
            st.success("✅ Profile updated successfully!")
    
    # Show 'Customize Profile' button
    if st.button("Customize Profile"):
        st.session_state.editing_profile = True
    else:
        st.session_state.editing_profile = False

    # Resume download button
    with open("resume.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button(label="📄 Download Resume", data=resume_bytes, file_name="resume.pdf", mime="application/pdf")
    
    st.markdown("---")

# Projects section
elif page == "Projects":
    st.title("💻 My Projects")
    
    # Project Filtering System
    category = st.selectbox("Filter projects by category:", ["All", "Year 1 Project", "Group Projects", "Dissertation"], key="project_filter")
    
    project_data = {
        "Year 1 Project": {
            "📊 Data Analysis Project": {
                "type": "Individual",
                "description": ".",
                "link": "https://github.com/orestenabayo/CathServ.git"
            }
        },
        "Year 2 Project": {
            "🤖 AI Chatbot": {
                "type": "Group",
                "description": "Together with my  collegues we developed a site where you can view our profile & what we have developed together.",
            }
        },
        "Year 3 Project": {
            "🌐 Student attendance system": {
                "type": "Group",
                "description": "Designed and developed a website for ONLINE STUDENT ATTENDANCE.",
            }
        },
        "Dissertation": {
            "🌍 Football System Management": {
                "type": "Individual",
                "description": "Designed and developed a website for football management system.",
            }
        }
    }
    
    # Display the projects based on the category filter
    if category == "All":
        filtered_projects = {k: v for cat in project_data.values() for k, v in cat.items()}
    else:
        filtered_projects = project_data.get(category, {})
    
    for project, details in filtered_projects.items():
        with st.expander(project, expanded=False):
            time.sleep(0.1)  # Smooth transition
            st.write(f"*Type:* {details['type']}")
            st.write(f"*Description:* {details['description']}")
            if details.get("link"):
                st.markdown(f"[Link to Code]({details['link']})")
    
    st.markdown("---")

# Skills section
elif page == "Skills":
    st.title("⚡ Skills and Achievements")
    
    st.subheader("Programming Skills")
    st.write("Python: 80%")
    st.progress(90)
    
    st.write("React: 75%")
    st.progress(75)
    
    st.write("Artificial Intelligence: 65%")
    st.progress(65)

    st.write("Machine Learning: 75%")
    st.progress(75)

    st.write("HTML: 100%")
    st.progress(75)
    
    st.subheader("🏆 Certifications & Achievements")
    st.write("✔ GAMING")
    st.write("✔ Certified E-football game Developer")

# Settings section
elif page == "Settings":
    st.title("⚙️ Settings")
    
    # Theme Customization (White/Dark Mode)
    theme = st.selectbox("Choose Theme", ["White", "Dark"], key="theme_selectbox")
    if theme == "White":
        st.markdown("""
            <style>
                .main {background-color: #ffffff; color: black;}
                .stSidebar {background-color: #f0f0f0; color: black;}
                .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
                .stExpander {background-color: #ffffff; color: black;}
                .stProgress {background-color: #D5D8DC;}
                .stSidebar .css-1d391kg, .stSidebar .css-1v3fvcr, .stSidebar .css-1v3fvcr a {color: black;} /* Navigation bar text color */
                .stSidebar .css-1v3fvcr {color: black;} /* Navigation bar text color */
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
                .main {background-color: #2E2E2E; color: white;}
                .stSidebar {background-color: #1E1E1E; color: white;}
                .stButton > button {background-color: #1F618D; color: white; border-radius: 10px;}
                .stExpander {background-color: #2E2E2E; color: white;}
                .stProgress {background-color: #D5D8DC;}
                .stSidebar .css-1d391kg, .stSidebar .css-1v3fvcr, .stSidebar .css-1v3fvcr a {color: white;} /* Navigation bar text color */
                .stSidebar .css-1v3fvcr {color: white;} /* Navigation bar text color */
            </style>
        """, unsafe_allow_html=True)

# Testimonials section
elif page == "Testimonials":
    st.title("🗣️ Student Testimonials")
    testimonials = [
        "Fabrice has demonstrated remarkable growth in a short period. Their ability to grasp new concepts quickly and apply them effectively has been impressive. They take initiative in learning new technologies and contribute meaningfully to projects.  – Dr. Theodore",
        "Working with Fabrice has been a great experience. They are proactive, eager to learn, and always open to feedback.! – Lecture. SHIMIRWA Aline Valerie",
        "A great team mentor and developer. Fabrice  delivers high-quality projects. – Teammate Prince"
    ]
    for testimonial in testimonials:
        st.write(f"🗨️ {testimonial}")
    
    st.markdown("---")

# Contact section
elif page == "Contact":
    st.title("📬 Contact Me")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your message")
        
        submitted = st.form_submit_button("Send message")
        if submitted:
            if name and email and message:
                st.success("✅ Message sent successfully!")
            else:
                st.error("❌ Please fill out all fields.")