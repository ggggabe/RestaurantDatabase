use Food;

select restaurant_name, item_name, veggie
from
    (Serves
    natural join
    (select name as item_name, veggie from Item) d)
order by restaurant_name, veggie
into outfile '/tmp/serves.csv'
fields terminated by ','
lines terminated by '\n';
