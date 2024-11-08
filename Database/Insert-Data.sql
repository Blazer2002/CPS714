USE lprs;

INSERT INTO USERS (
	User_ID, Username, Email, PasswordHash, Firstname, Lastname, Points
) VALUES (
	1, "johnsmithh", "johnsmith@gmail.com", "password", "john", "smith", 50
);

INSERT INTO PRODUCTS (
	Product_ID, Title, Exclusive
) VALUES (
	0, "UpgradeATestProduct", 100.00, 0
);

INSERT INTO PRODUCTS (
	Product_ID, Title, Exclusive
) VALUES (
	1, "UpgradeBTestProduct", 200.00, 0
);

INSERT INTO PRODUCTS (
	Product_ID, Title, Exclusive
) VALUES (
	2, "ExclusiveTestProduct", 300.00, 1
);

INSERT INTO REWARDS (
	Reward_ID, Type, Points, Start, Title
) VALUES (
	0, 0, 200, VALUES(NOW()), "PercentDiscountTest"
);

INSERT INTO REWARDS (
	Reward_ID, Type, Points, Start, Title
) VALUES (
	1, 1, 300, VALUES(NOW()), "PriceDiscountTest"
);

INSERT INTO REWARDS (
	Reward_ID, Type, Points, Start, Title
) VALUES (
	2, 2, 400, VALUES(NOW()), "UpgradeTest"
);

INSERT INTO REWARDS (
	Reward_ID, Type, Points, Start, Title
) VALUES (
	3, 3, 500, VALUES(NOW()), "ExclusiveTest"
);

INSERT INTO PERCENTDISCOUNTREWARD (
	Reward_ID, Percent
) VALUES (
	0, 50.00
);

INSERT INTO PRICEDISCOUNTREWARD (
	Reward_ID, Price
) VALUES (
	1, 25.00
);

INSERT INTO PRODUCTUPGRADEREWARD (
	Reward_ID, PrevProduct_ID, NextProduct_ID
) VALUES (
	2, 0, 1
);

INSERT INTO EXCLUSIVEPRODUCTREWARD (
	Reward_ID, Product_ID
) VALUES (
	3, 2
);

INSERT INTO REWARDTRANSACTION (
	Transaction_ID, User_ID, Reward_ID, Date
) VALUES (
	0, 1, 0, VALUES(NOW())
);

INSERT INTO REWARDTRANSACTION (
	Transaction_ID, User_ID, Reward_ID, Date
) VALUES (
	1, 1, 1, VALUES(NOW())
);

INSERT INTO REWARDTRANSACTION (
	Transaction_ID, User_ID, Reward_ID, Date
) VALUES (
	2, 1, 2, VALUES(NOW())
);

INSERT INTO REWARDTRANSACTION (
	Transaction_ID, User_ID, Reward_ID, Date
) VALUES (
	3, 1, 3, VALUES(NOW())
);
