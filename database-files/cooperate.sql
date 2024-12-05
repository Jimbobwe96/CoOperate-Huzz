DROP DATABASE IF EXISTS CoOperate;

CREATE DATABASE IF NOT EXISTS CoOperate;

SHOW DATABASES;

USE CoOperate;

DROP USER IF EXISTS 'jimbobwe'@'%';
CREATE USER 'jimbobwe'@'%' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON CoOperate.* TO 'jimbobwe'@'%';

CREATE TABLE Advisors
(
    AdvisorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName  VARCHAR(50) NOT NULL,
    College   VARCHAR(50),
    Email     VARCHAR(50) UNIQUE
);

CREATE TABLE Students
(
    StudentID   INT PRIMARY KEY AUTO_INCREMENT,
    FirstName   VARCHAR(50) NOT NULL,
    LastName    VARCHAR(50) NOT NULL,
    GPA         FLOAT CHECK (GPA BETWEEN 0 AND 4.0),
    Major       VARCHAR(50),
    CurrentYear INT CHECK (CurrentYear BETWEEN 1 AND 8),
    HomeCollege VARCHAR(50),
    AdvisorID   INT,
    Email       VARCHAR(50) UNIQUE,
    FOREIGN KEY (AdvisorID) REFERENCES Advisors (AdvisorID)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE Experiences
(
    ExperienceID INT AUTO_INCREMENT,
    StudentID    INT NOT NULL,
    Title        VARCHAR(50) NOT NULL,
    Industry     VARCHAR(50),
    StartTime    DATE,
    EndTime      DATE,
    Company      VARCHAR(50),

    PRIMARY KEY (ExperienceID),
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID)
        ON DELETE CASCADE
);

CREATE TABLE Skill
(
    SkillID   INT PRIMARY KEY AUTO_INCREMENT,
    SkillName VARCHAR(50) NOT NULL
);

CREATE TABLE StudentSkills
(
    StudentID   INT NOT NULL,
    SkillID     INT NOT NULL,
    Proficiency INT CHECK (Proficiency BETWEEN 1 AND 10),
    PRIMARY KEY (StudentID, SkillID),
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID)
        ON DELETE CASCADE,
    FOREIGN KEY (SkillID) REFERENCES Skill (SkillID)
        ON DELETE CASCADE
);

CREATE TABLE Company
(
    CompanyID    INT PRIMARY KEY AUTO_INCREMENT,
    Name         VARCHAR(50) NOT NULL,
    Industry     VARCHAR(50),
    Headquarters VARCHAR(50),
    Size         CHAR(1) CHECK (Size IN ('S', 'M', 'L')) -- S = Small, M = Medium, L = Large
);

CREATE TABLE CoopRole
(
    PositionID  INT AUTO_INCREMENT,
    CompanyID   INT NOT NULL,
    Title       VARCHAR(50) NOT NULL,
    City        VARCHAR(50),
    Country     VARCHAR(50),
    Pay         DECIMAL(10, 2),
    RequiredGPA FLOAT CHECK (RequiredGPA BETWEEN 0 AND 4.0),
    PRIMARY KEY (PositionID),
    FOREIGN KEY (CompanyID) REFERENCES Company (CompanyID)
        ON DELETE CASCADE
);

CREATE TABLE RequiredSkills
(
    PositionID  INT NOT NULL,
    SkillID     INT NOT NULL,
    Proficiency INT CHECK (Proficiency BETWEEN 1 AND 10),
    PRIMARY KEY (PositionID, SkillID),
    FOREIGN KEY (PositionID) REFERENCES CoopRole (PositionID)
        ON DELETE CASCADE,
    FOREIGN KEY (SkillID) REFERENCES Skill (SkillID)
        ON DELETE CASCADE
);

CREATE TABLE CoopList
(
    StudentID  INT NOT NULL,
    CompanyID  INT NOT NULL,
    PositionID INT NOT NULL,
    appliedStatus BOOLEAN NOT NULL DEFAULT FALSE,
    acceptedStatus BOOLEAN NOT NULL DEFAULT FALSE,
    appliedGPA FLOAT CHECK (appliedGPA BETWEEN 1 AND 10),
    prevExpCount INT,
    PRIMARY KEY (StudentID, CompanyID, PositionID),
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID)
        ON DELETE CASCADE,
    FOREIGN KEY (CompanyID) REFERENCES Company (CompanyID)
        ON DELETE CASCADE,
    FOREIGN KEY (PositionID) REFERENCES CoopRole (PositionID)
        ON DELETE CASCADE
);

