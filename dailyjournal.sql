SELECT * FROM Entries;
SELECT * FROM MOODS;

SELECT
    e.id,
    e.date,
    e.entry,
    e.mood_id,
    m.label
FROM entries e
JOIN Moods m ON e.mood_id = m.id

SELECT
    e.id,
    e.date,
    e.entry,
    e.mood_id,
    m.label
FROM entries e
JOIN Moods m ON e.mood_id = m.id
WHERE e.entry LIKE '%a%'

ALTER TABLE Entries
ADD concepts DataType 
    DEFAULT coding;