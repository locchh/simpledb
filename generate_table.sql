-- create table 
CREATE TABLE PERSONS IF NOT EXISTS(
    person_id INTEGER,
    first_name VARCHAR(100) NOT NULL;
    last_name VARCHAR(100) NOT NULL;
    birth_day DATE;
    email_address VARCHAR(150) UNIQUE NOT NULL;
    local_address VARCHAR(200),
    PRIMARY KEY (person_id)
);

-- insert few data
INSERT INTO PERSONS VALUE