-- script that creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
UPDATE items
FOR EACH ROW SET @quantity = @quantity - @NEW.NUMBER
WHERE name = NEW.item_name;
