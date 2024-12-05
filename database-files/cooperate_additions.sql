-- SQL Insert Statements with Dummy Data
-- Advisors
INSERT INTO Advisors (AdvisorID, FirstName, LastName, College, Email) VALUES
(1, 'Emily', 'Johnson', 'College of Arts, Media and Design', 'emily.johnson@northeastern.edu'),
(2, 'Michael', 'Brown', 'College of Engineering', 'michael.brown@northeastern.edu'),
(3, 'Sarah', 'Davis', 'DAmore-McKim School of Business', 'sarah.davis@northeastern.edu'),
(4, 'David', 'Garcia', 'College of Science', 'david.garcia@northeastern.edu'),
(5, 'Jessica', 'Martinez', 'Bouvé College of Health Sciences', 'jessica.martinez@northeastern.edu'),
(6, 'Christopher', 'Rodriguez', 'College of Computer and Information Science', 'christopher.rodriguez@northeastern.edu'),
(7, 'Amanda', 'Lee', 'College of Social Sciences and Humanities', 'amanda.lee@northeastern.edu'),
(8, 'Joshua', 'Walker', 'College of Professional Studies', 'joshua.walker@northeastern.edu'),
(9, 'Ashley', 'Hall', 'College of Arts, Media and Design', 'ashley.hall@northeastern.edu'),
(10, 'Matthew', 'Young', 'College of Engineering', 'matthew.young@northeastern.edu'),
(11, 'Lauren', 'Hernandez', 'DAmore-McKim School of Business', 'lauren.hernandez@northeastern.edu'),
(12, 'Andrew', 'King', 'College of Science', 'andrew.king@northeastern.edu'),
(13, 'Megan', 'Wright', 'Bouvé College of Health Sciences', 'megan.wright@northeastern.edu'),
(14, 'Brian', 'Lopez', 'College of Computer and Information Science', 'brian.lopez@northeastern.edu'),
(15, 'Stephanie', 'Hill', 'College of Social Sciences and Humanities', 'stephanie.hill@northeastern.edu'),
(16, 'Justin', 'Scott', 'College of Professional Studies', 'justin.scott@northeastern.edu'),
(17, 'Nicole', 'Green', 'College of Arts, Media and Design', 'nicole.green@northeastern.edu'),
(18, 'Daniel', 'Adams', 'College of Engineering', 'daniel.adams@northeastern.edu'),
(19, 'Heather', 'Baker', 'DAmore-McKim School of Business', 'heather.baker@northeastern.edu'),
(20, 'Ryan', 'Nelson', 'College of Science', 'ryan.nelson@northeastern.edu'),
(21, 'Rebecca', 'Carter', 'Bouvé College of Health Sciences', 'rebecca.carter@northeastern.edu'),
(22, 'Jacob', 'Mitchell', 'College of Computer and Information Science', 'jacob.mitchell@northeastern.edu'),
(23, 'Laura', 'Perez', 'College of Social Sciences and Humanities', 'laura.perez@northeastern.edu'),
(24, 'Nicholas', 'Roberts', 'College of Professional Studies', 'nicholas.roberts@northeastern.edu'),
(25, 'Victoria', 'Turner', 'College of Arts, Media and Design', 'victoria.turner@northeastern.edu'),
(26, 'Brandon', 'Phillips', 'College of Engineering', 'brandon.phillips@northeastern.edu'),
(27, 'Michelle', 'Campbell', 'DAmore-McKim School of Business', 'michelle.campbell@northeastern.edu'),
(28, 'Joshua', 'Parker', 'College of Science', 'joshua.parker@northeastern.edu'),
(29, 'Hannah', 'Evans', 'Bouvé College of Health Sciences', 'hannah.evans@northeastern.edu'),
(30, 'Alexander', 'Edwards', 'College of Computer and Information Science', 'alexander.edwards@northeastern.edu'),
(31, 'Samantha', 'Collins', 'College of Social Sciences and Humanities', 'samantha.collins@northeastern.edu'),
(32, 'Ethan', 'Stewart', 'College of Professional Studies', 'ethan.stewart@northeastern.edu'),
(33, 'Katherine', 'Sanchez', 'College of Arts, Media and Design', 'katherine.sanchez@northeastern.edu'),
(34, 'Benjamin', 'Morris', 'College of Engineering', 'benjamin.morris@northeastern.edu'),
(35, 'Abigail', 'Rogers', 'DAmore-McKim School of Business', 'abigail.rogers@northeastern.edu'),
(36, 'Joshua', 'Reed', 'College of Science', 'joshua.reed@northeastern.edu'),
(37, 'Elizabeth', 'Cook', 'Bouvé College of Health Sciences', 'elizabeth.cook@northeastern.edu'),
(38, 'Andrew', 'Morgan', 'College of Computer and Information Science', 'andrew.morgan@northeastern.edu'),
(39, 'Olivia', 'Bell', 'College of Social Sciences and Humanities', 'olivia.bell@northeastern.edu'),
(40, 'Tyler', 'Murphy', 'College of Professional Studies', 'tyler.murphy@northeastern.edu'),
(41, 'Emily', 'Clark', 'College of Arts, Media and Design', 'emily.clark@northeastern.edu'),
(42, 'Logan', 'Lewis', 'College of Engineering', 'logan.lewis@northeastern.edu'),
(43, 'Grace', 'Lee', 'DAmore-McKim School of Business', 'grace.lee@northeastern.edu'),
(44, 'Jacob', 'Walker', 'College of Science', 'jacob.walker@northeastern.edu'),
(45, 'Ella', 'Hall', 'Bouvé College of Health Sciences', 'ella.hall@northeastern.edu');

