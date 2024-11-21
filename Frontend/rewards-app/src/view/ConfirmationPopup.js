import React from "react";
import './ConfirmationPopup.css';
import formatDate from '../utility.js';

function ConfirmationPopup({ reward, isOpen, onClose, onConfirm}) {
    {/* get user */}
    if (!isOpen) return null;

    let startDateFormatted = formatDate(reward.start);
    let endDateFormatted = formatDate(reward.end);

    return (
        <div className="popup-overlay">
            <div className="popup-content">
                <h1>Redemption Confirmation</h1>
                <div className="terms-conditions">
                    Terms and Conditions
                </div>
                <div className="points-info">
                    <h3>Redemption Amount: {reward.points}</h3>
                    Current Points: {/* user.points */}
                </div>
                <div className="info-container">
                    <span className="align-left">
                        <h4>Product Name</h4>
                        <h4>Reward Start Date</h4>
                        <h4>Product Expiration Date</h4>
                        <h4>Points After Redemption</h4>
                    </span>
                    <span className="align-right">
                        <h4>{reward.title}</h4>
                        <h4>{startDateFormatted}</h4>
                        <h4>{endDateFormatted}</h4>
                        <h4>{/* user.points - reward.points */}Pts</h4>
                    </span>
                </div>
                <br></br>
                <div className="button-container">
                    <button className="close-button" onClick={onClose}>
                        Cancel
                    </button>
                    <button className="confirm-button" onClick={onConfirm}>
                        Redeem
                    </button>
                </div>
            </div>
        </div>
    );
}

export default ConfirmationPopup