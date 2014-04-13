-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 06, 2012 at 12:50 AM
-- Server version: 5.5.27
-- PHP Version: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `textbook`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE IF NOT EXISTS `book` (
  `isbn` varchar(13) NOT NULL,
  `title` varchar(20) NOT NULL,
  `online_support` tinyint(1) NOT NULL,
  `previous_use` tinyint(1) NOT NULL,
  `edition` int(2) NOT NULL,
  `free_copy` tinyint(1) NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`isbn`, `title`, `online_support`, `previous_use`, `edition`, `free_copy`, `price`) VALUES
('1020899345762', 'Python', 0, 1, 1, 1, 80.43),
('2147483647654', 'PythonProgramming', 0, 0, 3, 0, 124.89),
('3456879233456', 'Intro to Python', 1, 0, 2, 1, 50.03),
('6751238457349', 'PyPy', 1, 1, 5, 0, 34),
('9018908765789', 'Data Structures in C', 1, 0, 7, 1, 121.8),
('9090909090901', 'Discrete Mathematics', 1, 0, 1, 1, 122.8);

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE IF NOT EXISTS `courses` (
  `courseid` varchar(7) NOT NULL,
  `coursename` varchar(30) NOT NULL,
  PRIMARY KEY (`courseid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`courseid`, `coursename`) VALUES
('cse1002', 'Intro to Programming'),
('cse2383', 'Data Structures & Algorithms'),
('cse2813', 'Discrete Structures');

-- --------------------------------------------------------

--
-- Table structure for table `professor`
--

CREATE TABLE IF NOT EXISTS `professor` (
  `ssn` int(9) NOT NULL,
  `name` varchar(20) NOT NULL,
  `id` varchar(6) NOT NULL,
  `password` int(6) NOT NULL,
  PRIMARY KEY (`ssn`),
  KEY `ssn` (`ssn`),
  KEY `ssn_2` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `professor`
--

INSERT INTO `professor` (`ssn`, `name`, `id`, `password`) VALUES
(608345723, 'Gandalf', 'gan343', 456784),
(909909909, 'Ted', 'ted103', 123456),
(912213897, 'Patrick', 'pat345', 987654);

-- --------------------------------------------------------

--
-- Table structure for table `recommendation`
--

CREATE TABLE IF NOT EXISTS `recommendation` (
  `ssn` int(9) NOT NULL,
  `isbn` varchar(13) NOT NULL,
  PRIMARY KEY (`ssn`,`isbn`),
  KEY `ssn` (`ssn`),
  KEY `isbn` (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `recommendation`
--

INSERT INTO `recommendation` (`ssn`, `isbn`) VALUES
(608345723, '1020899345762'),
(608345723, '2147483647654'),
(608345723, '6751238457349'),
(909909909, '3456879233456'),
(912213897, '9018908765789');

-- --------------------------------------------------------

--
-- Table structure for table `sections`
--

CREATE TABLE IF NOT EXISTS `sections` (
  `courseid` varchar(7) NOT NULL,
  `sectionid` int(1) NOT NULL,
  PRIMARY KEY (`courseid`,`sectionid`),
  KEY `courseid` (`courseid`),
  KEY `sectionid` (`sectionid`),
  KEY `sectionid_2` (`sectionid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sections`
--

INSERT INTO `sections` (`courseid`, `sectionid`) VALUES
('cse1002', 1),
('cse1002', 2),
('cse2383', 3);

-- --------------------------------------------------------

--
-- Table structure for table `teaches`
--

CREATE TABLE IF NOT EXISTS `teaches` (
  `courseid` varchar(7) NOT NULL,
  `sectionid` int(1) NOT NULL,
  `ssn` int(9) NOT NULL,
  PRIMARY KEY (`courseid`,`sectionid`,`ssn`),
  KEY `courseid` (`courseid`,`sectionid`,`ssn`),
  KEY `sectionid` (`sectionid`),
  KEY `ssn` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teaches`
--

INSERT INTO `teaches` (`courseid`, `sectionid`, `ssn`) VALUES
('cse1002', 1, 608345723),
('cse1002', 2, 909909909),
('cse2383', 3, 912213897);

-- --------------------------------------------------------

--
-- Table structure for table `uses`
--

CREATE TABLE IF NOT EXISTS `uses` (
  `courseid` varchar(7) NOT NULL,
  `isbn` varchar(13) NOT NULL,
  `fromdate` date NOT NULL,
  `todate` date NOT NULL,
  `usedtill` date NOT NULL,
  PRIMARY KEY (`courseid`,`isbn`),
  KEY `isbn` (`isbn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `uses`
--

INSERT INTO `uses` (`courseid`, `isbn`, `fromdate`, `todate`, `usedtill`) VALUES
('cse1002', '1020899345762', '2006-07-01', '2009-07-01', '2009-07-01'),
('cse1002', '2147483647654', '2009-07-01', '2012-07-01', '2011-01-01'),
('cse1002', '3456879233456', '2010-07-01', '2013-07-01', '2013-07-01'),
('cse1002', '6751238457349', '2012-05-01', '2015-05-01', '2012-01-01'),
('cse2383', '9018908765789', '2010-01-01', '2013-01-01', '2013-01-01'),
('cse2813', '9090909090901', '2011-01-01', '2014-01-01', '2014-01-01');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `recommendation`
--
ALTER TABLE `recommendation`
  ADD CONSTRAINT `recommendation_ibfk_1` FOREIGN KEY (`ssn`) REFERENCES `professor` (`ssn`),
  ADD CONSTRAINT `recommendation_ibfk_2` FOREIGN KEY (`isbn`) REFERENCES `book` (`isbn`);

--
-- Constraints for table `sections`
--
ALTER TABLE `sections`
  ADD CONSTRAINT `sections_ibfk_1` FOREIGN KEY (`courseid`) REFERENCES `courses` (`courseid`);

--
-- Constraints for table `teaches`
--
ALTER TABLE `teaches`
  ADD CONSTRAINT `teaches_ibfk_2` FOREIGN KEY (`sectionid`) REFERENCES `sections` (`sectionid`),
  ADD CONSTRAINT `teaches_ibfk_3` FOREIGN KEY (`ssn`) REFERENCES `professor` (`ssn`),
  ADD CONSTRAINT `teaches_ibfk_4` FOREIGN KEY (`courseid`) REFERENCES `courses` (`courseid`);

--
-- Constraints for table `uses`
--
ALTER TABLE `uses`
  ADD CONSTRAINT `uses_ibfk_2` FOREIGN KEY (`isbn`) REFERENCES `book` (`isbn`),
  ADD CONSTRAINT `uses_ibfk_3` FOREIGN KEY (`courseid`) REFERENCES `courses` (`courseid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
