import streamlit as st

st.set_page_config(page_title="SnipeMe", page_icon="🎯", layout="wide")

# CSS BENER - yang rusak kemarin gue benerin
st.markdown("""
<style>
.stApp { background-color: #1f352d !important; }
section[data-testid="stSidebar"] { background-color: #16281f !important; }
section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3, section[data-testid="stSidebar"] p { color: white !important; }
h1, h2, h3, p, span { color: white !important; }
div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {
    border: 3px solid #ff6a00 !important; background-color: #2a4a3e !important; color: white !important;
}
div[data-testid="stNumberInput"] button { background-color: #ff6a00 !important; color: white !important; }
a[data-testid="stLinkButton"] { background-color: #ff3b30 !important; color: white !important; border: 2px solid #ff6a00 !important; }
a[data-testid="stLinkButton"] p { color: white !important; font-weight: bold !important; }
button[data-testid="stBaseButton-secondary"] { background-color: #ff3b30 !important; color: white !important; border: 2px solid #ff6a00 !important; }
button[data-testid="stBaseButton-secondary"] p { color: white !important; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns([3,1,1])
with c1: st.markdown("## 🎯 SnipeMe")
with c2: st.link_button("❤️ Donasi", "https://saweria.co/bodrohub")
with c3: st.link_button("🔗 Medsos", "https://facebook.com/bodrohub")

with st.sidebar:
    st.header("Filter Pencarian")
    keyword = st.text_input("Keyword", "vlog")
    views_min = st.number_input("Views Minimal", value=1000000)
    views_max = st.number_input("Views Maksimal", value=50000000)
    vph_min = st.number_input("VPH Minimal", value=10000)
    durasi_min = st.text_input("Durasi Min (menit)", "0")
    durasi_max = st.text_input("Durasi Max (menit)", "60")
    tanggal = st.selectbox("Tanggal Upload", ["Semua","Hari ini","Minggu ini","Bulan ini"])
    cari = st.button("🔍 CARI")

if cari:
    st.success(f"Nyari: {keyword} | Views {views_min}-{views_max} | VPH > {vph_min} | Durasi {durasi_min}-{durasi_max} menit | {tanggal}")
    txt = f"SnipeMe - {keyword}\nViews: {views_min}-{views_max} | VPH > {vph_min}\n"
    st.download_button("⬇️ Export txt/md", txt, file_name="snipeme.txt")
else:
    st.info("Isi filter di kiri, terus klik CARI 👈")
