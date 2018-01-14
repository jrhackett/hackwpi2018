
// Open a socket for Player Moved updates
var playerMovedSocket = new WebSocket("ws://localhost:8888/player_moved_ws");

// Callback for successful connection
playerMovedSocket.onopen = function() {
   playerMovedSocket.send("UI Listening For Player Moved Updates");
   console.log("Connected to socket, listening for Player Moved updates.")
};

// Callback for receiving new message
playerMovedSocket.onmessage = function(message) {
    // TODO write to DOM
	console.log(message);
};

// Open a socket for Tile Exhausted updates
var tileExhaustedSocket = new WebSocket("ws://localhost:8888/tile_exhausted_ws");

tileExhaustedSocket.onopen = function() {
    tileExhaustedSocket.send("UI Listening For Tile Exhausted Updates");
    console.log("Connected to socket, listening for Tile Exhausted updates.")
};

tileExhaustedSocket.onmessage = function(message) {
    // TODO write to DOM
    console.log(message);
};
