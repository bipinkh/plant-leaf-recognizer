-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 04, 2017 at 04:32 AM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `plantdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `plantdetails`
--

CREATE TABLE `plantdetails` (
  `id` smallint(20) NOT NULL,
  `name` char(30) NOT NULL,
  `sc_name` char(30) NOT NULL,
  `Link` varchar(70) NOT NULL,
  `other_names` varchar(200) NOT NULL,
  `Climate` varchar(100) NOT NULL,
  `Dimension` varchar(1000) NOT NULL,
  `Flower and Fruits` varchar(100) NOT NULL,
  `Bllooming Season` varchar(100) NOT NULL,
  `About` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `plantdetails`
--

INSERT INTO `plantdetails` (`id`, `name`, `sc_name`, `Link`, `other_names`, `Climate`, `Dimension`, `Flower and Fruits`, `Bllooming Season`, `About`) VALUES
(1, 'Hansaraj', 'Magnolia macrophylla', 'https://en.wikipedia.org/wiki/Magnolia_macrophylla', 'Bigleaf magnolia', 'Tropical region', '15–20 m tall', 'Smaller flowers, longer fruits', 'late spring', 'Bigleaf magnolia is often short-lived under cultivation unless its rather demanding requirements are met. This tree likes loose, undisturbed rich mesic soil (or mulch and compost substitutes) in full sun or part shade with plenty of moisture. This tree will likely succeed in sites that closely mimic its natural habitat and where it is protected from strong wind which can tatter its large foliage. It can be grown farther north than its southernly range suggests, but needs watering during extended dry periods. This plant is generally problem free.'),
(2, 'Kartike Bodi', 'Vigna unguiculata', 'https://en.wikipedia.org/wiki/Cowpea', 'Cowpea', 'Tropical region', '2m tall', 'purple, pink, yellow, white and blue flowers', 'Summer and autumn', 'Cowpeas are grown mostly for their edible beans, although the leaves, green peas and green pea pods can also be consumed, meaning the cowpea can be used as a food source before the dried peas are harvested.[48] Like other legumes, cowpea grain is cooked to make it edible, usually by boiling.[49] Cowpeas can be prepared in stews, soups, purees and casseroles,[50][51] but the most common way to eat them is in curries.'),
(3, 'Khari', 'Celtis australis', 'https://en.wikipedia.org/wiki/Celtis_australis', 'European nettle tree, Mediterranean hackberry, lote tree, or honeyberry', 'Mediterranean climate', '18 m tall', 'no flower', 'throughout the year', 'It is often planted as an ornamental as it is resistant to air pollution and long-living. The fruit of this tree is sweet and edible, and can be eaten raw or cooked. The leaves and fruit are astringent, lenitive and stomachic. Decoction of both leaves and fruit is used in the treatment of amenorrhoea, heavy menstrual and inter-menstrual bleeding and colic. The decoction can also be used to astringe the mucous membranes in the treatment of diarrhoea, dysentery and peptic ulcers. A yellow dye is obtained from the bark. '),
(4, 'Lalupate', 'Euphorbia pulcherrima', 'https://en.wikipedia.org/wiki/Poinsettia', 'Poinsettia', 'Tropical region', '0.6 – 4 m tall ', 'small yellow structures found in the center of each leaf bunch', 'summer', 'In the United States and perhaps elsewhere, there is a common misconception that the poinsettia is highly toxic. This misconception was spread by a 1919 urban legend of a two-year-old child dying after consuming a poinsettia leaf.'),
(5, 'Payou', 'Prunus cerasoides', 'https://en.wikipedia.org/wiki/Prunus_cerasoides', 'Himalayan Cherry', 'Temperate region', '30m tall', 'can be eaten raw or cooked', 'Summer', 'Prunus cerasoides is cultivated as an ornamental tree. The tree thrives in well-drained and moisture-retentive loamy soil, in an open, sunny, and sheltered location.The fruits and the leaves give a dark green dye. Seeds can be used in the manufacture of necklaces.\r\n\r\nThe wood is hard, strong, durable and aromatic, and branches are used as walking sticks.'),
(6, 'Peepal', 'Ficus religiosa', 'https://en.wikipedia.org/wiki/Ficus_religiosa', 'Sacred fig, bodhi tree, pippala tree', 'Tropical and sub-tropical region', '30m tall', 'no fruit', 'spring', 'Ficus religiosa is used in traditional medicine for about 50 types of disorders including asthma, diabetes, diarrhea, epilepsy, gastric problems, inflammatory disorders, infectious and sexual disorders'),
(7, 'Rose', 'Hulthemia × Rosa', 'https://en.wikipedia.org/wiki/Rose', '', 'Tropical and temperate', '3-5m tall', 'different colored flower', 'spring and summer', 'Roses are best known as ornamental plants grown for their flowers in the garden and sometimes indoors. They have been also used for commercial perfumery and commercial cut flower crops. Some are used as landscape plants, for hedging and for other utilitarian purposes such as game cover and slope stabilization. They also have minor medicinal uses.'),
(8, 'Saucer magnolia', 'Magnolia x soulangeana', 'https://en.wikipedia.org/wiki/Magnolia_%C3%97_soulangeana', 'Magnolia denudata, Magnolia liliiflora', 'Temperate region', '3-5m tall', 'white, pink and maroon flowers', 'spring and summer', 'Magnolia × soulangeana is notable for its ease of cultivation, and its relative tolerance to wind and alkaline soils (two vulnerabilities of many other magnolias). The cultivar \'Brozzonii\' has gained the Royal Horticultural Society\'s Award of Garden Merit.'),
(9, 'Silam', 'Perilla frutescens', 'https://en.wikipedia.org/wiki/Perilla_frutescens', 'Perilla, Korean perilla', 'Tropical region', '60–90 cm tall', 'schizocarp', 'summer and autumn', 'Perilla is used in traditional medicine as an infusion for respiratory and gastrointestinal complaints and recently in clinical trials for the treatment of various cancers.Perilla seeds are rich in dietary fiber and dietary minerals such as calcium, iron, niacin, protein, and thiamine.[13] Perilla leaves are also rich in dietary fiber and dietary minerals, such as calcium, iron, potassium, and vitamins A, C and riboflavin.[13] Perilla seed oil has anti-inflammatory properties, and perilla leaf components are under preliminary research for potential anti-inflammatory properties.[14] Perilla oil, with one of the highest proportion of omega-3 fatty acids, is beneficial to human health and in prevention of various diseases like cardiovascular disorders, cancer, inflammatory and rheumatoid arthritis, etc.'),
(10, 'Sunflower', 'Helianthus Compositae', 'https://en.wikipedia.org/wiki/Helianthus', '-', 'Tropical and temperate', '3m tall', 'Flowers with yellow petals and brown circular centre.', 'Hot Summer', 'Sunflowers thrive in slightly acidic to somewhat alkaline (pH 6.0 to 7.5).They are heavy feeders so the soil needs to be nutrient-rich with organic.They are distinguished technically by the fact that the ray florets (when present) are sterile, and by the presence on the disk flowers of a pappus that is of two awn-like scales that are caducous (that is, easily detached and falling at maturity). Some species also have additional shorter scales in the pappus, and there is one species that lacks a pappus entirely. Another technical feature that distinguishes the genus more reliably, but requires a microscope to see, is the presence of a prominent, multicellular appendage at the apex of the style. Sunflowers are especially well known for their symmetry based on Fibonacci numbers and the Golden angle.'),
(11, 'Sword lily', 'gladios hybridus', 'https://en.wikipedia.org/wiki/Gladiolus', 'Gladiolus', 'Mediterranean and tropical', '1-2m tall', 'pink, orange,red, yellow and white flowers', 'Summer and autumn', 'The genus Gladiolus contains about 300 species, the World Checklist of Selected Plant Families had over 276 species in 1988,[10] As of February 2017, it accepted 300 species.\r\nThere are 260 species of Gladiolus endemic in southern Africa,[7] and 76 in tropical Africa. About 10 species are native to Eurasia.[17]'),
(12, 'Tea', 'Camellia sinensis', 'https://en.wikipedia.org/wiki/Camellia_sinensis', 'te', 'Tropical and sub-tropical region', '2m tall', 'white flowers', 'spring', 'The leaves have been used in traditional Chinese medicine and other medical systems to treat asthma (functioning as a bronchodilator), angina pectoris, peripheral vascular disease, and coronary artery disease.\r\n\r\nAmong other bioactivities, (-)-catechin from C. sinensis acts as an agonist of the nuclear receptor protein peroxisome proliferator-activated receptor gamma, that is a current pharmacological target for the treatment of diabetes type 2.[18]\r\n\r\nTea may have some negative impacts on health, such as over-consumption of caffeine, and the presence of oxalates in tea.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `plantdetails`
--
ALTER TABLE `plantdetails`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
