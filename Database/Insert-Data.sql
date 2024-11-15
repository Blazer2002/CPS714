USE lprs;

INSERT INTO Users (Username, Email, PasswordHash, Firstname, Lastname, Role, Points)
VALUES 
('Mahit', 'mahit@torontomu.ca', 'pass1', 'Mahit', 'Parmar', 'Customer', 50),
('Patrick', 'patrick@torontomu.ca', 'pass2', 'Patrick', 'Urban', 'Admin', 0);

INSERT INTO PRODUCTS (
	ProductName, category, sustainability_level, Price
) VALUES (
	"PercentTestProduct", 'Monitoring', 'Moderate', 100.00
);

INSERT INTO PRODUCTS (
	ProductName, category, sustainability_level, Price
) VALUES (
	"PriceTestProduct", 'Category B', 'Low', 200.00
);

INSERT INTO PRODUCTS (
	ProductName, category, sustainability_level, Price
) VALUES (
	"UpgradeATestProduct", 'Monitoring', 'Moderate', 100.00
);

INSERT INTO PRODUCTS (
	ProductName, category, sustainability_level, Price
) VALUES (
	"UpgradeBTestProduct", 'Category B', 'Low', 200.00
);

INSERT INTO PRODUCTS (
	ProductName, category, sustainability_level, Price
) VALUES (
	"ExclusiveTestProduct", 'Category C', 'High', 300.00
);

INSERT INTO Client_Engagement (user_id, participation_type, participation_date)
VALUES 
(1, 'loyalty_program', '2024-11-07');

INSERT INTO Support_Tickets (user_id, ticket_status, ticket_start_date, ticket_end_date)
VALUES 
(1, 'Resolved', '2024-10-01', '2024-10-02');

INSERT INTO Support_Performance (ticket_id, response_time, resolution_time, resolution_effectiveness, customer_satisfaction)
VALUES 
(1, 15.25, 45.50, 8, 4.50);

INSERT INTO Program_Success (user_id, loyalty_effectiveness, engagement_score, evaluation_date)
VALUES 
(1, 92.50, 88.75, '2024-11-07');

INSERT INTO Admin_Access (admin_id, access_time, report_type)
VALUES 
(5001, '2024-11-07 10:15:00', 'client_engagement');

INSERT INTO Customer_Stats (user_id, loyalty_points, reward_transactions, product_purchases, initiative_points, campaign_points, survey_points, education_engagement)
VALUES 
(1, 1200, 5, 20, 150, 80, 60, 3.00);

INSERT INTO surveys (`name`, `description`, `created_date`, `expiry_date`) 
VALUES ('Service Satisfaction', 'Customer thoughts on the eco-initiative program', '2024-09-01', '2024-12-31');

INSERT INTO REWARDS (
	survey_id, Points, Start, Title
) VALUES (
	1, 200, NOW(), "PercentDiscountTest"
);

INSERT INTO REWARDS (
	survey_id, Points, Start, Title
) VALUES (
	1, 300, NOW(), "PriceDiscountTest"
);

INSERT INTO REWARDS (
	survey_id, Points, Start, Title
) VALUES (
	1, 400, NOW(), "UpgradeTest"
);

INSERT INTO REWARDS (
	survey_id, Points, Start, Title
) VALUES (
	1, 500, NOW(), "ExclusiveTest"
);

INSERT INTO PERCENTDISCOUNTREWARD (
	Reward_ID, Product_ID, Percent
) VALUES (
	200, 100, 50.00
);

INSERT INTO PRICEDISCOUNTREWARD (
	Reward_ID, Product_ID, Price
) VALUES (
	201, 101, 25.00
);

INSERT INTO PRODUCTUPGRADEREWARD (
	Reward_ID, PrevProduct_ID, NextProduct_ID
) VALUES (
	202, 102, 103
);

INSERT INTO EXCLUSIVEPRODUCTREWARD (
	Reward_ID, Product_ID
) VALUES (
	203, 104
);

INSERT INTO REWARDTRANSACTION (
	User_ID, Reward_ID, Date, Active
) VALUES (
	1, 200, NOW(), 0
);

INSERT INTO REWARDTRANSACTION (
	User_ID, Reward_ID, Date, Active
) VALUES (
	1, 201, NOW(), 1
);

INSERT INTO REWARDTRANSACTION (
	User_ID, Reward_ID, Date, Active
) VALUES (
	1, 202, NOW(), 0
);

INSERT INTO REWARDTRANSACTION (
	User_ID, Reward_ID, Date, Active
) VALUES (
	1, 203, NOW(), 1
);

INSERT INTO feedback (`user_id`, `date_submitted`, `product_id`, `service_rating`, `comments`, `sustainability_score`) 
VALUES (1, '2024-11-07', 100, 3, 'I thought it was great.', 2);

INSERT INTO surveyresponses (`survey_id`, `user_id`, `response_date`, `content`, `initiative_engagement`, `points_earned`)
VALUES ('1', '1', '2024-12-12', 'This was a great survey', 4.00, '15');

INSERT INTO analytics (`survey_id`, `client_engagement_score`, `average_rating`, `sustainability_engagement`)
VALUES ('1', '22.4', '4.3', '8.3');