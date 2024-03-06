import React, { useEffect } from 'react';
import { useWebSocket } from '../components/websocket/WebSocketProvider';
import { WebSocketButton } from '../components/websocket/WebSocketButton';

const WebSocketComponent = () => {
  const { isConnected } = useWebSocket();

  return (
    <div>
      {isConnected ? (
        <WebSocketButton />
      ) : (
        <div>Not connected to WebSocket server.</div>
      )}
      {/* ... more component parts could go here ... */}
    </div>
  );
};

export default WebSocketComponent;