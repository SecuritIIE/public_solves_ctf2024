The trick here is to understand if the given points form a graph that has an eulerian path, which means that there is a path that visits every edge exactly once (Possible to trace a single line without lifting the pen).

Using the script called solve.py we can check if each graph has an eulerian path and automate the process of submitting Yes or No to the server for each graph.

Luckily, the networkx library has a function that checks if a graph has an eulerian path, so we can use it to solve this problem.