-- Students
INSERT INTO Students (StudentID, FirstName, LastName, GPA, Major, CurrentYear, HomeCollege, AdvisorID, Email) VALUES
(1, 'John', 'Smith', 3.5, 'Computer Science', 3, 'College of Arts, Media and Design', 1, 'john.smith1@university.edu'),
(2, 'Jane', 'Johnson', 3.6, 'Business', 4, 'College of Arts and Sciences', 2, 'jane.johnson2@university.edu'),
(3, 'Michael', 'Williams', 3.7, 'Biology', 1, 'College of Computer and Information Science', 3, 'michael.williams3@university.edu'),
(4, 'Emily', 'Brown', 3.8, 'Psychology', 2, 'College of Engineering', 4, 'emily.brown4@university.edu'),
(5, 'David', 'Jones', 3.9, 'Mathematics', 3, 'Bouvé College of Health Sciences', 5, 'david.jones5@university.edu'),
(6, 'Sarah', 'Garcia', 3.0, 'Economics', 4, 'DAmore-McKim School of Business', 6, 'sarah.garcia6@university.edu'),
(7, 'Robert', 'Miller', 3.1, 'Political Science', 1, 'College of Professional Studies', 7, 'robert.miller7@university.edu'),
(8, 'Laura', 'Davis', 3.2, 'Chemistry', 2, 'Khoury College of Computer Sciences', 8, 'laura.davis8@university.edu'),
(9, 'James', 'Martinez', 3.3, 'English', 3, 'College of Arts, Media and Design', 9, 'james.martinez9@university.edu'),
(10, 'Linda', 'Hernandez', 3.4, 'Computer Science', 4, 'College of Arts and Sciences', 10, 'linda.hernandez10@university.edu'),
(11, 'William', 'Lopez', 3.5, 'Business', 1, 'College of Computer and Information Science', 11, 'william.lopez11@university.edu'),
(12, 'Karen', 'Gonzalez', 3.6, 'Biology', 2, 'College of Engineering', 12, 'karen.gonzalez12@university.edu'),
(13, 'Richard', 'Wilson', 3.7, 'Psychology', 3, 'Bouvé College of Health Sciences', 13, 'richard.wilson13@university.edu'),
(14, 'Barbara', 'Anderson', 3.8, 'Mathematics', 4, 'DAmore-McKim School of Business', 14, 'barbara.anderson14@university.edu'),
(15, 'Charles', 'Thomas', 3.9, 'Economics', 1, 'College of Professional Studies', 15, 'charles.thomas15@university.edu'),
(16, 'Susan', 'Taylor', 3.0, 'Political Science', 2, 'Khoury College of Computer Sciences', 16, 'susan.taylor16@university.edu'),
(17, 'Joseph', 'Moore', 3.1, 'Chemistry', 3, 'College of Arts, Media and Design', 17, 'joseph.moore17@university.edu'),
(18, 'Jessica', 'Jackson', 3.2, 'English', 4, 'College of Arts and Sciences', 18, 'jessica.jackson18@university.edu'),
(19, 'Thomas', 'Martin', 3.3, 'Computer Science', 1, 'College of Computer and Information Science', 19, 'thomas.martin19@university.edu'),
(20, 'Margaret', 'Lee', 3.4, 'Business', 2, 'College of Engineering', 20, 'margaret.lee20@university.edu'),
(21, 'John', 'Smith', 3.5, 'Biology', 3, 'Bouvé College of Health Sciences', 1, 'john.smith21@university.edu'),
(22, 'Jane', 'Johnson', 3.6, 'Economics', 4, 'DAmore-McKim School of Business', 2, 'jane.johnson22@university.edu'),
(23, 'Michael', 'Williams', 3.7, 'Political Science', 1, 'College of Professional Studies', 3, 'michael.williams23@university.edu'),
(24, 'Emily', 'Brown', 3.8, 'Chemistry', 2, 'Khoury College of Computer Sciences', 4, 'emily.brown24@university.edu'),
(25, 'David', 'Jones', 3.9, 'English', 3, 'College of Arts, Media and Design', 5, 'david.jones25@university.edu'),
(26, 'Sarah', 'Garcia', 3.0, 'Computer Science', 4, 'College of Arts and Sciences', 6, 'sarah.garcia26@university.edu'),
(27, 'Robert', 'Miller', 3.1, 'Business', 1, 'College of Computer and Information Science', 7, 'robert.miller27@university.edu'),
(28, 'Laura', 'Davis', 3.2, 'Biology', 2, 'College of Engineering', 8, 'laura.davis28@university.edu'),
(29, 'James', 'Martinez', 3.3, 'Economics', 3, 'Bouvé College of Health Sciences', 9, 'james.martinez29@university.edu'),
(30, 'Linda', 'Hernandez', 3.4, 'Political Science', 4, 'DAmore-McKim School of Business', 10, 'linda.hernandez30@university.edu'),
(31, 'William', 'Lopez', 3.5, 'Chemistry', 1, 'College of Professional Studies', 11, 'william.lopez31@university.edu'),
(32, 'Karen', 'Gonzalez', 3.6, 'English', 2, 'Khoury College of Computer Sciences', 12, 'karen.gonzalez32@university.edu'),
(33, 'Richard', 'Wilson', 3.7, 'Computer Science', 3, 'College of Arts, Media and Design', 13, 'richard.wilson33@university.edu'),
(34, 'Barbara', 'Anderson', 3.8, 'Business', 4, 'College of Arts and Sciences', 14, 'barbara.anderson34@university.edu'),
(35, 'Charles', 'Thomas', 3.9, 'Biology', 1, 'College of Computer and Information Science', 15, 'charles.thomas35@university.edu'),
(36, 'Susan', 'Taylor', 3.0, 'Economics', 2, 'College of Engineering', 16, 'susan.taylor36@university.edu'),
(37, 'Joseph', 'Moore', 3.1, 'Political Science', 3, 'Bouvé College of Health Sciences', 17, 'joseph.moore37@university.edu'),
(38, 'Jessica', 'Jackson', 3.2, 'Chemistry', 4, 'DAmore-McKim School of Business', 18, 'jessica.jackson38@university.edu'),
(39, 'Thomas', 'Martin', 3.3, 'English', 1, 'College of Professional Studies', 19, 'thomas.martin39@university.edu'),
(40, 'Margaret', 'Lee', 3.4, 'Computer Science', 2, 'Khoury College of Computer Sciences', 20, 'margaret.lee40@university.edu'),
(41, 'John', 'Smith', 3.5, 'Business', 3, 'College of Arts, Media and Design', 1, 'john.smith41@university.edu'),
(42, 'Jane', 'Johnson', 3.6, 'Biology', 4, 'College of Arts and Sciences', 2, 'jane.johnson42@university.edu'),
(43, 'Michael', 'Williams', 3.7, 'Economics', 1, 'College of Computer and Information Science', 3, 'michael.williams43@university.edu'),
(44, 'Emily', 'Brown', 3.8, 'Political Science', 2, 'College of Engineering', 4, 'emily.brown44@university.edu'),
(45, 'David', 'Jones', 3.9, 'Chemistry', 3, 'Bouvé College of Health Sciences', 5, 'david.jones45@university.edu'),
(46, 'Sarah', 'Garcia', 3.0, 'English', 4, 'DAmore-McKim School of Business', 6, 'sarah.garcia46@university.edu'),
(47, 'Robert', 'Miller', 3.1, 'Computer Science', 1, 'College of Professional Studies', 7, 'robert.miller47@university.edu'),
(48, 'Laura', 'Davis', 3.2, 'Business', 2, 'Khoury College of Computer Sciences', 8, 'laura.davis48@university.edu'),
(49, 'James', 'Martinez', 3.3, 'Biology', 3, 'College of Arts, Media and Design', 9, 'james.martinez49@university.edu'),
(50, 'Linda', 'Hernandez', 3.4, 'Economics', 4, 'College of Arts and Sciences', 10, 'linda.hernandez50@university.edu'),
(51, 'William', 'Lopez', 3.5, 'Political Science', 1, 'College of Computer and Information Science', 11, 'william.lopez51@university.edu'),
(52, 'Karen', 'Gonzalez', 3.6, 'Chemistry', 2, 'College of Engineering', 12, 'karen.gonzalez52@university.edu'),
(53, 'Richard', 'Wilson', 3.7, 'English', 3, 'Bouvé College of Health Sciences', 13, 'richard.wilson53@university.edu'),
(54, 'Barbara', 'Anderson', 3.8, 'Computer Science', 4, 'DAmore-McKim School of Business', 14, 'barbara.anderson54@university.edu'),
(55, 'Charles', 'Thomas', 3.9, 'Business', 1, 'College of Professional Studies', 15, 'charles.thomas55@university.edu'),
(56, 'Susan', 'Taylor', 3.0, 'Biology', 2, 'Khoury College of Computer Sciences', 16, 'susan.taylor56@university.edu'),
(57, 'Joseph', 'Moore', 3.1, 'Economics', 3, 'College of Arts, Media and Design', 17, 'joseph.moore57@university.edu'),
(58, 'Jessica', 'Jackson', 3.2, 'Political Science', 4, 'College of Arts and Sciences', 18, 'jessica.jackson58@university.edu'),
(59, 'Thomas', 'Martin', 3.3, 'Chemistry', 1, 'College of Computer and Information Science', 19, 'thomas.martin59@university.edu'),
(60, 'Margaret', 'Lee', 3.4, 'English', 2, 'College of Engineering', 20, 'margaret.lee60@university.edu'),
(61, 'John', 'Smith', 3.5, 'Economics', 3, 'Bouvé College of Health Sciences', 1, 'john.smith61@university.edu'),
(62, 'Jane', 'Johnson', 3.6, 'Political Science', 4, 'DAmore-McKim School of Business', 2, 'jane.johnson62@university.edu'),
(63, 'Michael', 'Williams', 3.7, 'Chemistry', 1, 'College of Professional Studies', 3, 'michael.williams63@university.edu'),
(64, 'Emily', 'Brown', 3.8, 'English', 2, 'Khoury College of Computer Sciences', 4, 'emily.brown64@university.edu'),
(65, 'David', 'Jones', 3.9, 'Computer Science', 3, 'College of Arts, Media and Design', 5, 'david.jones65@university.edu'),
(66, 'Sarah', 'Garcia', 3.0, 'Business', 4, 'College of Arts and Sciences', 6, 'sarah.garcia66@university.edu'),
(67, 'Robert', 'Miller', 3.1, 'Biology', 1, 'College of Computer and Information Science', 7, 'robert.miller67@university.edu'),
(68, 'Laura', 'Davis', 3.2, 'Economics', 2, 'College of Engineering', 8, 'laura.davis68@university.edu'),
(69, 'James', 'Martinez', 3.3, 'Political Science', 3, 'Bouvé College of Health Sciences', 9, 'james.martinez69@university.edu'),
(70, 'Linda', 'Hernandez', 3.4, 'Chemistry', 4, 'DAmore-McKim School of Business', 10, 'linda.hernandez70@university.edu'),
(71, 'William', 'Lopez', 3.5, 'English', 1, 'College of Professional Studies', 11, 'william.lopez71@university.edu'),
(72, 'Karen', 'Gonzalez', 3.6, 'Computer Science', 2, 'Khoury College of Computer Sciences', 12, 'karen.gonzalez72@university.edu'),
(73, 'Richard', 'Wilson', 3.7, 'Business', 3, 'College of Arts, Media and Design', 13, 'richard.wilson73@university.edu'),
(74, 'Barbara', 'Anderson', 3.8, 'Biology', 4, 'College of Arts and Sciences', 14, 'barbara.anderson74@university.edu'),
(75, 'Charles', 'Thomas', 3.9, 'Economics', 1, 'College of Computer and Information Science', 15, 'charles.thomas75@university.edu'),
(76, 'Susan', 'Taylor', 3.0, 'Political Science', 2, 'College of Engineering', 16, 'susan.taylor76@university.edu'),
(77, 'Joseph', 'Moore', 3.1, 'Chemistry', 3, 'Bouvé College of Health Sciences', 17, 'joseph.moore77@university.edu'),
(78, 'Jessica', 'Jackson', 3.2, 'English', 4, 'DAmore-McKim School of Business', 18, 'jessica.jackson78@university.edu'),
(79, 'Thomas', 'Martin', 3.3, 'Computer Science', 1, 'College of Professional Studies', 19, 'thomas.martin79@university.edu'),
(80, 'Margaret', 'Lee', 3.4, 'Business', 2, 'Khoury College of Computer Sciences', 20, 'margaret.lee80@university.edu'),
(81, 'John', 'Smith', 3.5, 'Biology', 3, 'College of Arts, Media and Design', 1, 'john.smith81@university.edu'),
(82, 'Jane', 'Johnson', 3.6, 'Economics', 4, 'College of Arts and Sciences', 2, 'jane.johnson82@university.edu'),
(83, 'Michael', 'Williams', 3.7, 'Political Science', 1, 'College of Computer and Information Science', 3, 'michael.williams83@university.edu'),
(84, 'Emily', 'Brown', 3.8, 'Chemistry', 2, 'College of Engineering', 4, 'emily.brown84@university.edu'),
(85, 'David', 'Jones', 3.9, 'English', 3, 'Bouvé College of Health Sciences', 5, 'david.jones85@university.edu'),
(86, 'Sarah', 'Garcia', 3.0, 'Computer Science', 4, 'DAmore-McKim School of Business', 6, 'sarah.garcia86@university.edu'),
(87, 'Robert', 'Miller', 3.1, 'Business', 1, 'College of Professional Studies', 7, 'robert.miller87@university.edu'),
(88, 'Laura', 'Davis', 3.2, 'Biology', 2, 'Khoury College of Computer Sciences', 8, 'laura.davis88@university.edu'),
(89, 'James', 'Martinez', 3.3, 'Economics', 3, 'College of Arts, Media and Design', 9, 'james.martinez89@university.edu'),
(90, 'Linda', 'Hernandez', 3.4, 'Political Science', 4, 'College of Arts and Sciences', 10, 'linda.hernandez90@university.edu'),
(91, 'William', 'Lopez', 3.5, 'Chemistry', 1, 'College of Computer and Information Science', 11, 'william.lopez91@university.edu'),
(92, 'Karen', 'Gonzalez', 3.6, 'English', 2, 'College of Engineering', 12, 'karen.gonzalez92@university.edu'),
(93, 'Richard', 'Wilson', 3.7, 'Computer Science', 3, 'Bouvé College of Health Sciences', 13, 'richard.wilson93@university.edu'),
(94, 'Barbara', 'Anderson', 3.8, 'Business', 4, 'DAmore-McKim School of Business', 14, 'barbara.anderson94@university.edu'),
(95, 'Charles', 'Thomas', 3.9, 'Biology', 1, 'College of Professional Studies', 15, 'charles.thomas95@university.edu'),
(96, 'Susan', 'Taylor', 3.0, 'Economics', 2, 'Khoury College of Computer Sciences', 16, 'susan.taylor96@university.edu'),
(97, 'Joseph', 'Moore', 3.1, 'Political Science', 3, 'College of Arts, Media and Design', 17, 'joseph.moore97@university.edu'),
(98, 'Jessica', 'Jackson', 3.2, 'Chemistry', 4, 'College of Arts and Sciences', 18, 'jessica.jackson98@university.edu'),
(99, 'Thomas', 'Martin', 3.3, 'English', 1, 'College of Computer and Information Science', 19, 'thomas.martin99@university.edu'),
(100, 'Margaret', 'Lee', 3.4, 'Computer Science', 2, 'College of Engineering', 20, 'margaret.lee100@university.edu'),
(101, 'John', 'Smith', 3.5, 'Economics', 3, 'Bouvé College of Health Sciences', 1, 'john.smith101@university.edu'),
(102, 'Jane', 'Johnson', 3.6, 'Political Science', 4, 'DAmore-McKim School of Business', 2, 'jane.johnson102@university.edu'),
(103, 'Michael', 'Williams', 3.7, 'Chemistry', 1, 'College of Professional Studies', 3, 'michael.williams103@university.edu'),
(104, 'Emily', 'Brown', 3.8, 'English', 2, 'Khoury College of Computer Sciences', 4, 'emily.brown104@university.edu'),
(105, 'David', 'Jones', 3.9, 'Computer Science', 3, 'College of Arts, Media and Design', 5, 'david.jones105@university.edu'),
(106, 'Sarah', 'Garcia', 3.0, 'Business', 4, 'College of Arts and Sciences', 6, 'sarah.garcia106@university.edu'),
(107, 'Robert', 'Miller', 3.1, 'Biology', 1, 'College of Computer and Information Science', 7, 'robert.miller107@university.edu'),
(108, 'Laura', 'Davis', 3.2, 'Economics', 2, 'College of Engineering', 8, 'laura.davis108@university.edu'),
(109, 'James', 'Martinez', 3.3, 'Political Science', 3, 'Bouvé College of Health Sciences', 9, 'james.martinez109@university.edu'),
(110, 'Linda', 'Hernandez', 3.4, 'Chemistry', 4, 'DAmore-McKim School of Business', 10, 'linda.hernandez110@university.edu'),
(111, 'William', 'Lopez', 3.5, 'English', 1, 'College of Professional Studies', 11, 'william.lopez111@university.edu'),
(112, 'Karen', 'Gonzalez', 3.6, 'Computer Science', 2, 'Khoury College of Computer Sciences', 12, 'karen.gonzalez112@university.edu'),
(113, 'Richard', 'Wilson', 3.7, 'Business', 3, 'College of Arts, Media and Design', 13, 'richard.wilson113@university.edu'),
(114, 'Barbara', 'Anderson', 3.8, 'Biology', 4, 'College of Arts and Sciences', 14, 'barbara.anderson114@university.edu'),
(115, 'Charles', 'Thomas', 3.9, 'Economics', 1, 'College of Computer and Information Science', 15, 'charles.thomas115@university.edu'),
(116, 'Susan', 'Taylor', 3.0, 'Political Science', 2, 'College of Engineering', 16, 'susan.taylor116@university.edu'),
(117, 'Joseph', 'Moore', 3.1, 'Chemistry', 3, 'Bouvé College of Health Sciences', 17, 'joseph.moore117@university.edu'),
(118, 'Jessica', 'Jackson', 3.2, 'English', 4, 'DAmore-McKim School of Business', 18, 'jessica.jackson118@university.edu'),
(119, 'Thomas', 'Martin', 3.3, 'Computer Science', 1, 'College of Professional Studies', 19, 'thomas.martin119@university.edu'),
(120, 'Margaret', 'Lee', 3.4, 'Business', 2, 'Khoury College of Computer Sciences', 20, 'margaret.lee120@university.edu'),
(121, 'John', 'Smith', 3.5, 'Biology', 3, 'College of Arts, Media and Design', 1, 'john.smith121@university.edu'),
(122, 'Jane', 'Johnson', 3.6, 'Economics', 4, 'College of Arts and Sciences', 2, 'jane.johnson122@university.edu'),
(123, 'Michael', 'Williams', 3.7, 'Political Science', 1, 'College of Computer and Information Science', 3, 'michael.williams123@university.edu'),
(124, 'Emily', 'Brown', 3.8, 'Chemistry', 2, 'College of Engineering', 4, 'emily.brown124@university.edu'),
(125, 'David', 'Jones', 3.9, 'English', 3, 'Bouvé College of Health Sciences', 5, 'david.jones125@university.edu'),
(126, 'Sarah', 'Garcia', 3.0, 'Computer Science', 4, 'DAmore-McKim School of Business', 6, 'sarah.garcia126@university.edu'),
(127, 'Robert', 'Miller', 3.1, 'Business', 1, 'College of Professional Studies', 7, 'robert.miller127@university.edu'),
(128, 'Laura', 'Davis', 3.2, 'Biology', 2, 'Khoury College of Computer Sciences', 8, 'laura.davis128@university.edu'),
(129, 'James', 'Martinez', 3.3, 'Economics', 3, 'College of Arts, Media and Design', 9, 'james.martinez129@university.edu'),
(130, 'Linda', 'Hernandez', 3.4, 'Political Science', 4, 'College of Arts and Sciences', 10, 'linda.hernandez130@university.edu'),
(131, 'William', 'Lopez', 3.5, 'Chemistry', 1, 'College of Computer and Information Science', 11, 'william.lopez131@university.edu'),
(132, 'Karen', 'Gonzalez', 3.6, 'English', 2, 'College of Engineering', 12, 'karen.gonzalez132@university.edu'),
(133, 'Richard', 'Wilson', 3.7, 'Computer Science', 3, 'Bouvé College of Health Sciences', 13, 'richard.wilson133@university.edu'),
(134, 'Barbara', 'Anderson', 3.8, 'Business', 4, 'DAmore-McKim School of Business', 14, 'barbara.anderson134@university.edu'),
(135, 'Charles', 'Thomas', 3.9, 'Biology', 1, 'College of Professional Studies', 15, 'charles.thomas135@university.edu'),
(136, 'Susan', 'Taylor', 3.0, 'Economics', 2, 'Khoury College of Computer Sciences', 16, 'susan.taylor136@university.edu'),
(137, 'Joseph', 'Moore', 3.1, 'Political Science', 3, 'College of Arts, Media and Design', 17, 'joseph.moore137@university.edu'),
(138, 'Jessica', 'Jackson', 3.2, 'Chemistry', 4, 'College of Arts and Sciences', 18, 'jessica.jackson138@university.edu'),
(139, 'Thomas', 'Martin', 3.3, 'English', 1, 'College of Computer and Information Science', 19, 'thomas.martin139@university.edu'),
(140, 'Margaret', 'Lee', 3.4, 'Computer Science', 2, 'College of Engineering', 20, 'margaret.lee140@university.edu'),
(141, 'John', 'Smith', 3.5, 'Economics', 3, 'Bouvé College of Health Sciences', 1, 'john.smith141@university.edu'),
(142, 'Jane', 'Johnson', 3.6, 'Political Science', 4, 'DAmore-McKim School of Business', 2, 'jane.johnson142@university.edu'),
(143, 'Michael', 'Williams', 3.7, 'Chemistry', 1, 'College of Professional Studies', 3, 'michael.williams143@university.edu'),
(144, 'Emily', 'Brown', 3.8, 'English', 2, 'Khoury College of Computer Sciences', 4, 'emily.brown144@university.edu'),
(145, 'David', 'Jones', 3.9, 'Computer Science', 3, 'College of Arts, Media and Design', 5, 'david.jones145@university.edu'),
(146, 'Sarah', 'Garcia', 3.0, 'Business', 4, 'College of Arts and Sciences', 6, 'sarah.garcia146@university.edu'),
(147, 'Robert', 'Miller', 3.1, 'Biology', 1, 'College of Computer and Information Science', 7, 'robert.miller147@university.edu'),
(148, 'Laura', 'Davis', 3.2, 'Economics', 2, 'College of Engineering', 8, 'laura.davis148@university.edu'),
(149, 'James', 'Martinez', 3.3, 'Political Science', 3, 'Bouvé College of Health Sciences', 9, 'james.martinez149@university.edu'),
(150, 'Linda', 'Hernandez', 3.4, 'Chemistry', 4, 'DAmore-McKim School of Business', 10, 'linda.hernandez150@university.edu');


