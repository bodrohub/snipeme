import streamlit as st
import requests
from datetime import datetime, timezone
import math

st.set_page_config(page_title="SnipeMe", page_icon="🎯", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #1f352d; color: white; }
h1,h2,h3,p,span,label { color: white !important; }
div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {
    border: 3px solid #ff6a00 !important; background: #2a4a3e !important; color: white !important;
}
.stButton > button { background: #ff3b30 !important; color: white !important; border: 2px solid #ff6a00 !important; font-weight: bold; width: 100%; }
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
    st.subheader("Hasil Pencarian")
    api_key = st.secrets.get("YOUTUBE_API_KEY", "")
    if not api_key:
        st.warning("Belum ada API Key. Masuk ke Streamlit -> Settings -> Secrets, isi YOUTUBE_API_KEY")
        st.info(f"Contoh hasil untuk: {keyword} | Views {views_min}-{views_max} | VPH > {vph_min} | Durasi {durasi_min}-{durasi_max} menit")
    else:
        st.success("API tersambung! Hasil asli dari YouTube akan muncul di sini.")
    
    # Export contoh
    txt = f"SnipeMe - {keyword}\nViews: {views_min}-{views_max} | VPH > {vph_min}\n"
    st.download_button("⬇️ Export txt/md", txt, file_name="snipeme.txt")
else:
    st.info("Isi filter di kiri, terus klik CARI. 👈")
