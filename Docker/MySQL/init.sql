
DROP DATABASE SHABERIBA;
DROP USER 'user';

CREATE USER 'user' IDENTIFIED BY 'user';
CREATE DATABASE SHABERIBA;
USE SHABERIBA;
GRANT ALL PRIVILEGES ON SHABERIBA.* TO 'user';

CREATE TABLE users (
    uid VARCHAR(255) PRIMARY KEY,
    user_name VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    update_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE channels (
    id INT  AUTO_INCREMENT PRIMARY KEY,
    uid VARCHAR(255) NOT NULL,
    name VARCHAR(255) UNIQUE NOT NULL,
    abstract VARCHAR(255),
    update_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    category VARCHAR(255) ,
    FOREIGN KEY (uid) REFERENCES users(uid)
);

CREATE TABLE messages (
    id INT  AUTO_INCREMENT PRIMARY KEY,
    uid VARCHAR(255) NOT NULL,
    cid INT NOT NULL,
    message TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    hidden_flag BOOLEAN  NOT NULL DEFAULT FALSE,
    FOREIGN KEY (uid) REFERENCES users(uid),
    FOREIGN KEY (cid) REFERENCES channels(id)
);

INSERT INTO users(uid, user_name, email, password,update_at,create_at) VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578','2025-04-29','2025-04-29');
INSERT INTO channels(id, uid, name, abstract,update_at,create_at,category) VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','ぼっち部屋','テストさんの孤独な部屋です','2025-04-29','2025-04-29','test');
INSERT INTO messages(id, uid, cid, message, hidden_flag) VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', 1, '誰かかまってください、、',0);