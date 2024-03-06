import React, { useState } from 'react';

const ShoppingCart = ({ cartItems, onAdd, onRemove, onClose }) => {
  const [commissionPercentage, setCommissionPercentage] = useState(0);
  const totalPrice = cartItems.reduce((acc, item) => acc + item.quantity * item.price, 0);
  const commission = (totalPrice * commissionPercentage) / 100;

  return (
    <div className="shopping-cart">
      <div className="cart-header">
        <button className="close-button" onClick={onClose}>Close</button>
      </div>
      {cartItems.map((item) => (
        <div key={item.id} className="cart-item">
          <span className="item-name">{item.name}</span>
          <span className="item-price">${item.price} x {item.quantity}</span>
          <span className="item-controls">
            <button onClick={() => onRemove(item)}>-</button>
            <button onClick={() => onAdd(item)}>+</button>
          </span>
        </div>
      ))}
      <div className="totals">
        <select
          className="commission-select"
          value={commissionPercentage}
          onChange={(e) => setCommissionPercentage(e.target.value)}
        >
          {Array.from({ length: 101 }, (_, i) => (
            <option key={i} value={i}>{i}%</option>
          ))}
        </select>
        <div className="commission-display">
          Commission: ${commission.toFixed(2)}
        </div>
        <div className="total-price">Total Price: ${totalPrice.toFixed(2)}</div>
      </div>
    </div>
  );
};

export default ShoppingCart;
