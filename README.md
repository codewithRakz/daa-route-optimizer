🚀 Smart Route Optimizer

📌 Project Overview

The Smart Route Optimizer is an AI-based web application that determines the most efficient route between two locations using graph algorithms. It intelligently computes the shortest and fastest path by considering both distance and real-time traffic conditions.

This project demonstrates the practical implementation of Design and Analysis of Algorithms (DAA) concepts in real-world navigation systems.

🧠 Algorithms Used
🟢 Dijkstra’s Algorithm – Finds the shortest path based on minimum cost (distance)
🔵 A Search Algorithm* – Optimized pathfinding using heuristic estimation for faster results

⚙️ Key Features
📍 Graph-based route modeling system
🚦 Dynamic traffic simulation for realistic path calculation
🧮 Shortest path computation using multiple algorithms
🌐 Interactive web-based UI using Flask
🔄 Option to compare Dijkstra vs A* results
⚡ Fast and efficient route optimization

💻 Technologies Used
Python 🐍
Flask 🌐
HTML5 / CSS3 🎨
Data Structures (Graphs, Priority Queue) 📊

📂 Project Structure
project-root/
│
├── app.py              # Main Flask application
├── main.py             # Script runner / testing file
├── graph.py            # Graph data structure implementation
├── dijkstra.py        # Dijkstra algorithm implementation
├── astar.py           # A* algorithm implementation
├── traffic.py         # Traffic simulation logic
├── ui.py              # UI helper functions
├── templates/         # HTML templates
├── requirements.txt   # Dependencies
└── Procfile           # Deployment configuration

▶️ How to Run the Project
🔧 Step 1: Install dependencies
pip install flask
🚀 Step 2: Run the application
python app.py
🌐 Step 3: Open in browser


🌍 Live Demo

👉 https://daa-route-optimizer--rakshitha110107.replit.app

📊 Learning Outcomes
Implementation of graph algorithms in real-world problems
Understanding of shortest path optimization techniques
Integration of backend logic with web UI
Basics of web deployment using Flask

⭐ Future Enhancements
Google Maps API integration
Real-time live traffic data
Mobile application version
Multiple route suggestions
