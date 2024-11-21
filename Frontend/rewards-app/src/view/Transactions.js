import React from 'react';
import './Transactions.css';
import './RewardDetails.css';

import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import TransactionPopup from './TransactionPopup';

function Transactions() {
    const { transaction_id } = useParams(); // Corrected typo here
    const [transactions, setTransactions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [showTransactionPopup, setShowTransactionPopup] = useState(false);

    useEffect(() => {
        fetch('http://localhost:8000/lprs/rewardtransactions/get-all/')
            .then(response => {
                if (!response.ok) {
                    console.error("Response Status:", response.status);
                    return response.text().then(text => {
                        throw new Error(`Error: ${text}`);
                    });
                }
                return response.json();
            })
            .then(data => {
                setTransactions(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });
    }, [transaction_id]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div class="reward-transactions-container">
            <h1>Reward Transactions</h1>
            <br></br>
            <div>
                <h2>Active</h2>
                <div>
                    {transactions.map((transaction) => (
                        <div class="each-transaction" key={transaction.transaction_id}>
                            <img src={transaction.image} alt="Reward Image" />
                                <div>
                                    <h3>{transaction.title}</h3>
                                    <p>End date:Ongoing</p>
                                </div>
                            <button type="button" onClick={() => setShowTransactionPopup(true)}>Redeem</button>
                        </div>
                    ))}
                </div>
            </div>
            <div>
                <h2>Inactive</h2>
            </div>

            {showTransactionPopup && (
                <TransactionPopup
                    reward={transactions}
                    isOpen={showTransactionPopup}
                    onClose={() => setShowTransactionPopup(false)}
                />
            )}
        </div>
    );
}

export default Transactions;
