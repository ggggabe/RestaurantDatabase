use Food;

(select day, avg(tip) from
    (select * from Visit where restaurant_name = 'Harvest') a
group by day) c

(select count(*) from
    (select firstname, lastname from Patron
        where veggie = 'Y'
        and
        (firstname, lastname) in
        (select distinct firstname, lastname from
        (select * from Visit
            where restaurant_name = 'Harvest'
            and day = c.day) b
    ) d
)

-- (select sum(tip)
--     from Visit v1
--     where v1.restaurant_name = a.restaurant_name
--         and v1.day = a.day)
-- /
-- (select count(*)
--     from
--     (select *
--         from Visit v2
--         where v2.restaurant_name = a.restaurant_name
--             and v2.day = a.day) b)
-- +
-- (select count(*)
--     from
--     (select *
--         from Patron p1
--         where p1.firstname = a.firstname
--             and p1.lastname = a.


into outfile '/tmp/csm.csv'
fields terminated by ','
lines terminated by '\n';
