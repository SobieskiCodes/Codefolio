import React, { useState } from 'react';
import products from '../../../components/fishbone/products';
import Product from '../../../components/fishbone/product';
import ShoppingCart from '../../../components/fishbone/ShoppingCart';
import './FishboneAquatics.css';

const FishboneAquatics = () => {
  const [cartItems, setCartItems] = useState([]);
  const [isCartVisible, setIsCartVisible] = useState(false);

  const handleAddToCart = (product) => {
    const exist = cartItems.find((item) => item.id === product.id);
    if (exist) {
      setCartItems(
        cartItems.map((item) =>
          item.id === product.id ? { ...exist, quantity: exist.quantity + 1 } : item
        )
      );
    } else {
      setCartItems([...cartItems, { ...product, quantity: 1 }]);
    }
  };

  const handleRemoveFromCart = (product) => {
    const exist = cartItems.find((item) => item.id === product.id);
    if (exist.quantity === 1) {
      setCartItems(cartItems.filter((item) => item.id !== product.id));
    } else {
      setCartItems(
        cartItems.map((item) =>
          item.id === product.id ? { ...exist, quantity: exist.quantity - 1 } : item
        )
      );
    }
  };

  const toggleCart = () => {
    setIsCartVisible(!isCartVisible);
  };

  const getTotalItemsInCart = () => {
    return cartItems.reduce((total, item) => total + item.quantity, 0);
  };

  return (
    <div className="fishbone">
      {!isCartVisible && (
        <>
          <h1>Fishbone Aquatics</h1>
          <div className="products">
            {products.map((product) => (
              <Product
                key={product.id}
                product={product}
                onAdd={handleAddToCart}
                onRemove={handleRemoveFromCart}
              />
            ))}
          </div>
        </>
      )}
      {isCartVisible && (
        <div className="shopping-cart-display">
          <ShoppingCart
            cartItems={cartItems}
            onAdd={handleAddToCart}
            onRemove={handleRemoveFromCart}
            onClose={toggleCart}
          />
        </div>
      )}
      {!isCartVisible && (
        <div className='toggle-cart'>
          <button onClick={toggleCart}>
            <img src="images/cart.svg" alt="Cart" />
            Cart ({getTotalItemsInCart()})
          </button>
        </div>
      )}
    </div>
  );
};

export default FishboneAquatics;
