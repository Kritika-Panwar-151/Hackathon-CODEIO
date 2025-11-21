Fake App Detector — Android + Django Web Application
====================================================

_A lightweight academic prototype for detecting fake/cloned Android apps using similarity scoring, icon hashing, publisher matching, permissions audit, and risk scoring._

Features
-----------

### **1\. Fake App Detection Engine**

The system compares a suspicious app with the genuine baseline app using:

*   **Name Similarity (SequenceMatcher)**
    
*   **Publisher Similarity**
    
*   **Package ID comparison**
    
*   **Icon similarity using perceptual hashing (imagehash + PIL)**
    
*   **Permissions risk scoring**
    
*   **Install count comparison**
    
*   **Rating-based risk**
    
*   **Overall risk score (0–100)**
    

### **2\. Evidence Panel**

When the user clicks **View**, the system shows:

*   App metadata
    
*   Risk score
    
*   Evidence table
    
*   Evidence JSON
    
*   Auto-generated takedown email
    
*   Icon hash comparison
    

### **3\. Android WebView App**

A lightweight Android wrapper that loads the Django website with:

*   Auto mobile scaling
    
*   Disabled zoom (prevents shaking)
    
*   No scrollbars
    
*   Fits perfectly on Android screens
    

### **4\. Detection Metrics**

The system automatically generates:

*   **TP / FP / FN / TN**
    
*   **Precision**
    
*   **Recall**
    

Presented in a clean expandable section.

### **5\. Safety & Ethics Notice**

Includes mandatory responsible-AI disclaimers.

Project Structure
---------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   /android_app/      MainActivity.kt      AndroidManifest.xml      activity_main.xml  /django_project/      /app/          apps_data.py          views.py          templates/home.html   `

How Detection Works
----------------------

CheckDescription**Name Similarity**Fuzzy match between suspicious and real app**Hash Matching**Compares icons using perceptual hashing**Publisher Match**Detects mismatched or suspicious publishers**Permission Audit**Flags READ\_SMS, RECORD\_AUDIO, CALL\_LOG etc**Installs & Rating**Fake apps often have very low installs + bad ratings

Tech Stack
--------------

*   **Backend:** Django
    
*   **Frontend:** HTML + CSS + Vanilla JS
    
*   **Image Processing:** Pillow + ImageHash
    
*   **Android:** Kotlin WebView wrapper
    
*   **Storage:** Local predefined dataset
    

Installation
---------------

### 1️⃣ Django Setup

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install pillow imagehash django  python manage.py runserver   `

### 2️⃣ Android App Setup

Open Android Studio → Build → Run on device

Modify URL in MainActivity.kt:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   webView.loadUrl("http://YOUR_IP:8000/")   `


Example Risk Report
----------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   App: PhonePay Free Cashback  Risk Score: 100/100  - App name not very similar to official (0.46)  - Package mismatch  - Publisher mismatch  - Suspicious keywords detected  - Icon visually identical to official  - Dangerous permissions (READ_SMS, RECORD_AUDIO)   `

Safety & Ethics
------------------

No real malware execution✔ No scraping violating ToS✔ No doxxing✔ App-level analysis only✔ Academic prototype, not production-ready

Future Improvements
---------------------

*   Automatic dataset expansion using web scraping
    
*   ML-based icon similarity
    
*   API to scan real APKs
    
*   Offline risk engine for mobile