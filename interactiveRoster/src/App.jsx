import { useState, useEffect } from 'react';
import PlayerList from './PlayerList';
import PlayerForm from './PlayerForm';


function App() {
  const [players, setPlayers] = useState([])

  useEffect(() => {
    fetchPlayers()
  }, []);

  const fetchPlayers = async () => {
    const response = await fetch("http://127.0.0.1:5000/players")
    const data = await response.json()
    setPlayers(data.players)
    console.log(data.players)
  };
  return ( <>
  <PlayerList players={players}/>
  <PlayerForm />
  </>
  );
}

export default App
