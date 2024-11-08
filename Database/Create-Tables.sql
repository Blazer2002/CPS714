CREATE DATABASE lprs;
USE lprs;

CREATE TABLE USERS (
	User_ID				Int					NOT NULL AUTO_INCREMENT,
	Username 			Varchar(25) 		NOT NULL,
	Email 				Varchar(100)		NULL,
	PasswordHash 		Varchar(255) 		NOT NULL,
	Firstname 			Varchar(25) 		NOT NULL,
	Lastname 			Varchar(25) 		NOT NULL,
	Points				Int					NOT NULL,

	CONSTRAINT 			UserPK				PRIMARY KEY(User_ID)
);

CREATE TABLE PRODUCTS (
	Product_ID			Int					NOT NULL AUTO_INCREMENT,
	ProductName			Varchar(25)			NOT NULL,
	Image				Varchar(500)		NULL,
	Description 		Text				NULL,
	Price				Decimal (10,2)		NOT NULL,
	Exclusive			TINYINT(1)			NOT NULL,

	CONSTRAINT 			UserPK				PRIMARY KEY(User_ID),
	CONSTRAINT 			ExclusiveValues		CHECK (Exclusive IN (0, 1))
);

ALTER TABLE PRODUCTS AUTO_INCREMENT = 100;

CREATE TABLE REWARDS (
	Reward_ID			Int					NOT NULL AUTO_INCREMENT,
	Type				TINYINT(1)			NOT NULL,
	Points				Int					NOT NULL,
	Start				DateTime			NOT NULL,
	End					DateTime			NULL,
	Title				Char(35)			NOT NULL,
	Image				Varchar(500)		NULL,
	Description 		Text				NULL,

	CONSTRAINT 			RewardPK			PRIMARY KEY(Reward_ID),
	CONSTRAINT 			TypeValues			CHECK (Type IN (0, 1, 2, 3))
);

ALTER TABLE REWARDS AUTO_INCREMENT = 200;

CREATE TABLE PERCENTDISCOUNTREWARD (
	Reward_ID			Int				NOT NULL,
	Percent				Decimal (10,2)	NOT NULL,

	CONSTRAINT 			RewardFK		FOREIGN KEY(Reward_ID)
										REFERENCES REWARDS(Reward_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT			Percent			CHECK ((Percent >= 0) AND (Percent <= 100))
);

CREATE TABLE PRICEDISCOUNTREWARD (
	Reward_ID			Int				NOT NULL,
	Price				Decimal (10,2)	NOT NULL,

	CONSTRAINT 			RewardFK		FOREIGN KEY(Reward_ID)
										REFERENCES REWARDS(Reward_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION
);

CREATE TABLE PRODUCTUPGRADEREWARD (
	Reward_ID			Int				NOT NULL,
	PrevProduct_ID		Int				NOT NULL,
	NextProduct_ID		Int				NOT NULL,

	CONSTRAINT 			RewardFK		FOREIGN KEY(Reward_ID)
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
	CONSTRAINT			DifferentProduct CHECK (PrevProductFK <> NextProductFK)
);

CREATE TABLE EXCLUSIVEPRODUCTREWARD (
	Reward_ID			Int				NOT NULL,
	Product_ID			Int				NOT NULL,
	
	CONSTRAINT 			RewardFK		FOREIGN KEY(Reward_ID)
										REFERENCES REWARDS(Reward_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT 			ProductFK		FOREIGN KEY(Product_ID)
										REFERENCES PRODUCTS(Product_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION
);

CREATE TABLE REWARDTRANSACTION (
	Transaction_ID		Int				NOT NULL AUTO_INCREMENT,
	User_ID				Int				NOT NULL,
	Reward_ID			Int				NOT NULL,
	Date				DateTime		NOT NULL,

	CONSTRAINT 			TransactionPK	PRIMARY KEY(Transaction_ID),
	CONSTRAINT 			UserFK			FOREIGN KEY(User_ID)
										REFERENCES USERS(User_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION,
	CONSTRAINT 			RewardFK		FOREIGN KEY(Reward_ID)
										REFERENCES REWARDS(Reward_ID)
 											ON UPDATE NO ACTION
											ON DELETE NO ACTION
);

ALTER TABLE REWARDTRANSACTION AUTO_INCREMENT = 300;
