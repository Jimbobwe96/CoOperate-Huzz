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
(1, 'Jennifer', 'Lee', 3.35, 'Sub', 8, 'Juarez Ltd', 1, 'courtneypatterson@lyons.com'),
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
(1, CURRENT_TIMESTAMP, 3, 4, 4, 5, 3, "I Love It", 1),
(2, CURRENT_TIMESTAMP, 4, 3, 2, 1, 4, "Great!!!", 1),
(3, CURRENT_TIMESTAMP, 2, 3, 4, 2, 2, "Phenom", 2);

-- Activity Logs
INSERT INTO Activity_Logs (AdminID, ActionType, Details) VALUES
(1, 'Data Analysis', NULL),
(2, 'Review Checking', NULL),
(3, 'Review Checking', NULL);

