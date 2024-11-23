import React from 'react';
import './Transactions.css';
import './RewardDetails.css';

import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import TransactionCard from '../components/TransactionCard';

function Transactions({user}) {
    const { activetransaction_id } = useParams();
    const { inactivetransaction_id } = useParams();
    const [activeTransactions, setActiveTransactions] = useState([]);
    const [inactiveTransactions, setInactiveTransactions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch('http://localhost:8000/lprs/rewardbyuser/1/' + user.user_id)
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

        fetch('http://localhost:8000/lprs/rewardbyuser/0/' + user.user_id)
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
    }, [user, activetransaction_id, inactivetransaction_id]);

    if (loading) {
        console.log('loading');
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div class="reward-transactions-container">
            <h1>Reward Transactions</h1>
            <h2>Active</h2>
            <div className='active-transaction-container'>
                {activeTransactions.length > 0 ? (
                    activeTransactions.map(transaction => (
                        <TransactionCard key={transaction.transaction_id} transaction={transaction} active={true}/>
                    ))
                ) : (
                    console.log('No active transactions for this user')
                )}
            </div>
            <br></br>
            <h2>Inactive</h2>
            <div className='inactive-transaction-container'>
                {inactiveTransactions.length > 0 ? (
                    inactiveTransactions.map(transaction => (
                        <TransactionCard key={transaction.transaction_id} transaction={transaction}/>
                    ))
                ) : (
                    console.log('No inactive transactions for this user')
                )}
            </div>
        </div>
    );
}

export default Transactions;
