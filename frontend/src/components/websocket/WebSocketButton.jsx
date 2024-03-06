import React from 'react';
import { useWebSocket } from './WebSocketProvider'; 

export const WebSocketButton = () => {
  const { sendMessage } = useWebSocket();

  return (
    <button onClick={() => sendMessage('Hello from WebSocketButton')}>Send Message</button>
  );
};
