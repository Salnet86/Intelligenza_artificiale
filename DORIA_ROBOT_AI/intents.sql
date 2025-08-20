

CREATE TABLE `intents` (
  `id` int NOT NULL,
  `intent` varchar(50) DEFAULT NULL,
  `pattern` text,
  `response` text
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


INSERT INTO `intents` (`id`, `intent`, `pattern`, `response`) VALUES
(1, 'saluti', 'ciao', 'Ciao! ');