INSERT INTO Skill (SkillID, SkillName) VALUES
    (1 'Data Analysis'),
    (2 'Statistical Analysis'),
    (3 'Machine Learning'),
    (4 'Project Management'),
    (5 'Technical Writing'),
    (6 'Research'),
    (7 'Laboratory Skills'),
    (8 'Data Visualization'),
    (9 'Information Literacy'),
    (10 'API Development'),

    -- Soft Skills
    (11 'Communication'),
    (12 'Teamwork'),
    (13 'Time Management'),
    (14 'Leadership'),
    (15 'Critical Thinking'),
    (16 'Problem Solving'),
    (17 'Adaptability'),
    (18 'Creativity'),
    (19 'Interpersonal Skills'),
    (20 'Conflict Resolution'),
    (21 'Organization'),
    (22 'Attention to Detail'),
    (23 'Initiative'),
    (24 'Dependability'),
    (25 'Public Speaking'),
    (26 'Collaboration'),
    (27 'Emotional Intelligence'),
    (28 'Networking'),
    (29 'Negotiation'),
    (30 'Mentoring'),

    -- Academic Skills
    (31 'Study Skills'),
    (32 'Exam Preparation'),
    (33 'Note-Taking'),
    (34 'Learning Strategies'),
    (35 'Academic Research'),
    (36 'Citation Management'),
    (37 'Ethical Reasoning'),
    (38 'Cultural Competency'),
    (39 'Diversity Awareness'),
    (40 'Teaching'),
    (41 'Presentation Skills'),
    (42 'Data Management'),
    (43 'Quantitative Reasoning'),
    (44 'Qualitative Analysis'),
    (45 'Information Synthesis');




