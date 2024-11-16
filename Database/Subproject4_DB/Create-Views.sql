USE lprs;

CREATE VIEW PERCENTDISCOUNTREWARDVIEW AS
	SELECT 	
        R.Reward_ID AS Reward_ID,
        R.Points AS Points,
        R.Start AS Start,
        R.End AS End,
        R.Title AS Title,
        R.Image AS Image,
        R.Description AS Description,
        PER.Percent AS Percent,
        
        P.Product_ID AS Product_ID,
        P.ProductName AS ProductName,
        P.Image AS ProductImage,
        P.Description AS ProductDescription,
        P.Price AS Price

	FROM REWARDS AS R JOIN PERCENTDISCOUNTREWARD AS PER
		ON 	R.Reward_ID = PER.Reward_ID
        JOIN PRODUCTS AS P
            ON 	P.Product_ID = PER.Product_ID;

CREATE VIEW PRICEDISCOUNTREWARDVIEW AS
	SELECT
		R.Reward_ID AS Reward_ID,
        R.Points AS Points,
        R.Start AS Start,
        R.End AS End,
        R.Title AS Title,
        R.Image AS Image,
        R.Description AS Description,
        PRI.Price AS DiscountPrice,
        
        P.Product_ID AS Product_ID,
        P.ProductName AS ProductName,
        P.Image AS ProductImage,
        P.Description AS ProductDescription,
        P.Price AS Price

	FROM REWARDS AS R JOIN PRICEDISCOUNTREWARD AS PRI
		ON 	R.Reward_ID = PRI.Reward_ID
        JOIN PRODUCTS AS P
            ON 	P.Product_ID = PRI.Product_ID;

CREATE VIEW PRODUCTUPGRADEREWARDVIEW AS
	SELECT 	
        R.Reward_ID AS Reward_ID,
        R.Points AS Points,
        R.Start AS Start,
        R.End AS End,
        R.Title AS RewardTitle,
        R.Image AS RewardImage,
        R.Description AS RewardDescription,

        A.Product_ID AS PrevProduct_ID,
        A.ProductName AS PrevProductName,
        A.Image AS PrevProductImage,
        A.Description AS PrevProductDescription,
        A.Price AS PrevPrice,

        B.Product_ID AS NextProduct_ID,
        B.ProductName AS NextProductName,
        B.Image AS NextProductImage,
        B.Description AS NextProductDescription,
        B.Price AS NextPrice

	FROM REWARDS AS R
		INNER JOIN PRODUCTUPGRADEREWARD AS U
			ON R.Reward_ID = U.Reward_ID
		INNER JOIN PRODUCTS AS A
			ON U.PrevProduct_ID = A.Product_ID
		INNER JOIN PRODUCTS AS B
			ON U.NextProduct_ID = B.Product_ID;

CREATE VIEW EXCLUSIVEPRODUCTREWARDVIEW AS
	SELECT 
		R.Reward_ID AS Reward_ID,
        R.Points AS Points,
        R.Start AS Start,
        R.End AS End,
        R.Title AS Title,
        R.Image AS Image,
        R.Description AS Description,

        P.Product_ID AS Product_ID,
        P.ProductName AS ProductName,
        P.Image AS ProductImage,
        P.Description AS ProductDescription,
        P.Price AS Price

	FROM REWARDS AS R JOIN EXCLUSIVEPRODUCTREWARD AS E
		ON 	R.Reward_ID = E.Reward_ID
        JOIN PRODUCTS AS P
            ON 	P.Product_ID = E.Product_ID;

CREATE VIEW REWARDTRANSACTIONVIEW AS
	SELECT 
		T.Transaction_ID AS Transaction_ID,
        U.User_ID AS User_ID,
        R.Reward_ID AS Reward_ID,
        R.End AS End,
        R.Title AS RewardTitle,
        R.Image AS RewardImage,
        T.Date AS Date,
        T.Active AS Active

	FROM REWARDTRANSACTION AS T JOIN REWARDS AS R
		ON 	T.Reward_ID = R.Reward_ID
        JOIN USERS AS U
            ON 	T.User_ID = U.User_ID;
