# To run the MCP Server and test it on the browser
fastmcp dev inspector server.py

# To run the client and talk to server
python client.py

This is one of the most common points of confusion when first working with the Model Context Protocol (MCP)!

When you use the **stdio (Standard Input/Output) transport layer**, the client and the server cannot talk to each other over the network (like a traditional website running on `localhost:5173`). Instead, they communicate by passing text directly to each other via terminal inputs and outputs.
Because of this, the client must start its own dedicated instance of the server as a background process [11/05/26 17:22:18].

Here is how the setup works:

1. Your current running server terminal: The script you started manually with `fastmcp dev` or `python server.py` is locked to that specific terminal session or the web browser developer dashboard. Other standalone Python scripts cannot reach into that terminal to talk to it.

2. The client script: When you run `python client.py`, the client reads that line of code, looks up where `server.py` is, and **spins up a fresh, private copy of the server** in the background just for itself. It then pipes commands directly into that fresh process.

