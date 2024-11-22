import React from "react";
import './ConfirmationPopup.css'
import Failure_Icon from '../components/icons/error.png'

function FailurePopup({ isOpen, onClose}) {
    if (!isOpen) return null;

    return (
        <div className="popup-overlay">
            <div className="popup-content">
                <img src={Failure_Icon} alt="Error Icon" className="failure-img"></img>
                <h2>Uh oh! Something went wrong.</h2>
                <br></br>
                <div className="button-container">
                    <button className="close-button" onClick={onClose}>
                        Close
                    </button>
                </div>
            </div>
        </div>
    );
}

export default FailurePopup