CREATE TABLE Admin
(
    AdminID   INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName  VARCHAR(50) NOT NULL,
    Email     VARCHAR(50) UNIQUE,
    Role      VARCHAR(50)
);
-- Testing
CREATE TABLE Reviews
(
    ReviewID            INT PRIMARY KEY AUTO_INCREMENT,
    StudentID           INT NOT NULL,
    Date                DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Culture             INT CHECK (Culture BETWEEN 1 AND 5),
    Satisfaction        INT CHECK (Satisfaction BETWEEN 1 AND 5),
    Compensation        INT CHECK (Compensation BETWEEN 1 AND 5),
    LearningOpportunity INT CHECK (LearningOpportunity BETWEEN 1 AND 5),
    WorkLifeBalance     INT CHECK (WorkLifeBalance BETWEEN 1 AND 5),
    Summary             TEXT,
    Flagged             BOOLEAN DEFAULT FALSE,
    ResolvedBy          INT DEFAULT NULL,
    PositionID          INT NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID)
        ON DELETE CASCADE,
    FOREIGN KEY (ResolvedBy) REFERENCES Admin (AdminID)
        ON DELETE SET NULL,
    FOREIGN KEY (PositionID) REFERENCES CoopRole (PositionID)
        ON DELETE CASCADE
);

CREATE TABLE Activity_Logs
(
    LogID      INT PRIMARY KEY AUTO_INCREMENT,
    AdminID    INT NOT NULL,
    ActionType VARCHAR(50) NOT NULL,
    Details    TEXT,
    Timestamp  DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AdminID) REFERENCES Admin (AdminID)
        ON DELETE CASCADE
);

-- SQL Insert Statements with Dummy Data
-- Advisors
INSERT INTO Advisors (AdvisorID, FirstName, LastName, College, Email) VALUES
(1, 'Jennifer', 'Melendez', 'Fields, Sanchez and Hamilton', 'erinwilson@melton.com'),
(2, 'Matthew', 'Miller', 'Charles Inc', 'steelejoseph@delacruz-newman.com'),
(3, 'Kathy', 'Morales', 'Greer, Greene and Underwood', 'pereznicole@bonilla.com'),
(4, 'Daniel', 'Gonzalez', 'Smith-Greene', 'llarson@hotmail.com'),
(5, 'Scott', 'Webb', 'Hernandez-Owens', 'olivia84@robinson.info');

-- Students
INSERT INTO Students (StudentID, FirstName, LastName, GPA, Major, CurrentYear, HomeCollege, AdvisorID, Email) VALUES
(1, 'Jennifer', 'Lee', 3.35, 'Sub', 3, 'Juarez Ltd', 1, 'courtneypatterson@lyons.com'),
(2, 'Katherine', 'Franklin', 2.63, 'Therapist, drama', 1, 'Roberts and Sons', 4, 'thomasbauer@bowman.com'),
(3, 'Jacob', 'Robles', 2.33, 'Accountant, chartered certified', 5, 'Wilson-Sims', 2, 'lisachapman@hampton-lawson.org'),
(4, 'Joseph', 'Wells', 3.09, 'Podiatrist', 2, 'Fernandez-Smith', 2, 'brentwhitehead@bridges.com'),
(5, 'Shannon', 'Campbell', 3.86, 'Travel agency manager', 1, 'Johnson PLC', 2, 'isabel09@hotmail.com'),
(6, 'Gina', 'Wagner', 3.86, 'Fitness centre manager', 7, 'Smith, Anderson and Carter', 4, 'reginaldmaynard@hotmail.com'),
(7, 'Karen', 'Willis', 2.03, 'Outdoor activities/education manager', 4, 'Soto-Palmer', 2, 'gblack@aguilar.com'),
(8, 'Sydney', 'Clark', 2.98, 'Soil scientist', 3, 'Walters, Farrell and Coleman', 3, 'phillipfisher@collins.info'),
(9, 'Amber', 'Li', 2.36, 'Ecologist', 4, 'Carter Ltd', 5, 'craigkennedy@wilson-larson.info'),
(10, 'Corey', 'Silva', 2.62, 'Dance movement psychotherapist', 4, 'Barry LLC', 2, 'kingjames@franklin-dyer.com'),
(11, 'Kristina', 'Dickerson', 3.22, 'Information systems manager', 1, 'Young, Bender and Hess', 2, 'angela62@yahoo.com'),
(12, 'Barry', 'Moore', 3.73, 'Control and instrumentation engineer', 2, 'Anderson, Guerra and Walker', 5, 'hgarner@parker.com'),
(13, 'Cynthia', 'Mcgee', 3.96, 'Accountant, chartered certified', 5, 'Thompson, Garcia and Price', 1, 'stephenjohnson@stephens.com'),
(14, 'Julie', 'Jackson', 2.7, 'Chief Executive Officer', 5, 'Jacobs, Dominguez and Fisher', 2, 'sarahthompson@fernandez.com'),
(15, 'Evan', 'Martin', 2.18, 'Curator', 2, 'Gonzalez and Sons', 3, 'dcortez@yahoo.com');

