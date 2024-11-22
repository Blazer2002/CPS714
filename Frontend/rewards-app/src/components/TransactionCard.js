import React from 'react';
import './TransactionCard.css';
import { useState } from 'react';
import TransactionPopup from '../view/TransactionPopup';

function TransactionCard( { transaction, active } ) {
    const [showTransactionPopup, setShowTransactionPopup] = useState(false);
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
                <h3>{transaction.title}</h3>
                {active && (
                    <p>End date:Ongoing</p>
                )}
                {!active && (
                    <p>Expired/Redeemed</p>
                )}
            </div>
            {active && (
                <button type="button" onClick={() => setShowTransactionPopup(true)}>Redeem</button>
            )}
            {showTransactionPopup && (
                <TransactionPopup
                    transaction={transaction}
                    isOpen={showTransactionPopup}
                    onClose={() => setShowTransactionPopup(false)}
                />
            )}
        </div>
    );
};

export default TransactionCard;