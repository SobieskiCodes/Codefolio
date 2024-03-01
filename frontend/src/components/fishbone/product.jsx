import React from 'react';

const Product = ({ product, onAdd, onRemove }) => {
  return (
    <div className="product">
      <img src={product.image} alt={product.name} style={{ width: '200px', height: '200px' }} />
      <h3>{product.name}</h3>
      <p>${product.price}</p>
      <div className="controls">
        <button onClick={() => onRemove(product)}>-</button>
        <button onClick={() => onAdd(product)}>+</button>
      </div>
    </div>
  );
};

export default Product;
