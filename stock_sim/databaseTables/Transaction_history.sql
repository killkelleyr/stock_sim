CREATE TABLE IF NOT EXISTS `stocksimdb`.`Transaction_history`(
	`Transaction_pk` bigint(20) AUTO_INCREMENT PRIMARY KEY,
    `row_create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `user_id` varchar(45) NULL,
    `ticker` varchar(4) NULL,
    `price`DECIMAL(65,2),
    `volume` INT NULL,
    `buy_sell` int NULL,
    `transaction_time` DATETIME NULL);
   
