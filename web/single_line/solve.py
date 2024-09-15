#!/usr/bin/env python3

import json
import requests
import networkx

url = "http://localhost:8080"

def graph_has_eulerian_path(segments):
    graph = networkx.Graph()
    graph.add_edges_from([
        [tuple(s[0]), tuple(s[1])]
        for s in segments
    ])

    return networkx.has_eulerian_path(graph)

session = requests.Session()
r = session.post(url)

while True:
    if "Step" not in r.text:
        print(r.text)
        break
    raw = r.text.split(':')[1].split('\n')[0]
    draw = json.loads(raw)
    if graph_has_eulerian_path(draw):
        r = session.post(url, data={'oneline_drawable': 'Yes'})
    else:
        r = session.post(url, data={'oneline_drawable': 'No'})

