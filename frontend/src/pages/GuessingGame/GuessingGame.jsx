import React, { useState } from 'react';
import './GuessingGame.css';

const initialGameState = () => ({
  id: Math.floor(Math.random() * 1000),
  low: 1,
  high: 100,
  guess: 50,
  guessesTaken: 0,
  message: '',
  history: [],
});

const GuessingGame = () => {
  const [game, setGame] = useState(initialGameState);

// Function to handle the "High" response
const handleHigh = () => {
  setGame((prevGame) => {
    const newHigh = prevGame.guess - 1;
    const newGuess = Math.floor((prevGame.low + newHigh) / 2);
    return {
      ...prevGame,
      high: newHigh,
      guess: newGuess,
      guessesTaken: prevGame.guessesTaken + 1,
      history: [...prevGame.history, prevGame.guess],
      message: `I think your number is ${newGuess}, am I low, high, or correct?`,
    };
  });
};

// Function to handle the "Low" response
const handleLow = () => {
  setGame((prevGame) => {
    const newLow = prevGame.guess + 1;
    const newGuess = Math.floor((newLow + prevGame.high) / 2);
    return {
      ...prevGame,
      low: newLow,
      guess: newGuess,
      guessesTaken: prevGame.guessesTaken + 1,
      history: [...prevGame.history, prevGame.guess],
      message: `I think your number is ${newGuess}, am I low, high, or correct?`,
    };
  });
};

// Function to handle the "Correct" response
const handleCorrect = () => {
  setGame((prevGame) => {
    const guesses = prevGame.guessesTaken + 1;
    return {
      ...prevGame,
      guessesTaken: guesses,
      message: `Congratulations to myself, I got the answer in ${guesses} guesses.`,
    };
  });
};

  // Function to determine if the game has ended
  const hasGameEnded = () => {
    return game.message.includes('Correct!');
  };
  
  
  // Function to restart the game
  const restartGame = () => {
    setGame(initialGameState());
  };

  return (
    <div className="game-container">
      <div className="guess-history">
        {game.history.map((entry, index) => (
          <div key={index} className="guess-box">{entry}</div>
        ))}
        {/* Render the current guess only if the game has not ended */}
        {!hasGameEnded() && (
          <div className="guess-box current-guess">{game.guess}</div>
        )}
      </div>
      
      <p className="game-message">{game.message}</p>

      <div className="interactive-buttons">
        <div className="button high-button" onClick={handleHigh}>High</div>
        <div className="button low-button" onClick={handleLow}>Low</div>
        <div className="button correct-button" onClick={handleCorrect}>Correct</div>
      </div>

  
      {hasGameEnded() && (
        <div className="button play-again-button" onClick={restartGame}>Play Again</div>
      )}
    </div>
  );
  
};

export default GuessingGame;
