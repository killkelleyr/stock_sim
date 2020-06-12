CREATE TABLE IF NOT EXISTS `stocksim`.`username` (
  `user_pk` bigint(20) AUTO_INCREMENT PRIMARY KEY,
  `user_id` VARCHAR(45) NULL,
  `user_level` INT NULL,
  `user_hash_pass` VARCHAR(192) NULL,
  `user_create_date` BIGINT(20) NULL,
  `user_recent_login` BIGINT(20) NULL);
