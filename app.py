import streamlit as st, requests, time
from datetime import datetime, timedelta

st.set_page_config(page_title="SnipeMe", page_icon="🎯", layout="wide")

# ========== POPUP 1x - TIMER 9.999.999 -> 0 DALAM 5 DETIK ==========
if "masuk" not in st.session_state: st.session_state.masuk = False
if "popup_start" not in st.session_state: st.session_state.popup_start = time.time()

if not st.session_state.masuk:
    elapsed = time.time() - st.session_state.popup_start
    total_durasi = 5.0
    # Hitung mundur 9.999.999 -> 0 dalam 5 detik
    if elapsed >= total_durasi:
        angka = 0
        sisa_detik = 0
    else:
        angka = int(9999999 * (1 - elapsed / total_durasi))
        sisa_detik = total_durasi - elapsed
    # Format pake titik: 9.999.999
    angka_str = f"{angka:,}".replace(",", ".")

    if angka > 0:
        teks_bawah = f"Tombol MASUK aktif setelah angka jadi 0, gak bisa di-skip!"
    else:
        teks_bawah = "Angka udah 0! Silakan klik MASUK!"

    st.markdown(f"""
    <style>
    .stApp{{background-color:#033333 !important;}}
    .popup-bg{{position:fixed;inset:0;background:#033333;z-index:9998;}}
    .popup-satu{{position:fixed !important;top:50% !important;left:50% !important;transform:translate(-50%,-50%) !important;width:80vw !important;height:80vh !important;background:#004D4D !important;border:4px solid #ff6a00 !important;border-radius:16px !important;display:flex !important;flex-direction:column !important;justify-content:center !important;align-items:center !important;text-align:center !important;z-index:9999 !important;padding:20px !important;}}
    /* ANGKA TIMER GEDE PUTIH TEBAL DI ATAS SNIPEME */
    .angka-timer{{color:white !important;font-size:72px !important;font-weight:900 !important;letter-spacing:2px !important;margin:0 !important;line-height:1 !important;}}
    .popup-satu h1{{color:#ff6a00 !important;font-size:48px;margin:10px 0 0 0;}} .popup-satu p{{color:white !important;font-size:22px;font-weight:bold;}}
    div[data-testid="stHorizontalBlock"]{{position:fixed !important;top:calc(50% + 28vh) !important;left:50% !important;transform:translateX(-50%) !important;width:76vw !important;z-index:10000 !important;}}
    div[data-testid="stLinkButton"] > a {{background-color:#ff8c00 !important;border:2px solid #ff6a00 !important;height:55px !important;border-radius:10px !important;}}
    div[data-testid="stLinkButton"] p{{color:white !important;font-size:18px !important;font-weight:bold !important;}}
    button[data-testid="stBaseButton-secondary"]{{background-color:#00e676 !important;border:2px solid #ff6a00 !important;height:55px !important;border-radius:10px !important;}}
    button[data-testid="stBaseButton-secondary"] p{{color:#ff3b30 !important;font-size:18px !important;font-weight:bold !important;}}
    button[data-testid="stBaseButton-secondary"]:disabled{{background-color:#555555 !important;opacity:0.6;}}
    </style>
    <div class="popup-bg"></div>
    <div class="popup-satu"><div class="angka-timer">{angka_str}</div><h1>🎯 SnipeMe</h1><p>Dukung biar tetap gratis! 🙏</p><p>{teks_bawah}</p></div>
    """, unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    with c1: st.link_button("DONASI", "https://saweria.co/mamangbora", use_container_width=True)
    with c2:
        if st.button("Masuk", use_container_width=True, disabled=(angka > 0)):
            st.session_state.masuk = True; st.rerun()
    with c3: st.link_button("MEDSOS", "https://facebook.com/mamangbora", use_container_width=True)
    if angka > 0:
        time.sleep(0.05); st.rerun()
    st.stop()

# ========== SEMBUNYIIN MANAGE APP + TOOLBAR + FOOTER - VERSI GALAK ==========
st.markdown("""
<style>
/* HAPUS TOTAL semua bawaan Streamlit */
[data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"], [data-testid="stAppDeployButton"], .stAppDeployButton, div:has(> button[data-testid="stAppDeployButton"]), footer, #MainMenu, header[data-testid="stHeader"], [data-testid="stHeader"]{display:none !important;visibility:hidden !important;height:0 !important;opacity:0 !important;pointer-events:none !important;}
.stApp{background-color:#033333 !important;}
section[data-testid="stSidebar"]{background-color:#022222 !important;}
section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] div{color:#ff6a00 !important;font-weight:bold !important;}
h1,h2,h3,p,span{color:#ff6a00 !important;font-weight:bold !important;}
div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input, div[data-testid="stTextArea"] textarea{border:3px solid #ff6a00 !important;background-color:#044444 !important;color:#ff6a00 !important;font-weight:bold !important;}
div[data-testid="stNumberInput"] button{background-color:#ff6a00 !important;color:#033333 !important;}
.banner-snipe{background-color:#004D4D !important;padding:14px 18px !important;border-radius:12px !important;border:3px solid #ff6a00 !important;}
.banner-snipe h1{color:#ff6a00 !important;margin:0 !important;font-size:32px !important;}
.banner-snipe p{color:#ff6a00 !important;margin:0 !important;}
.box-putih{background-color:#044444 !important;padding:10px !important;border-radius:8px !important;border:1px solid white !important;margin:10px 0 !important;}
.box-putih p, .box-putih span{color:white !important;font-weight:bold !important;}
.box-api{background-color:#004D4D !important;padding:14px !important;border-radius:10px !important;border:2px solid #ff6a00 !important;margin-bottom:16px !important;}
.box-api p, .box-api a{color:white !important;} .box-api b{color:#ff6a00 !important;}
.card-video{background-color:#004D4D !important;padding:12px !important;border-radius:10px !important;border:2px solid #ff6a00 !important;margin-bottom:10px !important;}
.card-video p, .card-video a{color:white !important;} .card-video b{color:#ff6a00 !important;}
.key-row{background-color:#022222 !important;padding:8px 12px !important;border-radius:8px !important;border:1px solid #ff6a00 !important;margin:6px 0 !important;}
.key-row p{color:white !important;font-family:monospace !important;font-size:16px !important;}
</style>
""", unsafe_allow_html=True)

if "api_keys" not in st.session_state: st.session_state.api_keys = []
if "show_settings" not in st.session_state: st.session_state.show_settings = False
if "show_add" not in st.session_state: st.session_state.show_add = False
if "pilih_hapus" not in st.session_state: st.session_state.pilih_hapus = {}

def mask_key(k):
    if len(k) <= 6: return k[:3] + "..." + k[-3:]
    return k[:3] + "." * (len(k)-6) + k[-3:]

# ========== HALAMAN UTAMA KOSONG POLOS - CUMA GEAR KIRI BAWAH ==========
# Gear cuma 1, di kiri bawah, pake CSS fixed biar nempel terus
st.markdown("""
<style>
/* GEAR KIRI BAWAH - 1 DOANG, GEDE */
div[data-testid="stHorizontalBlock"]{display:flex !important;}
.gear-wrap{position:fixed;left:16px;bottom:16px;z-index:9999;}
</style>
<div class="gear-wrap"></div>
""", unsafe_allow_html=True)

# Tombol gear asli (Streamlit) - kita bikin dia jadi melayang kiri bawah via kolom kosong
col_kosong, col_gear = st.columns([10,1])
with col_gear:
    pass

# Cara paling aman: taro gear di bawah pake container kosong, terus CSS fixed-in
# Kita pake st.button biasa tapi kita posisikan fixed lewat CSS di bawah
gear_clicked = st.button("⚙️", key="gear_satu_satunya")
st.markdown("""
<style>
/* Bikin tombol gear_satu_satunya jadi melayang kiri bawah, gede */
button[key="gear_satu_satunya"]{position:fixed !important;left:16px !important;bottom:16px !important;width:64px !important;height:64px !important;background:#FF6A00 !important;border:3px solid white !important;border-radius:50% !important;z-index:9999 !important;box-shadow:0 4px 12px rgba(0,0,0,0.6) !important;}
button[key="gear_satu_satunya"] p{font-size:30px !important;line-height:1 !important;}
/* Sembunyiin tombol gear duplikat yang kemarin muncul di atas */
</style>
""", unsafe_allow_html=True)
if gear_clicked:
    st.session_state.show_settings = not st.session_state.show_settings
    st.rerun()

# Kalau gear BELUM diklik, halaman STOP di sini - KOSONG POLOS, cuma gear
if not st.session_state.show_settings:
    st.stop()

# ========== BARU MUNCUL KALAU GEAR DIKLIK ==========
h1,h2,h3 = st.columns([2,1,1])
with h1: st.markdown("""<div class="banner-snipe"><h1>🎯 SnipeMe</h1><p>Cari video viral dari 20 tahun kebelakang</p></div>""", unsafe_allow_html=True)
with h2: st.link_button("❤️ DONASI", "https://saweria.co/mamangbora", use_container_width=True)
with h3: st.link_button("🔵 MEDSOS", "https://facebook.com/mamangbora", use_container_width=True)
st.markdown("""
<style>
div[data-testid="stHorizontalBlock"] > div:nth-child(2) a{background-color:#FF6A00 !important;border:3px solid white !important;}
div[data-testid="stHorizontalBlock"] > div:nth-child(2) a p{color:white !important;font-weight:900 !important;}
div[data-testid="stHorizontalBlock"] > div:nth-child(3) a{background-color:#1877F2 !important;border:3px solid white !important;}
div[data-testid="stHorizontalBlock"] > div:nth-child(3) a p{color:white !important;font-weight:900 !important;}
</style>
""", unsafe_allow_html=True)

# ========== PENGATURAN - MUNCUL BARENG GEAR ==========
st.markdown("""
<div class="box-api">
<p><b>⚙️ PENGATURAN - YouTube API Key</b></p>
<p>Kalau Key 1 habis kuotanya, otomatis pindah ke Key 2, 3, dst. 1 Key = 10.000 kuota / hari.</p>
<p>Belum punya? Klik 👉 <a href="https://console.cloud.google.com/" target="_blank">🌐 Buka Google Cloud Console</a> - Bikin Project > Library > Aktifkan YouTube Data API v3 > Credentials > Create API Key</p>
</div>
""", unsafe_allow_html=True)
st.link_button("🌐 Buka Google Cloud Console - Bikin API Key", "https://console.cloud.google.com/apis/library/youtube.googleapis.com")
if st.session_state.api_keys:
    st.markdown(f'<div class="box-putih"><p>✅ {len(st.session_state.api_keys)} API Key tersimpan - Rotasi otomatis aktif. Centang yang mau dihapus, baru klik Hapus.</p></div>', unsafe_allow_html=True)
    for idx, k in enumerate(st.session_state.api_keys):
        c_cek, c_key = st.columns([1,5])
        with c_cek: st.session_state.pilih_hapus[idx] = st.checkbox("", value=st.session_state.pilih_hapus.get(idx, False), key=f"cek_{idx}")
        with c_key: st.markdown(f'<div class="key-row"><p>Key {idx+1} : {mask_key(k)}</p></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="box-putih"><p>⚠️ Belum ada API Key. Klik Tambah untuk nambah.</p></div>', unsafe_allow_html=True)
b1,b2,b3 = st.columns(3)
with b1:
    if st.button("➕ TAMBAH", use_container_width=True):
        st.session_state.show_add = True; st.rerun()
with b2:
    if st.button("💾 SIMPAN", use_container_width=True):
        if st.session_state.show_add and st.session_state.get("input_key_baru", "").strip():
            st.session_state.api_keys.append(st.session_state.input_key_baru.strip())
            st.session_state.show_add = False; st.session_state.input_key_baru = ""; st.success("✅ API Key tersimpan!"); st.rerun()
        elif not st.session_state.show_add: st.warning("Klik TAMBAH dulu coy, baru isi key-nya!")
        else: st.warning("Isi dulu API Key-nya, jangan kosong!")
with b3:
    if st.button("🗑️ HAPUS", use_container_width=True):
        dipilih = [i for i, v in st.session_state.pilih_hapus.items() if v]
        if not dipilih: st.warning("⚠️ Pilih dulu mana yang mau dihapus! Centang dulu kotak di samping Key-nya. Gak ada yang kehapus.")
        else:
            st.session_state.api_keys = [k for i, k in enumerate(st.session_state.api_keys) if i not in dipilih]
            st.session_state.pilih_hapus = {}; st.success(f"✅ {len(dipilih)} Key berhasil dihapus!"); st.rerun()
if st.session_state.show_add:
    st.markdown('<div class="box-putih"><p>📝 Tempel 1 API Key baru di bawah, lalu klik SIMPAN:</p></div>', unsafe_allow_html=True)
    st.text_input("API Key baru", key="input_key_baru", placeholder="Tempel AIza... di sini", label_visibility="collapsed")
    if st.button("❌ BATAL"):
        st.session_state.show_add = False; st.rerun()

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
    if not st.session_state.api_keys: st.error("API Key belum ada! Klik ⚙️ GEAR kiri bawah > TAMBAH > isi Key > SIMPAN.")
    else:
        published_after = (datetime.utcnow() - timedelta(days=total_hari)).isoformat("T") + "Z" if total_hari > 0 else None
        stats, idx_key, err = youtube_search_rotasi(keyword, published_after, st.session_state.api_keys)
        if stats is None:
            if idx_key == -1: st.error(f"❌ SEMUA {len(st.session_state.api_keys)} API KEY HABIS KUOTANYA! {err}")
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
