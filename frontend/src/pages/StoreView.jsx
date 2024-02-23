import { useState, useEffect } from 'react';
import { tryFetchUrl } from '../components/apiConfig';

const StoreView = ({ isActiveTab }) => {
  const [stores, setStores] = useState([]);
  const [showCreateStore, setShowCreateStore] = useState(false);
  const [newStoreName, setNewStoreName] = useState('');
  const [creationResponse, setCreationResponse] = useState(null);

  useEffect(() => {
    if (isActiveTab) {
      tryFetchUrl('/api/classwork/store/stores/')
        .then(data => {
          if (data.detail === "No stores found") {
            setShowCreateStore(true);
            setStores([]);
          } else {
            setStores(data);
          }
        })
        .catch(error => {
          console.error('Error fetching stores:', error);
          setCreationResponse(error.message);
        });
    }
  }, [isActiveTab]);


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
          <button onClick={console.log('create store clicked')}>Create Store</button>
        </div>
      )}
      {/* Display success or failure notice <button onClick={handleCreateStore}>Create Store</button>*/}
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
