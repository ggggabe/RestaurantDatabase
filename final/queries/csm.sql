use Food;

select day, restaurant_name, avg_tip+veggie_count*v_factor as csm from

    (
    select day, restaurant_name, avg(tip) as avg_tip
    from Visit
    group by day, restaurant_name
    ) g
    natural join
    (
    select day, restaurant_name, count(*) as veggie_count
    from Visit natural join Patron
    where veggie = 'Y'
    group by day, restaurant_name
    ) h

natural join
(
select restaurant_name, veggie_count/total_count as v_factor from
    ((select restaurant_name, count(item_name) as veggie_count
    from
        (Serves
        natural join
        (select name as item_name, veggie from Item) d)
    where veggie = 'Y'
    group by restaurant_name) e
        natural join
    (select restaurant_name, count(item_name) as total_count
    from Serves
    group by restaurant_name) c)
) j

into outfile '/tmp/csm.csv'
fields terminated by ','
lines terminated by '\n';
