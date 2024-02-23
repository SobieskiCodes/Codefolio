function determineBackendUrl() {
    let backendUrl = 'http://backend:8000';
  
    // Check if we're running in a Codespaces environment
    const codespaceName = import.meta.env.VITE_CODESPACE_NAME;
    if (codespaceName) {
      backendUrl = `https://${codespaceName}-8000.app.github.dev`;
    }
  
    return backendUrl;
  }
  
  export async function tryFetchUrl(endpoint) {
    const headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');
  
    const backendUrl = determineBackendUrl();
    const url = `${backendUrl}${endpoint}`;
  
    console.log("Complete URL for fetch:", url);
  
    try {
      const response = await fetch(url, { headers });
      const data = await response.json(); // Always try to parse the JSON to get the detail
  
      if (!response.ok) {
        // If response is not ok, use the parsed JSON to throw an error
        // Assuming the server sends back an object with a "detail" property
        const errorMessage = data.detail || `HTTP error! status: ${response.status}`;
        throw new Error(errorMessage);
      }
      
      console.log(data);
      return data; // Return the data for use by the caller
    } catch (error) {
      console.error("Failed to fetch:", error.message);
      throw error; // Rethrow to allow the caller to handle the error with possibly more context
    }
  }
  
  export default determineBackendUrl;
  