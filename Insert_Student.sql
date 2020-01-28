CREATE PROCEDURE Insert_Student
@LastName       NVARCHAR(20),
@FirstName      NVARCHAR(20),
@SecondName     NVARCHAR(20),
@DOB            DATE,
@Group          NVARCHAR(20),
@CourseYear     INT,
@RecBookNum     INT,
@BudgContr      NVARCHAR(10),
@FOE            NVARCHAR(10),
@StsID          INT,
@Ñitizen        NVARCHAR(20),
@Doc            NVARCHAR(20),
@DocNum         NVARCHAR(20),
@Gender         NVARCHAR(10)
AS
BEGIN
 INSERT INTO Students VALUES(@LastName, @FirstName, @SecondName, @DOB, 
 (SELECT ID FROM Groups WHERE Number = @Group), @CourseYear, @RecBookNum, @BudgContr,
 @FOE, @StsID, @Ñitizen, @Doc, @DocNum, @Gender)
END
