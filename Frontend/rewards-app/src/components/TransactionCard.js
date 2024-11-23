import React from 'react';
import './TransactionCard.css';
import { useState, useEffect } from 'react';
import TransactionPopup from '../view/TransactionPopup';
import formatDate from '../utility';

function TransactionCard( { transaction, active } ) {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [reward, setFetchReward] = useState(null);
    const [showTransactionPopup, setShowTransactionPopup] = useState(false);

    useEffect(() => {
        fetch(`http://localhost:8000/lprs/rewards/${transaction.reward_id}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(rewardData => {
                setFetchReward(rewardData);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });
    }, [transaction]);

    if (loading) {
        console.log('Loading reward details');
    }

    if (error) {
        console.log('Error loading reward details');
    }

    return (
        <div className="transaction-card" >
            <div className="transaction-image">
                {transaction.image ? (
                    <img src={transaction.image} alt="Reward Image" />
                ) : (
                    <div className="no-image">No Image</div>
                )}
            </div>
            <div className='transaction-info'>
                <h3>#{transaction.transaction_id}: {transaction.title}</h3>
                <p>Transaction Date: {formatDate(transaction.date)}</p>
                {reward ? (
                    active ? (
                        <p>End date: {reward.end ? formatDate(transaction.date) : 'Ongoing'}</p>
                    ) : ( 
                        console.log('Inactive Transaction')
                    )
                ) : (
                    console.log('Loading rewards data')
                )}
            </div>
            {active && (
                <button className="redemption-button" onClick={() => setShowTransactionPopup(true)}>Redeem</button>
            )}
            {showTransactionPopup && reward && (
                <TransactionPopup
                    transaction={transaction}
                    reward={reward}
                    isOpen={showTransactionPopup}
                    onClose={() => setShowTransactionPopup(false)}
                />
            )}
        </div>
    );
};

export default TransactionCard;