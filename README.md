# [[Networking-tools Collection]](https://github.com/awes0m/the_networking_tools "https://github.com/awes0m/the_networking_tools")

Welcome to the most joyful networking toolbox on the internet! This repo is a playground for packet chasers, and blue-team heroes. Dive in, mash some buttons, and unleash **God-tier** automation on your daily ops.

## 🛠️ Networking Daily Scripts (`networking_daily_scripts/`)

### 🌍 **Bulk Traceroute Tool**

- **File**: `bulk traceroute/traceroute.ps1`
- **Why it bangs**:
  1. Reads hosts from `hostlist.txt` and auto-validates before firing.
  2. Dumps clean CSV reports and opens them for you.
  3. Console colors keep you in the loop like a pro gamer.

### 🧭 **NSLookup Arsenal**

1. **PowerShell Edition** (`NSLOOKUP hostname to ip/nslookup-hostnsame-ip.ps1`)
   - Bulk forward lookups with CSV output and graceful error handling.
2. **Python Squad** (`nslookup` folder)
   - `multilookup.py` for batch jobs.
   - `lookup.py` (Tkinter GUI) with clipboard magic and two-way resolution.
3. **Single-File Goodness**: Updated scripts across `nsLookup-Powershell/` and `nsLookup-Python/` keep things modular.

### 📡 **Ping and Status Finder**

- **File**: `Ping and Status finder/ping only.ps1`
- **Why you'll grin**:
  - Batch ping sweep with automatic CSV reports.
  - Host list managed in `hostlist.txt` for quick edits.
  - Console colors = instant green/red dopamine hits.

---

## 🧰 Python Powerhouse (`python_tools/`)

### 🧬 [JSON Correlator Flask App (`python_tools/Json_Corellator/`)](python_tools/Json_Corellator)

- **Core Engine**: `corellateJson.py`
- **Why it's legendary**:
  1. Launch a full web UI with Tailwind styling.
  2. Compare, visualize, and highlight JSON matches in real time.
  3. Add/remove panes on the fly with zero reloads.
  4. Built-in validation keeps payloads honest.

### 🛡️ [Security Incident Response Report Generator (`python_tools/Security_Incident_Response_Report_generator/`)](python_tools/Security_Incident_Response_Report_generator)

- **Show Runner**: `main.py` with Flask magic.
- **Mega Features**:
  - Full NIST SP 800-61 phase coverage with dynamic tables.
  - Markdown + DOCX report export (hello, compliance!).
  - Form templates, auto-save, and evidence management.
  - Timeline builder to keep your IR story straight.

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone <repository-url>
   cd Godly-Networking-Scripts
   ```
2. **Install Python goodies**
   ```bash
   # JSON Correlator
   cd python_tools/Json_Corellator
   pip install -r requirements.txt

   # Security IR Generator
   cd ../Security_Incident_Response_Report_generator
   pip install -r requirements.txt
   ```
3. **Run the Flask apps**
   ```bash
   # JSON Correlator
   cd python_tools/Json_Corellator
   python corellateJson.py
   # Visit http://127.0.0.1:5000/

   # Incident Response Generator
   cd ../Security_Incident_Response_Report_generator
   python main.py
   # Visit http://127.0.0.1:5000/
   ```
4. **PowerShell playground**
   ```powershell
   # Bulk traceroute
   cd "networking_daily_scripts/bulk traceroute"
   ./traceroute.ps1

   # Ping sweeper
   cd "networking_daily_scripts/Ping and Status finder"
   ./ping\ only.ps1
   ```

---

## 📊 Output Formats at a Glance

- **CSV**: Networking reports (traceroute, ping, lookups).
- **Markdown / DOCX**: Security incident reporting suites.
- **JSON**: Saved presets and form exports.

---

## 🔐 Security & Quality Vibes

- **Validation Everywhere**: Tools scream politely if inputs are funky.
- **Error Handling**: Friendly messages instead of cryptic stack traces.
- **UX First**: Tailwind + custom styling for comfy dashboards.
- **Evidence-ready**: Output formats designed for sharing with stakeholders.

---

## 🤝 Contribute Like a Legend

- **Add a tool** you adore.
- **Enhance UI/UX** components.
- **Boost automation** with new scripts.
- **Tighten security** checks.

Drop a PR, bring snacks, and let's build shiny things together. ✨

---

## 📝 License

See the [LICENSE](LICENSE) file for full details.

**awes0m.github.io** · *2025* · Keep the packets flowing! 🚀
