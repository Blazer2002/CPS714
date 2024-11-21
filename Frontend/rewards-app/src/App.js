import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Home from './view/Home'
import Rewards from './view/Rewards'
import RewardDetails from './view/RewardDetails';

function App() {
  return (
    <Router>
      <Sidebar />
      <div className='content_container'>
        <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/rewards' element={<Rewards />} />
        <Route path='/rewards/:reward_id' element={<RewardDetails />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
