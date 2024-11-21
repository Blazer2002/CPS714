import React from 'react'
import './RewardDetails.css'
import { useNavigate, useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import ConfirmationPopup from './ConfirmationPopup';
import SuccessPopup from './SuccessPopup';
import FailurePopup from './FailurePopup';
import TransactionPopup from './TransactionPopup';

function RewardDetails() {
    const { reward_id } = useParams();
    const [reward, setReward] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [isPopupOpen, setIsPopupOpen] = useState(false);
    const [showTransactionPopup, setShowTransactionPopup] = useState(false);
    const [redeemStatus, setRedeemStatus] = useState(null);

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

    const handleSuccess = () => {
        setShowTransactionPopup(true);
    }

    const closeTransactionPopup = () => {
        setShowTransactionPopup(false);
        navigate('/rewards');
    };

    const handleRedeemConfirmation = () => {
        if (200 < reward.points) {
            {/* user.points, fetch current user */}
            setRedeemStatus(false);
        } else {
            setRedeemStatus(true);
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
            .then(data => {
                setReward(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error.message);
                setLoading(false);
            });
    }, [reward_id]);

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
                        {reward.title}
                    </div>
                    <div className='reward-points'>
                        {reward.points} Points
                    </div>
                    <div className='reward-tags'>
                        
                    </div>
                    <div className='redemption-button'>
                        <button type='button' className='reward-redemption' onClick={openPopup}>Redeem</button>
                    </div>
                </div>
            </div>
            <div className="reward-description">
                {reward.description}
            </div>
            <ConfirmationPopup 
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

            {showTransactionPopup && (
                <TransactionPopup
                    reward={reward}
                    isOpen={showTransactionPopup}
                    onClose={closeTransactionPopup}/>
            )}
        </div>
    );
}

export default RewardDetails;