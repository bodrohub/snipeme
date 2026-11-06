import streamlit as st, requests, time
from datetime import datetime, timedelta

st.set_page_config(page_title="SnipeMe", page_icon="🎯", layout="wide")

# ========== POPUP DONASI - VERSI BENER, TOMBOL KELIATAN ==========
if "masuk" not in st.session_state: st.session_state.masuk = False
if "popup_start" not in st.session_state: st.session_state.popup_start = time.time()

if not st.session_state.masuk:
    sisa = 6 - int(time.time() - st.session_state.popup_start)
    if sisa > 0:
        # FASE 1: LAGI NGITUNG - BOLEH FULL LAYAR, KARENA BELUM ADA TOMBOL
        st.markdown(f"""
        <style>.stApp{{background-color:#033333 !important;}}
        .popup-bg{{position:fixed;inset:0;background:#033333;z-index:9999;display:flex;justify-content:center;align-items:center;}}
        .popup-box{{width:80vw;height:80vh;background:#004D4D;border:4px solid #ff6a00;border-radius:16px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;}}
        .popup-box h1{{color:#ff6a00 !important;font-size:48px;margin:0;}} .popup-box p{{color:white !important;font-size:22px;font-weight:bold;}}
        </style>
        <div class="popup-bg"><div class="popup-box"><h1>🎯 SnipeMe</h1><p>Dukung biar tetap gratis! 🙏</p><p>Donasi dulu coy, app kebuka dalam {sisa} detik...</p><p>Tombol MASUK aktif setelah 6 detik, gak bisa di-skip!</p></div></div>
        """, unsafe_allow_html=True)
        st.markdown(f"### ⏳ Tunggu {sisa} detik...")
        time.sleep(1); st.rerun()
    else:
        # FASE 2: UDAH HABIS - JANGAN PAKE FIXED LAGI! BIAR TOMBOL BISA DIKLIK
        st.markdown("""
        <style>
        .stApp{background-color:#033333 !important;}
        .popup-box2{width:80%;margin:40px auto 20px auto;background:#004D4D;border:4px solid #ff6a00;border-radius:16px;padding:40px 20px;text-align:center;}
        .popup-box2 h1{color:#ff6a00 !important;font-size:48px;margin:0;} .popup-box2 p{color:white !important;font-size:22px;font-weight:bold;}
        div[data-testid="stLinkButton"] > a {background-color:#ff3b30 !important;border:2px solid #ff6a00 !important;height:55px !important;}
        div[data-testid="stLinkButton"] p{color:white !important;font-size:18px !important;font-weight:bold !important;}
        button[data-testid="stBaseButton-secondary"]{background-color:#00c853 !important;border:2px solid #ff6a00 !important;height:55px !important;}
        button[data-testid="stBaseButton-secondary"] p{color:white !important;font-size:18px !important;font-weight:bold !important;}
        </style>
        <div class="popup-box2"><h1>🎯 SnipeMe</h1><p>Terima kasih udah nunggu! Silakan masuk 👇</p><p>Donasi dulu biar makin semangat bikinnya 🙏</p></div>
        """, unsafe_allow_html=True)
        # TOMBOLNYA DI LUAR POPUP, JADI PASTI KELIATAN & BISA DIKLIK
        c1,c2,c3 = st.columns(3)
        with c1: st.link_button("❤️ DONASI", "https://saweria.co/mamangbora", use_container_width=True)
        with c2:
            if st.button("✅ MASUK", use_container_width=True):
                st.session_state.masuk = True; st.rerun()
        with c3: st.link_button("🔗 MEDSOS", "https://facebook.com/mamangbora", use_container_width=True)
        st.stop()

