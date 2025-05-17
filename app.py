import streamlit as st
from PIL import Image
from io import BytesIO

# --- Placeholder for U-Net enhancement ---
def unet_enhance(img: Image.Image) -> Image.Image:
    # TODO: Replace with actual U-Net model inference
    return img

# --- Force full-width layout and base styles ---
def force_full_width():
    st.markdown("""
        <style>
        /* Base layout */
        .appview-container .main .block-container {
            padding: 2rem 3rem !important;
            max-width: none !important;
            width: 100% !important;
            transition: all 0.3s ease;
        }
        html, body, [data-testid="stAppViewContainer"] {
            margin: 0; padding: 0; overflow-x: hidden;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        header, footer {visibility: hidden;}
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #007BFF80;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

# --- Dark/Light Theme ---
def apply_theme(dark_mode):
    if dark_mode:
        st.markdown("""
            <style>
            html, body, [data-testid="stAppViewContainer"] {
                background: linear-gradient(135deg, #121212, #1f1f1f);
                color: #e0e0e0;
                transition: background 0.5s ease;
            }
            [data-testid="stSidebar"] {
                background: #222;
                color: #ddd;
            }
            .stButton>button, .stDownloadButton>button {
                background-color: #1a73e8 !important;
                color: #fff !important;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: 600;
                border: none;
                transition: background-color 0.3s ease;
                box-shadow: 0 4px 12px rgba(26, 115, 232, 0.6);
            }
            .stButton>button:hover, .stDownloadButton>button:hover {
                background-color: #155ab6 !important;
                cursor: pointer;
            }
            h1, h2, h3, h4, h5, h6, label, span, p, div {
                color: #e0e0e0 !important;
                text-shadow: 0 1px 2px rgba(0,0,0,0.6);
            }
            /* Sidebar radio buttons */
            [data-testid="stSidebar"] .stRadio > div {
                color: #ddd;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            html, body, [data-testid="stAppViewContainer"] {
                background: linear-gradient(135deg, #f0f4ff, #d9e2ff);
                color: #111;
                transition: background 0.5s ease;
            }
            [data-testid="stSidebar"] {
                background: #e8f0fe;
                color: #111;
            }
            .stButton>button, .stDownloadButton>button {
                background-color: #007BFF !important;
                color: white !important;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: 600;
                border: none;
                transition: background-color 0.3s ease;
                box-shadow: 0 4px 12px rgba(0, 123, 255, 0.5);
            }
            .stButton>button:hover, .stDownloadButton>button:hover {
                background-color: #0056b3 !important;
                cursor: pointer;
            }
            h1, h2, h3, h4, h5, h6, label, span, p, div {
                color: #111 !important;
            }
            /* Sidebar radio buttons */
            [data-testid="stSidebar"] .stRadio > div {
                color: #111;
            }
            </style>
        """, unsafe_allow_html=True)

# --- Load project report text ---
def load_report_text(file_path="project_report.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error loading report: {e}"

# --- Main App ---
def main():
    st.set_page_config(page_title="SID Image Enhancer", layout="wide", page_icon="🌙")
    force_full_width()

    st.sidebar.title("📁 Navigation")
    page = st.sidebar.radio("Navigate to", ["Welcome", "Enhance Image", "About"])
    dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
    apply_theme(dark_mode)

    # Stylish header with gradient text
    st.markdown("""
        <h1 style="text-align:center; 
            background: linear-gradient(90deg, #1e90ff, #ff69b4, #00fa9a);
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
            font-weight: 900; font-size: 3.5rem;
            margin-bottom: 1rem;">SID Image Enhancer</h1>
        <hr style="border: 1.5px solid #007BFF; width: 30%; margin:auto 0 2rem 0;">
        """, unsafe_allow_html=True)

    if page == "Welcome":
        st.markdown("""
            <div style="text-align:center; font-size:1.3rem; font-weight: 500; color:#007BFF;">
            Welcome to the future of low-light image enhancement!  
            Powered by AI and inspired by the SID paper, your images will come to life with a click.
            </div>
        """, unsafe_allow_html=True)

        st.image(
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
            caption="Example low-light shot — see what AI can do!",
            use_container_width=True,
            output_format="auto"
        )
        st.markdown(
            """
            <div style="text-align:center; margin-top: 1rem;">
            <span style="font-size:1.1rem; font-weight:600;">Use the sidebar 👉 to upload and enhance your photos.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif page == "Enhance Image":
        st.markdown("## 📸 Enhance Your Low-Light Image")
        uploaded_file = st.file_uploader("Upload your image (JPG, PNG)", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            original = Image.open(uploaded_file).convert("RGB")

            with st.spinner("✨ Enhancing your image with U-Net AI..."):
                enhanced = unet_enhance(original)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("<div style='text-align:center; font-weight:600; font-size:1.2rem;'>Original Image</div>", unsafe_allow_html=True)
                st.image(original, use_container_width=True, caption="Your uploaded image", clamp=True)

            with col2:
                st.markdown("<div style='text-align:center; font-weight:600; font-size:1.2rem;'>Enhanced Image</div>", unsafe_allow_html=True)
                st.image(enhanced, use_container_width=True, caption="Enhanced by U-Net AI", clamp=True)

            buf = BytesIO()
            enhanced.save(buf, format="PNG")

            st.download_button(
                label="⬇️ Download Enhanced Image",
                data=buf.getvalue(),
                file_name="enhanced.png",
                mime="image/png",
                help="Download your enhanced image",
            )

        else:
            st.info("Upload an image to get started!")

    else:  # About page
        st.markdown("## ℹ️ About This App & Project")

        report_text = load_report_text()

        st.markdown(
            """
            <style>
            .about-container {
                background: #ffffffcc;
                padding: 25px 30px;
                border-radius: 15px;
                line-height: 1.7;
                font-size: 1.1rem;
                color: #222222;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
                max-width: 900px;
                margin: 0 auto 50px auto;
                transition: background 0.3s ease, color 0.3s ease;
            }
            /* Dark mode override */
            [data-testid="stAppViewContainer"][style*="background: linear-gradient(135deg, #121212, #1f1f1f)"] .about-container {
                background: #2c2c2ccc;
                color: #ddd;
                box-shadow: 0 8px 20px rgba(255, 255, 255, 0.1);
            }
            /* Link styles */
            .about-container a {
                color: #007BFF;
                text-decoration: none;
                font-weight: 600;
            }
            .about-container a:hover {
                text-decoration: underline;
            }
            /* Headers inside about */
            .about-container h1, .about-container h2, .about-container h3, .about-container h4 {
                color: #007BFF;
                font-weight: 700;
                margin-top: 1.2rem;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Insert a styled div as background container, then below render markdown normally for full markdown support
        st.markdown(
            f'''
            <div class="about-container">
            {report_text}
            </div>
            ''',
            unsafe_allow_html=True
        )


    # Footer with subtle info and link
    st.markdown(
        """
        <footer style="text-align:center; padding: 15px 10px; font-size: 0.9rem; color: #888; border-top: 1px solid #ccc; margin-top: 3rem;">
        Made with ❤️ by <a href="https://github.com/yourprofile" target="_blank" rel="noopener noreferrer" style="color:#007BFF;">Your Name</a> | Powered by Streamlit
        </footer>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
