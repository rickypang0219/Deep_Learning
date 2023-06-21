# Data Engineering ith Amazon Web Services (AWS)

# Data Engineering 
## Amazon S3 
Amazon Simple Storage Service (S3) provides storage services to store *objects (files)*  inside any *buckets (directories)*. The name of any bucket must have a globally unique name. For each object, there is a *key* associated which is the full path of that object. Here are the example of keys

* <my_bucket>/my_file.txt
* <my_bucket>/my_folder/another_folder/my_file.txt
  
For the data partitioning, a good partitioning can speed up a range of queries. For instance, we can partition the data by date or product id

* By Date: s3://bucket/my-data-set/year/month/day/date.csv 
* By Product id: s3://bucket/my-data-set/product_id/data.csv 


## Amazon S3 Storage Classes & Glacier

Here is a list of S3 standard classes for data that is less frequently accessed, but requires rapid access when needed
* S3 Standard
* S3 Standard-Infrequent Access (S3 Standard-IA)
* S3 One Zone-Infrequent Access (S3 One Zone-IA)

And here is the Glacier classes for *archive and backup*
*  S3 Glacier Instant Retrieval
*  S3 Glacier Flexible Retrieval
*  S3 Glacier Deep Archive


  
