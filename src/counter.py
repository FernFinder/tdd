from flask import Flask
from src import status

app = Flask(__name__)

COUNTERS = {}

# We will use the app decorator and create a route called slash counters.
# specify the variable in route <name>
# let Flask know that the only methods that is allowed to called
# on this function is "POST".


@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


@app.route('/counters/<name>', methods=['PUT'])
def update_counter(name):
    """Update a Counter"""
    app.logger.info(f"Request to update a counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        COUNTERS[name] = COUNTERS[name] + 1
        return {name: COUNTERS[name]}, status.HTTP_200_OK
    return {"Message": f"Counter {name} found"}, status.HTTP_404_NOT_FOUND


@app.route('/counters/<name>', methods=['GET'])
def get_counter(name):
    """Get a Counter"""
    app.logger.info(f"Request to get a counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {name: COUNTERS[name]}, status.HTTP_200_OK
    return {"Message": f"Counter {name} found"}, status.HTTP_404_NOT_FOUND


@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter(name):
    """Delete a Counter"""
    app.logger.info(f"Request to delete a counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        del COUNTERS[name]
        return {"Message": f"Counter {name} deleted"}, status.HTTP_200_OK
    return {"Message": f"Counter {name} not found"}, status.HTTP_204_NO_CONTENT