INSERT INTO Company (CompanyID, Name, Industry, Headquarters, Size) 
VALUES
(1, 'Smith-Harris', 'Retail', 'Lake Leslie', 'L'),
(2, 'Moore Inc', 'Healthcare', 'Morrisfort', 'L'),
(3, 'Burns, Perry and Ramirez', 'Healthcare', 'Gregorymouth', 'S'),
(4, 'Gamble, Johnson and Lopez', 'Education', 'North Courtneyfurt', 'S'),
(5, 'Yu-Keith', 'Education', 'East Karenfurt', 'S'),
(6, 'Francis, Henson and Smith', 'Technology', 'East Mindyville', 'M'),
(7, 'Chavez-Drake', 'Finance', 'South Nicole', 'L'),
(8, 'Walker, Evans and Newman', 'Education', 'Markshire', 'L'),
(9, 'Taylor & Associates', 'Finance', 'West Brandon', 'M'),
(10, 'Bennett LLC', 'Technology', 'Port Jeffrey', 'S'),
(11, 'Carter, Lee and Thompson', 'Healthcare', 'Springfield', 'M'),
(12, 'Davis Corp', 'Retail', 'Riverside', 'L'),
(13, 'Edwards Group', 'Education', 'Hilltown', 'M'),
(14, 'Foster-Gray', 'Technology', 'Lakeside', 'S'),
(15, 'Garcia & Sons', 'Construction', 'Pineville', 'L'),
(16, 'Harris Enterprises', 'Finance', 'Oakwood', 'M'),
(17, 'Irwin Partners', 'Healthcare', 'Mapleton', 'S'),
(18, 'Johnson & Johnson', 'Retail', 'Brookfield', 'L'),
(19, 'Kimberly-Clark', 'Manufacturing', 'Fairview', 'M'),
(20, 'Lewis Technologies', 'Technology', 'Cedar Grove', 'S'),
(21, 'Morris Industries', 'Manufacturing', 'Elmhurst', 'M'),
(22, 'Nelson & Co.', 'Finance', 'Ashford', 'L'),
(23, 'Owens LLC', 'Healthcare', 'Greenfield', 'S'),
(24, 'Parker Enterprises', 'Education', 'Westbrook', 'M'),
(25, 'Quinn Group', 'Retail', 'Sunnyvale', 'L'),
(26, 'Robinson & Sons', 'Construction', 'Hillcrest', 'M'),
(27, 'Scott Technologies', 'Technology', 'Lakeview', 'S'),
(28, 'Turner Inc', 'Finance', 'Maplewood', 'L'),
(29, 'Underwood LLC', 'Healthcare', 'Fairview', 'M'),
(30, 'Vasquez & Associates', 'Education', 'Riverdale', 'S'),
(31, 'White Industries', 'Manufacturing', 'Greenwood', 'M'),
(32, 'Xavier Group', 'Technology', 'Pleasantville', 'L'),
(33, 'Young Enterprises', 'Retail', 'Oakridge', 'M'),
(34, 'Zimmerman LLC', 'Finance', 'Lakewood', 'S'),
(35, 'Anderson-Scott', 'Healthcare', 'Hill Valley', 'M'),
(36, 'Brown & Brown', 'Construction', 'Sunnybrook', 'L'),
(37, 'Clark Technologies', 'Technology', 'Westfield', 'M'),
(38, 'Duncan Group', 'Finance', 'Easton', 'S'),
(39, 'Evans & Co.', 'Education', 'Northgate', 'M'),
(40, 'Fletcher Inc', 'Retail', 'Southport', 'L'),
(41, 'Gibson LLC', 'Manufacturing', 'Brighton', 'M'),
(42, 'Hayes & Associates', 'Healthcare', 'Lakeview', 'S'),
(43, 'Ingram Enterprises', 'Finance', 'Riverton', 'M'),
(44, 'Jordan Group', 'Education', 'Mapleton', 'L'),
(45, 'Klein & Sons', 'Construction', 'Fairmont', 'M'),
(46, 'Long Technologies', 'Technology', 'Brookside', 'S'),
(47, 'Miller LLC', 'Retail', 'Greenfield', 'L'),
(48, 'Norton Inc', 'Finance', 'Hillcrest', 'M'),
(49, 'OConnor & Co.', 'Healthcare', 'Sunnyvale', 'S'),
(50, 'Peterson Group', 'Education', 'Westbrook', 'M');


-- Admin
INSERT INTO Admin (AdminID, FirstName, LastName, Email, Role) 
VALUES
(1, 'Dana', 'Levine', 'kristenluna@hunter-alvarez.com', 'System Administrator'),
(2, 'Gregory', 'Smith', 'deanna76@dyer-martin.com', 'System Administrator'),
(3, 'Michael', 'Gutierrez', 'benjaminvasquez@yahoo.com', 'Operations Manager');

