import React from "react";
import './TransactionPopup.css'

function TransactionPopup({ transaction, isOpen, onClose}) {
    if (!isOpen) return null;
    console.log(transaction);

    return (
        <div className="transac-overlay">
            <div className="transac-content">
            <button className="transac-close-button" onClick={onClose}>X</button>
                <div className="left-col">
                    {/* reward.rewardname */}
                    <h2 className="transaction-title">Confirmation: Transaction #{transaction.transaction_id}</h2>
                    <h4 className="reward-exp-date">Thank you for your reward redemption!</h4>
                    <div className="textbox">
                        <p className="description-text">Description</p>
                        <br></br>
                        <p className="terms-text">Terms and conditions</p>
                    </div>
                </div>
                <div className="right-col">
                    <div className="qr-code-box">
                        {/* qr code */}
                        <div className="qr-code-placeholder">
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