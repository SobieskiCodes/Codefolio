import { useState, useEffect, useRef } from 'react';
import { tryFetchUrl } from '../components/apiConfig';

const StoreView = ({ isActiveTab }) => {
  const [stores, setStores] = useState([]);
  const [showCreateStore, setShowCreateStore] = useState(false);
  const [newStoreName, setNewStoreName] = useState('');
  const [creationResponse, setCreationResponse] = useState(null);
  const fetchedRef = useRef(false);

  const fetchStores = () => {
    tryFetchUrl('/api/classwork/store/stores/')
      .then(data => {
        console.log(data)
        if (Array.isArray(data) && data.length === 0) {
          setShowCreateStore(true);
          setStores([]);
        } else {
          setStores(data);
          setShowCreateStore(false);
        }
      })
      .catch(error => {
        console.error('Error fetching stores:', error);
        setCreationResponse(error.message);
        setShowCreateStore(false); 
      });
  };
  
  useEffect(() => {
    if (isActiveTab && !fetchedRef.current) {
      fetchStores();
      fetchedRef.current = true; 
    }
  }, [isActiveTab]);

  const selectStore = (store) => {
    console.log(`Viewing store: ${store.name}`);
    // Maybe set a state here to show the selected store's details
  };

  const deleteStore = async (storeId) => {
    try {
      await tryFetchUrl(`/api/classwork/store/stores/${storeId}`, {
        method: 'DELETE',
        // Additional options if needed
      });
      // Update the UI by filtering out the deleted store
      setStores(prevStores => prevStores.filter(store => store.id !== storeId));
    } catch (error) {
      console.error('Error deleting store:', error);
      // Handle deletion error
    }
  };
  

  const handleCreateStore = async () => {
    const storeData = {
      name: newStoreName,
      balance: 0,  // Assuming the default balance is 0
      is_open: true,  // Assuming you want the new store to be open by default
    };
  
    console.log('Sending store creation request with data:', storeData);  // Debugging log
  
    try {
      const data = await tryFetchUrl('/api/classwork/store/stores/', {
        method: 'POST',
        body: JSON.stringify(storeData),
        headers: {
          'Content-Type': 'application/json',
        },
      });
  
      console.log('Store creation response:', data);  // Debugging log
  
      // If the server returned an object with a name, it likely means the store was created successfully
      if (data && data.name) {
        setCreationResponse(`Store "${data.name}" created successfully.`);
        setNewStoreName('');
        setShowCreateStore(false); // Hide the create store form
        setStores(prevStores => [...prevStores, data]); // Add the new store to the list of stores
      } else {
        // If the data is not in the expected format, show an error message
        setCreationResponse('Unexpected response from server. Store may not have been created.');
      }
    } catch (error) {
      console.error('Error creating store:', error);
      // Display the error message from the server if available, otherwise a generic message
      setCreationResponse(error.response?.data?.detail || 'Error creating store. Please try again.');
    }
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
      {creationResponse && <p>{creationResponse}</p>}
      {stores && stores.length > 0 && (
        <div>
          <h2>Select a Store to View</h2>
          <ul>
            {stores.map((store) => (
              <li key={store.id}>
                {store.name} - Balance: {store.balance} {store.is_open ? 'Open' : 'Closed'}
                <button onClick={() => deleteStore(store.id)}>Delete</button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default StoreView;
