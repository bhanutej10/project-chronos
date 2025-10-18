# Project Chronos: The AI Archeologist

###Student Info
Name: K. Bhanutej 
ID: SE24UMCS036

Name: C. Vivek
ID: SE24UMCS002

Name: G. Saanvi Rao
ID: SE25UDSC014



---

##Project Description
**Project Chronos** reconstructs incomplete or obscure internet texts using Google's Gemini API and performs automated web searches to provide context. 
It outputs a detailed *Reconstruction Report* containing the original text, AI reconstruction, and contextual sources.

---

##Setup Instructions

### 1. Clone or Download
```bash
git clone <your_repo_url>
cd project-chronos
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
Create a `.env` file in the project folder:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

### 5. Run the App
```bash
python main.py
```

### Example Input:
```
smh at the top 8 drama. ppl need to chill. g2g, ttyl.
```

---

## Output
A Markdown report will be saved in the `reports/` folder:
```
# RECONSTRUCTION REPORT
> Original text
> Reconstructed version
> Context links
```

---

## Files
- **main.py** — Core logic (Gemini + web search + report)
- **requirements.txt** — Dependencies
- **README.md** — Documentation & setup guide