-- Skills
INSERT INTO Skill (SkillID, SkillName) VALUES
(1, 'Java'),
(2, 'Excel'),
(3, 'Word'),
(4, 'SQL'),
(5, 'KQL'),
(6, 'Azure'),
(7, 'Streamlit'),
(8, 'Docker'),
(9, 'Python'),
(10, 'JavaScript');

-- Company
INSERT INTO Company (CompanyID, Name, Industry, Headquarters, Size) VALUES
(1, 'Smith-Harris', 'Retail', 'Lake Leslie', 'L'),
(2, 'Moore Inc', 'Healthcare', 'Morrisfort', 'L'),
(3, 'Burns, Perry and Ramirez', 'Healthcare', 'Gregorymouth', 'S'),
(4, 'Gamble, Johnson and Lopez', 'Education', 'North Courtneyfurt', 'S'),
(5, 'Yu-Keith', 'Education', 'East Karenfurt', 'S'),
(6, 'Francis, Henson and Smith', 'Technology', 'East Mindyville', 'M'),
(7, 'Chavez-Drake', 'Finance', 'South Nicole', 'L'),
(8, 'Walker, Evans and Newman', 'Education', 'Markshire', 'L');

-- Admin
INSERT INTO Admin (AdminID, FirstName, LastName, Email, Role) VALUES
(1, 'Dana', 'Levine', 'kristenluna@hunter-alvarez.com', 'System Administrator'),
(2, 'Gregory', 'Smith', 'deanna76@dyer-martin.com', 'System Administrator'),
(3, 'Michael', 'Gutierrez', 'benjaminvasquez@yahoo.com', 'Operations Manager');

-- Student Skills
INSERT INTO StudentSkills (StudentID, SkillID, Proficiency) VALUES
(1, 1, 8),
(1, 2, 6),
(3, 8, 4),
(3, 9, 10),
(4, 3, 7);

-- Co-op Role
INSERT INTO CoopRole (CompanyID, Title, City, Country, Pay, RequiredGPA) VALUES
(1, 'Data Scientist', 'Boston', 'US', 45000, 3.7),
(1, 'Financial Analyst', 'Boston', 'US', 30000, 3.3),
(2, 'Engineer', 'Cambridge', 'US', 50000, 3.5),
(4, 'Social Media Manger', 'Burlington', 'US', 35000, 3.4);

-- Required Skills
INSERT INTO RequiredSkills (PositionID, SkillID, Proficiency) VALUES
(3, 8, 4),
(3, 6, 9),
(1, 1, 7),
(1, 4, 8),
(4, 2, 10);

-- Experiences
INSERT INTO Experiences (StudentID, Title, Industry, StartTime, EndTime, Company) VALUES
(1, 'Waiter', 'Food Service', DATE_ADD(CURRENT_TIMESTAMP, INTERVAL -2 year), CURRENT_TIMESTAMP, 'Pressed'),
(2, 'Data Analyst', 'Data Science', DATE_ADD(CURRENT_TIMESTAMP, INTERVAL -6 month), CURRENT_TIMESTAMP, 'TD Bank'),
(3, 'Lifeguard', 'Health Care', DATE_ADD(CURRENT_TIMESTAMP, INTERVAL -3 year), CURRENT_TIMESTAMP, 'YMCA');

-- Co-op List
INSERT INTO CoopList (StudentID, CompanyID, PositionID, appliedGPA, prevExpCount) VALUES
(1, 1, 1, 3.8, 1),
(2, 1, 2, 3.5, 2),
(3, 2, 3, 3.3, 1);

