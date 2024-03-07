chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
  if (changeInfo.url) {
    const hostname = new URL(changeInfo.url).hostname;
    if (hostname.includes('localhost')) {
      try {
        const ws = new WebSocket('ws://localhost:8050/ws/logs');
        ws.onopen = () => {
          console.log('WebSocket connection established to localhost');
          startHeartbeat(ws);
        };
        ws.onclose = () => {
          console.log('WebSocket connection closed');
        };
        ws.onerror = (error) => console.log('WebSocket error:', error);
        ws.onmessage = (message) => {
          console.log('WebSocket message:', message.data);
          // Here you can handle incoming messages, such as a response to your heartbeat
          if (message.data === 'pong') {
            console.log('Heartbeat pong received');
          }
        };
      } catch (error) {
        console.error('Failed to create WebSocket connection:', error);
      }
    }
  }
});

function startHeartbeat(ws) {
  const heartbeatInterval = 30000; // 30 seconds
  const heartbeatMsg = 'ping';
  setInterval(() => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.send(heartbeatMsg);
      console.log('Heartbeat ping sent');
    }
  }, heartbeatInterval);
}
