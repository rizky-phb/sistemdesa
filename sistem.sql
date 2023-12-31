-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 19, 2023 at 04:29 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sistem`
--

-- --------------------------------------------------------

--
-- Table structure for table `berita`
--

CREATE TABLE `berita` (
  `id` int(11) NOT NULL,
  `judul` varchar(100) NOT NULL,
  `gambar` varchar(100) NOT NULL,
  `deskripsi` text NOT NULL,
  `tanggal` date NOT NULL DEFAULT current_timestamp(),
  `link` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `berita`
--

INSERT INTO `berita` (`id`, `judul`, `gambar`, `deskripsi`, `tanggal`, `link`) VALUES
(2, 'CC#11 day 1', 'MuMu20230624010544.png', 'EZ CC', '2023-06-26', 'CC11_day_1'),
(3, 'CC#11 permanen map', 'MuMu20230703144805.png', 'Welcome to my gameplay series. i am play just for fun, so I hope this video helps you. ', '2023-07-04', 'CC11_permanen_map'),
(4, 'sadsa', 'belalang sangit.JPG', 'sdqwfewf', '2023-07-05', 'sadsa'),
(6, 'tikus', 'padi .jpg', 'tgbrthrt\r\n', '2023-07-05', 'tikus'),
(8, 'csdc', 'WhatsApp Image 2023-07-09 at 14.41.21.jpeg', '1. Penerimaan Pajak, mulai tahun 2021 s/d 2022 mengalami peningkatan. Peningkatan dari tahun 2021 ke tahun 2022 adalah sebesar 87 %, sedangkan dari tahun 2022 ke tahun 2023 adalah sebesar 92.%. Adapun penyebab dari peningkatan penerimaan pajak selama tahun 2021 s/d 2023 adalah sebagia berikut: \r\nscs\r\ncsc\r\ncsd\r\ndw\r\nwad bold\r\n', '2023-07-09', 'csdc');

-- --------------------------------------------------------

--
-- Table structure for table `dana`
--

CREATE TABLE `dana` (
  `id` int(11) NOT NULL,
  `tahun` int(11) NOT NULL,
  `gambar` varchar(100) NOT NULL,
  `total_anggaran` int(100) NOT NULL,
  `realisasi` int(100) NOT NULL,
  `lebih` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dana`
--

INSERT INTO `dana` (`id`, `tahun`, `gambar`, `total_anggaran`, `realisasi`, `lebih`) VALUES
(6, 2022, 'WhatsApp Image 2023-07-09 at 14.41.21(1).jpeg', 1900624136, 1858460748, 42163388),
(7, 2023, 'WhatsApp Image 2023-07-09 at 14.41.21(1).jpeg', 2147483647, 0, 13123121);

-- --------------------------------------------------------

--
-- Table structure for table `monografi`
--