-- Student Skills
-- Batch 1: Students 1 to 25
INSERT INTO StudentSkills (StudentID, SkillID, Proficiency) 
VALUES
    -- Student 1
    (1, 1, 8),
    (1, 26, 7),

    -- Student 2
    (2, 2, 6),
    (2, 27, 5),

    -- Student 3
    (3, 3, 9),
    (3, 28, 4),

    -- Student 4
    (4, 4, 7),
    (4, 29, 6),

    -- Student 5
    (5, 5, 8),
    (5, 30, 5),

    -- Student 6
    (6, 6, 7),
    (6, 31, 9),

    -- Student 7
    (7, 7, 5),
    (7, 32, 6),

    -- Student 8
    (8, 8, 9),
    (8, 33, 7),

    -- Student 9
    (9, 9, 6),
    (9, 34, 8),

    -- Student 10
    (10, 10, 7),
    (10, 35, 5),

    -- Student 11
    (11, 11, 8),
    (11, 36, 6),

    -- Student 12
    (12, 12, 7),
    (12, 37, 9),

    -- Student 13
    (13, 13, 5),
    (13, 38, 8),

    -- Student 14
    (14, 14, 6),
    (14, 39, 7),

    -- Student 15
    (15, 15, 9),
    (15, 40, 5),

    -- Student 16
    (16, 16, 8),
    (16, 41, 6),

    -- Student 17
    (17, 17, 7),
    (17, 42, 9),

    -- Student 18
    (18, 18, 5),
    (18, 43, 8),

    -- Student 19
    (19, 19, 6),
    (19, 44, 7),

    -- Student 20
    (20, 20, 8),
    (20, 45, 5),

    -- Student 21
    (21, 21, 7),
    (21, 46, 6),

    -- Student 22
    (22, 22, 9),
    (22, 47, 7),

    -- Student 23
    (23, 23, 5),
    (23, 48, 8),

    -- Student 24
    (24, 24, 6),
    (24, 49, 9),

    -- Student 25
    (25, 25, 8),
    (25, 50, 5),

    -- Student 26
    (26, 1, 7),
    (26, 26, 8),

    -- Student 27
    (27, 2, 6),
    (27, 27, 7),

    -- Student 28
    (28, 3, 9),
    (28, 28, 5),

    -- Student 29
    (29, 4, 7),
    (29, 29, 6),

    -- Student 30
    (30, 5, 8),
    (30, 30, 5),

    -- Student 31
    (31, 6, 7),
    (31, 31, 9),

    -- Student 32
    (32, 7, 5),
    (32, 32, 6),

    -- Student 33
    (33, 8, 9),
    (33, 33, 7),

    -- Student 34
    (34, 9, 6),
    (34, 34, 8),

    -- Student 35
    (35, 10, 7),
    (35, 35, 5),

    -- Student 36
    (36, 11, 8),
    (36, 36, 6),

    -- Student 37
    (37, 12, 7),
    (37, 37, 9),

    -- Student 38
    (38, 13, 5),
    (38, 38, 8),

    -- Student 39
    (39, 14, 6),
    (39, 39, 7),

    -- Student 40
    (40, 15, 9),
    (40, 40, 5),

    -- Student 41
    (41, 16, 8),
    (41, 41, 6),

    -- Student 42
    (42, 17, 7),
    (42, 42, 9),

    -- Student 43
    (43, 18, 5),
    (43, 43, 8),

    -- Student 44
    (44, 19, 6),
    (44, 44, 7),

    -- Student 45
    (45, 20, 8),
    (45, 45, 5),

    -- Student 46
    (46, 21, 7),
    (46, 46, 6),

    -- Student 47
    (47, 22, 9),
    (47, 47, 7),

    -- Student 48
    (48, 23, 5),
    (48, 48, 8),

    -- Student 49
    (49, 24, 6),
    (49, 49, 9),

    -- Student 50
    (50, 25, 8),
    (50, 50, 5)

    -- Student 51
    (51, 1, 7),
    (51, 26, 8),

    -- Student 52
    (52, 2, 6),
    (52, 27, 7),

    -- Student 53
    (53, 3, 9),
    (53, 28, 5),

    -- Student 54
    (54, 4, 7),
    (54, 29, 6),

    -- Student 55
    (55, 5, 8),
    (55, 30, 5),

    -- Student 56
    (56, 6, 7),
    (56, 31, 9),

    -- Student 57
    (57, 7, 5),
    (57, 32, 6),

    -- Student 58
    (58, 8, 9),
    (58, 33, 7),

    -- Student 59
    (59, 9, 6),
    (59, 34, 8),

    -- Student 60
    (60, 10, 7),
    (60, 35, 5),

    -- Student 61
    (61, 11, 8),
    (61, 36, 6),

    -- Student 62
    (62, 12, 7),
    (62, 37, 9),

    -- Student 63
    (63, 13, 5),
    (63, 38, 8),

    -- Student 64
    (64, 14, 6),
    (64, 39, 7),

    -- Student 65
    (65, 15, 9),
    (65, 40, 5),

    -- Student 66
    (66, 16, 8),
    (66, 41, 6),

    -- Student 67
    (67, 17, 7),
    (67, 42, 9),

    -- Student 68
    (68, 18, 5),
    (68, 43, 8),

    -- Student 69
    (69, 19, 6),
    (69, 44, 7),

    -- Student 70
    (70, 20, 8),
    (70, 45, 5),

    -- Student 71
    (71, 21, 7),
    (71, 46, 6),

    -- Student 72
    (72, 22, 9),
    (72, 47, 7),

    -- Student 73
    (73, 23, 5),
    (73, 48, 8),

    -- Student 74
    (74, 24, 6),
    (74, 49, 9),

    -- Student 75
    (75, 25, 8),
    (75, 50, 5),

    -- Student 76
    (76, 1, 7),
    (76, 26, 8),

    -- Student 77
    (77, 2, 6),
    (77, 27, 7),

    -- Student 78
    (78, 3, 9),
    (78, 28, 5),

    -- Student 79
    (79, 4, 7),
    (79, 29, 6),

    -- Student 80
    (80, 5, 8),
    (80, 30, 5),

    -- Student 81
    (81, 6, 7),
    (81, 31, 9),

    -- Student 82
    (82, 7, 5),
    (82, 32, 6),

    -- Student 83
    (83, 8, 9),
    (83, 33, 7),

    -- Student 84
    (84, 9, 6),
    (84, 34, 8),

    -- Student 85
    (85, 10, 7),
    (85, 35, 5),

    -- Student 86
    (86, 11, 8),
    (86, 36, 6),

    -- Student 87
    (87, 12, 7),
    (87, 37, 9),

    -- Student 88
    (88, 13, 5),
    (88, 38, 8),

    -- Student 89
    (89, 14, 6),
    (89, 39, 7),

    -- Student 90
    (90, 15, 9),
    (90, 40, 5),

    -- Student 91
    (91, 16, 8),
    (91, 41, 6),

    -- Student 92
    (92, 17, 7),
    (92, 42, 9),

    -- Student 93
    (93, 18, 5),
    (93, 43, 8),

    -- Student 94
    (94, 19, 6),
    (94, 44, 7),

    -- Student 95
    (95, 20, 8),
    (95, 45, 5),

    -- Student 96
    (96, 21, 7),
    (96, 46, 6),

    -- Student 97
    (97, 22, 9),
    (97, 47, 7),

    -- Student 98
    (98, 23, 5),
    (98, 48, 8),

    -- Student 99
    (99, 24, 6),
    (99, 49, 9),

    -- Student 100
    (100, 25, 8),
    (100, 50, 5),

    -- Student 101
    (101, 1, 7),
    (101, 26, 8),

    -- Student 102
    (102, 2, 6),
    (102, 27, 7),

    -- Student 103
    (103, 3, 9),
    (103, 28, 5),

    -- Student 104
    (104, 4, 7),
    (104, 29, 6),

    -- Student 105
    (105, 5, 8),
    (105, 30, 5),

    -- Student 106
    (106, 6, 7),
    (106, 31, 9),

    -- Student 107
    (107, 7, 5),
    (107, 32, 6),

    -- Student 108
    (108, 8, 9),
    (108, 33, 7),

    -- Student 109
    (109, 9, 6),
    (109, 34, 8),

    -- Student 110
    (110, 10, 7),
    (110, 35, 5),

    -- Student 111
    (111, 11, 8),
    (111, 36, 6),

    -- Student 112
    (112, 12, 7),
    (112, 37, 9),

    -- Student 113
    (113, 13, 5),
    (113, 38, 8),

    -- Student 114
    (114, 14, 6),
    (114, 39, 7),

    -- Student 115
    (115, 15, 9),
    (115, 40, 5),

    -- Student 116
    (116, 16, 8),
    (116, 41, 6),

    -- Student 117
    (117, 17, 7),
    (117, 42, 9),

    -- Student 118
    (118, 18, 5),
    (118, 43, 8),

    -- Student 119
    (119, 19, 6),
    (119, 44, 7),

    -- Student 120
    (120, 20, 8),
    (120, 45, 5),

    -- Student 121
    (121, 21, 7),
    (121, 46, 6),

    -- Student 122
    (122, 22, 9),
    (122, 47, 7),

    -- Student 123
    (123, 23, 5),
    (123, 48, 8),

    -- Student 124
    (124, 24, 6),
    (124, 49, 9),

    -- Student 125
    (125, 25, 8),
    (125, 50, 5),

    -- Student 126
    (126, 1, 7),
    (126, 26, 8),

    -- Student 127
    (127, 2, 6),
    (127, 27, 7),

    -- Student 128
    (128, 3, 9),
    (128, 28, 5),

    -- Student 129
    (129, 4, 7),
    (129, 29, 6),

    -- Student 130
    (130, 5, 8),
    (130, 30, 5),

    -- Student 131
    (131, 6, 7),
    (131, 31, 9),

    -- Student 132
    (132, 7, 5),
    (132, 32, 6),

    -- Student 133
    (133, 8, 9),
    (133, 33, 7),

    -- Student 134
    (134, 9, 6),
    (134, 34, 8),

    -- Student 135
    (135, 10, 7),
    (135, 35, 5),

    -- Student 136
    (136, 11, 8),
    (136, 36, 6),

    -- Student 137
    (137, 12, 7),
    (137, 37, 9),

    -- Student 138
    (138, 13, 5),
    (138, 38, 8),

    -- Student 139
    (139, 14, 6),
    (139, 39, 7),

    -- Student 140
    (140, 15, 9),
    (140, 40, 5),

    -- Student 141
    (141, 16, 8),
    (141, 41, 6),

    -- Student 142
    (142, 17, 7),
    (142, 42, 9),

    -- Student 143
    (143, 18, 5),
    (143, 43, 8),

    -- Student 144
    (144, 19, 6),
    (144, 44, 7),

    -- Student 145
    (145, 20, 8),
    (145, 45, 5),

    -- Student 146
    (146, 21, 7),
    (146, 46, 6),

    -- Student 147
    (147, 22, 9),
    (147, 47, 7),

    -- Student 148
    (148, 23, 5),
    (148, 48, 8),

    -- Student 149
    (149, 24, 6),
    (149, 49, 9),

    -- Student 150
    (150, 25, 8),
    (150, 50, 5);

-- Co-op Role
INSERT INTO CoopRole (CompanyID, Title, City, Country, Pay, RequiredGPA) VALUES
(1, 'Data Scientist', 'Boston', 'US', 45000, 3.7),
(1, 'Financial Analyst', 'Boston', 'US', 30000, 3.3),
(1, 'Software Engineer', 'Cambridge', 'US', 50000, 3.5),
(1, 'Marketing Coordinator', 'Boston', 'US', 35000, 3.4),

