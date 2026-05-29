# NAVARROTEX - Intelligent ChatBot for Croptops Sales

This is a virtual assistant developed in Python that uses Machine Learning (natural language processing via TF-IDF and Cosine Similarity) to automate customer service and sales for NAVARROTEX croptops.

The simulation interface is built with Streamlit, emulating the behavior the bot will have when deployed to WhatsApp.

---

## Features
* Advanced Text Processing: Analyzes characters and n-grams, allowing the bot to understand the user even if they make spelling mistakes.
* Flexible Knowledge Base: Responses and training patterns are fully configurable in a structured intents.json file.
* Dynamic Responses: Random selection of predefined answers to make the conversation feel more natural and human.
* Simulation Interface: A web-based chat panel to perform quick real-time testing.

---

## Technologies Used
* Python 3
* Scikit-Learn (TfidfVectorizer and Cosine Similarity)
* NumPy (Numerical processing and random selection)
* Streamlit (Web User Interface)

---

## Project Structure

chatbot-croptops/
│
├── __pycache__/        # Python cached files (automatically generated)
├── venv/               # Virtual environment folder (local libraries)
├── .gitignore          # Files and folders excluded from Git tracking
├── app.py              # Streamlit graphical interface (WhatsApp simulator)
├── chatbot.py          # Main Bot class (Mathematical logic)
├── intents.json        # Database with questions, categories, and answers
├── logo.png            # Brand image logo for NAVARROTEX
├── requirements.txt    # List of project library dependencies
└── README.md           # This instruction manual
