CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW SET @quantity = @quantity - @NEW.NUMBER;
