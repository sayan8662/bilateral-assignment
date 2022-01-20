SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


-- --------------------------------------------------------

--
-- Table structure for table `files`
--

DROP TABLE IF EXISTS `files`;
CREATE TABLE IF NOT EXISTS `files` (
  `File_Name` varchar(100) NOT NULL,
  `Status` int(5) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;
