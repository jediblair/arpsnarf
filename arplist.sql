CREATE TABLE `arplist` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `routerip` varchar(15) DEFAULT NULL,
  `portindex` mediumint(9) DEFAULT NULL,
  `alias` varchar(64) DEFAULT NULL,
  `description` varchar(64) DEFAULT NULL,
  `arpip` varchar(15) DEFAULT NULL,
  `arpmac` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `arp_unique` (`routerip`,`portindex`,`arpip`,`arpmac`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