(2, 'Engineer', 'Cambridge', 'US', 50000, 3.5),
(2, 'Project Manager', 'Cambridge', 'US', 55000, 3.6),
(2, 'Quality Assurance Tester', 'Cambridge', 'US', 40000, 3.2),
(2, 'Technical Support Specialist', 'Cambridge', 'US', 38000, 3.1),

(3, 'Research Assistant', 'Morrisfort', 'US', 32000, 3.4),
(3, 'Lab Technician', 'Morrisfort', 'US', 34000, 3.3),
(3, 'Data Analyst', 'Morrisfort', 'US', 42000, 3.5),
(3, 'Clinical Coordinator', 'Morrisfort', 'US', 50000, 3.6),

(4, 'Social Media Manager', 'Burlington', 'US', 35000, 3.4),
(4, 'Content Strategist', 'Burlington', 'US', 36000, 3.5),
(4, 'Digital Marketing Specialist', 'Burlington', 'US', 37000, 3.2),
(4, 'Public Relations Coordinator', 'Burlington', 'US', 38000, 3.3),

(5, 'Education Consultant', 'East Karenfurt', 'US', 40000, 3.5),
(5, 'Curriculum Developer', 'East Karenfurt', 'US', 42000, 3.6),
(5, 'Academic Advisor', 'East Karenfurt', 'US', 39000, 3.4),
(5, 'Instructional Designer', 'East Karenfurt', 'US', 41000, 3.3),

(6, 'Software Developer', 'East Mindyville', 'US', 60000, 3.7),
(6, 'Systems Analyst', 'East Mindyville', 'US', 58000, 3.6),
(6, 'IT Support Specialist', 'East Mindyville', 'US', 45000, 3.4),
(6, 'Network Engineer', 'East Mindyville', 'US', 62000, 3.8),

(7, 'Financial Planner', 'South Nicole', 'US', 50000, 3.5),
(7, 'Accountant', 'South Nicole', 'US', 48000, 3.4),
(7, 'Investment Analyst', 'South Nicole', 'US', 52000, 3.6),
(7, 'Tax Specialist', 'South Nicole', 'US', 47000, 3.3),

(8, 'Educational Coordinator', 'Markshire', 'US', 39000, 3.4),
(8, 'Admissions Counselor', 'Markshire', 'US', 37000, 3.2),
(8, 'Student Services Representative', 'Markshire', 'US', 35000, 3.1),
(8, 'Registrar Assistant', 'Markshire', 'US', 33000, 3.0),

(9, 'Business Analyst', 'West Brandon', 'US', 45000, 3.5),
(9, 'Marketing Analyst', 'West Brandon', 'US', 43000, 3.4),
(9, 'Sales Manager', 'West Brandon', 'US', 50000, 3.6),
(9, 'Operations Coordinator', 'West Brandon', 'US', 41000, 3.3),

(10, 'Product Manager', 'Port Jeffrey', 'US', 65000, 3.7),
(10, 'UX/UI Designer', 'Port Jeffrey', 'US', 55000, 3.5),
(10, 'Graphic Designer', 'Port Jeffrey', 'US', 48000, 3.4),
(10, 'Quality Assurance Engineer', 'Port Jeffrey', 'US', 50000, 3.5),

(11, 'Clinical Research Coordinator', 'Springfield', 'US', 47000, 3.4),
(11, 'Healthcare Administrator', 'Springfield', 'US', 52000, 3.6),
(11, 'Nursing Assistant', 'Springfield', 'US', 35000, 3.2),
(11, 'Pharmacy Technician', 'Springfield', 'US', 36000, 3.3),

(12, 'Store Manager', 'Riverside', 'US', 45000, 3.5),
(12, 'Retail Associate', 'Riverside', 'US', 30000, 3.1),
(12, 'Inventory Specialist', 'Riverside', 'US', 32000, 3.3),
(12, 'Customer Service Representative', 'Riverside', 'US', 31000, 3.2),

(13, 'Curriculum Specialist', 'Hilltown', 'US', 42000, 3.4),
(13, 'Educational Program Coordinator', 'Hilltown', 'US', 44000, 3.5),
(13, 'Teaching Assistant', 'Hilltown', 'US', 35000, 3.1),
(13, 'Education Policy Analyst', 'Hilltown', 'US', 48000, 3.6),

(14, 'Software Tester', 'Lakeside', 'US', 40000, 3.3),
(14, 'DevOps Engineer', 'Lakeside', 'US', 58000, 3.7),
(14, 'Technical Writer', 'Lakeside', 'US', 39000, 3.2),
(14, 'Database Administrator', 'Lakeside', 'US', 60000, 3.8),

(15, 'Construction Project Manager', 'Pineville', 'US', 55000, 3.5),
(15, 'Site Supervisor', 'Pineville', 'US', 48000, 3.4),
(15, 'Safety Coordinator', 'Pineville', 'US', 50000, 3.6),
(15, 'Estimator', 'Pineville', 'US', 53000, 3.5),

(16, 'Financial Consultant', 'Oakwood', 'US', 52000, 3.5),
(16, 'Credit Analyst', 'Oakwood', 'US', 48000, 3.4),
(16, 'Risk Manager', 'Oakwood', 'US', 60000, 3.7),
(16, 'Budget Analyst', 'Oakwood', 'US', 50000, 3.3),

(17, 'Research Analyst', 'Mapleton', 'US', 44000, 3.4),
(17, 'Laboratory Technician', 'Mapleton', 'US', 40000, 3.2),
(17, 'Data Coordinator', 'Mapleton', 'US', 42000, 3.3),
(17, 'Health Services Manager', 'Mapleton', 'US', 55000, 3.6),

(18, 'Store Associate', 'Brookfield', 'US', 31000, 3.1),
(18, 'Retail Buyer', 'Brookfield', 'US', 45000, 3.4),
(18, 'Visual Merchandiser', 'Brookfield', 'US', 38000, 3.2),
(18, 'Inventory Manager', 'Brookfield', 'US', 42000, 3.3),

(19, 'Manufacturing Engineer', 'Fairview', 'US', 58000, 3.6),
(19, 'Production Supervisor', 'Fairview', 'US', 50000, 3.4),
(19, 'Quality Control Inspector', 'Fairview', 'US', 42000, 3.3),
(19, 'Process Engineer', 'Fairview', 'US', 60000, 3.7),

(20, 'Software Architect', 'Cedar Grove', 'US', 70000, 3.8),
(20, 'IT Project Manager', 'Cedar Grove', 'US', 65000, 3.7),
(20, 'Cybersecurity Analyst', 'Cedar Grove', 'US', 62000, 3.6),
(20, 'Cloud Solutions Engineer', 'Cedar Grove', 'US', 68000, 3.7),

(21, 'Manufacturing Technician', 'Elmhurst', 'US', 39000, 3.2),
(21, 'Production Planner', 'Elmhurst', 'US', 41000, 3.3),
(21, 'Logistics Coordinator', 'Elmhurst', 'US', 43000, 3.4),
(21, 'Operations Analyst', 'Elmhurst', 'US', 45000, 3.5),

(22, 'Financial Advisor', 'Ashford', 'US', 50000, 3.4),
(22, 'Investment Manager', 'Ashford', 'US', 70000, 3.8),
(22, 'Account Manager', 'Ashford', 'US', 48000, 3.3),
(22, 'Treasury Analyst', 'Ashford', 'US', 52000, 3.5),

(23, 'Healthcare Administrator', 'Greenfield', 'US', 55000, 3.6),
(23, 'Medical Billing Specialist', 'Greenfield', 'US', 42000, 3.3),
(23, 'Clinical Data Manager', 'Greenfield', 'US', 48000, 3.5),
(23, 'Health Information Technician', 'Greenfield', 'US', 40000, 3.2),

(24, 'Educational Program Manager', 'Westbrook', 'US', 45000, 3.4),
(24, 'Teaching Coordinator', 'Westbrook', 'US', 43000, 3.3),
(24, 'Admissions Counselor', 'Westbrook', 'US', 40000, 3.2),
(24, 'Student Affairs Coordinator', 'Westbrook', 'US', 42000, 3.3),

(25, 'Retail Manager', 'Sunnyvale', 'US', 48000, 3.5),
(25, 'Sales Representative', 'Sunnyvale', 'US', 35000, 3.2),
(25, 'Customer Success Manager', 'Sunnyvale', 'US', 50000, 3.6),
(25, 'E-commerce Specialist', 'Sunnyvale', 'US', 42000, 3.3),

(26, 'Construction Laborer', 'Hillcrest', 'US', 30000, 3.1),
(26, 'Site Engineer', 'Hillcrest', 'US', 55000, 3.5),
(26, 'Estimator', 'Hillcrest', 'US', 53000, 3.4),
(26, 'Project Coordinator', 'Hillcrest', 'US', 48000, 3.3),

(27, 'DevOps Specialist', 'Lakeview', 'US', 62000, 3.7),
(27, 'Systems Engineer', 'Lakeview', 'US', 60000, 3.6),
(27, 'Infrastructure Analyst', 'Lakeview', 'US', 58000, 3.5),
(27, 'Automation Engineer', 'Lakeview', 'US', 61000, 3.7),

(28, 'Business Development Manager', 'Maplewood', 'US', 52000, 3.5),
(28, 'Sales Director', 'Maplewood', 'US', 65000, 3.8),
(28, 'Account Executive', 'Maplewood', 'US', 48000, 3.3),
(28, 'Marketing Manager', 'Maplewood', 'US', 50000, 3.4),

