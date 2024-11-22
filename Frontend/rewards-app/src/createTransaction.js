export const createTransaction = async (user_id, reward_id) => {
    const transactionData = {
        user_id: user_id,
        reward_id: reward_id
    };

    const formatData = JSON.stringify(transactionData);

    try {
        console.log(formatData);
        const response = await fetch('http://localhost:8000/lprs/rewardtransactions/post/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: formatData,
        });

        if (!response.ok) {
            throw new Error('Failed to create transaction');
        }

        const transaction = await response.json();
        return transaction;
    } catch (error) {
        console.error('Error creating transaction:', error);
        throw error;
    }
};