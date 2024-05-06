create table Nessie.staging.yelp_tips as
select user_id, business_id, "text", "date", compliment_count
from Reviews.raw.yelp_tips;

create
or replace view Reviews.staging.yelp_tips as
select *
FROM Nessie.staging.yelp_tips at branch main;