(29, 'Quality Assurance Manager', 'Fairmont', 'US', 55000, 3.6),
(29, 'Manufacturing Supervisor', 'Fairmont', 'US', 50000, 3.4),
(29, 'Process Improvement Specialist', 'Fairmont', 'US', 53000, 3.5),
(29, 'Operations Manager', 'Fairmont', 'US', 58000, 3.7),

(30, 'Software Engineer', 'Brookside', 'US', 60000, 3.6),
(30, 'Technical Lead', 'Brookside', 'US', 65000, 3.7),
(30, 'Full Stack Developer', 'Brookside', 'US', 62000, 3.5),
(30, 'Mobile App Developer', 'Brookside', 'US', 58000, 3.4),

(31, 'Manufacturing Manager', 'Brighton', 'US', 57000, 3.6),
(31, 'Production Manager', 'Brighton', 'US', 55000, 3.5),
(31, 'Supply Chain Manager', 'Brighton', 'US', 60000, 3.7),
(31, 'Inventory Manager', 'Brighton', 'US', 52000, 3.4),

(32, 'Data Engineer', 'Pleasantville', 'US', 63000, 3.7),
(32, 'Machine Learning Engineer', 'Pleasantville', 'US', 70000, 3.8),
(32, 'Data Architect', 'Pleasantville', 'US', 68000, 3.6),
(32, 'Big Data Analyst', 'Pleasantville', 'US', 64000, 3.5),

(33, 'Store Manager', 'Oakridge', 'US', 48000, 3.4),
(33, 'Retail Sales Associate', 'Oakridge', 'US', 35000, 3.1),
(33, 'Customer Service Manager', 'Oakridge', 'US', 50000, 3.5),
(33, 'Visual Merchandiser', 'Oakridge', 'US', 42000, 3.3),

(34, 'Business Intelligence Analyst', 'Lakewood', 'US', 58000, 3.6),
(34, 'Data Visualization Specialist', 'Lakewood', 'US', 54000, 3.4),
(34, 'Analytics Manager', 'Lakewood', 'US', 62000, 3.7),
(34, 'Reporting Analyst', 'Lakewood', 'US', 50000, 3.3),

(35, 'Healthcare Coordinator', 'Hill Valley', 'US', 50000, 3.5),
(35, 'Medical Assistant', 'Hill Valley', 'US', 35000, 3.2),
(35, 'Clinical Data Analyst', 'Hill Valley', 'US', 45000, 3.4),
(35, 'Health Program Manager', 'Hill Valley', 'US', 55000, 3.6),

(36, 'Retail Associate', 'Sunnybrook', 'US', 30000, 3.1),
(36, 'Store Supervisor', 'Sunnybrook', 'US', 40000, 3.3),
(36, 'Inventory Specialist', 'Sunnybrook', 'US', 32000, 3.2),
(36, 'Sales Coordinator', 'Sunnybrook', 'US', 35000, 3.3),

(37, 'Systems Administrator', 'Westfield', 'US', 60000, 3.5),
(37, 'IT Support Engineer', 'Westfield', 'US', 45000, 3.3),
(37, 'Network Administrator', 'Westfield', 'US', 58000, 3.6),
(37, 'Security Analyst', 'Westfield', 'US', 62000, 3.7),

(38, 'Business Operations Analyst', 'Riverton', 'US', 50000, 3.4),
(38, 'Financial Operations Manager', 'Riverton', 'US', 65000, 3.7),
(38, 'Operations Coordinator', 'Riverton', 'US', 42000, 3.3),
(38, 'Process Manager', 'Riverton', 'US', 55000, 3.5),

(39, 'Educational Counselor', 'Northgate', 'US', 40000, 3.3),
(39, 'Academic Coordinator', 'Northgate', 'US', 42000, 3.4),
(39, 'Admissions Officer', 'Northgate', 'US', 38000, 3.2),
(39, 'Student Engagement Specialist', 'Northgate', 'US', 41000, 3.3),

(40, 'Store Manager', 'Southport', 'US', 50000, 3.5),
(40, 'Retail Sales Associate', 'Southport', 'US', 35000, 3.1),
(40, 'Customer Service Representative', 'Southport', 'US', 32000, 3.2),
(40, 'Inventory Manager', 'Southport', 'US', 42000, 3.3),

(41, 'Manufacturing Supervisor', 'Brighton', 'US', 55000, 3.5),
(41, 'Quality Control Specialist', 'Brighton', 'US', 45000, 3.4),
(41, 'Production Coordinator', 'Brighton', 'US', 48000, 3.3),
(41, 'Supply Chain Analyst', 'Brighton', 'US', 50000, 3.4),

(42, 'Healthcare IT Specialist', 'Fairview', 'US', 60000, 3.6),
(42, 'Clinical Systems Analyst', 'Fairview', 'US', 58000, 3.5),
(42, 'Health Informatics Specialist', 'Fairview', 'US', 62000, 3.7),
(42, 'Medical IT Coordinator', 'Fairview', 'US', 55000, 3.4),

(43, 'Data Scientist', 'Portland', 'US', 70000, 3.8),
(43, 'Machine Learning Engineer', 'Portland', 'US', 72000, 3.9),
(43, 'AI Researcher', 'Portland', 'US', 75000, 4.0),
(43, 'Data Engineer', 'Portland', 'US', 68000, 3.7),

(44, 'Business Development Associate', 'Greenville', 'US', 45000, 3.4),
(44, 'Sales Manager', 'Greenville', 'US', 60000, 3.6),
(44, 'Account Executive', 'Greenville', 'US', 50000, 3.5),
(44, 'Client Relations Manager', 'Greenville', 'US', 55000, 3.6),

(45, 'Biology Lab Assistant', 'Columbus', 'US', 35000, 3.2),
(45, 'Research Coordinator', 'Columbus', 'US', 40000, 3.4),
(45, 'Field Researcher', 'Columbus', 'US', 42000, 3.3),
(45, 'Laboratory Manager', 'Columbus', 'US', 48000, 3.5),

(46, 'Technical Support Specialist', 'Fairmont', 'US', 45000, 3.4),
(46, 'IT Consultant', 'Fairmont', 'US', 55000, 3.6),
(46, 'Help Desk Technician', 'Fairmont', 'US', 40000, 3.3),
(46, 'Systems Support Engineer', 'Fairmont', 'US', 50000, 3.5),

(47, 'Retail Store Manager', 'Mapleton', 'US', 50000, 3.5),
(47, 'Sales Associate', 'Mapleton', 'US', 32000, 3.2),
(47, 'Visual Merchandiser', 'Mapleton', 'US', 38000, 3.3),
(47, 'Customer Service Manager', 'Mapleton', 'US', 45000, 3.4),

(48, 'Financial Analyst', 'Oakridge', 'US', 48000, 3.4),
(48, 'Investment Advisor', 'Oakridge', 'US', 60000, 3.7),
(48, 'Credit Analyst', 'Oakridge', 'US', 52000, 3.5),
(48, 'Budget Analyst', 'Oakridge', 'US', 50000, 3.3),

(49, 'Retail Manager', 'Westlake', 'US', 50000, 3.5),
(49, 'Store Supervisor', 'Westlake', 'US', 42000, 3.3),
(49, 'Sales Representative', 'Westlake', 'US', 35000, 3.2),
(49, 'Customer Experience Specialist', 'Westlake', 'US', 40000, 3.4),

