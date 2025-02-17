### **AI Code Reviewer - GenAI Application**  
🚀 **AI-powered Python Code Reviewer using Google Gemini API and Streamlit**  

![AI Code Reviewer](https://user-images.githubusercontent.com/yourimage.png) *(Optional: Add an image/banner here)*  

## 📌 **Overview**  
AI Code Reviewer is a **GenAI-powered web application** built with **Streamlit** and **Google Gemini API**. It analyzes Python code, detects bugs, suggests optimizations, and provides best practices.  

## 🔥 **Features**  
- 📌 **Bug Detection**: Identifies logical errors in Python code.  
- ⚡ **Code Optimization**: Suggests performance improvements.  
- ✅ **Best Practices**: Enforces clean and efficient coding standards.  
- 🖥 **Simple UI**: Built with **Streamlit** for ease of use.  

## 🛠 **Tech Stack**  
- **Python**  
- **Streamlit**  
- **Google Gemini API**  
- **OS Module** (for API key management)  

## 🚀 **Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/ai-code-reviewer.git
cd ai-code-reviewer
```

### **2️⃣ Set Up a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Google Gemini API Key**  
Create a `.env` file in the root directory and add your API key:  
```
GEMINI_API_KEY=your_google_gemini_api_key
```
Or set it as an **environment variable**:  
```bash
export GEMINI_API_KEY="your_google_gemini_api_key"  # macOS/Linux
set GEMINI_API_KEY="your_google_gemini_api_key"     # Windows
```

### **5️⃣ Run the Application**  
```bash
streamlit run app.py
```

