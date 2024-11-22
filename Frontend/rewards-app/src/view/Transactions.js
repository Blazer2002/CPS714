import React from 'react';
import './Transactions.css';
import './RewardDetails.css';

import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import TransactionPopup from './TransactionPopup';

function Transactions() {
    const { activetransaction_id } = useParams(); // Corrected typo here
    const { inactivetransaction_id } = useParams(); // Corrected typo here
    const [activeTransactions, setActiveTransactions] = useState([]);
    const [inactiveTransactions, setInactiveTransactions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [showTransactionPopup, setShowTransactionPopup] = useState(false);

    const user_id = 1;

    useEffect(() => {
        fetch('http://localhost:8000/lprs/rewardbyuser/1/' + user_id)
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
                setActiveTransactions(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });
    }, [activetransaction_id]);

    useEffect(() => {
        fetch('http://localhost:8000/lprs/rewardbyuser/0/' + user_id)
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
                setInactiveTransactions(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });
    }, [inactivetransaction_id]);

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
                    {activeTransactions.map((transaction) => (
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
                <div>
                    {inactiveTransactions.map((transaction) => (
                        <div class="each-transaction" key={transaction.transaction_id}>
                            <img src={transaction.image} alt="Reward Image" />
                            <div>
                                <h3>{transaction.title}</h3>
                                <p>End date:Ongoing</p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            {showTransactionPopup && (
                <TransactionPopup
                    reward={activeTransactions}
                    isOpen={showTransactionPopup}
                    onClose={() => setShowTransactionPopup(false)}
                />
            )}
        </div>
    );
}

export default Transactions;
