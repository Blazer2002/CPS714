USE lprs;

-- Create Users table
CREATE TABLE USERS (
	User_ID				Int					NOT NULL AUTO_INCREMENT,
	Username 			Varchar(100) 		NOT NULL,
	Email 				Varchar(255)		NULL,
	PasswordHash 		Varchar(255) 		NOT NULL,
	Firstname 			Varchar(100) 		NOT NULL,
	Lastname 			Varchar(100) 		NOT NULL,
    Role				Varchar(50)			NOT NULL,
	Points				Int					DEFAULT 0,

	CONSTRAINT 			UserPK				PRIMARY KEY(User_ID)
);

-- Create Products table
CREATE TABLE PRODUCTS (
	Product_ID			Int					NOT NULL AUTO_INCREMENT,
	ProductName			Varchar(25)			NOT NULL,
	Image				Varchar(500)		NULL,
	Description 		Text				NULL,
	category 			VARCHAR(50),
    sustainability_level VARCHAR(50),
	Price				Decimal (10,2)		NOT NULL,

	CONSTRAINT 			ProductPK			PRIMARY KEY(Product_ID)
);

ALTER TABLE PRODUCTS AUTO_INCREMENT = 100;

-- Create Feedback table
CREATE TABLE Feedback (
    feedback_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    date_submitted DATE NOT NULL,
    product_id INT,
    service_rating INT CHECK (service_rating BETWEEN 1 AND 5),
    comments TEXT,
    sustainability_score INT CHECK (sustainability_score BETWEEN 1 AND 5),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Create Surveys table
CREATE TABLE Surveys (
    survey_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_date DATE NOT NULL,
    expiry_date DATE
);

-- Create SurveyResponses table
CREATE TABLE SurveyResponses (
    response_id INT PRIMARY KEY AUTO_INCREMENT,
    survey_id INT NOT NULL,
    user_id INT NOT NULL,
    response_date DATE NOT NULL,
    content TEXT,
    initiative_engagement DECIMAL(5,2),  -- from sub 5 -> for green initiative participation/effectiveness
    points_earned INT DEFAULT 0,
    FOREIGN KEY (survey_id) REFERENCES Surveys(survey_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create Rewards table
CREATE TABLE REWARDS (
	Reward_ID			Int					NOT NULL AUTO_INCREMENT,
	Points				Int					NOT NULL,
	Start				DateTime			NOT NULL,
	End					DateTime			NULL,
	Title				VARCHAR(255),
	Image				Varchar(500)		NULL,
	Description 		Text				NULL,
    
	CONSTRAINT 			RewardPK			PRIMARY KEY(Reward_ID)
);

ALTER TABLE REWARDS AUTO_INCREMENT = 200;

-- Create Percent Discount Reward transactions table
CREATE TABLE PERCENTDISCOUNTREWARD (
	Reward_ID			Int				NOT NULL,
	Product_ID			Int				NOT NULL,
	Percent				Decimal (10,2)	NOT NULL,

	CONSTRAINT 			RewardPercentFK	FOREIGN KEY(Reward_ID)
										REFERENCES REWARDS(Reward_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT 			ProductPercentFK FOREIGN KEY(Product_ID)
										REFERENCES PRODUCTS(Product_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT			Percent			CHECK ((Percent >= 0) AND (Percent <= 100))
);

-- Create price discount reward transactions table
CREATE TABLE PRICEDISCOUNTREWARD (
	Reward_ID			Int				NOT NULL,
	Product_ID			Int				NOT NULL,
	Price				Decimal (10,2)	NOT NULL,

	CONSTRAINT 			RewardPriceFK	FOREIGN KEY(Reward_ID)
										REFERENCES REWARDS(Reward_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT 			ProductPriceFK FOREIGN KEY(Product_ID)
										REFERENCES PRODUCTS(Product_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION
);

-- Create product upgrade reward transactions table
CREATE TABLE PRODUCTUPGRADEREWARD (
	Reward_ID			Int				NOT NULL,
	PrevProduct_ID		Int				NOT NULL,
	NextProduct_ID		Int				NOT NULL,

	CONSTRAINT 			RewardUpgradeFK	FOREIGN KEY(Reward_ID)
										REFERENCES REWARDS(Reward_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT 			PrevProductFK	FOREIGN KEY(PrevProduct_ID)
										REFERENCES PRODUCTS(Product_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT 			NextProductFK	FOREIGN KEY(NextProduct_ID)
										REFERENCES PRODUCTS(Product_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT			DifferentProduct CHECK (PrevProduct_ID <> NextProduct_ID)
);

-- Create exclusive product reward transactions table
CREATE TABLE EXCLUSIVEPRODUCTREWARD (
	Reward_ID			Int				NOT NULL,
	Product_ID			Int				NOT NULL,
	
	CONSTRAINT 			RewardExclusiveFK	FOREIGN KEY(Reward_ID)
										REFERENCES REWARDS(Reward_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT 			ProductFK		FOREIGN KEY(Product_ID)
										REFERENCES PRODUCTS(Product_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION
);

-- Create reward transaction table
CREATE TABLE REWARDTRANSACTION (
	Transaction_ID		Int				NOT NULL AUTO_INCREMENT,
	User_ID				Int				NOT NULL,
	Reward_ID			Int				NOT NULL,
	Date				DateTime		NOT NULL,
    Active				TINYINT			NOT NULL,

	CONSTRAINT 			TransactionPK	PRIMARY KEY(Transaction_ID),
	CONSTRAINT 			UserRewardFK	FOREIGN KEY(User_ID)
										REFERENCES USERS(User_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT 			RewardUserFK	FOREIGN KEY(Reward_ID)
										REFERENCES REWARDS(Reward_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT 			ActiveValues		CHECK (Active IN (0, 1))
);

ALTER TABLE REWARDTRANSACTION AUTO_INCREMENT = 300;

-- Create Analytics table
CREATE TABLE Analytics (
    analytics_id INT PRIMARY KEY AUTO_INCREMENT,
    survey_id INT NOT NULL,
    client_engagement_score FLOAT,
    average_rating FLOAT,
    sustainability_engagement FLOAT,
    FOREIGN KEY (survey_id) REFERENCES Surveys(survey_id)
);

-- Create client engagement table
CREATE TABLE Client_Engagement (
    engagement_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    participation_type ENUM('loyalty_program', 'educational_content', 'green_initiatives'),
    participation_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create support ticket table from sub-project 3
CREATE TABLE Support_Tickets (
    ticket_id INT PRIMARY KEY auto_increment,      -- from sub 3
	user_id int NOT NULL,
    ticket_status VARCHAR(15),  -- from sub 3 -> for resolution effectiveness
    ticket_start_date DATE,     -- from sub 3 -> for response times
    ticket_end_date DATE,        -- from sub 3 -> for response times
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create support performance table
CREATE TABLE Support_Performance (
    ticket_id INT PRIMARY KEY,
    response_time DECIMAL(5, 2),            -- minutes
    resolution_time DECIMAL(5, 2),          -- minutes
    resolution_effectiveness DECIMAL(5, 2), -- percentage
    customer_satisfaction DECIMAL(5, 2),     
    FOREIGN KEY (ticket_id) REFERENCES Support_Tickets(ticket_id)
);

-- Create program success table
CREATE TABLE Program_Success (
	program_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    loyalty_effectiveness DECIMAL(5,2),-- percentage
    engagement_score DECIMAL(5,2),
    evaluation_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create admin access table
CREATE TABLE Admin_Access (
    admin_id INT PRIMARY KEY,
    access_time TIMESTAMP,
    report_type ENUM ('client_engagement', 'support_performance', 'program_success')
);

-- Create customer stats table
CREATE TABLE Customer_Stats (
    user_id INT PRIMARY KEY,        -- from sub 4 -> for client loyalty prog participation
    loyalty_points INT,
    reward_transactions INT,                -- from sub 4 -> for client loyalty prog participation/ effectiveness
    product_purchases INT,                  -- from sub 2 -> for client loyalty prog participation/ effectiveness
    initiative_points INT,                  -- from sub 4 -> for green initiaitive participation, client loyalty prog participation/effectiveness  
    campaign_points INT,                    -- from sub 4 -> for educ content participation, client loyalty prog participation/effectiveness                           
    survey_points INT,                      -- from sub5 -> --from sub 5 -> for client loyalty prog participation/effectiveness
    education_engagement DECIMAL(5,2),       -- from sub 6 -> for user interaction with educational content, client loyalty prog participation/effectiveness
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
