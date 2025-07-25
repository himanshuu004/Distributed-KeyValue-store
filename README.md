🗃️ Consistent Hashing Based Distributed Key-Value Store
This project demonstrates a simple distributed key-value store using consistent hashing for request routing. It consists of multiple Flask-based storage nodes and a client that routes PUT and GET requests to the appropriate node based on the hashed key.

📂 Project Structure
bash
Copy
Edit
.
├── client.py             # Client script to interact with the distributed system
├── consistent_hash.py    # Consistent hashing logic
├── server.py             # Flask server code for each node
├── Dockerfile            # Docker configuration for each node
├── docker-compose.yml    # Compose file to spin up all nodes


🚀 How It Works
Consistent Hashing: Ensures minimal data movement when nodes are added/removed.

Multiple Nodes: Three Flask servers act as storage nodes.

Client: Uses consistent hashing to determine the appropriate node for each key.

🛠️ Setup Instructions
✅ Prerequisites
Docker

Docker Compose

Python 3.x (for running client.py)

📦 Step 1: Build and Run the Nodes
From your project directory, run:

bash
Copy
Edit
docker-compose up --build
This will start three servers on:

http://localhost:5000

http://localhost:5001

http://localhost:5002

📡 Step 2: Run the Client
In a separate terminal window, run:

bash
Copy
Edit
python client.py
This will:

PUT key-value pairs like ("name", "Praachi") and ("city", "San Francisco")

GET and print their values from the correct node (based on consistent hashing)

📘 Example Output
bash
Copy
Edit
PUT name → http://localhost:5001: {'status': 'success'}
PUT city → http://localhost:5000: {'status': 'success'}
GET name → http://localhost:5001: {'value': 'Praachi'}
GET city → http://localhost:5000: {'value': 'San Francisco'}


🧠 How Consistent Hashing Works
The consistent_hash.py file implements basic consistent hashing:

Each node is hashed and placed on a ring.

A key is routed to the first node hash >= key hash.

Wraps around if no such node exists (circular behavior).

This approach helps with scalability and fault tolerance.

🔧 Customize
You can add more nodes by editing the docker-compose.yml and the nodes list in client.py.

To simulate adding/removing nodes and observing redistribution, extend the hashing to use virtual nodes.

📚 Learn More
Consistent Hashing - Wikipedia

Flask Documentation: https://flask.palletsprojects.com/

Docker Compose Docs: https://docs.docker.com/compose/

🙌 Author
Himanshu Rawat
Email: himanshuu004@gmail.com