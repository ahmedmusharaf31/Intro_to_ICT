CREATE DATABASE FAMILY_Ahmed_Musharaf;

USE FAMILY_Ahmed_Musharaf;

CREATE TABLE Immediate_Family (
  Name VARCHAR(255) NOT NULL,
  Date_of_Birth DATE NOT NULL
-- Relation column left intentionally
);

ALTER TABLE Immediate_Family
ADD COLUMN Relation VARCHAR(255) AFTER Date_of_Birth;

INSERT INTO Immediate_Family (Name, Date_of_Birth, Relation)
VALUES
  ('Ali Musharaf', '1980-01-01', 'Brother'),
  ('Fatima Musharaf', '1982-05-15', 'Sister'),
  ('Hassan Musharaf', '1985-11-20', 'Father'),
  ('Aisha Musharaf', '1987-03-08', 'Mother');

CREATE TABLE Maternal_Relatives (
  Name VARCHAR(255) NOT NULL,
  Date_of_Birth DATE NOT NULL
-- Relation column left intentionally
);

ALTER TABLE Maternal_Relatives
ADD COLUMN Relation VARCHAR(255) AFTER Date_of_Birth;

INSERT INTO Maternal_Relatives (Name, Date_of_Birth, Relation)
VALUES
  ('Khalid Ahmed', '1955-12-24', 'Uncle'),
  ('Salma Ahmed', '1960-07-04', 'Aunt'),
  ('Ibrahim Ahmed', '1962-09-11', 'Uncle'),
  ('Hajar Ahmed', '1964-02-23', 'Aunt');

CREATE TABLE Paternal_Relatives (
  Name VARCHAR(255) NOT NULL,
  Date_of_Birth DATE NOT NULL
-- Relation column left intentionally
);

ALTER TABLE Paternal_Relatives
ADD COLUMN Relation VARCHAR(255) AFTER Date_of_Birth;

INSERT INTO Paternal_Relatives (Name, Date_of_Birth, Relation)
VALUES
  ('Mohammed Ahmed', '1950-06-18', 'Uncle'),
  ('Fatima Ahmed', '1952-10-09', 'Aunt'),
  ('Zaid Ahmed', '1954-03-13', 'Uncle'),
  ('Zainab Ahmed', '1956-08-05', 'Aunt');

-- Queries to display entire information of a TABLE:

SELECT * FROM `Immediate_Family`
SELECT * FROM `Maternal_Relatives`
SELECT * FROM `Paternal_Relatives`
