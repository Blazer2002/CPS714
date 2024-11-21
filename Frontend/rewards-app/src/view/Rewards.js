import React from 'react'
import './Rewards.css'
import RewardCard from '../components/RewardCard.js'
import { useEffect, useState } from 'react';

function Rewards() {
    const [rewards, setReward] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

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
        return <p>Loading rewards...</p>;
    }

    if (error) {
        return <p>Error loading rewards from api: {error}</p>;
    }

    return (
        <div className='rewards-container'>
            <div className='banner'>
                <h1>Rewards</h1>
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