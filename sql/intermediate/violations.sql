create or replace view Reviews.intermediate.violations as
select m.yelp_id, v."date", v.minor, v.major, v.severe from Reviews.staging.violations as v
join Reviews.staging.id_mappings as m
on v.restaurant_id = m.restaurant_id;
