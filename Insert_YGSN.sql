CREATE PROCEDURE Insert_YGSN
@NewName NVARCHAR(500)
AS
DECLARE @NAM VARCHAR (500)
DECLARE @CURSOR CURSOR
DECLARE @Flag INT = 0

SET @CURSOR  = CURSOR SCROLL
FOR
SELECT NAME FROM  YGSNs

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
  INSERT INTO YGSNs VALUES(@NewName)
 END