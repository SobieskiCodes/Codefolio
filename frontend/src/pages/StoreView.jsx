// StoreView.jsx
import { useState, useEffect } from 'react';

let headers = new Headers();
headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');

const StoreView = () => {
  const [stores, setStores] = useState([]);
  const [showCreateStore, setShowCreateStore] = useState(false);
  const [newStoreName, setNewStoreName] = useState('');
  const [creationResponse, setCreationResponse] = useState(null);

  useEffect(() => {
    const codespaceName = import.meta.env.VITE_CODESPACE_NAME;
    const backend_url = `https://${codespaceName}-8000.app.github.dev`
    console.log("backend_url:", backend_url)
    fetch(`${backend_url}/api/classwork/store/stores/`, headers=headers)
      .then(response => {
        // Check for a 404 status code
        if (response.status === 404) {
          return response.json().then(data => {
            if (data.detail === "No stores found") {
              setShowCreateStore(true);
            }
          });
        } else if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        } else {
          return response.json();
        }
      })
      .then(data => {
        if (data && !showCreateStore) {
          setStores(data);
        }
      })
      .catch(error => {
        console.error('Error fetching data: ', error);
        setCreationResponse(error.message);
      });
  }, []);

  const handleCreateStore = () => {
    const storeData = {
      name: newStoreName,
      balance: 0,
      is_open: true,
    };

    fetch(`${backend_url}/api/classwork/store/stores/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(storeData),
    })
      .then((response) => {
        if (response.status === 201) {
          // Store creation was successful
          return response.json().then((data) => {
            setCreationResponse(`Store "${data.store.name}" created successfully.`);
            setNewStoreName(''); // Clear the input field
            // You can also update your list of stores if needed
          });
        } else if (!response.ok) {
          // Handle other error statuses here if needed
          throw new Error('Store creation failed.');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        setCreationResponse('Store creation failed.');
      });
  };

  return (
    <div className="store-view">
      {showCreateStore && (
        <div>
          <p>No stores exist. Would you like to create one?</p>
          <input
            type="text"
            value={newStoreName}
            onChange={(e) => setNewStoreName(e.target.value)}
            placeholder="Enter store name"
          />
          <button onClick={handleCreateStore}>Create Store</button>
        </div>
      )}

      {/* Display success or failure notice */}
      {creationResponse && <p>{creationResponse}</p>}

      {stores && stores.length > 0 && (
        <ul>
          {stores.map((store) => (
            <li key={store.id}>
              {store.name} - Balance: {store.balance} {store.is_open ? 'Open' : 'Closed'}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default StoreView;