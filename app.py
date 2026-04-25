from base64 import b64encode
from datetime import date, time
from html import escape
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Until I See You",
    page_icon="heart",
    layout="wide",
    initial_sidebar_state="collapsed",
)


ROOT = Path(__file__).parent
BACKGROUND_DIR = ROOT / "assets" / "backgrounds"
DEFAULT_DATE = date(2026, 5, 1)
DEFAULT_TIME = time(1, 30)
IMAGE_MIME_TYPES = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
}


def background_images() -> list[str]:
    images: list[str] = []
    for index in range(1, 6):
        for extension, mime in IMAGE_MIME_TYPES.items():
            image_path = BACKGROUND_DIR / f"background_{index}{extension}"
            if image_path.exists():
                encoded = b64encode(image_path.read_bytes()).decode("ascii")
                images.append(f"data:{mime};base64,{encoded}")
                break

    if images:
        return images

    for extension, mime in IMAGE_MIME_TYPES.items():
        image_path = BACKGROUND_DIR / f"background{extension}"
        if image_path.exists():
            encoded = b64encode(image_path.read_bytes()).decode("ascii")
            return [f"data:{mime};base64,{encoded}"]

    return []


def fallback_background_css() -> str:
    return (
        "radial-gradient(circle at 14% 16%, rgba(255, 214, 186, 0.95), transparent 26%), "
        "radial-gradient(circle at 86% 12%, rgba(184, 242, 208, 0.7), transparent 24%), "
        "linear-gradient(135deg, #fff7ec 0%, #ffe5ef 46%, #f7f0ff 100%)"
    )


defaults = {
    "meeting_date": DEFAULT_DATE,
    "meeting_time": DEFAULT_TIME,
    "girlfriend_name": "my love",
    "your_name": "me",
    "note": "Every second is quietly choosing us. I cannot wait to see your face.",
}
for key, value in defaults.items():
    st.session_state.setdefault(key, value)


meeting_date = st.session_state.meeting_date
meeting_time = st.session_state.meeting_time
girlfriend_name = st.session_state.girlfriend_name
your_name = st.session_state.your_name
note = st.session_state.note

target_iso = f"{meeting_date.isoformat()}T{meeting_time.strftime('%H:%M:%S')}"
display_time = meeting_time.strftime("%I:%M %p").lstrip("0")
display_date = meeting_date.strftime("%A, %d %B %Y")
safe_girlfriend_name = escape(girlfriend_name)
safe_your_name = escape(your_name)
safe_note = escape(note).replace("\n", "<br>")
backgrounds = background_images()
background_layers = "\n".join(
    f'<div class="bg-slide bg-{index}" style="background-image: url({image});"></div>'
    for index, image in enumerate(backgrounds, start=1)
)
background_duration = max(len(backgrounds), 1) * 7
background_animation_css = "\n".join(
    f"""
    .bg-{index} {{
        animation-delay: {((index - 1) * 7) - background_duration}s;
    }}
    """
    for index in range(1, len(backgrounds) + 1)
)
app_background = "transparent" if backgrounds else fallback_background_css()


