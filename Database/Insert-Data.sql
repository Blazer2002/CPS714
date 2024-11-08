USE lprs;

INSERT INTO USERS (
	User_ID, Username, Email, PasswordHash, Firstname, Lastname, Points
) VALUES (
	1, "johnsmithh", "johnsmith@gmail.com", "password", "john", "smith", 50
);

INSERT INTO PRODUCTS (
	ProductName, Price, Exclusive
) VALUES (
	"UpgradeATestProduct", 100.00, 0
);

INSERT INTO PRODUCTS (
	ProductName, Price, Exclusive
) VALUES (
	"UpgradeBTestProduct", 200.00, 0
);

INSERT INTO PRODUCTS (
	ProductName, Price, Exclusive
) VALUES (
	"ExclusiveTestProduct", 300.00, 1
);

INSERT INTO REWARDS (
	Type, Points, Start, Title
) VALUES (
	0, 200, NOW(), "PercentDiscountTest"
);

INSERT INTO REWARDS (
	Type, Points, Start, Title
) VALUES (
	1, 300, NOW(), "PriceDiscountTest"
);

INSERT INTO REWARDS (
	Type, Points, Start, Title
) VALUES (
	2, 400, NOW(), "UpgradeTest"
);

INSERT INTO REWARDS (
	Type, Points, Start, Title
) VALUES (
	3, 500, NOW(), "ExclusiveTest"
);

INSERT INTO PERCENTDISCOUNTREWARD (
	Reward_ID, Percent
) VALUES (
	200, 50.00
);

INSERT INTO PRICEDISCOUNTREWARD (
	Reward_ID, Price
) VALUES (
	201, 25.00
);

INSERT INTO PRODUCTUPGRADEREWARD (
	Reward_ID, PrevProduct_ID, NextProduct_ID
) VALUES (
	202, 100, 101
);

INSERT INTO EXCLUSIVEPRODUCTREWARD (
	Reward_ID, Product_ID
) VALUES (
	203, 102
);

INSERT INTO REWARDTRANSACTION (
	User_ID, Reward_ID, Date
) VALUES (
	1, 200, NOW()
);

INSERT INTO REWARDTRANSACTION (
	User_ID, Reward_ID, Date
) VALUES (
	1, 201, NOW()
);

INSERT INTO REWARDTRANSACTION (
	User_ID, Reward_ID, Date
) VALUES (
	1, 202, NOW()
);

INSERT INTO REWARDTRANSACTION (
	User_ID, Reward_ID, Date
) VALUES (
	1, 203, NOW()
);