CREATE TABLE `monografi` (
  `id` int(11) NOT NULL,
  `tahun` int(100) NOT NULL,
  `jpenduduk` int(11) NOT NULL,
  `jkk` int(11) NOT NULL,
  `laki` int(11) NOT NULL,
  `perempuan` int(11) NOT NULL,
  `jkkprese` int(11) NOT NULL,
  `jkkseja` int(11) NOT NULL,
  `jkkkaya` int(11) NOT NULL,
  `jkksedang` int(11) NOT NULL,
  `jkkmiskin` int(11) NOT NULL,
  `islam` int(11) NOT NULL,
  `kristen` int(11) NOT NULL,
  `protestan` int(11) NOT NULL,
  `katolik` int(11) NOT NULL,
  `hindu` int(11) NOT NULL,
  `budha` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `monografi`
--

INSERT INTO `monografi` (`id`, `tahun`, `jpenduduk`, `jkk`, `laki`, `perempuan`, `jkkprese`, `jkkseja`, `jkkkaya`, `jkksedang`, `jkkmiskin`, `islam`, `kristen`, `protestan`, `katolik`, `hindu`, `budha`) VALUES
(1, 2021, 7063, 2434, 3733, 3830, 313, 480, 306, 798, 537, 6916, 65, 82, 0, 0, 0),
(2, 2022, 7352, 2648, 3632, 3720, 313, 480, 306, 798, 537, 7039, 207, 0, 88, 3, 13);

-- --------------------------------------------------------

--
-- Table structure for table `sejarah_desa`
--

CREATE TABLE `sejarah_desa` (
  `id` int(11) NOT NULL,
  `sejarah` text NOT NULL,
  `visi` text NOT NULL,
  `misi` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sejarah_desa`
--

INSERT INTO `sejarah_desa` (`id`, `sejarah`, `visi`, `misi`) VALUES
(1, '<p><strong>Pada Tahun 1942</strong> Tegal kembali menjadi Kabupaten lagi, setelah sebelumnya bergantiganti fungsi sebagai Karesidenan. Pangkah merupakan salah satu Kawedanan. Sedagkan kawedanan yang lain pada sat itu adlah Slawi, Adiwerna, Balapulang, dan Bumijawa. Pada era awal kemerdekaan ,Pangkah dijadikan salah satu wilayah cabang gesadassadadadrakan tiga daerah , yaitu Brebes, Tegal dan Pemalang. Pangkah makin hari makin ramai dengan bertambahnya buruh pabrik.Pada walnya Desa Pangkah terbentuk dari Pedukuhan Pesawahan, Benda, Kauman,Sabrang, Posong, Wungu. Sekitar tahun 1985 berdiri komplek perumahan oleh pengembang yang dikenaldengan Griya Pangkah Indah (Gripin). Pemukiman tersebut kemudian masuk menjadi pedukuhan di desa pangkah dengan nama dukuh waringin. Sebagai pusat ibukota kecamatan ,perkembangan desa Pangkah sangat pesat.</p>', '<p>wdaTerbangunnya tata kelola pemerintahan desa yang baik, bersih, dan jujur serta melayani masyarakat desa Pangkah secara menyeluruh demi terwujudnya desa Pangkah yang maju dan sejahtera yang berakar pada nilai Pancasila serta budaya dan agama</p>', '<p>blablahjkjansjw</p><p> dwkqnd</p><p> cwq kc qw\'c \' \' q\' wk; s</p><p> </p><p>1</p><p>2kmsak</p><ol><li>saodm</li><li>awmd </li><li>dmwo</li></ol>');

-- --------------------------------------------------------

--
-- Table structure for table `surat`
--

CREATE TABLE `surat` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `hp` int(15) NOT NULL,
  `keterangan` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `surat`
--

INSERT INTO `surat` (`id`, `nama`, `hp`, `keterangan`) VALUES
(2, 'Adi Sangjaya', 857123, 'asgdhsadabsabhdsadwq'),
(3, 'Adi Sangjaya', 857123, 'asgdhsadabsabhdsadwq');

-- --------------------------------------------------------

--
-- Table structure for table `tanah`
--

CREATE TABLE `tanah` (
  `id` int(11) NOT NULL,
  `luas` float NOT NULL,
  `sawahteri` int(11) NOT NULL,
  `sawahhu` int(11) NOT NULL,
  `pemukiman` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tanah`
--

INSERT INTO `tanah` (`id`, `luas`, `sawahteri`, `sawahhu`, `pemukiman`) VALUES
(1, 215, 88, 28, 96);

-- --------------------------------------------------------

--
-- Table structure for table `user_admin`
--

CREATE TABLE `user_admin` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_admin`
--

INSERT INTO `user_admin` (`id`, `username`, `password`) VALUES
(3, 'admin', '$2b$12$77bhMr.tHSXAD7B8Mn//Me6kkPsMqK14j1.1ctZyQWoKMzSby1.hi'),
(4, 'admin2', '$2b$12$eFZKgdFxyH4gilF8KsZ30O5iQqc/sjK580a42X1rDzm5waVU3Gs0S');

-- --------------------------------------------------------

--
-- Table structure for table `wilayah`
--

CREATE TABLE `wilayah` (
  `id` int(11) NOT NULL,
  `utara` varchar(100) NOT NULL,
  `selatan` varchar(100) NOT NULL,
  `timur` varchar(100) NOT NULL,
  `barat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wilayah`
--

INSERT INTO `wilayah` (`id`, `utara`, `selatan`, `timur`, `barat`) VALUES
(1, 'Desa Talok', 'Desa Penusupan', 'Desa Bogares Lor', 'Desa Talok');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `berita`
--
ALTER TABLE `berita`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dana`
--
ALTER TABLE `dana`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `monografi`
--
ALTER TABLE `monografi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sejarah_desa`
--
ALTER TABLE `sejarah_desa`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `surat`
--
ALTER TABLE `surat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tanah`
--
ALTER TABLE `tanah`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_admin`
--
ALTER TABLE `user_admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `wilayah`
--
ALTER TABLE `wilayah`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `berita`
--
ALTER TABLE `berita`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `dana`
--
ALTER TABLE `dana`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `monografi`
--
ALTER TABLE `monografi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sejarah_desa`
--
ALTER TABLE `sejarah_desa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `surat`
--
ALTER TABLE `surat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tanah`
--
ALTER TABLE `tanah`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_admin`
--
ALTER TABLE `user_admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `wilayah`
--
ALTER TABLE `wilayah`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
