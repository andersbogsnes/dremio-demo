create table Nessie.staging.yelp_review as
select review_id,
       user_id,
       business_id,
       stars,
       useful,
       funny,
       cool,
       "text",
       "date"
from Reviews.raw.yelp_review;

create
or replace view Reviews.staging.yelp_review as
SELECT *
from Nessie.staging.yelp_review at branch main;