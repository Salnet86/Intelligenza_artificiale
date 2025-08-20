
CREATE TABLE `chatlog` (
  `id` int NOT NULL,
  `domanda` text,
  `risposta` text,
  `data` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

