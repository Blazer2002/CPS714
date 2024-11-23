import React from 'react'
import './Rewards.css'
import RewardCard from '../components/RewardCard.js'
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Rewards() {
    const [rewards, setReward] = useState([]);
    const [percentDiscounts, setPercentDiscounts] = useState([]);
    const [priceDiscounts, setPricedDiscounts] = useState([]);
    const [productUpgrades, setProductUpgrade] = useState([]);
    const [exclusiveUpgrades, setExclusiveUpgrade] = useState([]);

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

        fetch('http://localhost:8000/lprs/percentdisccountrewards/get-all/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setPercentDiscounts(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });

        fetch('http://localhost:8000/lprs/pricedisccountrewards/get-all/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setPricedDiscounts(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });

        fetch('http://localhost:8000/lprs/productupgraderewards/get-all/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setProductUpgrade(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });

        fetch('http://localhost:8000/lprs/exclusiveupgraderewards/get-all/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setExclusiveUpgrade(data);
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

    const referenceToReward= (rewardId) => {
        const reward = rewards.find(r => r.reward_id === rewardId);
        if (reward) return reward;
        return null;
    };
    
    return (
        <div className='rewards-container'>
            <div className='banner'>
                <h1>Rewards</h1>
                <button className="transaction-history" onClick={rewardsTransactions}>Reward Transactions</button>
            </div>
            <h2 className='reward-types'>Percent Discount</h2>
            <div className='card-container'>
                {percentDiscounts.length > 0 ? (
                    percentDiscounts.map(percentDiscount => {
                        const reward = referenceToReward(percentDiscount.reward_id);
                        return (reward ? <RewardCard key={reward.reward_id} reward={reward} rewardType={percentDiscount}/> : null)
                    })
                ) : (
                    <p>No rewards available.</p>
                )}
            </div>
            <h2 className='reward-types'>Price Discount</h2>
            <div className='card-container'>
                {priceDiscounts.length > 0 ? (
                    priceDiscounts.map(priceDiscount => {
                        const reward = referenceToReward(priceDiscount.reward_id);
                        return (reward ? <RewardCard key={reward.reward_id} reward={reward} rewardType={priceDiscount}/> : null)
                    })
                ) : (
                    <p>No rewards available.</p>
                )}
            </div>
            <h2 className='reward-types'>Product Upgrade</h2>
            <div className='card-container'>
                {productUpgrades.length > 0 ? (
                    productUpgrades.map(productUpgrade => {
                        const reward = referenceToReward(productUpgrade.reward_id);
                        return (reward ? <RewardCard key={reward.reward_id} reward={reward} rewardType={productUpgrade}/> : null)
                    })
                ) : (
                    <p>No rewards available.</p>
                )}
            </div>
            <h2 className='reward-types'>Exclusive Upgrade</h2>
            <div className='card-container'>
                {exclusiveUpgrades.length > 0 ? (
                    exclusiveUpgrades.map(exclusiveUpgrade => {
                        const reward = referenceToReward(exclusiveUpgrade.reward_id);
                        return (reward ? <RewardCard key={reward.reward_id} reward={reward} rewardType={exclusiveUpgrade}/> : null)
                    })
                ) : (
                    <p>No rewards available.</p>
                )}
            </div>
        </div>
        
    );
}

export default Rewards;