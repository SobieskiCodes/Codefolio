import React, { createContext, useContext, useState, useEffect } from 'react';

const WebSocketContext = createContext();

export const useWebSocket = () => useContext(WebSocketContext);

export const WebSocketProvider = ({ children }) => {
  const [ws, setWs] = useState(null);
  const [messages, setMessages] = useState([]);
  const [isConnected, setIsConnected] = useState(false);
  const [shouldReconnect, setShouldReconnect] = useState(true);

  useEffect(() => {
    let timeoutId = null;

    function connectWebSocket() {
      setIsConnected(false);
      const newWs = new WebSocket("ws://localhost:8050/ws/logs");

      newWs.onopen = () => {
        console.log("Connected to WebSocket server");
        setIsConnected(true);
        setShouldReconnect(true);
      };

      newWs.onmessage = (event) => {
        setMessages((prevMessages) => [...prevMessages, event.data]);
      };

      newWs.onerror = (error) => {
        console.error("WebSocket error observed:", error);
        // TODO: Error handling could be improved by setting an error state and displaying it in the UI
      };

      newWs.onclose = (event) => {
        console.log("WebSocket connection closed", event);
        setIsConnected(false);
        if (shouldReconnect) {
          timeoutId = setTimeout(() => {
            connectWebSocket();
          }, 5000);
        }
      };

      setWs(newWs);
    }

    connectWebSocket();

    return () => {
      setShouldReconnect(false); 
      if (timeoutId) clearTimeout(timeoutId); 
      if (ws) ws.close();
    };
  }, []);

  const sendMessage = (message) => {
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(message);
    }
  };

  const value = { sendMessage, messages, isConnected };

  return (
    <WebSocketContext.Provider value={value}>
      {children}
    </WebSocketContext.Provider>
  );
};
