import React from "react";
import './TransactionPopup.css'
import { useState } from 'react';

function TransactionPopup({ transaction, reward, isOpen, onClose}) {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const deactivateTransaction = () => {
        const reward_id = (transaction.reward_id == null) ? transaction.reward : (transaction.reward == null ? transaction.reward_id : transaction.reward);
        const newData = {
            transaction_id: transaction.transaction_id,
            date: transaction.date,
            active: 0,
            user: transaction.user,
            reward_id: reward_id,
        };
        console.log(newData)

        fetch(`http://localhost:8000/lprs/rewardtransactions/${transaction.transaction_id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(updatedData => {
            console.log('Active set to: ', updatedData.active)
            setLoading(false);
        })
        .catch(error => {
            setError(error.message);
            setLoading(false);
        });
    };

    if (!isOpen) return null;

    if (loading) {
        console.log('Loading reward details');
    }

    if (error) {
        console.log('Error loading reward details');
    }

    return (
        <div className="transac-overlay">
            <div className="transac-content">
            <button className="transac-close-button" onClick={onClose}>X</button>
                <div className="left-col">
                    <h2 className="transaction-title">Confirmation: Transaction #{transaction.transaction_id}</h2>
                    <h4 className="transaction-date">Thank you for your reward redemption!</h4>
                    <div className="textbox">
                        <p className="description-text">Description</p>
                        <p>{reward.rewardname}</p>
                        <br></br>
                        <p className="terms-text">Terms and conditions</p>
                    </div>
                </div>
                <div className="right-col">
                    <div className="qr-code-box">
                        <div className="qr-code-placeholder" onClick={deactivateTransaction}>
                            QR Code
                        </div>
                    </div>
                    <div className="buttons-container">
                        <button className="email-button" >Send To Email</button>
                        <button className="download-button" >Download As PDF</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default TransactionPopup