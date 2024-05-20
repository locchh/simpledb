-- create table 
CREATE TABLE IF NOT EXISTS PERSONS(
    person_id SERIAL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    gender CHAR(2) NOT NULL,
    birth_day DATE,
    email_address VARCHAR(150) UNIQUE NOT NULL,
    local_address VARCHAR(200),
    PRIMARY KEY (person_id)
);

-- insert few data
-- INSERT INTO PERSONS VALUES ("Loc","Chuong","M","1996-01-07","locchuong@email.com"),
-- ("Dott. Sue","Battaglia","F","1990-04-21","battaglia-dott@email.com","Stretto Testa 3\nBorgo Gelsomina ligure, 56906 Terni (IM)"),
-- ("Sig. Giorgio","Ricci","M","1895-07-15","giorgio@hotmail.com","ontrada Mariani 01 Appartamento 46Sala a mare, 30911 L'Aquila (SV)"),
-- ("Ileana","Guerra","F","1994-06-04","GuerraIleana@gmail.com","Canale Bruno 81 Settimo Azue, 37320 Piacenza"),
-- ("testa","bastian","M","1981-10-29","testasebastian@gmail.com","Incrocio Rossetti 322 Borgo Ariel salentino, 06903 Genova (AL)");

INSERT INTO PERSONS (first_name, last_name, gender, birth_day, email_address, local_address)
VALUES 
    ('Loc','Chuong','M','1996-01-07','locchuong@email.com',NULL),
    ('John', 'Doe', 'M', '1990-05-15', 'john.doe@example.com', '123 Main St, Anytown'),
    ('Jane', 'Smith', 'F', '1995-08-20', 'jane.smith@example.com', '456 Elm St, Othertown'),
    ('Michael', 'Johnson', 'M', '1987-02-10', 'michael.johnson@example.com', '789 Oak St, Another Town'),
    ('Emily', 'Williams', 'F', '1983-11-25', 'emily.williams@example.com', '101 Pine St, Somewhere'),
    ('Christopher', 'Brown', 'M', '1992-09-30', 'christopher.brown@example.com', '222 Cedar St, Anywhere'),
    ('Jessica', 'Jones', 'F', '1998-04-05', 'jessica.jones@example.com', '333 Maple St, Nowhere'),
    ('Daniel', 'Garcia', 'M', '1994-06-18', 'daniel.garcia@example.com', '444 Birch St, Elsewhere'),
    ('Ashley', 'Martinez', 'F', '1989-12-12', 'ashley.martinez@example.com', '555 Walnut St, Everywhere'),
    ('Matthew', 'Hernandez', 'M', '1991-07-23', 'matthew.hernandez@example.com', '666 Pineapple St, Anyplace'),
    ('Sarah', 'Lopez', 'F', '1996-03-08', 'sarah.lopez@example.com', '777 Peach St, Somewhere');


-- view table
SELECT * FROM PERSONS;