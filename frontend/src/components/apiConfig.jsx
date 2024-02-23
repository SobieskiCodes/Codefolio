function determineBackendUrl() {
    let backendUrl = 'http://backend:8000';
  
    // Check if we're running in a Codespaces environment
    const codespaceName = import.meta.env.VITE_CODESPACE_NAME;
    if (codespaceName) {
      backendUrl = `https://${codespaceName}-8000.app.github.dev`;
    }
  
    return backendUrl;
  }
  
  export async function tryFetchUrl(endpoint, options = {}) {
    // The `options` parameter will be an object that includes method, headers, body, etc.
  
    const backendUrl = determineBackendUrl();
    const url = `${backendUrl}${endpoint}`;
  
    console.log("Complete URL for fetch:", url);
  
    try {
      // Include the options object in the fetch call
      const response = await fetch(url, options);
      const data = await response.json(); // Always try to parse the JSON to get the detail
  
      if (!response.ok) {
        // If response is not ok, use the parsed JSON to throw an error
        const errorMessage = data.detail || `HTTP error! status: ${response.status}`;
        throw new Error(errorMessage);
      }
      
      console.log('Response data:', data);
      return data; // Return the data for use by the caller
  
    } catch (error) {
      console.error("Failed to fetch:", url, error.message);
      throw error; // Rethrow to allow the caller to handle the error with possibly more context
    }
  }
  
  export default determineBackendUrl;
  