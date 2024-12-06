# CoOperate Database System

## Team Members
Sean Fitzgerald, Jimmy Mayer, Andrew Lengyel, Max Grotstein

## Overview
CoOperate is a comprehensive database system designed to manage cooperative education (co-op) programs for educational institutions. The system facilitates the connection between students, advisors, companies, and administrative staff while tracking co-op experiences, skills, and reviews.

## Table of Contents
- [Features](#features)
- [Database Schema](#database-schema)
- [Installation](#installation)
- [Usage](#usage)
- [Data Structure](#data-structure)
- [Security](#security)
- [Contributing](#contributing)

## Features
- Student profile management with academic information
- Advisor assignment and tracking
- Company and co-op position listings
- Skill tracking and matching
- Experience documentation
- Review system for co-op positions
- Administrative oversight and logging
- GPA and qualification tracking
- Comprehensive reporting capabilities

## Database Schema

### Core Tables
- `Students`: Stores student information including academic details
- `Advisors`: Manages academic advisor information
- `Companies`: Contains company profiles and details
- `CoopRole`: Lists available co-op positions
- `Experiences`: Tracks student work experiences
- `Reviews`: Stores student reviews of co-op experiences

### Supporting Tables
- `Skill`: Maintains skill catalog
- `StudentSkills`: Maps students to their skills with proficiency levels
- `RequiredSkills`: Maps required skills to co-op positions
- `CoopList`: Tracks applications and placements
- `Admin`: Stores administrative user information
- `Activity_Logs`: Tracks system activities

## Installation

### Prerequisites
- MySQL 5.7 or higher
- Sufficient storage space for database (recommended: 1GB minimum)

### Setup Steps
1. Clone the repository:
```bash
git clone https://github.com/yourusername/cooperate.git
```

2. Create the database:
```sql
DROP DATABASE IF EXISTS CoOperate;
CREATE DATABASE IF NOT EXISTS CoOperate;
USE CoOperate;
```

3. Run the setup script:
```bash
mysql -u your_username -p CoOperate < setup.sql
```

4. Set up the user (optional):
```sql
CREATE USER 'jimbobwe'@'%' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON CoOperate.* TO 'jimbobwe'@'%';
```

## Usage

### Basic Queries

1. View all available positions:
```sql
SELECT c.Name, cr.Title, cr.City, cr.Pay
FROM Company c
JOIN CoopRole cr ON c.CompanyID = cr.CompanyID;
```

2. Check student skills:
```sql
SELECT s.FirstName, s.LastName, sk.SkillName, ss.Proficiency
FROM Students s
JOIN StudentSkills ss ON s.StudentID = ss.StudentID
JOIN Skill sk ON ss.SkillID = sk.SkillID;
```

3. View company reviews:
```sql
SELECT c.Name, cr.Title, r.Culture, r.Satisfaction, r.Summary
FROM Reviews r
JOIN CoopRole cr ON r.PositionID = cr.PositionID
JOIN Company c ON cr.CompanyID = c.CompanyID;
```

## Data Structure

### Data Validation
- GPA values are constrained between 0 and 4.0
- Skill proficiency levels range from 1 to 10
- Review ratings range from 1 to 5
- Company sizes are categorized as S (Small), M (Medium), or L (Large)

### Relationships
- Students can have multiple skills and experiences
- Each co-op position can require multiple skills
- Students can apply to multiple positions
- Each review is linked to a specific position and student

## Security

### Access Control
- User authentication required
- Role-based access control
- Activity logging for administrative actions
- Data encryption for sensitive information

### Best Practices
- Regular backups recommended
- Periodic security audits
- Password policy enforcement
- SSL/TLS encryption for connections

## Contributing

### Guidelines
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### Code Standards
- Follow SQL best practices
- Document all major changes
- Include appropriate error handling
- Maintain data integrity constraints

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any queries or support, please contact [fitzgerald.sean@northeastern.edu]

---
**Note**: This database system is designed for educational institutions managing co-op programs. Always follow your institution's data privacy and security policies when implementing this system.
