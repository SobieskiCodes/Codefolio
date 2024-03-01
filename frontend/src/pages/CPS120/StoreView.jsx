import { useState, useEffect, useRef } from 'react';
import { tryFetchUrl } from '../../components/apiConfig';
import PropTypes from 'prop-types';


const StoreView = ({ isActiveTab }) => {
  const [stores, setStores] = useState([]);
  const [newStoreName, setNewStoreName] = useState('');
  const [creationResponse, setCreationResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(true); 
  const fetchedRef = useRef(false);
  const [fetchError, setFetchError] = useState(false); 

  StoreView.propTypes = {
    isActiveTab: PropTypes.bool.isRequired
  };

  const fetchStores = () => {
    setIsLoading(true); 
    tryFetchUrl('/api/classwork/store/stores/')
      .then(data => {
        console.log(data);
        setStores(data || []);
        setIsLoading(false); 
        setFetchError(false); 
      })
      .catch(error => {
        console.error('Error fetching stores:', error);
        setCreationResponse(error.message);
        setIsLoading(false); 
        setFetchError(true); 
      });
  };
  
  useEffect(() => {
    if (isActiveTab && !fetchedRef.current) {
      fetchStores();
      fetchedRef.current = true; 
    }
  }, [isActiveTab]);

  const deleteStore = async (storeId) => {
    try {
      await tryFetchUrl(`/api/classwork/store/stores/${storeId}`, {
        method: 'DELETE',
      });
      setStores(prevStores => prevStores.filter(store => store.id !== storeId));
    } catch (error) {
      console.error('Error deleting store:', error);
    }
  };
  
  const handleCreateStore = async () => {
    if (!newStoreName.trim()) {
      setCreationResponse("Store name cannot be empty.");
      return;
    }

    const storeData = {
      name: newStoreName.trim(),
      balance: 0,
      is_open: true,
    };
  
    try {
      const data = await tryFetchUrl('/api/classwork/store/stores/', {
        method: 'POST',
        body: JSON.stringify(storeData),
        headers: {
          'Content-Type': 'application/json',
        },
      });
  
      if (data && data.store) {
        setCreationResponse(`Store "${data.store.name}" created successfully.`);
        setNewStoreName('');
        setStores(prevStores => [...prevStores, data.store]);
      } else {
        setCreationResponse('Unexpected response from server. Store may not have been created.');
      }      
    } catch (error) {
      console.error('Error creating store:', error);
      setCreationResponse(error.response?.data?.detail || 'Error loading stores. Please try again later.');
    }
  };
  
  return (
    <div className="store-view">
      {isLoading ? (
        <p>Loading stores...</p>
      ) : fetchError ? (
        <p>It looks like there was an error connecting to the database. Please try again later.</p>
      ) : (
        <>
          <div>
            <p>Add a new store:</p>
            <input
              type="text"
              value={newStoreName}
              onChange={(e) => setNewStoreName(e.target.value)}
              placeholder="Enter store name"
            />
            <button onClick={handleCreateStore}>Create Store</button>
          </div>
          {creationResponse && <p>{creationResponse}</p>}
          {stores && stores.length > 0 && (
            <div>
              <h2>Select a Store to View</h2>
              <ul>
                {stores.map((store) => (
                  <li key={store.id}>
                    ID: {store.id}, {store.name} - Balance: {store.balance} {store.is_open ? 'Open' : 'Closed'}
                    <button onClick={() => deleteStore(store.id)}>Delete</button>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </>
      )}
    </div>
  );
}

export default StoreView;