# ========== APP UTAMA ==========
st.markdown("""
<style>
.stApp{background-color:#033333 !important;}
section[data-testid="stSidebar"]{background-color:#022222 !important;}
section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] div{color:#ff6a00 !important;font-weight:bold !important;}
h1,h2,h3,p,span{color:#ff6a00 !important;font-weight:bold !important;}
div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input, div[data-testid="stTextArea"] textarea{border:3px solid #ff6a00 !important;background-color:#044444 !important;color:#ff6a00 !important;font-weight:bold !important;}
div[data-testid="stNumberInput"] button{background-color:#ff6a00 !important;color:#033333 !important;}
a[data-testid="stLinkButton"]{background-color:#ff3b30 !important;border:2px solid #ff6a00 !important;}
a[data-testid="stLinkButton"] p{color:white !important;font-weight:bold !important;}
button[data-testid="stBaseButton-secondary"]{background-color:#ff3b30 !important;border:2px solid #ff6a00 !important;}
button[data-testid="stBaseButton-secondary"] p{color:white !important;font-weight:bold !important;}
.banner-snipe{background-color:#004D4D !important;padding:18px 20px !important;border-radius:12px !important;margin-top:-10px !important;margin-bottom:18px !important;border:3px solid #ff6a00 !important;}
.banner-snipe h1{color:#ff6a00 !important;margin:0 !important;font-size:38px !important;}
.banner-snipe p{color:#ff6a00 !important;margin:0 !important;}
.box-putih{background-color:#044444 !important;padding:10px !important;border-radius:8px !important;border:1px solid white !important;margin:10px 0 !important;}
.box-putih p, .box-putih span{color:white !important;font-weight:bold !important;}
.box-api{background-color:#004D4D !important;padding:14px !important;border-radius:10px !important;border:2px solid #ff6a00 !important;margin-bottom:16px !important;}
.box-api p, .box-api a{color:white !important;} .box-api b{color:#ff6a00 !important;}
.card-video{background-color:#004D4D !important;padding:12px !important;border-radius:10px !important;border:2px solid #ff6a00 !important;margin-bottom:10px !important;}
.card-video p, .card-video a{color:white !important;} .card-video b{color:#ff6a00 !important;}
</style>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns([3,1,1])
with c1: st.markdown("""<div class="banner-snipe"><h1>🎯 SnipeMe</h1><p>Cari video viral dari 20 tahun kebelakang</p></div>""", unsafe_allow_html=True)
with c2: st.link_button("❤️ Donasi", "https://saweria.co/mamangbora")
with c3: st.link_button("🔗 Medsos", "https://facebook.com/mamangbora")

# ========== MULTI API KEY - ROTASI OTOMATIS ==========
if "api_keys" not in st.session_state: st.session_state.api_keys = []
st.markdown("""
<div class="box-api">
<p><b>🔑 YouTube API Key (BISA LEBIH DARI 1)</b> - Kalau Key 1 habis kuotanya, otomatis pindah ke Key 2, 3, dst.</p>
<p>Belum punya? Klik 👉 <a href="https://console.cloud.google.com/" target="_blank">🌐 Buka Google Cloud Console</a> - Bikin Project > Library > Aktifkan YouTube Data API v3 > Credentials > Create API Key</p>
<p>Cara isi: 1 baris 1 API Key.</p>
</div>
""", unsafe_allow_html=True)
api_text = st.text_area("Tempel API Key di sini (1 baris 1 key)", value="\n".join(st.session_state.api_keys), type="password", placeholder="AIza...Key1\nAIza...Key2", height=100)
col_simpan, col_hapus = st.columns([1,1])
with col_simpan:
    if st.button("💾 SIMPAN SEMUA API KEY"):
        st.session_state.api_keys = [k.strip() for k in api_text.splitlines() if k.strip()]
        st.success(f"✅ {len(st.session_state.api_keys)} API Key tersimpan & disembunyikan!")
with col_hapus:
    if st.button("🗑️ HAPUS SEMUA KEY"):
        st.session_state.api_keys = []; st.rerun()
if st.session_state.api_keys:
    st.markdown(f'<div class="box-putih"><p>✅ {len(st.session_state.api_keys)} API Key tersimpan & disembunyikan (****) - Rotasi otomatis aktif.</p></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="box-putih"><p>⚠️ API Key belum diisi - Klik link Google Cloud Console di atas!</p></div>', unsafe_allow_html=True)
    st.link_button("🌐 Buka Google Cloud Console - Bikin API Key", "https://console.cloud.google.com/apis/library/youtube.googleapis.com")

def youtube_search_rotasi(keyword, published_after, api_keys):
    last_error = None
    for i, key in enumerate(api_keys):
        params = {"part": "snippet", "q": keyword, "type": "video", "maxResults": 20, "key": key, "order": "viewCount"}
        if published_after: params["publishedAfter"] = published_after
        r = requests.get("https://www.googleapis.com/youtube/v3/search", params=params).json()
        if "items" in r:
            ids = ",".join([x["id"]["videoId"] for x in r["items"]])
            stats = requests.get("https://www.googleapis.com/youtube/v3/videos", params={"part": "statistics,contentDetails,snippet", "id": ids, "key": key}).json()
            return stats, i, None
        err = r.get("error", {}).get("errors", [{}])[0].get("reason", "")
        last_error = r
        if err in ["quotaExceeded", "dailyLimitExceeded"]: continue
        else: return None, i, r
    return None, -1, last_error

with st.sidebar:
    st.header("Filter Pencarian")
    keyword = st.text_input("Keyword", "vlog")
    views_min = st.number_input("Views Minimal", value=1000000)
    views_max = st.number_input("Views Maksimal", value=50000000)
    vph_min = st.number_input("VPH Minimal", value=10000)
    durasi_min = st.text_input("Durasi Min (menit)", "0")
    durasi_max = st.text_input("Durasi Max (menit)", "60")
    st.markdown("### ⏰ Waktu Upload")
    col_h, col_m = st.columns(2)
    with col_h: hari = st.number_input("Hari Terakhir", min_value=0, max_value=3650, value=0)
    with col_m: minggu = st.number_input("Minggu Terakhir", min_value=0, max_value=1040, value=0)
    col_b, col_t = st.columns(2)
    with col_b: bulan = st.number_input("Bulan Terakhir", min_value=0, max_value=240, value=0)
    with col_t: tahun = st.number_input("Tahun Terakhir", min_value=0, max_value=20, value=0)
    total_hari = hari + (minggu*7) + (bulan*30) + (tahun*365)
    if total_hari > 0: st.markdown(f'<div class="box-putih"><p>Waktu Upload: {total_hari} hari terakhir</p></div>', unsafe_allow_html=True)
    else: st.markdown('<div class="box-putih"><p>Waktu Upload: Semua (dari 20 tahun kebelakang)</p></div>', unsafe_allow_html=True)
    cari = st.button("🔍 CARI")

if cari:
    if not st.session_state.api_keys: st.error("Masukin dulu API Key di atas!")
    else:
        published_after = (datetime.utcnow() - timedelta(days=total_hari)).isoformat("T") + "Z" if total_hari > 0 else None
        stats, idx_key, err = youtube_search_rotasi(keyword, published_after, st.session_state.api_keys)
        if stats is None:
            if idx_key == -1: st.error(f"❌ SEMUA {len(st.session_state.api_keys)} API KEY HABIS KUOTANYA! Bikin baru / tunggu reset besok. {err}")
            else: st.error(f"API Error: {err}")
        else:
            if idx_key > 0: st.warning(f"⚠️ Key 1 sampai {idx_key} habis, otomatis pindah ke Key {idx_key+1}")
            else: st.success(f"✅ Pakai API Key ke-{idx_key+1}")
            hasil = [v for v in stats.get("items", []) if views_min <= int(v["statistics"].get("viewCount", 0)) <= views_max]
            st.markdown(f"### Ditemukan: {len(hasil)} video")
            for v in hasil:
                sn = v["snippet"]; views = int(v["statistics"].get("viewCount", 0))
                st.markdown(f'<div class="card-video"><p><b>{sn["title"]}</b></p><p>Channel: {sn["channelTitle"]} | Views: {views:,} | Upload: {sn["publishedAt"][:10]}</p><p><a href="https://youtube.com/watch?v={v["id"]}" target="_blank">▶️ Tonton di YouTube</a></p></div>', unsafe_allow_html=True)
            if hasil:
                txt = "\n".join([f"{x['snippet']['title']} - https://youtube.com/watch?v={x['id']}" for x in hasil])
                st.download_button("⬇️ Export txt/md", txt, file_name="snipeme.txt")
