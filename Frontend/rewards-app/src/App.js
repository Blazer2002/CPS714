import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Home from './view/Home'
import Rewards from './view/Rewards'
import RewardDetails from './view/RewardDetails';
import Transactions from './view/Transactions';
import { useState, useEffect } from 'react';

function App() {
  /* user_id defined for testing */
  const user_id = 1;

  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  /* user info should be fetched outside of the reward system, with its data passed as a parameter */
  useEffect(() => {
    fetch(`http://localhost:8000/lprs/users/${user_id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch user data');
            }
            return response.json();
        })
        .then(userData => {
            setUser(userData);
        })
        .catch(error => {
            setError(error.message);
            setLoading(false);
        });
  }, [user_id]);

  if (loading) {
      console.log("Loading user details");
  }

  if (error) {
      return <p>Error loading user details: {error}</p>;
  }

  return (
    <Router>
      <Sidebar />
      <div className='content_container'>
        <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/rewards' element={<Rewards />} />
        <Route path='/rewards/:reward_id' element={<RewardDetails user={user}/>} />
        <Route path='/rewards/transactions' element={<Transactions user={user}/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
