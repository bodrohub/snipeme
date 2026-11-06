import streamlit as st

st.set_page_config(page_title="SnipeMe", page_icon="🎯", layout="wide")

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
/* Banner SnipeMe - Tosca Muda + Teks Oren */
.banner-snipe {
    background-color: #8FE3D0 !important;
    padding: 18px 20px !important;
    border-radius: 12px !important;
    margin-top: -10px !important;
    margin-bottom: 18px !important;
    border: 3px solid #ff6a00 !important;
}
.banner-snipe h1 { color: #ff6a00 !important; margin: 0 !important; font-size: 38px !important; }
.banner-snipe p { color: #ff6a00 !important; margin: 0 !important; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

# BANNER TOSCA MUDA
c1,c2,c3 = st.columns([3,1,1])
with c1:
    st.markdown("""
    <div class="banner-snipe">
        <h1>🎯 SnipeMe</h1>
        <p>Cari video viral dari 20 tahun kebelakang</p>
    </div>
    """, unsafe_allow_html=True)
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

    st.markdown("### ⏰ Waktu Upload")
    st.caption("Isi salah satu aja, sisanya biarin 0. Contoh: mau video 20 tahun terakhir, isi Tahun = 20")
    # 4 kolom isian manual
    col_h, col_m = st.columns(2)
    with col_h:
        hari = st.number_input("Hari Terakhir", min_value=0, max_value=3650, value=0)
    with col_m:
        minggu = st.number_input("Minggu Terakhir", min_value=0, max_value=1040, value=0)
    col_b, col_t = st.columns(2)
    with col_b:
        bulan = st.number_input("Bulan Terakhir", min_value=0, max_value=240, value=0)
    with col_t:
        tahun = st.number_input("Tahun Terakhir", min_value=0, max_value=20, value=0)

    # Hitung total hari buat info
    total_hari = hari + (minggu*7) + (bulan*30) + (tahun*365)
    if total_hari > 0:
        st.success(f"Nyari video dari {total_hari} hari terakhir")
    else:
        st.info("Waktu Upload: Semua (dari 20 tahun kebelakang)")

    cari = st.button("🔍 CARI")

if cari:
    waktu_text = f"{total_hari} hari terakhir" if total_hari > 0 else "Semua waktu (20 tahun)"
    st.success(f"Nyari: {keyword} | Views {views_min}-{views_max} | VPH > {vph_min} | Durasi {durasi_min}-{durasi_max} menit | Waktu: {waktu_text} | Hari:{hari} Minggu:{minggu} Bulan:{bulan} Tahun:{tahun}")
    txt = f"SnipeMe - {keyword}\nViews: {views_min}-{views_max} | VPH > {vph_min}\nWaktu Upload: {waktu_text}\nHari:{hari} Minggu:{minggu} Bulan:{bulan} Tahun:{tahun}\n"
    st.download_button("⬇️ Export txt/md", txt, file_name="snipeme.txt")
else:
    st.info("Isi filter di kiri, terus klik CARI 👈")
