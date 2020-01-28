USE SPbPU

CREATE TABLE Students (
ID             INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Students PRIMARY KEY CLUSTERED (ID),
LastName       NVARCHAR(20)    NOT NULL,
FirstName      NVARCHAR(20)    NOT NULL,
SecondName     NVARCHAR(20)    NOT NULL,
DOB            DATE            NOT NULL,
GroupID        INT             NOT NULL,
CourseYear     INT             NOT NULL,
RecBookNum     NVARCHAR(30)    NOT NULL,
DepartmentID   INT             NOT NULL,
BudgContr      NVARCHAR(10)    NOT NULL,
FOE            NVARCHAR(50)    NOT NULL,
Sts            NVARCHAR(100)    NOT NULL,
Ñitizen        NVARCHAR(20)    NOT NULL,
Doc            NVARCHAR(20)    NOT NULL,
DocNum         NVARCHAR(20)    NOT NULL,
Gender         NVARCHAR(10)     NOT NULL,
);

ALTER TABLE Students
ADD CONSTRAINT FK_Students_Groups FOREIGN KEY (GroupID) REFERENCES Groups(ID),
    CONSTRAINT FK_Students_Departments FOREIGN KEY (DepartmentID) REFERENCES Departments(ID)
      ON DELETE CASCADE
      ON UPDATE CASCADE
;

CREATE TABLE Institutes (
ID         INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Institutes PRIMARY KEY CLUSTERED (ID),
Name       NVARCHAR(20)    NOT NULL,
Number     INT             NOT NULL
);

CREATE TABLE LogPss (
ID         INT            IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_LogPss PRIMARY KEY CLUSTERED (ID),
Lin       NVARCHAR(30)    NOT NULL,
Psword    NVARCHAR(30)    NOT NULL
);

CREATE TABLE Departments (
ID           INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Departments PRIMARY KEY CLUSTERED (ID),
Name         NVARCHAR(100)    NOT NULL,
InstituteID  INT             NOT NULL,
);

ALTER TABLE Departments
ADD CONSTRAINT FK_Departments_Institutes FOREIGN KEY (InstituteID) REFERENCES Institutes(ID)
      ON DELETE CASCADE
      ON UPDATE CASCADE
;

CREATE TABLE YGSNs (
ID         INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_YGSNs PRIMARY KEY CLUSTERED (ID),
Name       NVARCHAR(20)    NOT NULL,
);

CREATE TABLE Directions (
ID         INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Directions PRIMARY KEY CLUSTERED (ID),
Name       NVARCHAR(20)    NOT NULL,
YGSNID     INT             NOT NULL,
);

ALTER TABLE Directions
ADD CONSTRAINT FK_Directions_YGSNs FOREIGN KEY (YGSNID) REFERENCES YGSNs(ID)
      ON DELETE CASCADE
      ON UPDATE CASCADE
;

CREATE TABLE Profiles (
ID          INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Profiles PRIMARY KEY CLUSTERED (ID),
Name        NVARCHAR(20)    NOT NULL,
DirectionID INT             NOT NULL
); 

CREATE TABLE Groups (
ID           INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Groups PRIMARY KEY CLUSTERED (ID),
Number       NVARCHAR(20)    NOT NULL,
InstituteID  INT             NOT NULL,
Degree       NVARCHAR(20)    NOT NULL,
ProfilesID   INT             NOT NULL,
);

ALTER TABLE Groups
ADD CONSTRAINT FK_Groups_Profiles FOREIGN KEY (ProfilesID) REFERENCES Profiles(ID),
    CONSTRAINT FK_Groups_Institutes FOREIGN KEY (InstituteID) REFERENCES Institutes(ID)
      ON DELETE CASCADE
      ON UPDATE CASCADE
;

CREATE TABLE Statuses (
ID        INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Statuses PRIMARY KEY CLUSTERED (ID),
Name      NVARCHAR(100)   NOT NULL,
);

CREATE TABLE Teachers (
ID               INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Teachers PRIMARY KEY CLUSTERED (ID),
LastName         NVARCHAR(20)    NOT NULL,
FirstName        NVARCHAR(20)    NOT NULL,
SecondName       NVARCHAR(20)    NOT NULL,
Position         NVARCHAR(20)    NOT NULL,
Rate             REAL            NOT NULL,
FinancingSource  NVARCHAR(20)    NOT NULL,
Registr          NVARCHAR(30)    NOT NULL,
);

CREATE TABLE Subjects (
ID           INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Subjects PRIMARY KEY CLUSTERED (ID),
Name         NVARCHAR(100)    NOT NULL,
);

CREATE TABLE Schedule (
ID            INT             IDENTITY (1, 1) NOT NULL, CONSTRAINT PK_Schedule PRIMARY KEY CLUSTERED (ID),
DateAndTime   DATETIME        NOT NULL,
GroupID       INT             NOT NULL,
SubjectID     INT             NOT NULL,
Type          NVARCHAR(20)    NOT NULL,
TeacherID     INT             NOT NULL,
Ñlassroom     NVARCHAR(20)    NOT NULL,
);

ALTER TABLE Schedule
ADD CONSTRAINT FK_Schedule_Groups FOREIGN KEY (GroupID) REFERENCES Groups(ID),
    CONSTRAINT FK_Schedule_Subjects FOREIGN KEY (SubjectID) REFERENCES Subjects(ID),
	CONSTRAINT FK_Schedule_Teachers FOREIGN KEY (TeacherID) REFERENCES Teachers(ID)
      ON DELETE CASCADE
      ON UPDATE CASCADE
;

