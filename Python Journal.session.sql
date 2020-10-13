
CREATE TABLE `Moods` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label`    TEXT NOT NULL
);

CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'date'	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);
CREATE TABLE `Tags` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`subject`  TEXT NOT NULL
);

CREATE TABLE `EntryTags` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`entry_id`	INTEGER NOT NULL,
	`tag_id`	INTEGER NOT NULL,
	FOREIGN KEY(`entry_id`) REFERENCES `Entries`(`id`)
	FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)

);


INSERT INTO `Moods` VALUES (null, 'Cheerful');
INSERT INTO `Moods` VALUES (null, 'Reflective');
INSERT INTO `Moods` VALUES (null, 'Gloomy');
INSERT INTO `Moods` VALUES (null, 'Humorous');

INSERT INTO `Entries` VALUES (null, '2020-07-14', 'We talked about HTML components and how to make grid layouts with Flexbox in CSS.', 2);
INSERT INTO `Entries` VALUES (null, '2020-07-13', 'We learned how to add Javascript into our projects in order to automate the writing of html when adding new content', 1);

INSERT INTO `Tags` VALUES (null, 'API');
INSERT INTO `Tags` VALUES (null, 'Components');
INSERT INTO `Tags` VALUES (null, 'Fetch');
INSERT INTO `Tags` VALUES (null, 'HTML');
INSERT INTO `Tags` VALUES (null, 'CSS');
INSERT INTO `Tags` VALUES (null, 'Javascript');

INSERT INTO `EntryTags` VALUES (null, 1, 2);
INSERT INTO `EntryTags` VALUES (null, 1, 4);
INSERT INTO `EntryTags` VALUES (null, 2, 6);
INSERT INTO `EntryTags` VALUES (null, 2, 5);
INSERT INTO `EntryTags` VALUES (null, 2, 3);



