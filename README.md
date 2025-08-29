# (Godly Networking Scripts Collection)[https://github.com/awes0m/Godly-Networking-Scripts]

A comprehensive collection of networking utilities and security tools designed for network administrators, security analysts, and IT professionals. This repository contains three main categories of tools: general networking scripts, JSON correlation utilities, and security incident response generators.

## 📁 Repository Structure

### 1. General Networking Daily Scripts (`general_networking_daily_scripts/`)[https://github.com/awes0m/Godly-Networking-Scripts/tree/main/general_networking_daily_scripts]

A collection of PowerShell and Python scripts for common networking tasks and diagnostics.

#### (🔍 **Bulk Traceroute Tool**)[https://github.com/awes0m/Godly-Networking-Scripts/tree/main/general_networking_daily_scripts/bulk%20traceroute]

- **File**: `bulk traceroute/traceroute.ps1`
- **Language**: PowerShell
- **Features**:
  - Performs traceroute operations on multiple hosts from a list
  - Reads hostnames/IPs from `hostlist.txt`
  - Tests connectivity before traceroute execution
  - Generates detailed CSV reports with results
  - Color-coded console output for easy monitoring
  - Automatically opens results file upon completion

#### 🌐 **NSLookup Tools**

##### (PowerShell NSLookup (Hostname to IP))[https://github.com/awes0m/Godly-Networking-Scripts/tree/main/general_networking_daily_scripts/NSLOOKUP%20hostname%20to%20ip]

- **File**: `nsLookup-Powershell/NSLOOKUP hostname to ip/nslookup-hostnsame-ip.ps1`
- **Language**: PowerShell
- **Features**:
  - Bulk hostname to IP address resolution
  - Reads from `hostlist.txt` input file
  - Exports results to CSV format
  - Handles DNS resolution failures gracefully
  - Automatic result file opening

##### (Python NSLookup Tools)[https://github.com/awes0m/Godly-Networking-Scripts/tree/main/general_networking_daily_scripts/nsLookup-Python]

- **Bulk NSLookup**: `nsLookup-Python/bulk/multi_nslookup.py`

  - **Language**: Python
  - **Features**:
    - Batch DNS lookups for multiple hosts
    - CSV output generation
    - Subprocess-based nslookup execution
    - Error handling for invalid entries
- **Single NSLookup GUI**: `nsLookup-Python/Single/lookup.py`

  - **Language**: Python (Tkinter GUI)
  - **Features**:
    - User-friendly graphical interface
    - Bidirectional DNS lookup (IP ↔ Hostname)
    - Radio button selection for lookup type
    - Automatic clipboard copying functionality
    - Input validation and error messaging
    - Real-time result display

#### 📡 (**Ping and Status Finder**)[https://github.com/awes0m/Godly-Networking-Scripts/tree/main/general_networking_daily_scripts/Ping%20and%20Status%20finder]

- **File**: `Ping and Status finder/ping only.ps1`
- **Language**: PowerShell
- **Features**:
  - Bulk ping testing for network connectivity
  - Reads target hosts from `hostlist.txt`
  - Color-coded console feedback (Green/Red)
  - CSV report generation with status indicators
  - Automatic result file opening

### 2. JSON Correlator (`Json_Corellator/`)[https://github.com/awes0m/Godly-Networking-Scripts/tree/main/Json_Corellator]

A Flask-based web application for analyzing and correlating JSON data structures.

#### 🔗 **JSON Correlation Web Tool**

- **Main File**: `corellateJson.py`
- **Language**: Python (Flask)
- **Features**:
  - **Multi-JSON Comparison**: Compare up to 4 JSON files simultaneously
  - **Interactive Web Interface**: Modern, responsive design with Tailwind CSS
  - **Visual JSON Tree**: Expandable/collapsible JSON structure visualization
  - **Similarity Highlighting**: Automatically highlights matching values across JSONs
  - **Security Focus**: Particularly useful for security incident JSON correlation
  - **Dynamic Pane Management**: Add/remove JSON comparison panes as needed
  - **Real-time Analysis**: Instant correlation results without page refresh
  - **Error Handling**: Comprehensive JSON validation and error reporting

#### 🎯 **Use Cases**:

- Security incident analysis and correlation
- API response comparison
- Configuration file validation
- Data structure analysis
- Forensic JSON examination

### 3. Security Incident Response Report Generator (`Security_Incident_Response_Report_generator(Standardised)/`)[https://github.com/awes0m/Godly-Networking-Scripts/tree/main/Security_Incident_Response_Report_generator(Standardised)]

