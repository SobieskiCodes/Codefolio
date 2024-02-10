import React, { useState } from 'react';

const gameState = (id) => {
  const _generateWinningNumber = () => {
    return Math.floor(Math.random() * 100);
  };

  return {
    id: id,
    winningNumber: _generateWinningNumber(),
    numberOfGuessesTaken: 0,
    numberOfGuessesAllowed: 10,
    wins: 0,
  };
};

const GuessingGame = () => {
  const [game, setGame] = useState(gameState(Math.floor(Math.random() * 100)));
  const [userInput, setUserInput] = useState("");
  
  const handleChange = (e) => {
    setUserInput(e.target.value);
  };

  const handleGuess = () => {
    const newGuessesTaken = game.numberOfGuessesTaken + 1;

    setGame({
      ...game,
      numberOfGuessesTaken: newGuessesTaken,
    });
    setUserInput("");
  };

  return (
    <div>
      <p>ID: {game.id}</p>
      <p>Winning Number: {game.winningNumber}</p>
      <p>The game currently allows for a total of {game.numberOfGuessesAllowed} guesses.</p>
      <p>You have taken {game.numberOfGuessesTaken} guesses.</p>
      <p>You are allowed {game.numberOfGuessesAllowed - game.numberOfGuessesTaken} more guesses.</p>
      <p>
        Guess a number 1-100.{' '}
        <input
          name="gameGuessInput"
          value={userInput}
          onChange={handleChange}
          placeholder="Enter your guess"
        />
        <button onClick={handleGuess}>Guess</button>
      </p>
      <p>Your current guess is: {userInput}</p>
      <p>Wins: {game.wins}</p>
    </div>
  );
};

export default GuessingGame;