(50, 'Graphic Designer', 'Westbrook', 'US', 40000, 3.3),
(50, 'HR Specialist', 'Westbrook', 'US', 42000, 3.4),
(50, 'Operations Manager', 'Westbrook', 'US', 60000, 3.8),
(50, 'Sales Associate', 'Westbrook', 'US', 32000, 3.0);

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
INSERT INTO Reviews (ReviewID, DATETIME, Culture, Satisfaction, Compensation, LearningOpportunity, WorkLifeBalance, Summary, Flagged) VALUES
    (1, '2024-01-01 09:00:00', 3, 4, 3, 5, 5, 'Great experience', 57),
    (2, '2024-01-02 10:15:30', 1, 5, 4, 3, 3, 'Learned a lot', 23),
    (3, '2024-01-03 11:30:45', 4, 3, 4, 4, 3, 'Challenging work', 142),
    (4, '2024-01-04 12:45:00', 2, 4, 5, 2, 4, 'Excellent role', 89),
    (5, '2024-01-05 14:00:15', 5, 2, 3, 4, 4, 'Good learning opportunity', 176),
    (6, '2024-01-06 09:30:00', 1, 5, 4, 3, 3, 'Valuable experience', 34),
    (7, '2024-01-07 10:45:20', 4, 3, 2, 5, 5, 'Met great people', 119),
    (8, '2024-01-08 11:00:35', 2, 4, 5, 4, 4, 'Innovative projects', 67),
    (9, '2024-01-09 13:15:50', 3, 3, 3, 3, 3, 'Balanced workload', 150),
    (10, '2024-01-10 14:30:05', 5, 5, 4, 4, 4, 'Supportive team', 92),
    
    (11, '2024-01-11 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 8),
    (12, '2024-01-12 10:15:30', 4, 5, 4, 3, 3, 'Hands-on experience', 33),
    (13, '2024-01-13 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 199),
    (14, '2024-01-14 12:45:00', 5, 4, 5, 2, 4, 'Excellent learning environment', 47),
    (15, '2024-01-15 14:00:15', 3, 2, 3, 4, 4, 'Good work-life balance', 121),
    (16, '2024-01-16 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 65),
    (17, '2024-01-17 10:45:20', 4, 3, 2, 5, 5, 'Met industry experts', 176),
    (18, '2024-01-18 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 49),
    (19, '2024-01-19 13:15:50', 3, 3, 3, 3, 3, 'Balanced responsibilities', 102),
    (20, '2024-01-20 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 77),
    
    (21, '2024-01-21 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 189),
    (22, '2024-01-22 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 45),
    (23, '2024-01-23 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 160),
    (24, '2024-01-24 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 138),
    (25, '2024-01-25 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 54),
    (26, '2024-01-26 09:30:00', 3, 5, 4, 3, 3, 'Valuable networking', 99),
    (27, '2024-01-27 10:45:20', 2, 3, 2, 5, 5, 'Met industry experts', 30),
    (28, '2024-01-28 11:00:35', 4, 4, 5, 4, 4, 'Innovative tasks', 75),
    (29, '2024-01-29 13:15:50', 1, 3, 3, 3, 3, 'Balanced responsibilities', 182),
    (30, '2024-01-30 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 112),
    
    (31, '2024-01-31 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 66),
    (32, '2024-02-01 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 190),
    (33, '2024-02-02 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 138),
    (34, '2024-02-03 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 24),
    (35, '2024-02-04 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 143),
    (36, '2024-02-05 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 52),
    (37, '2024-02-06 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 178),
    (38, '2024-02-07 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 64),
    (39, '2024-02-08 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 14),
    (40, '2024-02-09 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 105),
    
    (41, '2024-02-10 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 89),
    (42, '2024-02-11 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 67),
    (43, '2024-02-12 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 176),
    (44, '2024-02-13 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 31),
    (45, '2024-02-14 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 115),
    (46, '2024-02-15 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 55),
    (47, '2024-02-16 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 93),
    (48, '2024-02-17 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 130),
    (49, '2024-02-18 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 5),
    (50, '2024-02-19 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 88),
    
    (51, '2024-02-20 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 120),
    (52, '2024-02-21 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 179),
    (53, '2024-02-22 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 33),
    (54, '2024-02-23 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 142),
    (55, '2024-02-24 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 41),
    (56, '2024-02-25 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 62),
    (57, '2024-02-26 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 15),
    (58, '2024-02-27 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 84),
    (59, '2024-02-28 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 190),
    (60, '2024-02-29 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 73),
    
    (61, '2024-03-01 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 158),
    (62, '2024-03-02 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 29),
    (63, '2024-03-03 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 104),
    (64, '2024-03-04 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 46),
    (65, '2024-03-05 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 112),
    (66, '2024-03-06 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 36),
    (67, '2024-03-07 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 150),
    (68, '2024-03-08 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 95),
    (69, '2024-03-09 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 83),
    (70, '2024-03-10 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 110),
    
    (71, '2024-03-11 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 25),
    (72, '2024-03-12 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 138),
    (73, '2024-03-13 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 170),
    (74, '2024-03-14 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 63),
    (75, '2024-03-15 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 47),
    (76, '2024-03-16 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 89),
    (77, '2024-03-17 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 105),
    (78, '2024-03-18 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 32),
    (79, '2024-03-19 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 143),
    (80, '2024-03-20 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 58),
    
    (81, '2024-03-21 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 102),
    (82, '2024-03-22 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 136),
    (83, '2024-03-23 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 44),
    (84, '2024-03-24 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 95),
    (85, '2024-03-25 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 167),
    (86, '2024-03-26 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 77),
    (87, '2024-03-27 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 56),
    (88, '2024-03-28 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 27),
    (89, '2024-03-29 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 199),
    (90, '2024-03-30 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 36),
    
    (91, '2024-03-31 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 110),
    (92, '2024-04-01 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 168),
    (93, '2024-04-02 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 85),
    (94, '2024-04-03 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 105),
    (95, '2024-04-04 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 144),
    (96, '2024-04-05 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 119),
    (97, '2024-04-06 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 34),
    (98, '2024-04-07 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 3),
    (99, '2024-04-08 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 178),
    (100, '2024-04-09 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 62),
    
    (101, '2024-04-10 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 130),
    (102, '2024-04-11 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 58),
    (103, '2024-04-12 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 95),
    (104, '2024-04-13 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 36),
    (105, '2024-04-14 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 149),
    (106, '2024-04-15 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 144),
    (107, '2024-04-16 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 81),
    (108, '2024-04-17 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 72),
    (109, '2024-04-18 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 95),
    (110, '2024-04-19 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 149),
    
    (111, '2024-04-20 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 18),
    (112, '2024-04-21 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 78),
    (113, '2024-04-22 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 162),
    (114, '2024-04-23 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 189),
    (115, '2024-04-24 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 200),
    (116, '2024-04-25 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 77),
    (117, '2024-04-26 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 5),
    (118, '2024-04-27 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 59),
    (119, '2024-04-28 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 161),
    (120, '2024-04-29 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 10),
    
    (121, '2024-05-30 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 18),
    (122, '2024-05-31 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 58),
    (123, '2024-06-01 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 130),
    (124, '2024-06-02 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 45),
    (125, '2024-06-03 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 112),
    (126, '2024-06-04 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 167),
    (127, '2024-06-05 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 81),
    (128, '2024-06-06 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 72),
    (129, '2024-06-07 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 95),
    (130, '2024-06-08 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 149),
    
    (131, '2024-06-09 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 18),
    (132, '2024-06-10 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 78),
    (133, '2024-06-11 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 162),
    (134, '2024-06-12 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 189),
    (135, '2024-06-13 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 200),
    (136, '2024-06-14 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 119),
    (137, '2024-06-15 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 34),
    (138, '2024-06-16 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 64),
    (139, '2024-06-17 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 161),
    (140, '2024-06-18 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 58),
    
    (141, '2024-06-19 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 158),
    (142, '2024-06-20 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 29),
    (143, '2024-06-21 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 104),
    (144, '2024-06-22 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 167),
    (145, '2024-06-23 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 81),
    (146, '2024-06-24 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 95),
    (147, '2024-06-25 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 33),
    (148, '2024-06-26 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 77),
    (149, '2024-06-27 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 112),
    (150, '2024-06-28 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 145),
    
    (151, '2024-06-29 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 95),
    (152, '2024-06-30 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 167),
    (153, '2024-07-01 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 81),
    (154, '2024-07-02 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 112),
    (155, '2024-07-03 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 158),
    (156, '2024-07-04 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 34),
    (157, '2024-07-05 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 77),
    (158, '2024-07-06 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 95),
    (159, '2024-07-07 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 130),
    (160, '2024-07-08 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 181),
    
    (161, '2024-07-09 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 72),
    (162, '2024-07-10 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 34),
    (163, '2024-07-11 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 145),
    (164, '2024-07-12 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 95),
    (165, '2024-07-13 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 112),
    (166, '2024-07-14 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 130),
    (167, '2024-07-15 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 95),
    (168, '2024-07-16 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 77),
    (169, '2024-07-17 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 58),
    (170, '2024-07-18 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 145),
    
    (171, '2024-07-19 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 95),
    (172, '2024-07-20 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 167),
    (173, '2024-07-21 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 81),
    (174, '2024-07-22 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 112),
    (175, '2024-07-23 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 158),
    (176, '2024-07-24 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 95),
    (177, '2024-07-25 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 34),
    (178, '2024-07-26 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 77),
    (179, '2024-07-27 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 95),
    (180, '2024-07-28 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 130),
    
    (181, '2024-07-29 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 72),
    (182, '2024-07-30 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 34),
    (183, '2024-07-31 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 145),
    (184, '2024-08-01 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 95),
    (185, '2024-08-02 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 112),
    (186, '2024-08-03 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 130),
    (187, '2024-08-04 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 95),
    (188, '2024-08-05 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 77),
    (189, '2024-08-06 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 58),
    (190, '2024-08-07 14:30:05', 5, 5, 4, 4, 4, 'Supportive colleagues', 145),
    
    (191, '2024-08-08 09:00:00', 2, 4, 3, 5, 5, 'Great mentorship', 95),
    (192, '2024-08-09 10:15:30', 3, 5, 4, 3, 3, 'Hands-on experience', 167),
    (193, '2024-08-10 11:30:45', 1, 3, 4, 4, 3, 'Challenging projects', 81),
    (194, '2024-08-11 12:45:00', 4, 4, 5, 2, 4, 'Excellent learning environment', 112),
    (195, '2024-08-12 14:00:15', 5, 2, 3, 4, 4, 'Good work-life balance', 158),
    (196, '2024-08-13 09:30:00', 2, 5, 4, 3, 3, 'Valuable networking', 95),
    (197, '2024-08-14 10:45:20', 3, 3, 2, 5, 5, 'Met industry experts', 34),
    (198, '2024-08-15 11:00:35', 1, 4, 5, 4, 4, 'Innovative tasks', 77),
    (199, '2024-08-16 13:15:50', 4, 3, 3, 3, 3, 'Balanced responsibilities', 95),
    (200, '2024-07-18 17:30:00', 5, 3, 4, 4, 4, 'Excellent role', 150);




-- Activity Logs
INSERT INTO Activity_Logs (AdminID, ActionType, Details) VALUES
(1, 'Data Analysis', NULL),
(2, 'Review Checking', NULL),
(3, 'Review Checking', NULL);