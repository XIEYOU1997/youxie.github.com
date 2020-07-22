/*
 Navicat Premium Data Transfer

 Source Server         : TeamProject
 Source Server Type    : MySQL
 Source Server Version : 80018
 Source Host           : localhost:3306
 Source Schema         : SharedBikes

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : 65001

 Date: 06/11/2019 23:32:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Bikes
-- ----------------------------
DROP TABLE IF EXISTS `Bikes`;
CREATE TABLE `Bikes` (
  `idBikes` int(11) NOT NULL,
  `location` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `usable` varchar(45) DEFAULT NULL,
  `broken_time` float(75,0) DEFAULT NULL,
  PRIMARY KEY (`idBikes`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of Bikes
-- ----------------------------
BEGIN;
INSERT INTO `Bikes` VALUES (1, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (2, 'station3', 'no', 'yes', NULL);
INSERT INTO `Bikes` VALUES (3, 'station5', 'no', 'yes', NULL);
INSERT INTO `Bikes` VALUES (4, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (5, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (6, 'station2', 'no', 'yes', NULL);
INSERT INTO `Bikes` VALUES (7, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (8, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (9, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (10, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (11, 'station5', 'no', 'yes', 1573079168);
INSERT INTO `Bikes` VALUES (12, 'station12', 'no', 'no', 1573079296);
INSERT INTO `Bikes` VALUES (13, 'station2', 'no', 'yes', 1573079680);
INSERT INTO `Bikes` VALUES (14, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (15, 'station15', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (16, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (17, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (18, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (19, 'station19', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (20, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (21, 'station5', 'no', 'yes', 1573079168);
INSERT INTO `Bikes` VALUES (22, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (23, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (24, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (25, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (26, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (27, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (28, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (29, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (30, 'station4', 'no', 'yes', 1573078272);
INSERT INTO `Bikes` VALUES (31, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (32, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (33, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (34, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (35, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (36, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (37, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (38, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (39, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (40, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (41, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (42, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (43, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (44, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (45, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (46, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (47, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (48, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (49, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (50, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (51, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (52, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (53, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (54, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (55, 'station4', 'no', 'yes', NULL);
INSERT INTO `Bikes` VALUES (56, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (57, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (58, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (59, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (60, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (61, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (62, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (63, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (64, 'station2', 'no', 'yes', NULL);
INSERT INTO `Bikes` VALUES (65, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (66, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (67, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (68, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (69, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (70, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (71, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (72, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (73, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (74, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (75, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (76, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (77, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (78, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (79, 'station2', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (80, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (81, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (82, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (83, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (84, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (85, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (86, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (87, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (88, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (89, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (90, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (91, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (92, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (93, 'station1', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (94, 'station3', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (95, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (96, 'station5', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (97, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (98, 'station4', 'yes', 'yes', NULL);
INSERT INTO `Bikes` VALUES (99, 'station2', 'yes', 'yes', NULL);
COMMIT;

-- ----------------------------
-- Table structure for Managers
-- ----------------------------
DROP TABLE IF EXISTS `Managers`;
CREATE TABLE `Managers` (
  `ManagerName` text NOT NULL,
  `Password` text NOT NULL,
  PRIMARY KEY (`ManagerName`(10))
) ENGINE=InnoDB DEFAULT CHARSET=armscii8;

-- ----------------------------
-- Records of Managers
-- ----------------------------
BEGIN;
INSERT INTO `Managers` VALUES ('123', '123');
INSERT INTO `Managers` VALUES ('admin1', '456');
INSERT INTO `Managers` VALUES ('admin2', '4567');
INSERT INTO `Managers` VALUES ('manager1', '123');
COMMIT;

-- ----------------------------
-- Table structure for Operators
-- ----------------------------
DROP TABLE IF EXISTS `Operators`;
CREATE TABLE `Operators` (
  `Operators_ID` text NOT NULL,
  `password` text NOT NULL,
  PRIMARY KEY (`Operators_ID`(20))
) ENGINE=InnoDB DEFAULT CHARSET=armscii8;

-- ----------------------------
-- Records of Operators
-- ----------------------------
BEGIN;
INSERT INTO `Operators` VALUES ('987', '987');
INSERT INTO `Operators` VALUES ('999', '999');
COMMIT;

-- ----------------------------
-- Table structure for Users
-- ----------------------------
DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
  `email` varchar(45) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  `recentbill` varchar(45) DEFAULT NULL,
  `balance` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of Users
-- ----------------------------
BEGIN;
INSERT INTO `Users` VALUES ('10002@uk.com', '123', NULL, '15');
INSERT INTO `Users` VALUES ('111', '111', '0', '99.54');
INSERT INTO `Users` VALUES ('1111', '1111', '0.01', '12');
INSERT INTO `Users` VALUES ('1233333', '123333333', NULL, '33');
INSERT INTO `Users` VALUES ('2222', '111', '0', '-0.25');
INSERT INTO `Users` VALUES ('24433', '11', '0.01', '100');
INSERT INTO `Users` VALUES ('7851', 'hc3201', '0.01', '100');
INSERT INTO `Users` VALUES ('97879', '234', NULL, '50');
INSERT INTO `Users` VALUES ('aaa', 'aa', '0.01', '1');
INSERT INTO `Users` VALUES ('bbb', 'bbb', '0.01', '1');
INSERT INTO `Users` VALUES ('canh', '1111', '0.01', '100');
INSERT INTO `Users` VALUES ('exit', 'd', NULL, 'd');
INSERT INTO `Users` VALUES ('fuy', '11', '0.01', '13');
INSERT INTO `Users` VALUES ('ooo', 'ooo', NULL, '100');
INSERT INTO `Users` VALUES ('qqq', '111', '0.01', '100');
INSERT INTO `Users` VALUES ('www', 'www', '0.01', '99.99');
INSERT INTO `Users` VALUES ('xxx', 'xxx', '0.00', '12.0');
INSERT INTO `Users` VALUES ('```', '```', '0.01', '11.99');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