st.markdown(
    f"""
    <style>
    .stApp {{
        background: {app_background};
        color: #351728;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        z-index: 0;
        background: {fallback_background_css()};
        pointer-events: none;
    }}

    .stApp::after {{
        content: "";
        position: fixed;
        inset: 0;
        z-index: 1;
        background:
            radial-gradient(circle at 18% 18%, rgba(255, 214, 186, 0.58), transparent 30%),
            radial-gradient(circle at 82% 10%, rgba(255, 229, 239, 0.66), transparent 32%),
            linear-gradient(rgba(255, 226, 238, 0.78), rgba(255, 244, 249, 0.84));
        pointer-events: none;
    }}

    .stApp > * {{
        position: relative;
        z-index: 2;
    }}

    .bg-slide {{
        position: fixed;
        inset: 0;
        z-index: 0;
        background-position: center;
        background-size: cover;
        background-repeat: no-repeat;
        opacity: 0;
        transform: scale(1.03);
        animation: photoFade {background_duration}s linear infinite;
        pointer-events: none;
    }}

    {background_animation_css}

    @keyframes photoFade {{
        0% {{ opacity: 0; transform: scale(1.03); }}
        5% {{ opacity: 0.34; }}
        20% {{ opacity: 0.34; }}
        27% {{ opacity: 0; transform: scale(1.08); }}
        100% {{ opacity: 0; transform: scale(1.08); }}
    }}

    .block-container {{
        max-width: 100%;
        padding: 0.25rem 0.5rem 1.25rem;
    }}

    header[data-testid="stHeader"] {{
        background: transparent;
    }}

    section[data-testid="stSidebar"] {{
        display: none;
    }}

    div[data-testid="stExpander"] {{
        position: fixed;
        right: 16px;
        bottom: 14px;
        z-index: 9999;
        width: 330px;
        max-width: calc(100vw - 32px);
        border: 1px solid rgba(157, 23, 77, 0.15);
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.76);
        box-shadow: 0 16px 42px rgba(57, 28, 47, 0.14);
        opacity: 0.18;
        transition: opacity 160ms ease, transform 160ms ease;
        backdrop-filter: blur(12px);
    }}

    div[data-testid="stExpander"]:hover,
    div[data-testid="stExpander"]:focus-within {{
        opacity: 0.96;
        transform: translateY(-2px);
    }}

    div[data-testid="stExpander"] summary {{
        font-size: 0.76rem;
        color: #6d3155;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)

if background_layers:
    st.markdown(background_layers, unsafe_allow_html=True)


def render_romantic_page() -> None:
    components.html(
        f"""
<!doctype html>
<html>
<head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;600;700&family=Playfair+Display:wght@700&display=swap');

    * {{ box-sizing: border-box; }}

    body {{
        margin: 0;
        color: #351728;
        font-family: 'Comfortaa', cursive;
        background: transparent;
        overflow-x: hidden;
    }}

    .page {{
        min-height: 940px;
        position: relative;
        display: grid;
        place-items: start center;
        padding: clamp(30px, 6vh, 70px) clamp(14px, 4vw, 58px) 32px;
        text-align: center;
    }}

    .doodle {{
        position: absolute;
        color: rgba(157, 23, 77, 0.34);
        font-weight: 800;
        pointer-events: none;
        user-select: none;
        animation: floaty 4s ease-in-out infinite;
    }}

    .d1 {{ top: 11%; left: 12%; font-size: 2.2rem; transform: rotate(-18deg); }}
    .d2 {{ top: 18%; right: 13%; font-size: 2rem; transform: rotate(12deg); animation-delay: 0.5s; }}
    .d3 {{ top: 52%; left: 9%; font-size: 1.7rem; transform: rotate(18deg); animation-delay: 1s; }}
    .d4 {{ top: 66%; right: 10%; font-size: 2.4rem; transform: rotate(-12deg); animation-delay: 1.4s; }}
    .d5 {{ top: 35%; left: 22%; font-size: 1.4rem; opacity: 0.8; animation-delay: 0.9s; }}
    .d6 {{ top: 41%; right: 25%; font-size: 1.4rem; opacity: 0.75; animation-delay: 1.8s; }}

    .hero {{
        width: min(100%, 1180px);
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    .kicker {{
        margin-top: 6.5rem;
        padding: 0.5rem 0.9rem;
        border: 1px solid rgba(255, 93, 143, 0.34);
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.62);
        color: #9d174d;
        font-size: 0.86rem;
        font-weight: 700;
    }}

    h1 {{
        margin: 2rem 0 1.35rem;
        color: #351728;
        font-family: 'Playfair Display', serif;
        font-size: clamp(3rem, 6vw, 6.3rem);
        line-height: 0.92;
        letter-spacing: 0;
        text-shadow: 0 8px 35px rgba(255, 255, 255, 0.75);
    }}

    .subtitle {{
        width: min(100%, 1040px);
        margin: 0 auto 1.65rem;
        color: #57243f;
        font-size: clamp(1rem, 1.55vw, 1.25rem);
        line-height: 1.75;
    }}

    .countdown {{
        width: min(100%, 1050px);
        position: relative;
        display: grid;
        grid-template-columns: repeat(4, minmax(110px, 1fr));
        gap: 16px;
        padding: clamp(16px, 2.4vw, 28px);
        border: 1px solid rgba(157, 23, 77, 0.18);
        border-radius: 28px;
        background: rgba(255, 255, 255, 0.82);
        box-shadow: 0 22px 70px rgba(157, 23, 77, 0.16);
        overflow: hidden;
    }}

    .countdown::before {{
        content: "";
        position: absolute;
        inset: 0;
        background-image:
            radial-gradient(circle, rgba(255, 93, 143, 0.18) 1.7px, transparent 2.4px),
            radial-gradient(circle, rgba(57, 28, 47, 0.1) 1.2px, transparent 2px);
        background-size: 44px 44px, 70px 70px;
        animation: drift 12s linear infinite;
    }}

    .unit {{
        position: relative;
        z-index: 2;
        min-height: 138px;
        display: grid;
        place-items: center;
        padding: 14px 8px;
        border: 1px solid rgba(157, 23, 77, 0.13);
        border-radius: 20px;
        background: rgba(255, 247, 236, 0.9);
    }}

    .number {{
        color: #9d174d;
        font-size: clamp(3rem, 8vw, 5.65rem);
        font-weight: 700;
        line-height: 1;
        font-variant-numeric: tabular-nums;
    }}

    .label {{
        margin-top: 0.55rem;
        color: #6d3155;
        font-size: 0.9rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0;
    }}

    .message {{
        grid-column: 1 / -1;
        position: relative;
        z-index: 2;
        color: #4c203b;
        font-size: clamp(1rem, 1.7vw, 1.18rem);
        line-height: 1.55;
    }}

    .animation {{
        position: relative;
        width: min(100%, 780px);
        height: 215px;
        margin: 0.85rem auto 0;
        overflow: hidden;
    }}

    .ground {{
        position: absolute;
        left: 8%;
        right: 8%;
        bottom: 28px;
        height: 12px;
        border-radius: 999px;
        background: rgba(157, 23, 77, 0.14);
    }}

    .bear {{
        position: absolute;
        bottom: 40px;
        width: 92px;
        height: 108px;
        border: 4px solid #3b2431;
        border-radius: 48% 48% 40% 40%;
    }}

    .bear.left {{
        left: 18%;
        background: #ffe3b4;
        animation: runLeft 2.7s ease-in-out infinite;
    }}

    .bear.right {{
        right: 18%;
        background: #f8f8f8;
        animation: runRight 2.7s ease-in-out infinite;
    }}

    .ear {{
        position: absolute;
        top: -22px;
        width: 38px;
        height: 38px;
        border: 4px solid #3b2431;
        border-radius: 999px;
        background: inherit;
    }}

    .ear.left-ear {{ left: 10px; }}
    .ear.right-ear {{ right: 10px; }}
    .ear::after {{
        content: "";
        position: absolute;
        inset: 8px;
        border-radius: 999px;
        background: #ffc3d2;
    }}

    .eye {{
        position: absolute;
        top: 34px;
        width: 9px;
        height: 14px;
        border-radius: 999px;
        background: #2f1826;
    }}

    .eye.left-eye {{ left: 29px; }}
    .eye.right-eye {{ right: 29px; }}

    .snout {{
        position: absolute;
        left: 50%;
        top: 54px;
        width: 42px;
        height: 28px;
        transform: translateX(-50%);
        border: 3px solid #3b2431;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.75);
    }}

    .nose {{
        position: absolute;
        left: 50%;
        top: 5px;
        width: 13px;
        height: 9px;
        transform: translateX(-50%);
        border-radius: 999px;
        background: #2f1826;
    }}

    .kiss {{
        position: absolute;
        left: 50%;
        bottom: 113px;
        width: 42px;
        height: 42px;
        margin-left: -21px;
        background: #ff5d8f;
        transform: rotate(45deg) scale(0);
        animation: popHeart 2.7s ease-in-out infinite;
    }}

    .kiss::before,
    .kiss::after {{
        content: "";
        position: absolute;
        width: 42px;
        height: 42px;
        border-radius: 999px;
        background: #ff5d8f;
    }}

    .kiss::before {{ left: -21px; }}
    .kiss::after {{ top: -21px; }}

    .caption {{
        position: absolute;
        left: 50%;
        bottom: 0;
        transform: translateX(-50%);
        width: min(92%, 620px);
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.66);
        color: #6d3155;
        font-weight: 800;
    }}

    .love-note {{
        width: min(100%, 760px);
        margin: 1.1rem auto 0;
        padding: 1rem 1.15rem;
        border-left: 5px solid #ff5d8f;
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.7);
        color: #4c203b;
        line-height: 1.65;
        text-align: left;
    }}

    .scroll-note {{
        margin: 1rem 0 0;
        color: rgba(87, 36, 63, 0.72);
        font-size: 0.92rem;
    }}

    @keyframes drift {{
        from {{ background-position: 0 0, 0 0; }}
        to {{ background-position: 44px 44px, -70px 70px; }}
    }}

    @keyframes floaty {{
        0%, 100% {{ translate: 0 0; }}
        50% {{ translate: 0 12px; }}
    }}

    @keyframes runLeft {{
        0%, 100% {{ transform: translateX(0) rotate(-3deg); }}
        45%, 55% {{ transform: translateX(145px) rotate(5deg); }}
    }}

    @keyframes runRight {{
        0%, 100% {{ transform: translateX(0) rotate(3deg); }}
        45%, 55% {{ transform: translateX(-145px) rotate(-5deg); }}
    }}

    @keyframes popHeart {{
        0%, 34% {{ transform: rotate(45deg) scale(0); opacity: 0; }}
        48% {{ transform: rotate(45deg) scale(1); opacity: 1; }}
        70%, 100% {{ transform: rotate(45deg) translateY(-48px) scale(0.85); opacity: 0; }}
    }}

    @media (max-width: 680px) {{
        .page {{
            min-height: 980px;
            padding-top: 24px;
        }}

        .kicker {{
            margin-top: 2.7rem;
        }}

        .countdown {{
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }}

        .unit {{
            min-height: 112px;
        }}

        .bear.left {{ left: 5%; }}
        .bear.right {{ right: 5%; }}

        @keyframes runLeft {{
            0%, 100% {{ transform: translateX(0) rotate(-3deg); }}
            45%, 55% {{ transform: translateX(90px) rotate(5deg); }}
        }}

        @keyframes runRight {{
            0%, 100% {{ transform: translateX(0) rotate(3deg); }}
            45%, 55% {{ transform: translateX(-90px) rotate(-5deg); }}
        }}
    }}
    </style>
