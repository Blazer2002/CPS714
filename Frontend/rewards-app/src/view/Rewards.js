import React from 'react'
import './Rewards.css'
import RewardCard from '../components/RewardCard.js'
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Rewards() {
    const [rewards, setReward] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const navigate = useNavigate();
    
    const rewardsTransactions = () => {
        navigate('/rewards/transactions');
    };

    useEffect(() => {
        fetch('http://localhost:8000/lprs/rewards/get-all/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setReward(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });
    }, []);

    if (loading) {
        console.log("Loading rewards...")
    }

    if (error) {
        return <div>Error loading rewards from api: {error}</div>;
    }

    
    return (
        <div className='rewards-container'>
            <div className='banner'>
                <h1>Rewards</h1>
                <button className="transaction-history" onClick={rewardsTransactions}>Reward Transactions</button>
            </div>
            <div className='search-filter'>
                <button className="percent-discount-button">Percent Discount</button>
                <button className="priced-discount-button">Priced Discount</button>
                <button className="exclusive-upgrade-button">Exclusive Upgrade</button>
                <button className="product-upgrade-button">Product Upgrade</button>
            </div>
            <div className='card-container'>
                {rewards.length > 0 ? (
                    rewards.map(reward => (
                        <RewardCard key={reward.reward_id} reward={reward}/>
                    ))
                ) : (
                    <p>No rewards available.</p>
                )}
            </div>
        </div>
        
    );
}

export default Rewards;