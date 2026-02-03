# 🍽️ Restaurant FAQ System using Generative AI

## 📌 Overview
Choosing the right dish from a restaurant menu can be overwhelming, especially for customers with dietary preferences, allergies, or health-related restrictions. Menus are often long, unstructured, and difficult to quickly analyze.

This project is a **Generative AI-powered Restaurant FAQ system** that intelligently **compresses menu information and dietary options**, allowing users to ask natural language questions and receive clear, concise answers. The system acts as a smart dining assistant, helping customers make informed food choices efficiently.

This project has been **developed with the assistance of Generative AI** to demonstrate practical, real-world applications of GenAI in the food and hospitality domain.

---

## ❓ Problem Statement
Restaurant menus:
- Contain excessive information with little structure
- Do not clearly highlight dietary options (vegan, gluten-free, allergies, etc.)
- Make it hard for customers to quickly decide what to order
- Are especially challenging for users with medical or dietary restrictions

There is a need for an **intelligent, conversational system** that can simplify menus and answer user-specific questions instantly.

---

## 💡 Solution
The Restaurant FAQ System uses **Generative AI and Natural Language Processing (NLP)** to:
- Analyze restaurant menu data
- Compress and summarize dish descriptions
- Identify dietary attributes and ingredients
- Answer user queries in a conversational FAQ format

Users can ask questions like:
- *“Which dishes are vegan?”*
- *“Does this dish contain nuts?”*
- *“Suggest a low-calorie meal.”*
- *“What are the best options for diabetics?”*

The system provides **fast, accurate, and easy-to-understand responses**, improving the overall dining experience.

---

## ✨ Key Features
- 📄 Menu data ingestion (JSON / text-based menus)
- 🧠 AI-powered menu summarization
- 💬 Natural language FAQ-style interaction
- 🥗 Dietary filtering (vegan, vegetarian, gluten-free, allergies)
- ⚡ Quick and concise responses
- 🤖 Built using Generative AI models

---

## 🛠️ Tech Stack
**Frontend**
- React.js
- HTML, CSS / Tailwind CSS

**Backend**
- Python
- Flask / FastAPI

**Generative AI**
- Large Language Model (LLM) API
- Prompt-based question answering and summarization

**Data**
- Menu stored in JSON format

---

## 🧩 System Architecture
1. User submits a question via the frontend
2. Backend receives the query and menu data
3. Prompt is generated combining menu + user query
4. Generative AI model processes the prompt
5. AI-generated answer is returned to the user

---

## 🚀 How to Run the Project (Basic Setup)

### Backend
```bash
pip install -r requirements.txt
python app.py

```
### Frontend
```bash
npm install
npm start

```
### 📜 License

This project is licensed under the MIT License.

