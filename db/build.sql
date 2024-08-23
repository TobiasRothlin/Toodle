-- MySQL Workbench Forward Engineering
 
SET NAMES utf8mb4;
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
 
-- =========================================
-- == Schema for Events registration         ==
-- =========================================
 
DROP SCHEMA IF EXISTS `ToodleEventData`;
CREATE SCHEMA IF NOT EXISTS `ToodleEventData`  DEFAULT CHARACTER SET utf8 ;
 
-- Als default Schema setzen
SELECT SLEEP(1);  -- wait 1 sec, just to give a chance to set schema as default
USE `ToodleEventData`;
 
-- -----------------------------------------------------
-- Table `mydb`.`Events`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Events` (
  `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `EventName` VARCHAR(45) NOT NULL,
  `SignUpDeadLine` DATE NULL,
  `Eventdate` DATE NULL,
  `Partners` BOOLEAN DEFAULT FALSE,
 
  PRIMARY KEY (`ID`));
 
 
-- -----------------------------------------------------
-- Table `mydb`.`SignUp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SignUp` (
  `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `SurName` VARCHAR(45) NOT NULL,
  `Events_ID` INT UNSIGNED NOT NULL,
  `Partners` INT UNSIGNED  NULL,
  PRIMARY KEY (`ID`, `Events_ID`),
  INDEX `fk_SignUp_Events_idx` (`Events_ID` ASC) VISIBLE,
  CONSTRAINT `fk_SignUp_Events`
    FOREIGN KEY (`Events_ID`)
    REFERENCES `Events` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
 
 
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;