</head>
<body>
    <main class="page">
        <div class="doodle d1">&hearts;</div>
        <div class="doodle d2">+</div>
        <div class="doodle d3">xoxo</div>
        <div class="doodle d4">&hearts;</div>
        <div class="doodle d5">.</div>
        <div class="doodle d6">&infin;</div>

        <section class="hero">
            <div class="kicker">a little wait for a very big hug</div>
            <h1>Until I See You</h1>
            <p class="subtitle">
                {display_date} at {display_time}. I am keeping this night soft,
                silly, and entirely yours.
            </p>

            <div class="countdown">
                <div class="unit"><div><div class="number" id="days">00</div><div class="label">Days</div></div></div>
                <div class="unit"><div><div class="number" id="hours">00</div><div class="label">Hours</div></div></div>
                <div class="unit"><div><div class="number" id="minutes">00</div><div class="label">Minutes</div></div></div>
                <div class="unit"><div><div class="number" id="seconds">00</div><div class="label">Seconds</div></div></div>
                <div class="message" id="message">Every second is one tiny step closer to you.</div>
            </div>

            <div class="animation">
                <div class="ground"></div>
                <div class="bear left">
                    <div class="ear left-ear"></div>
                    <div class="ear right-ear"></div>
                    <div class="eye left-eye"></div>
                    <div class="eye right-eye"></div>
                    <div class="snout"><div class="nose"></div></div>
                </div>
                <div class="bear right">
                    <div class="ear left-ear"></div>
                    <div class="ear right-ear"></div>
                    <div class="eye left-eye"></div>
                    <div class="eye right-eye"></div>
                    <div class="snout"><div class="nose"></div></div>
                </div>
                <div class="kiss"></div>
                <div class="caption">two tiny hearts racing toward one very necessary hug</div>
            </div>

            <div class="love-note" id="love-message">
                <strong>For {safe_girlfriend_name}</strong><br>
                {safe_note}
                <br><br>
                <span>With all my heart,<br>{safe_your_name}</span>
            </div>
            <div class="scroll-note">scroll down to the little message when you want the soft part</div>
        </section>
    </main>

    <script>
    const target = new Date("{target_iso}");
    const pad = (value) => String(value).padStart(2, "0");
    const setText = (id, value) => document.getElementById(id).textContent = value;

    function tick() {{
        const now = new Date();
        let diff = target - now;

        if (diff <= 0) {{
            setText("days", "00");
            setText("hours", "00");
            setText("minutes", "00");
            setText("seconds", "00");
            document.getElementById("message").textContent = "It is time. Go hold her hand.";
            return;
        }}

        const days = Math.floor(diff / 86400000);
        diff -= days * 86400000;
        const hours = Math.floor(diff / 3600000);
        diff -= hours * 3600000;
        const minutes = Math.floor(diff / 60000);
        diff -= minutes * 60000;
        const seconds = Math.floor(diff / 1000);

        setText("days", pad(days));
        setText("hours", pad(hours));
        setText("minutes", pad(minutes));
        setText("seconds", pad(seconds));
    }}

    tick();
    setInterval(tick, 1000);
    </script>
</body>
</html>
        """,
        height=960,
    )


render_romantic_page()


with st.expander("."):
    st.date_input("Date", key="meeting_date", format="DD/MM/YYYY")
    st.time_input("Time", key="meeting_time", step=60)
    st.text_input("Her", key="girlfriend_name")
    st.text_input("You", key="your_name")
    st.text_area("Message", key="note", height=100)

