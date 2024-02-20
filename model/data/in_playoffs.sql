-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 06, 2024 at 05:32 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nba`
--

-- --------------------------------------------------------

--
-- Table structure for table `in_playoffs`
--

CREATE TABLE `in_playoffs` (
  `Season` varchar(10) NOT NULL,
  `Atlanta-Hawks` tinyint(1) DEFAULT NULL,
  `Boston-Celtics` tinyint(1) DEFAULT NULL,
  `Brooklyn-Nets` tinyint(1) DEFAULT NULL,
  `Charlotte-Hornets` tinyint(1) DEFAULT NULL,
  `Chicago-Bulls` tinyint(1) DEFAULT NULL,
  `Cleveland-Cavaliers` tinyint(1) DEFAULT NULL,
  `Dallas-Mavericks` tinyint(1) DEFAULT NULL,
  `Denver-Nuggets` tinyint(1) DEFAULT NULL,
  `Detroit-Pistons` tinyint(1) DEFAULT NULL,
  `Golden-State-Warriors` tinyint(1) DEFAULT NULL,
  `Houston-Rockets` tinyint(1) DEFAULT NULL,
  `Indiana-Pacers` tinyint(1) DEFAULT NULL,
  `Los-Angeles-Clippers` tinyint(1) DEFAULT NULL,
  `Los-Angeles-Lakers` tinyint(1) DEFAULT NULL,
  `Memphis-Grizzlies` tinyint(1) DEFAULT NULL,
  `Miami-Heat` tinyint(1) DEFAULT NULL,
  `Milwaukee-Bucks` tinyint(1) DEFAULT NULL,
  `Minnesota-Timberwolves` tinyint(1) DEFAULT NULL,
  `New-Orleans-Pelicans` tinyint(1) DEFAULT NULL,
  `New-York-Knicks` tinyint(1) DEFAULT NULL,
  `Oklahoma-City-Thunder` tinyint(1) DEFAULT NULL,
  `Orlando-Magic` tinyint(1) DEFAULT NULL,
  `Philadelphia-Sixers` tinyint(1) DEFAULT NULL,
  `Phoenix-Suns` tinyint(1) DEFAULT NULL,
  `Portland-Trail-Blazers` tinyint(1) DEFAULT NULL,
  `Sacramento-Kings` tinyint(1) DEFAULT NULL,
  `San-Antonio-Spurs` tinyint(1) DEFAULT NULL,
  `Toronto-Raptors` tinyint(1) DEFAULT NULL,
  `Utah-Jazz` tinyint(1) DEFAULT NULL,
  `Washington-Wizards` tinyint(1) DEFAULT NULL
) ;

--
-- Dumping data for table `in_playoffs`
--

INSERT INTO `in_playoffs` (`Season`, `Atlanta-Hawks`, `Boston-Celtics`, `Brooklyn-Nets`, `Charlotte-Hornets`, `Chicago-Bulls`, `Cleveland-Cavaliers`, `Dallas-Mavericks`, `Denver-Nuggets`, `Detroit-Pistons`, `Golden-State-Warriors`, `Houston-Rockets`, `Indiana-Pacers`, `Los-Angeles-Clippers`, `Los-Angeles-Lakers`, `Memphis-Grizzlies`, `Miami-Heat`, `Milwaukee-Bucks`, `Minnesota-Timberwolves`, `New-Orleans-Pelicans`, `New-York-Knicks`, `Oklahoma-City-Thunder`, `Orlando-Magic`, `Philadelphia-Sixers`, `Phoenix-Suns`, `Portland-Trail-Blazers`, `Sacramento-Kings`, `San-Antonio-Spurs`, `Toronto-Raptors`, `Utah-Jazz`, `Washington-Wizards`) VALUES
('1990-1991', 1, 1, NULL, NULL, 1, NULL, NULL, NULL, 1, 1, 1, 1, NULL, 1, NULL, NULL, 1, NULL, NULL, 1, 1, NULL, 1, 1, 1, NULL, 1, NULL, 1, NULL),
('1991-1992', NULL, 1, 1, NULL, 1, 1, NULL, NULL, 1, 1, NULL, 1, 1, 1, NULL, 1, NULL, NULL, NULL, 1, 1, NULL, NULL, 1, 1, NULL, 1, NULL, 1, NULL),
('1992-1993', 1, 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL, 1, 1, 1, 1, NULL, NULL, NULL, NULL, NULL, 1, 1, NULL, NULL, 1, 1, NULL, 1, NULL, 1, NULL),
('1993-1994', 1, NULL, 1, NULL, 1, 1, NULL, 1, NULL, 1, 1, 1, NULL, NULL, NULL, 1, NULL, NULL, NULL, 1, 1, 1, NULL, 1, 1, NULL, 1, NULL, 1, NULL),
('1994-1995', 1, 1, NULL, 1, 1, 1, NULL, 1, NULL, NULL, 1, 1, NULL, 1, NULL, NULL, NULL, NULL, NULL, 1, 1, 1, NULL, 1, 1, NULL, 1, NULL, 1, NULL),
('1995-1996', 1, NULL, NULL, NULL, 1, 1, NULL, NULL, 1, NULL, 1, 1, NULL, 1, NULL, 1, NULL, NULL, NULL, 1, 1, 1, NULL, 1, 1, 1, 1, NULL, 1, NULL),
('1996-1997', 1, NULL, NULL, 1, 1, NULL, NULL, NULL, 1, NULL, 1, NULL, 1, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, NULL, 1, 1, NULL, NULL, NULL, 1, 1),
('1997-1998', 1, NULL, 1, 1, 1, 1, NULL, NULL, NULL, NULL, 1, 1, NULL, 1, NULL, 1, NULL, 1, NULL, 1, 1, NULL, NULL, 1, 1, NULL, 1, NULL, 1, NULL),
('1998-1999', 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, 1, 1, NULL, 1, NULL, 1, 1, 1, NULL, 1, NULL, 1, 1, 1, 1, 1, 1, NULL, 1, NULL),
('1999-2000', NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 1, NULL, NULL, 1, NULL, 1, NULL, 1, 1, 1, NULL, 1, 1, NULL, 1, 1, 1, 1, 1, 1, 1, NULL),
('2000-2001', NULL, NULL, NULL, 1, NULL, NULL, 1, NULL, NULL, NULL, NULL, 1, NULL, 1, NULL, 1, 1, 1, NULL, 1, NULL, 1, 1, 1, 1, 1, 1, 1, 1, NULL),
('2001-2002', NULL, 1, 1, 1, NULL, NULL, 1, NULL, 1, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, 1, NULL, NULL, 1, 1, 1, NULL, 1, 1, 1, 1, 1, NULL),
('2002-2003', NULL, 1, 1, NULL, NULL, NULL, 1, NULL, 1, NULL, NULL, 1, NULL, 1, NULL, NULL, 1, 1, 1, NULL, NULL, 1, 1, 1, 1, 1, 1, NULL, 1, NULL),
('2003-2004', NULL, 1, 1, NULL, NULL, NULL, 1, 1, 1, NULL, 1, 1, NULL, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL, NULL, 1, 1, NULL, NULL, NULL),
('2004-2005', NULL, 1, 1, NULL, 1, NULL, 1, 1, 1, NULL, 1, 1, NULL, NULL, 1, 1, NULL, NULL, NULL, NULL, 1, NULL, 1, 1, NULL, 1, 1, NULL, NULL, 1),
('2005-2006', NULL, NULL, 1, NULL, 1, 1, 1, 1, 1, NULL, NULL, 1, 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, 1, 1, NULL, NULL, 1),
('2006-2007', NULL, NULL, 1, NULL, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, NULL, NULL, 1, NULL, 1, NULL, NULL, 1, 1, 1, 1),
('2007-2008', 1, 1, NULL, NULL, NULL, 1, 1, 1, 1, NULL, 1, NULL, NULL, 1, NULL, NULL, NULL, NULL, 1, NULL, NULL, 1, 1, 1, NULL, NULL, 1, 1, 1, 1),
('2008-2009', 1, 1, NULL, NULL, 1, 1, 1, 1, 1, NULL, 1, NULL, NULL, 1, NULL, 1, NULL, NULL, 1, NULL, NULL, 1, 1, NULL, 1, NULL, 1, NULL, 1, NULL),
('2009-2010', 1, 1, NULL, 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL, NULL, 1, NULL, 1, 1, NULL, NULL, NULL, 1, 1, NULL, 1, 1, NULL, 1, NULL, 1, NULL),
('2010-2011', 1, 1, NULL, NULL, 1, NULL, 1, 1, NULL, NULL, NULL, 1, NULL, 1, 1, 1, NULL, NULL, 1, 1, 1, 1, 1, NULL, 1, NULL, 1, NULL, NULL, NULL),
('2011-2012', 1, 1, NULL, NULL, 1, NULL, 1, 1, NULL, NULL, NULL, 1, 1, 1, 1, 1, NULL, NULL, NULL, 1, 1, 1, 1, NULL, NULL, NULL, 1, NULL, 1, NULL),
('2012-2013', 1, 1, 1, NULL, 1, NULL, NULL, 1, NULL, 1, 1, 1, 1, 1, 1, 1, 1, NULL, NULL, 1, 1, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL),
('2013-2014', 1, NULL, 1, 1, 1, NULL, 1, NULL, NULL, 1, 1, 1, 1, NULL, 1, 1, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, 1, NULL, 1, 1, NULL, 1),
('2014-2015', 1, 1, 1, NULL, 1, 1, 1, NULL, NULL, 1, 1, NULL, 1, NULL, 1, NULL, 1, NULL, 1, NULL, NULL, NULL, NULL, NULL, 1, NULL, 1, 1, NULL, 1),
('2015-2016', 1, 1, NULL, 1, NULL, 1, 1, NULL, 1, 1, 1, 1, 1, NULL, 1, 1, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, 1, NULL, 1, 1, NULL, NULL),
('2016-2017', 1, 1, NULL, NULL, 1, 1, NULL, NULL, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1, NULL, NULL, NULL, 1, NULL, NULL, NULL, 1, NULL, 1, 1, 1, 1),
('2017-2018', NULL, 1, NULL, NULL, NULL, 1, NULL, NULL, NULL, 1, 1, 1, NULL, NULL, NULL, 1, 1, 1, 1, NULL, 1, NULL, 1, NULL, 1, NULL, 1, 1, 1, 1),
('2018-2019', NULL, 1, 1, NULL, NULL, NULL, NULL, 1, 1, 1, 1, 1, 1, NULL, NULL, NULL, 1, NULL, NULL, NULL, 1, 1, 1, NULL, 1, NULL, 1, 1, 1, NULL),
('2019-2020', NULL, 1, 1, NULL, NULL, NULL, 1, 1, NULL, NULL, 1, 1, 1, 1, NULL, 1, 1, NULL, NULL, NULL, 1, 1, 1, NULL, 1, NULL, NULL, 1, 1, NULL),
('2020-2021', 1, 1, 1, NULL, NULL, NULL, 1, 1, NULL, NULL, NULL, NULL, 1, 1, 1, 1, 1, NULL, NULL, 1, NULL, NULL, 1, 1, 1, NULL, NULL, NULL, 1, 1),
('2021-2022', 1, 1, 1, NULL, 1, NULL, 1, 1, NULL, 1, NULL, NULL, NULL, NULL, 1, 1, 1, 1, 1, NULL, NULL, NULL, 1, 1, NULL, NULL, NULL, 1, 1, NULL),
('2022-2023', 1, 1, 1, NULL, NULL, 1, NULL, 1, NULL, 1, NULL, NULL, 1, 1, 1, 1, 1, 1, NULL, 1, NULL, NULL, 1, 1, NULL, 1, NULL, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `in_playoffs`
--
ALTER TABLE `in_playoffs`
  ADD PRIMARY KEY (`Season`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
