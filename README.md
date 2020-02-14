# socket_demo
Simple demo program to introduce a friend to sockets

Demo pulled from [Nischaya Sharma's Answer on StackOverflow](https://stackoverflow.com/a/53536336), updated a little bit for formatting and to work with Python3.

# To Run:
1. Get the code on your machine. (Clone the repo, copy and paste, whatever.)
2. Open up your terminal and run the server. (`python3 server.py`)
3. Open up another terminal window and run the client. (`python3 client.py`)
4. Send messages back and forth.
  * Disconnect a client by typing `bye` from the client's terminal.
  * Close the server by typing `bye` from the server's terminal. (This will ruin the fun for the clients.)
  
This demo's hardcoded for a single port on a single IP, but feel free to test things out with multiple machines, IPs, etc.
See what happens if you try to run the client before the server. Maybe play with it and make the server has some specific responses given some specific commands.