-- Reviews
INSERT INTO Reviews (StudentID, Date, Culture, Satisfaction, Compensation, LearningOpportunity, WorkLifeBalance, Summary, PositionID) VALUES
(47, '2024-11-14 22:05:33', 2, 4, 2, 2, 1, 'Liked the team collaboration', 37),
(5, '2024-10-11 07:10:54', 1, 4, 5, 1, 3, 'Disliked the lack of growth opportunities', 26),
(55, '2024-01-25 13:17:12', 5, 2, 3, 5, 5, 'Appreciated the flexible work hours', 33),
(45, '2024-02-09 18:35:25', 3, 4, 2, 1, 3, 'Liked the team collaboration', 83),
(95, '2024-09-15 19:12:02', 1, 5, 4, 2, 4, 'Felt overwhelmed with workload', 30),
(11, '2024-03-09 11:38:37', 1, 3, 3, 1, 1, 'Felt overwhelmed with workload', 69),
(7, '2024-07-22 01:52:57', 4, 3, 3, 1, 3, 'Enjoyed the company culture', 35),
(40, '2023-12-19 14:58:23', 5, 4, 3, 5, 1, 'Enjoyed the company culture', 94),
(37, '2024-01-31 07:53:09', 2, 4, 3, 1, 2, 'Disliked the lack of growth opportunities', 76),
(99, '2024-04-02 18:38:00', 3, 2, 3, 5, 4, 'Appreciated the flexible work hours', 31),
(81, '2024-11-29 13:34:15', 2, 1, 1, 3, 5, 'Liked the team collaboration', 28),
(73, '2024-06-11 01:39:03', 3, 4, 2, 4, 1, 'Appreciated the flexible work hours', 9),
(8, '2024-08-23 14:15:24', 4, 1, 4, 1, 1, 'Appreciated the flexible work hours', 19),
(68, '2024-01-19 02:58:51', 3, 4, 5, 3, 5, 'Appreciated the flexible work hours', 26),
(49, '2024-11-09 01:32:24', 2, 4, 2, 2, 4, 'Felt overwhelmed with workload', 77),
(65, '2024-09-01 00:32:19', 4, 5, 2, 5, 4, 'Liked the team collaboration', 61),
(39, '2024-08-19 16:43:51', 1, 3, 3, 2, 3, 'Disliked the lack of growth opportunities', 9),
(3, '2024-05-29 18:29:00', 5, 5, 2, 3, 4, 'Enjoyed the company culture', 59),
(39, '2024-01-11 09:01:42', 5, 2, 5, 2, 3, 'Disliked the lack of growth opportunities', 63),
(54, '2024-01-22 18:12:01', 2, 1, 4, 3, 3, 'Enjoyed the company culture', 5),
(56, '2024-11-30 05:32:47', 5, 1, 4, 4, 1, 'Liked the team collaboration', 96),
(71, '2024-06-13 01:08:03', 4, 1, 3, 1, 5, 'Disliked the lack of growth opportunities', 94),
(63, '2024-08-30 10:18:26', 2, 4, 1, 2, 5, 'Disliked the lack of growth opportunities', 54),
(62, '2024-05-17 23:27:04', 2, 4, 3, 2, 1, 'Disliked the lack of growth opportunities', 58),
(80, '2023-12-30 18:08:27', 4, 4, 3, 5, 2, 'Felt overwhelmed with workload', 97),
(97, '2024-01-05 02:27:19', 2, 2, 3, 4, 4, 'Liked the team collaboration', 35),
(84, '2024-03-14 01:37:42', 1, 4, 5, 3, 1, 'Disliked the lack of growth opportunities', 12),
(49, '2024-05-14 08:27:54', 3, 2, 4, 3, 4, 'Felt overwhelmed with workload', 58),
(34, '2024-10-12 17:52:38', 5, 5, 5, 2, 4, 'Disliked the lack of growth opportunities', 5),
(57, '2024-09-03 03:23:58', 4, 2, 1, 4, 5, 'Appreciated the flexible work hours', 39),
(73, '2023-12-13 03:14:46', 3, 4, 3, 5, 5, 'Enjoyed the company culture', 66),
(83, '2024-07-07 02:04:32', 4, 1, 3, 1, 1, 'Felt overwhelmed with workload', 52),
(92, '2024-11-12 18:32:15', 2, 1, 2, 3, 2, 'Appreciated the flexible work hours', 37),
(38, '2024-02-17 11:28:21', 2, 5, 4, 4, 4, 'Felt overwhelmed with workload', 30),
(21, '2024-03-04 10:44:00', 4, 3, 2, 4, 3, 'Felt overwhelmed with workload', 15),
(11, '2024-08-10 20:05:31', 4, 4, 4, 1, 4, 'Appreciated the flexible work hours', 80),
(49, '2023-12-20 07:45:03', 4, 4, 3, 3, 4, 'Felt overwhelmed with workload', 81),
(75, '2024-10-27 04:19:00', 3, 2, 4, 5, 1, 'Enjoyed the company culture', 36),
(23, '2024-01-02 21:29:58', 1, 3, 2, 1, 5, 'Enjoyed the company culture', 74),
(98, '2024-07-12 19:11:51', 4, 4, 4, 3, 5, 'Appreciated the flexible work hours', 51),
(38, '2024-01-14 14:36:06', 2, 4, 1, 5, 1, 'Appreciated the flexible work hours', 13),
(95, '2024-02-24 02:27:48', 1, 3, 1, 4, 4, 'Enjoyed the company culture', 96),
(91, '2024-05-04 13:59:42', 1, 4, 4, 2, 2, 'Liked the team collaboration', 70),
(24, '2024-03-04 18:28:15', 3, 5, 1, 5, 1, 'Enjoyed the company culture', 91),
(10, '2024-10-02 21:01:04', 3, 2, 2, 5, 2, 'Disliked the lack of growth opportunities', 15),
(95, '2024-02-05 08:47:50', 5, 5, 4, 3, 4, 'Liked the team collaboration', 69),
(86, '2024-11-30 10:16:29', 4, 3, 3, 4, 4, 'Appreciated the flexible work hours', 87),
(99, '2024-04-02 09:12:53', 4, 5, 1, 3, 4, 'Disliked the lack of growth opportunities', 6),
(70, '2024-07-30 07:38:43', 5, 3, 3, 1, 2, 'Felt overwhelmed with workload', 63),
(36, '2024-10-15 04:54:07', 1, 3, 1, 2, 3, 'Felt overwhelmed with workload', 46),
(37, '2024-02-29 15:06:12', 5, 1, 1, 5, 5, 'Enjoyed the company culture', 1),
(88, '2024-07-15 23:41:57', 3, 2, 3, 1, 5, 'Liked the team collaboration', 22),
(52, '2024-01-06 11:21:20', 3, 5, 4, 2, 4, 'Appreciated the flexible work hours', 78),
(68, '2024-07-04 10:03:44', 3, 4, 4, 4, 3, 'Felt overwhelmed with workload', 33),
(42, '2024-02-01 12:49:00', 2, 2, 1, 2, 5, 'Liked the team collaboration', 24),
(69, '2024-10-01 20:45:54', 2, 1, 3, 5, 2, 'Disliked the lack of growth opportunities', 17),
(55, '2024-05-10 16:05:53', 1, 2, 3, 1, 5, 'Appreciated the flexible work hours', 97),
(18, '2024-05-29 21:50:59', 4, 3, 5, 2, 1, 'Liked the team collaboration', 54),
(74, '2024-01-12 15:14:08', 4, 3, 5, 4, 5, 'Liked the team collaboration', 58),
(94, '2024-11-16 07:10:27', 2, 5, 1, 4, 2, 'Disliked the lack of growth opportunities', 9),
(21, '2023-12-11 06:00:06', 4, 5, 2, 3, 2, 'Appreciated the flexible work hours', 6),
(70, '2024-07-03 01:01:47', 1, 1, 5, 3, 4, 'Enjoyed the company culture', 29),
(22, '2024-05-18 14:33:25', 3, 5, 3, 5, 4, 'Liked the team collaboration', 57),
(18, '2024-10-03 21:41:07', 5, 1, 1, 4, 4, 'Appreciated the flexible work hours', 9),
(94, '2024-08-20 00:04:06', 5, 4, 2, 3, 1, 'Felt overwhelmed with workload', 59),
(40, '2024-02-03 04:41:13', 1, 3, 3, 3, 3, 'Enjoyed the company culture', 46),
(96, '2024-08-20 08:12:40', 5, 4, 2, 4, 1, 'Appreciated the flexible work hours', 71),
(27, '2024-02-07 22:49:21', 3, 1, 5, 4, 4, 'Appreciated the flexible work hours', 53),
(99, '2024-03-21 15:57:59', 2, 5, 3, 4, 4, 'Liked the team collaboration', 19),
(67, '2024-06-03 01:48:40', 2, 2, 5, 3, 1, 'Felt overwhelmed with workload', 72),
(76, '2024-08-27 14:07:55', 3, 3, 1, 4, 1, 'Liked the team collaboration', 69),
(77, '2023-12-11 17:51:37', 4, 1, 2, 2, 5, 'Disliked the lack of growth opportunities', 36),
(1, '2024-08-07 23:01:35', 3, 2, 2, 2, 2, 'Enjoyed the company culture', 72),
(26, '2024-10-27 14:50:39', 2, 4, 4, 3, 3, 'Felt overwhelmed with workload', 20),
(89, '2024-06-30 11:17:29', 4, 1, 3, 3, 5, 'Appreciated the flexible work hours', 61),
(14, '2024-05-10 17:25:27', 1, 2, 5, 3, 5, 'Enjoyed the company culture', 30),
(92, '2024-05-10 17:48:44', 5, 2, 3, 5, 3, 'Felt overwhelmed with workload', 86),
(59, '2024-01-26 22:57:42', 2, 4, 4, 2, 4, 'Appreciated the flexible work hours', 89),
(49, '2024-04-09 20:45:39', 3, 3, 2, 1, 1, 'Appreciated the flexible work hours', 60),
(75, '2024-10-21 19:23:00', 2, 1, 5, 1, 1, 'Enjoyed the company culture', 27),
(45, '2024-03-03 13:17:11', 3, 2, 2, 3, 3, 'Appreciated the flexible work hours', 23),
(45, '2024-02-25 17:28:54', 2, 2, 2, 1, 1, 'Felt overwhelmed with workload', 99),
(46, '2024-02-15 18:24:25', 5, 1, 5, 5, 4, 'Felt overwhelmed with workload', 22),
(61, '2024-10-20 04:22:01', 1, 3, 4, 5, 3, 'Appreciated the flexible work hours', 17),
(21, '2024-05-12 10:00:27', 1, 2, 5, 5, 5, 'Liked the team collaboration', 3),
(73, '2024-07-21 17:55:25', 5, 2, 3, 1, 5, 'Liked the team collaboration', 10),
(28, '2024-05-08 10:46:58', 4, 5, 5, 5, 3, 'Liked the team collaboration', 95),
(60, '2024-03-27 04:17:08', 5, 5, 3, 4, 5, 'Enjoyed the company culture', 66),
(66, '2024-08-24 21:26:23', 2, 5, 3, 5, 5, 'Felt overwhelmed with workload', 10),
(50, '2024-03-14 08:13:54', 3, 3, 2, 2, 3, 'Felt overwhelmed with workload', 79),
(6, '2024-02-01 20:19:02', 2, 1, 2, 1, 2, 'Liked the team collaboration', 66),
(42, '2024-01-31 18:13:44', 2, 1, 5, 1, 1, 'Felt overwhelmed with workload', 10),
(70, '2024-03-29 19:26:06', 1, 3, 1, 4, 4, 'Enjoyed the company culture', 56),
(87, '2024-07-20 23:34:44', 2, 2, 3, 2, 2, 'Felt overwhelmed with workload', 10),
(46, '2024-04-09 05:57:17', 3, 1, 1, 5, 4, 'Felt overwhelmed with workload', 18),
(1, '2024-08-11 18:30:48', 2, 2, 1, 4, 2, 'Disliked the lack of growth opportunities', 63),
(3, '2024-02-02 14:54:21', 2, 4, 2, 3, 5, 'Felt overwhelmed with workload', 14),
(21, '2024-10-17 06:15:26', 2, 3, 5, 5, 5, 'Liked the team collaboration', 76),
(34, '2023-12-14 04:37:25', 1, 5, 2, 1, 2, 'Appreciated the flexible work hours', 85),
(19, '2024-08-07 03:15:18', 1, 4, 4, 4, 4, 'Liked the team collaboration', 86);

-- Activity Logs
INSERT INTO Activity_Logs (AdminID, ActionType, Details) VALUES
(1, 'Data Analysis', NULL),
(2, 'Review Checking', NULL),
(3, 'Review Checking', NULL);