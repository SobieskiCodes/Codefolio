import React from 'react';
import { useWebSocket } from './WebSocketProvider'; 

export const WebSocketStatusComponent = () => {
  const { isConnecting } = useWebSocket();

  if (isConnecting) {
    return <div>Connecting to the server...</div>;
  }

  return null; // or some other UI element when not connecting
};
