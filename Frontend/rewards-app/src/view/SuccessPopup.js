import React from "react";
import './ConfirmationPopup.css'
import Success_Icon from '../components/icons/check.png'

function SuccessPopup({ isOpen, onClose, onSuccess}) {
    if (!isOpen) return null;

    const handleCloseButton = () => {
        onClose();
        onSuccess();
    }

    return (
        <div className="popup-overlay">
            <div className="popup-content">
                <img src={Success_Icon} alt="Success Icon" className="success-img"></img>
                <h2>Your Reward Has Been Redeemed!</h2>
                <br></br>
                <div className="button-container">
                    <button className="confirm-button" onClick={handleCloseButton}>
                        OK
                    </button>
                </div>
            </div>
        </div>
    );
}

export default SuccessPopup