import React from 'react'
import './RewardDetails.css'
import { useNavigate, useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import ConfirmationPopup from './ConfirmationPopup';
import SuccessPopup from './SuccessPopup';
import FailurePopup from './FailurePopup';
import TransactionPopup from './TransactionPopup';
import { createTransaction } from '../createTransaction';

function RewardDetails({ user }) {
    const { reward_id } = useParams();
    const [reward, setReward] = useState(null);

    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [showTransactionPopup, setShowTransactionPopup] = useState(false);
    const [redeemStatus, setRedeemStatus] = useState(null);
    const [newTransaction, setNewTransaction] = useState(null);

    const navigate = useNavigate();
    
    const backButton = () => {
        navigate('/rewards');
    };

    const openPopup = () => {
        setIsPopupOpen(true);
    };

    const closePopup = () => {
        setIsPopupOpen(false);
    };

    const logTransaction = (transaction) => {
        setNewTransaction(transaction);
    }

    const handleSuccess = () => {
        setShowTransactionPopup(true);
    }

    const closeTransactionPopup = () => {
        setShowTransactionPopup(false);
        navigate('/rewards');
    };

    const handleRedeemConfirmation = () => {
        if (user.points < reward.points) {
            console.log("User doesn't have enough points");
            setRedeemStatus(false);
        } else {
            createTransaction(user.user_id, reward.reward_id)
            .then(transaction => {
                setRedeemStatus(true);
                logTransaction(transaction);
            })
            .catch(error => {
                setRedeemStatus(false);
                console.error("Error creating transaction:", error);
            });

        }
        setIsPopupOpen(false);
    };

    useEffect(() => {
        fetch(`http://localhost:8000/lprs/rewards/${reward_id}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(rewardData => {
                setReward(rewardData);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });
    }, [reward_id, user]);

    if (loading) {
        return <p>Loading reward details...</p>;
    }

    if (error) {
        return <p>Error loading reward details: {error}</p>;
    }

    return (
        <div className="content-container">
            <div className="banner">
                <button type='button' className='back-button' onClick={backButton}>
                    Back
                </button>
            </div>
            <div className="reward-info">
                <div className="reward-image">
                    <img src={reward.image} alt="Reward Image" />
                </div>
                <div className="reward-details">
                    <div className='reward-name' >
                        {reward.rewardname}
                    </div>
                    <div className='reward-points'>
                        {reward.points} Points
                    </div>
                    <div className='reward-tags'>
                        {/* tags */}
                    </div>
                    <div className='redeem-button-container'>
                        <button type='button' className='redeem-button' onClick={openPopup}>Redeem</button>
                    </div>
                </div>
            </div>
            <div className="reward-description">
                {reward.description == null && (
                    <>No Description</>
                )}
                {reward.description}
            </div>
            <ConfirmationPopup 
                user={user}
                reward={reward} 
                isOpen={isPopupOpen} 
                onClose={closePopup} 
                onConfirm={() => handleRedeemConfirmation(true)}/>

            {redeemStatus === true && (
                <SuccessPopup
                    isOpen={redeemStatus === true}
                    onClose={() => setRedeemStatus(null)}
                    onSuccess={handleSuccess}/>
            )}

            {redeemStatus === false && (
                <FailurePopup
                    isOpen={redeemStatus === false}
                    onClose={() => setRedeemStatus(null)}/>
                
            )}

            {showTransactionPopup && newTransaction && (
                <TransactionPopup
                    transaction={newTransaction}
                    isOpen={showTransactionPopup}
                    onClose={closeTransactionPopup}/>
            )}
        </div>
    );
}

export default RewardDetails;