CREATE OR REFRESH STREAMING TABLE we47catalog1.default.drugstbl_bronze2
AS
SELECT *
FROM STREAM(lakehousecat.deltadb.drugstbl);