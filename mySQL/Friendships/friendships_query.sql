Use Friendships;
-- 
-- INSERT INTO users (first_name, last_name, created_at, updated_at)
-- VALUES ('Jessica', 'Davidson', NOW(), NOW());

-- SELECT * FROM users
-- 
-- 
-- INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
-- VALUES (2,1,NOW(),NOW());

Select * FROM friendships;

SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;





