import { useState } from 'react';
import './GuessingGame.css';
/* 
I'd like to add a connection to the existing database and have a way to view a history / previous game table within the "game".
When a game completes it gets added to the database which can then be viewed in the table. (spoiler alert, the debug panel)

Thoughts for myself: Perhaps this would allow me to utilize an actual component that's not a page. 
Thus it can *doh* be reused in the pages, dealing with database connection issues / alerts / bypassing etc.
*/
const initialGameState = () => ({
  id: Math.floor(Math.random() * 1000),
  low: 1,
  high: 100,
  guess: 50,
  guessesTaken: 0,
  message: `I think your number is 50, am I low, high, or correct?`,
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
        history: [],
      };
    });
  };

  const hasGameEnded = () => {
    return game.message.includes('Congratulations');
  };

  const restartGame = () => {
    setGame(initialGameState());
  };

  return (
    <div className="game-container">
      {!hasGameEnded() && (
        <>
          <div className="guess-history">
            {game.history.map((entry, index) => (
              <div key={index} className="guess-box">{entry}</div>
            ))}
            <div className="guess-box current-guess">{game.guess}</div>
          </div>
          <div className="game-message-box">
            <p className="game-message">{game.message}</p>
          </div>
          <div className="interactive-buttons">
            <div className="button high-button" onClick={handleHigh}>High</div>
            <div className="button low-button" onClick={handleLow}>Low</div>
            <div className="button correct-button" onClick={handleCorrect}>Correct</div>
          </div>
        </>
      )}
      {hasGameEnded() && (
        <>
          <div className="game-message-box">
            <p className="game-message">{game.message}</p>
          </div>
          <div className="button play-again-button" onClick={restartGame}>Play Again</div>
        </>
      )}
    </div>
  );
};

export default GuessingGame;