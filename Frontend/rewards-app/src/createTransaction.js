export const createTransaction = async (user_id, reward) => {
    const transactionData = {
        user: user_id,
        reward: reward.id,
        date: new Date().toISOString(),
    };

    try {
        const response = await fetch('http://localhost:8000/lprs/rewardtransactions/post/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(transactionData),
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