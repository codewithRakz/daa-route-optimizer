from flask import Flask, render_template, request
from graph import Graph
from dijkstra import dijkstra
from traffic import apply_traffic
from astar import astar, get_path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find():
    start = request.form['start']
    end = request.form['end']

    g = Graph()
    g.add_edge("Hostel", "College", 5)
    g.add_edge("College", "Hospital", 3)
    g.add_edge("Hostel", "Mall", 10)
    g.add_edge("Mall", "Hospital", 4)

    traffic_graph = apply_traffic(g)

    distances, came_from = astar(traffic_graph, start, end)
    path = get_path(came_from, start, end)

    return render_template('index.html',
                           path=" -> ".join(path),
                           distance=distances[end])

if __name__ == '__main__':
    app.run(debug=True)