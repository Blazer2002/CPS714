import React from 'react';
import './RewardCard.css';
import { useNavigate } from 'react-router-dom';

function RewardCard( { reward, rewardType } ) {
    console.log(rewardType)
    const startDate = new Date(reward.start).toLocaleDateString();
    const endDate = reward.end ? new Date(reward.end).toLocaleDateString() : 'Ongoing';
    
    const navigate = useNavigate();
    const handleClick = () => {
        navigate(`/rewards/${reward.reward_id}`);
    };
    
    return (
        <div className="reward-card" onClick={handleClick}>
            <div className="reward-image">
                {reward.image ? (
                    <img src={reward.image} alt={reward.rewardname} />
                ) : (
                    <div className="no-image">No Image</div>
                )}
            </div>
            <div className="reward-details">
                <h3>{reward.title}</h3>
                {rewardType.product_id != null && (
                    <p><strong>ID:{rewardType.product_id}</strong></p>
                )}
                {rewardType.discountpercent != null && (
                    <p><strong>-{rewardType.discountpercent}%</strong></p>
                )}
                {rewardType.discountprice != null && (
                    <p><strong>-${rewardType.discountprice}</strong></p>
                )}
                {rewardType.prev_product_id != null && rewardType.next_product_id != null && (
                    <p><strong>{rewardType.prev_product_id}{'>>'}{rewardType.next_product_id}</strong></p>
                )}
                <br></br>
                <p><strong>Points: </strong>{reward.points}</p>
                <p><strong>StartDate: </strong>{startDate}</p>
                <p><strong>EndDate: </strong>{endDate}</p>
            </div>
        </div>
    );
};

export default RewardCard;