A comprehensive Flask web application for creating standardized security incident response reports.

#### 📋 **Incident Response Workflow Tool**

- **Main File**: `main.py`
- **Language**: Python (Flask)
- **Features**:

##### **Core Functionality**:

- **NIST SP 800-61 Compliance**: Follows standardized incident response procedures
- **Multi-format Export**: Generate reports in Markdown (.md) and Word (.docx) formats
- **Form Persistence**: Save and load incident forms for ongoing investigations
- **Image Attachment**: Support for screenshot and evidence attachment
- **Validation System**: Required field validation before report generation

##### **Incident Response Phases**:

1. **Triage & Initial Assessment**

   - Incident ID generation
   - Reporter information
   - Priority classification (Low/Medium/High/Critical)
   - Initial incident summary
2. **Identification & Scoping**

   - Dynamic evidence tables
   - Host/asset tracking
   - IP address correlation
   - Indicators of Compromise (IoCs) documentation
   - Evidence attachment support
3. **Containment**

   - Action tracking with timestamps
   - Personnel assignment
   - System/asset impact documentation
   - Containment strategy planning
4. **Eradication**

   - Remediation action logging
   - Outcome tracking
   - Eradication strategy documentation
5. **Recovery**

   - Recovery action planning
   - Validation step documentation
   - System restoration tracking
6. **Post-Incident Activities**

   - Timeline summary generation
   - Root cause analysis
   - Lessons learned documentation
   - Follow-up action items with assignments
7. **Conclusion**

   - Incident classification (True/False Positive/Negative)
   - Final summary and recommendations

##### **Advanced Features**:

- **Collapsible Sections**: Organized, space-efficient interface
- **Dynamic Tables**: Add/remove rows for evidence and actions
- **Auto-save Functionality**: Prevent data loss during long investigations
- **Form Templates**: Save common incident types as templates
- **Professional Formatting**: Clean, professional report output
- **Timestamp Management**: UTC timestamp handling throughout

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+** (for Python scripts and Flask applications)
- **PowerShell 5.0+** (for PowerShell scripts)
- **Required Python packages**:
  ```bash
  pip install flask python-docx
  ```

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Godly-Networking-Scripts
   ```
2. Install Python dependencies:

   ```bash
   # For JSON Correlator
   cd Json_Corellator
   pip install -r requirements.txt

   # For Security Incident Response Generator
   cd ../Security_Incident_Response_Report_generator(Standardised)
   pip install -r requirements.txt
   ```

### Usage Examples

#### Running the JSON Correlator:

```bash
cd Json_Corellator
python corellateJson.py
# Access at http://127.0.0.1:5000/
```

#### Running the Incident Response Generator:

```bash
cd Security_Incident_Response_Report_generator(Standardised)
python main.py
# Access at http://127.0.0.1:5000/
```

#### Using PowerShell Scripts:

```powershell
# For bulk traceroute
cd "general_networking_daily_scripts/bulk traceroute"
# Edit hostlist.txt with your target hosts
./traceroute.ps1

# For ping testing
cd "general_networking_daily_scripts/Ping and Status finder"
# Edit hostlist.txt with your target hosts
./ping\ only.ps1
```

## 📊 Output Formats

### Networking Scripts

- **CSV Reports**: Structured data output for analysis
- **Console Output**: Real-time colored feedback
- **Text Files**: Detailed traceroute results

### JSON Correlator

- **Web Interface**: Interactive visual comparison
- **Highlighted Similarities**: Color-coded matching values

### Incident Response Generator

- **Markdown Reports**: Lightweight, version-controllable format
- **Word Documents**: Professional, formatted reports with embedded images
- **JSON Data**: Saved form data for persistence

## 🛡️ Security Features

- **Input Validation**: Comprehensive validation across all tools
- **Error Handling**: Graceful handling of network failures and invalid inputs
- **Data Sanitization**: Safe handling of user inputs and file operations
- **Professional Reporting**: Standardized incident response documentation

## 🤝 Contributing

This collection is designed for network administrators and security professionals. Contributions are welcome for:

- Additional networking utilities
- Enhanced error handling
- New export formats
- UI/UX improvements
- Security enhancements

## 📝 License

See LICENSE file for details.

## 👨‍💻 Author

**awes0m.github.io**

*2025*

---

*These tools are designed to streamline network administration tasks and enhance security incident response capabilities. Each tool focuses on practical, real-world networking and security challenges.*
