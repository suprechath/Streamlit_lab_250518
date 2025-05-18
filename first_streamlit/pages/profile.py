import streamlit as st
from PIL import Image
import io
# if ('data' not in st.session_state):
#     st.session_state.data = []

# if ('data' in st.session_state):
#     st.write(st.session_state.data)

# name = st.text_input("name")
# if (name != ""):
#     st.session_state.data.append(name)
if 'profile_data' not in st.session_state:
    st.session_state.profile_data = {
        'name': '',
        'email': '',
        'interests': []
    }

# Create two columns for layout
col1, col2 = st.columns([1, 2])

with col1:
     # Display uploaded
    if 'profile_picture' not in st.session_state:
        st.session_state.profile_picture = "https://via.placeholder.com/150"
    
    # st.image(st.session_state.profile_picture, caption="Profile Picture")
    
    upload_image = st.file_uploader("Upload new profile picture", type=['jpg', 'png', 'jpeg'])
    if upload_image is not None and 'last_uploaded_image' not in st.session_state:
        image = Image.open(upload_image)
        image = image.resize((150, 150))
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        st.session_state.profile_picture = buf.getvalue()
        st.session_state.last_uploaded_image = upload_image.name
        st.success("Profile picture updated!")
        st.rerun()

    # Reset the last_uploaded_image when a new image is selected
    if upload_image is None and 'last_uploaded_image' in st.session_state:
        del st.session_state.last_uploaded_image

with col2:
    with st.form("profile_form"):
        name = st.text_input("Full Name", st.session_state.profile_data['name'])
        email = st.text_input("Email", st.session_state.profile_data['email'])
        interests = st.multiselect(
            "Interests",
            options=["Technology", "Science", "Arts", "Sports", "Music", "Travel", "Reading"],
            default=st.session_state.profile_data['interests']
        )
        
        submit = st.form_submit_button("Save Profile")
        if submit:
            st.session_state.profile_data.update({
                'name': name,
                'email': email,
                'interests': interests
            })
            st.success("Profile updated successfully!")

# Display current profile information
if st.session_state.profile_data['name']:
    st.balloons()
    st.markdown("### Current Profile")
    st.write(f"**Name:** {st.session_state.profile_data['name']}")
    st.write(f"**Email:** {st.session_state.profile_data['email']}")
    join = ", ".join(st.session_state.profile_data['interests'])
    if st.session_state.profile_data['interests']:
        st.write(f"**Interests:** {join}")