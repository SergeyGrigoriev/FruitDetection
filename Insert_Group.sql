CREATE PROCEDURE Insert_Group
@NewName NVARCHAR(500),
@Inst NVARCHAR(500),
@Degree       NVARCHAR(20),
@Prof  INT,
@Direct NVARCHAR(500),
@Inst_num INT
AS
DECLARE @NAM VARCHAR (500)
DECLARE @CURSOR CURSOR
DECLARE @Flag INT = 0

SET @CURSOR  = CURSOR SCROLL
FOR
SELECT Number FROM  Groups

OPEN @CURSOR
FETCH NEXT FROM @CURSOR INTO @NAM
WHILE @@FETCH_STATUS = 0
BEGIN
        IF (@NewName=@NAM)
        BEGIN
		 SET @Flag = 1;
        END
FETCH NEXT FROM @CURSOR INTO @NAM
END
CLOSE @CURSOR
IF (@Flag=0)
 BEGIN
  INSERT INTO Groups VALUES(@NewName, (SELECT ID FROM Institutes WHERE Name = @Inst), @Degree,
  (SELECT ID FROM Profiles WHERE Name = @Prof), (SELECT ID FROM Directions WHERE Name = @Direct))
  UPDATE Institutes SET Institutes.Number = @Inst_num WHERE Name = @Inst
 END