# from flask import Flask, request, jsonify
# from threading import Thread
# from dispatcher import dispatch_query
# from voice import get_voice_input, speak

# app = Flask(__name__)

# @app.route('/ask', methods=['POST'])
# def ask():
#     query = request.json.get('query')
#     response = dispatch_query(query)
#     return jsonify({'response': response})

# def run_voice_interaction():
#     # Main loop for voice interaction
#     while True:
#         query = get_voice_input().lower()
#         if query == "none":
#             continue
#         response = dispatch_query(query)
#         print(f"Assistant: {response}")
#         speak(response)

# if __name__ == '__main__':
#     # Start the voice interaction in a separate thread
#     voice_thread = Thread(target=run_voice_interaction)
#     voice_thread.start()
    
#     # Run the Flask app in the main thread
#     app.run(debug=True)
from dispatcher import dispatch_query
from voice import get_voice_input, speak
import threading
import queue

# Queue to communicate between threads
response_queue = queue.Queue()

# Function to process the query and put the response in the queue
def process_query(query):
    response = dispatch_query(query)
    response_queue.put(response)

# Function to handle the voice interaction
def run_voice_interaction():
    while True:
        query = get_voice_input().lower()
        if query == "none":
            continue

        # Create a thread to process the query
        threading.Thread(target=process_query, args=(query,)).start()

        # Retrieve the response from the queue and speak it
        while True:
            try:
                response = response_queue.get(timeout=5)
                print(f"Assistant: {response}")
                speak(response)
                break
            except queue.Empty:
                continue

if __name__ == '__main__':
    # Start the voice interaction loop
    run_voice_interaction()
