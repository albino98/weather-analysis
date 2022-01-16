

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `weatherdataanalisys`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `forecastdata`
--

CREATE TABLE `forecastdata` (
  `temp` float NOT NULL,
  `feels_like` float NOT NULL,
  `temp_min` float NOT NULL,
  `temp_max` float NOT NULL,
  `pressure` int(11) NOT NULL,
  `sea_level` int(11) NOT NULL,
  `grnd_level` int(11) NOT NULL,
  `humidity` int(11) NOT NULL,
  `weather_id` int(11) NOT NULL,
  `weather_main` varchar(50) NOT NULL,
  `weather_desc` varchar(400) NOT NULL,
  `clouds_all` int(11) NOT NULL,
  `wind_speed` float NOT NULL,
  `wind_deg` int(11) NOT NULL,
  `wind_gust` float NOT NULL,
  `visibility` int(11) NOT NULL,
  `pop` float NOT NULL,
  `pod` varchar(1) NOT NULL,
  `dt` datetime NOT NULL COMMENT 'dateTime'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `forecastdata`
--

INSERT INTO `forecastdata` (`temp`, `feels_like`, `temp_min`, `temp_max`, `pressure`, `sea_level`, `grnd_level`, `humidity`, `weather_id`, `weather_main`, `weather_desc`, `clouds_all`, `wind_speed`, `wind_deg`, `wind_gust`, `visibility`, `pop`, `pod`, `dt`) VALUES
(5.77, 2.3, 4.26, 5.77, 1010, 1010, 951, 86, 804, 'Clouds', 'cielo coperto', 89, 5, 320, 9.29, 10000, 0, 'n', '2022-01-08 18:00:00'),
(4.93, 1.36, 4.13, 4.93, 1011, 1011, 951, 87, 804, 'Clouds', 'cielo coperto', 96, 4.77, 313, 8.93, 10000, 0, 'n', '2022-01-08 21:00:00'),
(2.38, -1.5, 2.38, 2.38, 1010, 1010, 950, 90, 803, 'Clouds', 'nubi sparse', 68, 4.22, 306, 8.45, 10000, 0, 'n', '2022-01-09 00:00:00'),
(1.5, -1.82, 1.5, 1.5, 1008, 1008, 948, 85, 800, 'Clear', 'cielo sereno', 6, 3.15, 310, 6.3, 10000, 0, 'n', '2022-01-09 03:00:00'),
(1.09, -0.56, 1.09, 1.09, 1007, 1007, 947, 79, 800, 'Clear', 'cielo sereno', 5, 1.53, 292, 1.72, 10000, 0, 'n', '2022-01-09 06:00:00'),
(4.41, 2.1, 4.41, 4.41, 1006, 1006, 946, 71, 804, 'Clouds', 'cielo coperto', 100, 2.62, 183, 4.41, 10000, 0, 'd', '2022-01-09 09:00:00'),
(6.68, 3.4, 6.68, 6.68, 1002, 1002, 943, 73, 804, 'Clouds', 'cielo coperto', 100, 5.09, 169, 5.75, 10000, 0, 'd', '2022-01-09 12:00:00'),
(4.97, 1.94, 4.97, 4.97, 1000, 1000, 941, 91, 500, 'Rain', 'pioggia leggera', 100, 3.8, 142, 7.04, 10000, 0.84, 'd', '2022-01-09 15:00:00');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `forecastdata`
--
ALTER TABLE `forecastdata`
  ADD PRIMARY KEY (`dt`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
