CREATE TABLE IF NOT EXISTS `stocksimdb`.`username` (
  `user_pk` bigint(20) AUTO_INCREMENT PRIMARY KEY,
  `user_id` VARCHAR(45) NULL,
  `user_level` INT NULL,
  `user_hash_pass` VARCHAR(192) NULL,
  `user_create_date` VARCHAR(20) NULL,
  `user_recent_login` VARCHAR(20) NULL);
