# 🌍 Voyagent: An End-to-End Agentic AI Travel Planning Agent with LLMOps

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Your intelligent travel companion powered by advanced AI and real-time data integration**

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [🛠️ Setup](#️-setup) • [📖 Usage](#-usage) • [🔧 API](#-api) • [🤝 Contributing](#-contributing)

</div>

---

## 🎯 **Project Overview**

Voyagent is an AI-powered travel planning agent that creates personalized itineraries using LLMs, LangChain, and agentic workflows. It integrates real-time data with advanced prompt engineering and LangGraph orchestration, demonstrating end-to-end GenAI application development and LLMOps best practices in a modular, production-ready system.

### **Key Highlights**

- 🤖 **Agentic AI Workflows**: Uses LangGraph to orchestrate multi-step tools and LLM reasoning
- 🌐 **Real-Time Data Integration**: Weather, places, currency APIs for live, accurate plans
- ⚙️ **Full-Stack AI Application**: FastAPI backend, Streamlit frontend for seamless UX
- 🛠️ **LLMOps Integration**: Modular design, environment configs, scalable structure
- 🎨 **Modern UI**: Beautiful, responsive Streamlit interface
- 📊 **Comprehensive Logging**: Structured logging with file rotation
- 🛡️ **Robust Error Handling**: Custom exception classes and graceful degradation
- 📱 **Export Capabilities**: Download travel plans in multiple formats

---




https://github.com/user-attachments/assets/dddee97f-929f-42fd-8e5e-b4664dd9d07a



---
## ✨ **Features**

### **🤖 AI-Powered Planning**

- **Intelligent Itinerary Generation**: Creates comprehensive day-by-day travel plans
- **Multi-Provider Support**: Groq and OpenAI integration
- **Contextual Understanding**: Analyzes user preferences and requirements
- **Dynamic Recommendations**: Suggests both popular and off-beat locations

### **🌐 Real-time Data Integration**

- **Weather Information**: Current conditions and 5-day forecasts via OpenWeatherMap
- **Place Recommendations**: Attractions, restaurants, activities via Google Places API
- **Currency Conversion**: Real-time exchange rates for budget planning
- **Fallback Mechanisms**: Tavily search when primary APIs are unavailable

### **🎨 Modern User Interface**

- **Responsive Design**: Works seamlessly on desktop and mobile
- **Progress Indicators**: Multi-step loading with visual feedback
- **Interactive Elements**: Real-time updates and smooth transitions
- **Professional Styling**: Clean, modern aesthetic with gradient backgrounds

### **⚙️ Backend Orchestration**
- **FastAPI REST** endpoints for efficient AI requests
- **LangGraph Workflows**: Structured, tool-based agent orchestration
- **Error Handling**: Try-catch with fallback mechanisms for reliability

### **📊 Advanced Logging & Monitoring**

- **Structured Logging**: JSON-formatted logs with different levels
- **File Rotation**: Automatic log management with size limits
- **Error Tracking**: Comprehensive exception handling and reporting
- **Performance Monitoring**: API call tracking and response time analysis

### **📱 Export & Download**

- **Text Export**: Clean, readable travel plan downloads
- **Metadata Inclusion**: Generation timestamps and source information
- **Professional Formatting**: Well-structured output with proper formatting

---

## 🚀 **Quick Start**

### **Prerequisites**

- Python 3.10 or higher
- Required API keys (see [Configuration](#-configuration))

### **Installation**

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd AI_Trip_Planner
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   ```bash
   # Create .env file with your API keys
   cp .env.example .env
   # Edit .env with your actual API keys
   ```

4. **Start the application**

   ```bash
   # Terminal 1: Start backend API
   python main.py

   # Terminal 2: Start frontend
   streamlit run streamlit_app.py
   ```

5. **Access the application**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000

---

## 🛠️ **Setup & Configuration**

### **Required API Keys**

Create a `.env` file in the project root with the following keys:

```env
# LLM Provider (choose one)
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# Weather API
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key_here

# Places API
GPLACES_API_KEY=your_google_places_api_key_here

# Currency API
EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key_here

# Search API (fallback)
TAVILY_API_KEY=your_tavily_api_key_here
```

### **API Key Sources**

| Service               | URL                                                                                               | Purpose                  |
| --------------------- | ------------------------------------------------------------------------------------------------- | ------------------------ |
| **Groq**              | [console.groq.com](https://console.groq.com/)                                                     | Primary LLM provider     |
| **OpenAI**            | [platform.openai.com](https://platform.openai.com/)                                               | Alternative LLM provider |
| **OpenWeatherMap**    | [openweathermap.org/api](https://openweathermap.org/api)                                          | Weather data             |
| **Google Places**     | [developers.google.com/maps](https://developers.google.com/maps/documentation/places/web-service) | Location information     |
| **Exchange Rate API** | [exchangerate-api.com](https://www.exchangerate-api.com/)                                         | Currency conversion      |
| **Tavily**            | [tavily.com](https://tavily.com/)                                                                 | Web search fallback      |

---

## 📖 **Usage**

### **Web Interface**

1. **Open the application** in your browser (http://localhost:8501)
2. **Enter your travel request** in the text area
   - Be specific about destination, duration, and preferences
   - Include budget constraints and activities of interest
3. **Click "Generate Itinerary"** and watch the progress
4. **Review your personalized travel plan**
5. **Download the plan** as a text file for offline access

### **Example Queries**

```
"Plan a 7-day cultural trip to Japan with a focus on traditional experiences and food"
"Create a budget-friendly 5-day adventure itinerary for Bali with beach activities"
"Design a luxury 10-day European tour covering Paris, Rome, and Barcelona"
"Plan a family-friendly 3-day weekend trip to Disney World with accommodation"
```

### **API Usage**

```python
import requests

# Generate a travel plan
response = requests.post("http://localhost:8000/query", json={
    "question": "Plan a 5-day trip to Paris with cultural activities"
})

if response.status_code == 200:
    plan = response.json()
    print(plan["answer"])
    print(f"Processing time: {plan['metadata']['processing_time']}s")
else:
    print(f"Error: {response.json()}")
```

---

## 🏗️ **Architecture**

### **Project Structure**

```
AI_Trip_Planner/
├── 🌍 Frontend (Streamlit)
│   └── streamlit_app.py          # Modern web interface
├── ⚙️ Backend (FastAPI)
│   └── main.py                   # REST API server
├── 🤖 AI Agent
│   └── agent/agentic_workflow.py # LangGraph workflow orchestration
├── 🛠️ Tools & Utilities
│   ├── tools/                    # Functional tools (weather, places, etc.)
│   ├── utils/                    # Utility modules
│   └── prompt_library/           # AI prompts and templates
├── 📊 Logging & Error Handling
│   ├── logger/logging.py         # Structured logging system
│   └── exception/exceptiohandling.py # Custom exception classes
├── ⚙️ Configuration
│   └── config/config.yaml        # Application configuration
└── 📚 Documentation & Testing
    ├── README.md                 # This file
    └── test_*.py                 # Test suites
```

### **Technology Stack**

| Component         | Technology                    | Purpose                     |
| ----------------- | ----------------------------- | --------------------------- |
| **AI Framework**  | LangChain + LangGraph         | Workflow orchestration      |
| **LLM Providers** | Groq, OpenAI                  | Language model integration  |
| **Frontend**      | Streamlit                     | Modern web interface        |
| **Backend**       | FastAPI, Uvicorn                       | High-performance REST API endpoints |
| **Data APIs**     | OpenWeatherMap, Google Places | Real-time information       |
| **DevOps/LLMOps**     | configs, modular setup, production-ready design | Structured codebase for deployment scalability       |
| **Logging**       | Custom structured logger      | Application monitoring      |
| **Testing**       | Python unittest               | Quality assurance           |

---

## 🔧 **API Reference**

### **POST /query**

Generate a travel plan based on user input.

**Request:**

```json
{
  "question": "Plan a 5-day trip to Paris with cultural activities"
}
```

**Response:**

```json
{
  "answer": "# Your AI-Generated Travel Plan\n\n## Day 1\n- Arrive in Paris...",
  "metadata": {
    "processing_time": 12.5,
    "generated_at": "2024-01-15T10:30:00Z",
    "model_provider": "groq"
  }
}
```

**Error Response:**

```json
{
  "error": true,
  "message": "Query must be at least 10 characters long",
  "error_code": "VALIDATION_ERROR",
  "details": {
    "min_length": 10,
    "provided_length": 5
  }
}
```

---

## 🧪 **Testing**

### **Run Test Suite**

```bash
# Test all improvements
python test_improvements.py

# Test basic functionality
python test_simple_changes.py
```

### **Test Coverage**

- ✅ **Logging System**: Structured logging with file rotation
- ✅ **Exception Handling**: Custom exception classes and error responses
- ✅ **Export Functionality**: Text file generation and download
- ✅ **Integration**: Component interaction and API responses
- ✅ **UI Components**: Streamlit interface and user interactions

---

## 🚀 **Deployment**

### **Local Development**

```bash
# Development mode with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
streamlit run streamlit_app.py --server.port 8501
```

### **Production Deployment**

#### **Backend (FastAPI)**

- **Render**: [render.com](https://render.com/)
- **Heroku**: [heroku.com](https://heroku.com/)
- **AWS**: [aws.amazon.com](https://aws.amazon.com/)
- **DigitalOcean**: [digitalocean.com](https://digitalocean.com/)

#### **Frontend (Streamlit)**

- **Streamlit Cloud**: [streamlit.io/cloud](https://streamlit.io/cloud)
- **Self-hosted**: Any web server with Python support

### **Environment Variables**

Ensure all required environment variables are set in your deployment environment:

```bash
GROQ_API_KEY=your_key
OPENWEATHERMAP_API_KEY=your_key
GPLACES_API_KEY=your_key
EXCHANGE_RATE_API_KEY=your_key
TAVILY_API_KEY=your_key
```

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

### **Development Setup**

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests** for new functionality
5. **Run the test suite**
   ```bash
   python test_improvements.py
   ```
6. **Submit a pull request**

### **Guidelines**

- **Code Style**: Follow PEP 8 guidelines
- **Documentation**: Add docstrings and comments
- **Testing**: Include tests for new features
- **Error Handling**: Implement proper exception handling
- **Logging**: Use structured logging for debugging

### **Areas for Contribution**

- 🌐 **New API Integrations**: Additional data sources
- 🎨 **UI Enhancements**: Better user experience
- 🤖 **AI Improvements**: Enhanced prompts and workflows
- 📊 **Analytics**: Usage statistics and insights
- 🔒 **Security**: Authentication and authorization
- 📱 **Mobile**: Native mobile applications

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **LangChain Team**: For the amazing AI workflow framework
- **Streamlit Team**: For the intuitive web app framework
- **FastAPI Team**: For the high-performance API framework
- **OpenWeatherMap**: For reliable weather data
- **Google Places API**: For comprehensive location information
- **All Contributors**: For making this project better

---

## 📞 **Support**

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- **Email**: your-email@example.com

---

<div align="center">

**Made with ❤️ by the Voyagent Team**

_Your intelligent travel companion powered by AI_

[⬆️ Back to Top](#-voyagent-an-end-to-end-agentic-ai-travel-planning-agent-with-llmops)

</div>
