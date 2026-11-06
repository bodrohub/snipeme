import streamlit as st, requests, time
from datetime import datetime, timedelta

st.set_page_config(page_title="SnipeMe", page_icon="🎯", layout="wide")

# ========== POPUP - 9.999.999 -> 0 DALAM 5 DETIK ==========
if "masuk" not in st.session_state: st.session_state.masuk = False
if "popup_start" not in st.session_state: st.session_state.popup_start = time.time()
if not st.session_state.masuk:
    elapsed = time.time() - st.session_state.popup_start
    angka = 0 if elapsed >= 5.0 else int(9999999 * (1 - elapsed / 5.0))
    angka_str = f"{angka:,}".replace(",", ".")
    teks_bawah = "Tombol MASUK aktif setelah angka jadi 0, gak bisa di-skip!" if angka > 0 else "Angka udah 0! Silakan klik MASUK!"
    st.markdown(f"""
    <style>
    .stApp{{background-color:#033333 !important;}}
    .popup-bg{{position:fixed;inset:0;background:#033333;z-index:9998;}}
    .popup-satu{{position:fixed !important;top:50% !important;left:50% !important;transform:translate(-50%,-50%) !important;width:80vw !important;height:80vh !important;background:#004D4D !important;border:4px solid #ff6a00 !important;border-radius:16px !important;display:flex !important;flex-direction:column !important;justify-content:center !important;align-items:center !important;text-align:center !important;z-index:9999 !important;padding:20px !important;}}
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
    if angka > 0: time.sleep(0.05); st.rerun()
    st.stop()

# ========== STYLE ==========
st.markdown("""
<style>
[data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"], [data-testid="stAppDeployButton"], .stAppDeployButton, footer, #MainMenu, header[data-testid="stHeader"]{display:none !important;visibility:hidden !important;height:0 !important;opacity:0 !important;pointer-events:none !important;}
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
.hasil-scroll{max-height:650px !important;overflow-y:auto !important;overflow-x:hidden !important;padding:12px !important;background:#022222 !important;border:2px solid #ff6a00 !important;border-radius:12px !important;}
</style>
""", unsafe_allow_html=True)

if "api_keys" not in st.session_state: st.session_state.api_keys = []
if "show_settings" not in st.session_state: st.session_state.show_settings = False
if "show_add" not in st.session_state: st.session_state.show_add = False
if "pilih_hapus" not in st.session_state: st.session_state.pilih_hapus = {}
if "sort_mode" not in st.session_state: st.session_state.sort_mode = "Terbaru"
if "hasil" not in st.session_state: st.session_state.hasil = []
if "hasil_info" not in st.session_state: st.session_state.hasil_info = ""
if "trigger_search" not in st.session_state: st.session_state.trigger_search = False
if "last_params" not in st.session_state: st.session_state.last_params = {}

def mask_key(k):
    if len(k) <= 6: return k[:3] + "..." + k[-3:]
    return k[:3] + "." * (len(k)-6) + k[-3:]

def parse_tanggal(s):
    try: return datetime.fromisoformat(s.replace("Z","+00:00")).replace(tzinfo=None)
    except: return None

def klik_cari():
    # Dipanggil pas tombol CARI diklik - simpen params + tandain mau cari
    st.session_state.trigger_search = True
    st.session_state.last_params = {
        "keyword": st.session_state.get("kw", "vlog"),
        "views_min": st.session_state.get("vmin", 1000000),
        "views_max": st.session_state.get("vmax", 50000000),
        "total_hari": st.session_state.get("total_hari_val", 0),
    }

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("Filter Pencarian")
    keyword = st.text_input("Keyword", "motocross", key="kw")
    views_min = st.number_input("Views Minimal", value=1000000, key="vmin")
    views_max = st.number_input("Views Maksimal", value=50000000, key="vmax")
    vph_min = st.number_input("VPH Minimal", value=10000, key="vph")
    durasi_min = st.text_input("Durasi Min (menit)", "10")
    durasi_max = st.text_input("Durasi Max (menit)", "60")
    st.markdown("### ⏰ Waktu Upload")
    col_h, col_m = st.columns(2)
    with col_h: hari = st.number_input("Hari Terakhir", min_value=0, max_value=3650, value=0, key="hari")
    with col_m: minggu = st.number_input("Minggu Terakhir", min_value=0, max_value=1040, value=0, key="minggu")
    col_b, col_t = st.columns(2)
    with col_b: bulan = st.number_input("Bulan Terakhir", min_value=0, max_value=240, value=0, key="bulan")
    with col_t: tahun = st.number_input("Tahun Terakhir", min_value=0, max_value=20, value=10, key="tahun")
    total_hari = hari + (minggu*7) + (bulan*30) + (tahun*365)
    st.session_state.total_hari_val = total_hari
    if total_hari > 0: st.markdown(f'<div class="box-putih"><p>Waktu Upload: {total_hari} hari terakhir</p></div>', unsafe_allow_html=True)
    else: st.markdown('<div class="box-putih"><p>Waktu Upload: Semua (dari 20 tahun kebelakang)</p></div>', unsafe_allow_html=True)
    # TOMBOL CARI PAKE CALLBACK - BIAR GAK KEHAPUS PAS RERUN
    st.button("🔍 CARI", use_container_width=True, on_click=klik_cari)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⚙️", key="gear_sidebar"):
        st.session_state.show_settings = True
        st.session_state.show_add = False
        st.rerun()

st.markdown("""
<style>
section[data-testid="stSidebar"] button[key="gear_sidebar"]{background-color:#FF6A00 !important;border:3px solid white !important;border-radius:50% !important;width:56px !important;height:56px !important;min-width:56px !important;}
section[data-testid="stSidebar"] button[key="gear_sidebar"] p{font-size:28px !important;line-height:1 !important;}
</style>
""", unsafe_allow_html=True)

# ========== PENGATURAN - MUNCUL GEAR SAMPAI SIMPAN ==========
if st.session_state.show_settings:
    h1,h2,h3 = st.columns([2,1,1])
    with h1: st.markdown("""<div class="banner-snipe"><h1>🎯 SnipeMe</h1><p>Cari video viral dari 20 tahun kebelakang</p></div>""", unsafe_allow_html=True)
    with h2: st.link_button("❤️ DONASI", "https://saweria.co/mamangbora", use_container_width=True)
    with h3: st.link_button("🔵 MEDSOS", "https://facebook.com/mamangbora", use_container_width=True)
    st.markdown("""<div class="box-api"><p><b>⚙️ PENGATURAN - YouTube API Key</b></p><p>Kalau Key 1 habis, otomatis pindah ke Key 2, 3, dst.</p><p>Belum punya? Klik 👉 <a href="https://console.cloud.google.com/" target="_blank">🌐 Buka Google Cloud Console</a></p></div>""", unsafe_allow_html=True)
    st.link_button("🌐 Buka Google Cloud Console - Bikin API Key", "https://console.cloud.google.com/apis/library/youtube.googleapis.com")
    if st.session_state.api_keys:
        st.markdown(f'<div class="box-putih"><p>✅ {len(st.session_state.api_keys)} API Key tersimpan - Centang yang mau dihapus, baru klik Hapus.</p></div>', unsafe_allow_html=True)
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
                st.success("✅ API Key tersimpan!")
            st.session_state.show_settings = False
            st.session_state.show_add = False
            st.session_state.input_key_baru = ""
            st.session_state.pilih_hapus = {}
            time.sleep(0.3); st.rerun()
    with b3:
        if st.button("🗑️ HAPUS", use_container_width=True):
            dipilih = [i for i, v in st.session_state.pilih_hapus.items() if v]
            if not dipilih: st.warning("⚠️ Pilih dulu mana yang mau dihapus! Centang dulu kotak di samping Key-nya.")
            else:
                st.session_state.api_keys = [k for i, k in enumerate(st.session_state.api_keys) if i not in dipilih]
                st.session_state.pilih_hapus = {}; st.success(f"✅ {len(dipilih)} Key berhasil dihapus!"); st.rerun()
    if st.session_state.show_add:
        st.markdown('<div class="box-putih"><p>📝 Tempel 1 API Key baru di bawah, lalu klik SIMPAN:</p></div>', unsafe_allow_html=True)
        st.text_input("API Key baru", key="input_key_baru", placeholder="Tempel AIza... di sini", label_visibility="collapsed")
        if st.button("❌ BATAL"):
            st.session_state.show_add = False; st.rerun()
    st.stop()

# ========== SPACE UTAMA - SORTING ==========
st.markdown("### 🔽 Urutkan Hasil:")
s1,s2,s3,s4,s5,s6 = st.columns(6)
with s1:
    if st.button("⏪ Terlama", use_container_width=True): st.session_state.sort_mode = "Terlama"; st.rerun()
with s2:
    if st.button("⏩ Terbaru", use_container_width=True): st.session_state.sort_mode = "Terbaru"; st.rerun()
with s3:
    if st.button("👁️ Views Terbanyak", use_container_width=True): st.session_state.sort_mode = "Views Terbanyak"; st.rerun()
with s4:
    if st.button("👁️ Views Paling Sedikit", use_container_width=True): st.session_state.sort_mode = "Views Paling Sedikit"; st.rerun()
with s5:
    if st.button("⚡ VPH Tertinggi", use_container_width=True): st.session_state.sort_mode = "VPH Tertinggi"; st.rerun()
with s6:
    if st.button("👥 Subscriber Terbanyak", use_container_width=True): st.session_state.sort_mode = "Subscriber Terbanyak"; st.rerun()
st.markdown(f'<div class="box-putih"><p>Mode urut aktif: <b>{st.session_state.sort_mode}</b> | Klik CARI di sidebar kiri untuk cari ulang.</p></div>', unsafe_allow_html=True)

# ========== LOGIKA CARI - JALAN KALAU TRIGGER_SEARCH TRUE ==========
if st.session_state.trigger_search:
    st.session_state.trigger_search = False
    p = st.session_state.last_params
    kw = p.get("keyword", "motocross")
    vmin = p.get("views_min", 1000000)
    vmax = p.get("views_max", 50000000)
    th = p.get("total_hari", 0)
    if not st.session_state.api_keys:
        st.error("API Key belum ada! Klik ⚙️ GEAR di sidebar kiri bawah > TAMBAH > isi Key > SIMPAN.")
    else:
        now = datetime.utcnow()
        if th > 0:
            published_after = (now - timedelta(days=th)).isoformat("T") + "Z"
            published_before = now.isoformat("T") + "Z"
            batas_bawah = now - timedelta(days=th)
        else:
            published_after = None; published_before = None; batas_bawah = None
        with st.spinner("🔍 Lagi cari ke YouTube... tunggu bentar..."):
            hasil_detail = None; idx_key = 0; err_msg = ""
            for i, key in enumerate(st.session_state.api_keys):
                params = {"part": "snippet", "q": kw, "type": "video", "maxResults": 50, "key": key, "order": "date"}
                if published_after: params["publishedAfter"] = published_after
                if published_before: params["publishedBefore"] = published_before
                try: r = requests.get("https://www.googleapis.com/youtube/v3/search", params=params, timeout=20).json()
                except Exception as e: err_msg = str(e); continue
                if "items" not in r:
                    err = r.get("error", {}).get("errors", [{}])[0].get("reason", "")
                    err_msg = str(r.get("error", {}).get("message", r))
                    if err in ["quotaExceeded", "dailyLimitExceeded"]: continue
                    else: break
                ids = ",".join([x["id"]["videoId"] for x in r["items"]])
                if not ids: hasil_detail = []; idx_key = i; break
                stats = requests.get("https://www.googleapis.com/youtube/v3/videos", params={"part": "statistics,contentDetails,snippet", "id": ids, "key": key}, timeout=20).json()
                hasil_detail = stats.get("items", []); idx_key = i
                # Subscriber
                try:
                    ch_ids = ",".join(list(set([x["snippet"]["channelId"] for x in hasil_detail])))
                    ch = requests.get("https://www.googleapis.com/youtube/v3/channels", params={"part": "statistics", "id": ch_ids, "key": key}, timeout=20).json()
                    ch_map = {c["id"]: int(c["statistics"].get("subscriberCount", 0)) for c in ch.get("items", [])}
                    for v in hasil_detail: v["subs"] = ch_map.get(v["snippet"]["channelId"], 0)
                except: pass
                break
            if hasil_detail is None:
                st.error(f"❌ Gagal cari! API Error: {err_msg} | Cek API Key lu, pastikan YouTube Data API v3 udah aktif!")
            else:
                filtered = []
                for v in hasil_detail:
                    tgl = parse_tanggal(v["snippet"]["publishedAt"])
                    if batas_bawah and tgl and tgl < batas_bawah: continue
                    views = int(v["statistics"].get("viewCount", 0))
                    if not (vmin <= views <= vmax): continue
                    filtered.append(v)
                st.session_state.hasil = filtered
                st.session_state.hasil_info = f"✅ Pakai API Key ke-{idx_key+1} | Filter: {batas_bawah.date() if batas_bawah else 'Semua'} s/d {now.date()} | Lolos filter: {len(filtered)} dari {len(hasil_detail)} | Keyword: {kw}"
                st.rerun()

# ========== TAMPILIN HASIL ==========
if st.session_state.hasil:
    st.markdown(f'<div class="box-putih"><p>{st.session_state.hasil_info}</p></div>', unsafe_allow_html=True)
    hasil = list(st.session_state.hasil)
    now = datetime.utcnow()
    for v in hasil:
        tgl = parse_tanggal(v["snippet"]["publishedAt"])
        jam = max(1, (now - tgl).total_seconds() / 3600) if tgl else 1
        v["vph"] = int(v["statistics"].get("viewCount", 0)) / jam
    mode = st.session_state.sort_mode
    if mode == "Terlama": hasil.sort(key=lambda x: x["snippet"]["publishedAt"])
    elif mode == "Terbaru": hasil.sort(key=lambda x: x["snippet"]["publishedAt"], reverse=True)
    elif mode == "Views Terbanyak": hasil.sort(key=lambda x: int(x["statistics"].get("viewCount", 0)), reverse=True)
    elif mode == "Views Paling Sedikit": hasil.sort(key=lambda x: int(x["statistics"].get("viewCount", 0)))
    elif mode == "VPH Tertinggi": hasil.sort(key=lambda x: x.get("vph", 0), reverse=True)
    elif mode == "Subscriber Terbanyak": hasil.sort(key=lambda x: x.get("subs", 0), reverse=True)
    st.markdown(f"### Ditemukan: {len(hasil)} video - Mode: {mode}")
    st.markdown('<div class="hasil-scroll">', unsafe_allow_html=True)
    for v in hasil[:100]:
        sn = v["snippet"]; views = int(v["statistics"].get("viewCount", 0))
        st.markdown(f'<div class="card-video"><p><b>{sn["title"]}</b></p><p>Channel: {sn["channelTitle"]} | Subs: {v.get("subs",0):,} | Views: {views:,} | VPH: {int(v.get("vph",0)):,} | Upload: {sn["publishedAt"][:10]}</p><p><a href="https://youtube.com/watch?v={v["id"]}" target="_blank">▶️ Tonton di YouTube</a></p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    txt = "\n".join([f"{x['snippet']['title']} - https://youtube.com/watch?v={x['id']}" for x in hasil[:100]])
    st.download_button("⬇️ Export txt/md", txt, file_name="snipeme.txt")
else:
    st.markdown('<div class="box-putih"><p>👈 Atur filter di sidebar kiri, lalu klik 🔍 CARI. Hasil akan muncul di sini dengan scrollbar atas-bawah.</p></div>', unsafe_allow_html=True)
