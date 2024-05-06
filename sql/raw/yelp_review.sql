create view Reviews.raw.yelp_review as
select *
from datalake."demo-datalake"."extract"."yelp_academic_dataset_review.json"