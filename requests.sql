-- ������ ��� ���������:

/* �������� �� �������� ������� �����������. ������������ SELECT ��� ��������� ������� ����������� ����������� �� ���� user_id. */
SELECT * FROM tasks WHERE user_id = 10;

/* ������� �������� �� ������ ��������. ������������ ������� ��� ������ ������� � ���������� ��������, ���������, 'new'. */
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

/* ������� ������ ����������� ��������. ����� ������ ����������� �������� �� 'in progress' ��� ����� ������. */
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 6;

/* �������� ������ ������������, �� �� ����� ������� ��������. ������������ ��������� SELECT, WHERE NOT IN � �������. */
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

/* ������ ���� �������� ��� ����������� �����������. ������������ INSERT ��� ��������� ������ ��������. */
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('create new function on C++', 'calculate A+B*2', (SELECT id FROM status WHERE name = 'new'), 22);

/* �������� �� ��������, �� �� �� ���������. ������� ��������, ��� ������ �� � '���������'. */
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

/* �������� ��������� ��������. ������������ DELETE ��� ��������� �������� �� ���� id. */
DELETE FROM tasks WHERE id = 1;

/* ������ ������������ � ������ ����������� ������. ������������ SELECT �� ������ LIKE ��� ���������� �� ����������� ������. */
SELECT * FROM users WHERE email LIKE '%@example.com';

/* ������� ��'� �����������. ����� ��'� ����������� �� ��������� UPDATE. */
UPDATE users SET fullname = 'Anthony Duncan junior' WHERE id = 30;

/* �������� ������� ������� ��� ������� �������. ������������ SELECT, COUNT, GROUP BY ��� ���������� ������� �� ���������.*/
SELECT status.name, COUNT(tasks.id) AS task_count
FROM tasks
JOIN status ON tasks.status_id = status.id
GROUP BY status.name;

/* �������� ��������, �� ��������� ������������ � ������ �������� �������� ���������� �����. ������������ SELECT � ������ LIKE � ������� � JOIN, ��� ������� ��������, ��������� ������������, ��� ���������� ����� ������ ������ ����� (���������, '%@example.com').*/
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';

/* �������� ������ �������, �� �� ����� �����. ������� ��������, � ���� ������� ����.*/
SELECT * FROM tasks WHERE description IS NULL OR description = '';

/* ������� ������������ �� ��� ��������, �� � � ������ 'in progress'. ������������ INNER JOIN ��� ��������� ������ ������������ �� ���� ������� �� ������ ��������.*/
SELECT users.fullname, tasks.title
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
INNER JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';

/* �������� ������������ �� ������� ���� �������. ������������ LEFT JOIN �� GROUP BY ��� ������ ������������ �� ��������� ���� �������.*/
SELECT users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id, users.fullname;

