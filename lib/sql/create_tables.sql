
CREATE TABLE `portal_user` (
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`username` VARCHAR(100) NOT NULL,
	`pass_hash` VARCHAR(255) NOT NULL,
	`create_datetime` DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
	`update_datetime` DATETIME DEFAULT (CURRENT_TIMESTAMP),
	`is_active` BOOLEAN NOT NULL
);

CREATE TABLE `dashboard_user` (
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`username` VARCHAR(50) NOT NULL,
	`pass_hash` VARCHAR(255) NOT NULL,
	`create_datetime` DATETIME DEFAULT (CURRENT_TIMESTAMP),
	`is_active` BOOLEAN DEFAULT (true) NOT NULL,
	`clearance` ENUM('base', 'medium', 'high') DEFAULT ('base') NOT NULL
);

CREATE TABLE `garden` (
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(255) NOT NULL,
	`address1` VARCHAR(255) NOT NULL,
	`address2` VARCHAR(255),
	`state` VARCHAR(50) NOT NULL,
	`zip` VARCHAR(10) NOT NULL,
	`sq_ft` INT,
	`plot_count` INT,
	`lat` DECIMAL(8,5),
	`lng` DECIMAL(8,5),
	`is_active` BOOLEAN DEFAULT (true) NOT NULL
);

CREATE TABLE `garden_group` (
	`user_id` INT NOT NULL,
	`garden_id` INT NOT NULL,
	CONSTRAINT `unq_garden_group` UNIQUE (`user_id`, `garden_id`)
);

ALTER TABLE urban_eden.garden_group ADD CONSTRAINT fk_garden_group_portal_user
FOREIGN KEY (garden_id) REFERENCES urban_eden.garden(id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE urban_eden.garden_group ADD CONSTRAINT fk_garden_group_garden_group
FOREIGN KEY (user_id) REFERENCES urban_eden.portal_user(id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

CREATE TABLE `custom_content` (
	`garden_id` INT NOT NULL PRIMARY KEY,
	`open_hours` JSON,
	`contact_email` VARCHAR(100),
	`contact_phone` INT UNSIGNED
);

ALTER TABLE urban_eden.custom_content ADD CONSTRAINT fk_custom_content_garden
FOREIGN KEY (garden_id) REFERENCES urban_eden.garden(id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

CREATE TABLE `garden_admin` (
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`admin_id` INT NOT NULL,
	`garden_id` INT NOT NULL
);

ALTER TABLE urban_eden.garden_admin ADD CONSTRAINT fk_garden_admin_dashboard_user
FOREIGN KEY (admin_id) REFERENCES urban_eden.dashboard_user(id)
ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE urban_eden.garden_admin ADD CONSTRAINT fk_garden_admin_garden
FOREIGN KEY (garden_id) REFERENCES urban_eden.garden(id)
ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE  TABLE `user_contact` (
	`user_id` INT NOT NULL,
	`source_table` ENUM('portal_user','dashboard_user') NOT NULL,
	`email` VARCHAR(255),
	`phone` BIGINT UNSIGNED,
	CONSTRAINT pk_user_contact PRIMARY KEY (`user_id`, `source_table`)
);

ALTER TABLE urban_eden.user_contact ADD CONSTRAINT fk_user_contact_dashboard_user
FOREIGN KEY (user_id) REFERENCES urban_eden.dashboard_user(id)
ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE urban_eden.user_contact ADD CONSTRAINT fk_user_contact_portal_user
FOREIGN KEY (user_id) REFERENCES urban_eden.portal_user(id)
ON DELETE NO ACTION ON UPDATE NO ACTION;
