# Romantic Countdown Site

A Streamlit countdown page for your 1 May meeting, with a cute romantic bear theme, floating hearts, and an editable meeting time.

## Run in VS Code

1. Install Python from <https://www.python.org/downloads/>.
2. Open this folder in VS Code.
3. Open the terminal in VS Code.
4. Install Streamlit:

```powershell
py -m pip install -r requirements.txt
```

5. Start the app:

```powershell
py -m streamlit run app.py
```

## Customize

Use the tiny bottom-right `.` button in the app to change:

- Meeting date
- Meeting time
- Her name
- Your name
- The love note

## Background Image

Put your background image here:

```text
assets/backgrounds
```

For rotating images, use these filenames:

- `background_1.jpg` / `background_1.jpeg` / `background_1.png` / `background_1.webp`
- `background_2.jpg` / `background_2.jpeg` / `background_2.png` / `background_2.webp`
- `background_3.jpg` / `background_3.jpeg` / `background_3.png` / `background_3.webp`
- `background_4.jpg` / `background_4.jpeg` / `background_4.png` / `background_4.webp`
- `background_5.jpg` / `background_5.jpeg` / `background_5.png` / `background_5.webp`

For one still image, use one of these exact filenames:

- `background.jpg`
- `background.jpeg`
- `background.png`
- `background.webp`

Then rerun the Streamlit app.
