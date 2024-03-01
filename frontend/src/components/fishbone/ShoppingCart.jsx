// src/ShoppingCart.js
import React from 'react';

const ShoppingCart = ({ cartItems, onAdd, onRemove, onClose }) => {
  const totalPrice = cartItems.reduce((acc, item) => acc + item.quantity * item.price, 0);

  return (
    <div className="shopping-cart">
      <button onClick={onClose}>Close</button>
      {cartItems.map((item) => (
        <div key={item.id}>
          <h3>{item.name}</h3>
          <p>
            ${item.price} x {item.quantity}
          </p>
          <button onClick={() => onRemove(item)}>-</button>
          <button onClick={() => onAdd(item)}>+</button>
        </div>
      ))}
      <div>Total Price: ${totalPrice.toFixed(2)}</div>
    </div>
  );
};

export default ShoppingCart;
