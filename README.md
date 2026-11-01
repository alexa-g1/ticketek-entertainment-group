# ticketek-entertainment-group
# using pyspark because spark is required from job description, although pandas could be used for such a small data set, i wanted to show my spark capabilities for a simple pipeline.
# sale_date as a string in the read schema because formats are different and needs transformation first
# for transformation: missing product_id would already be null swhen using spark so nothing needed there
# put schemas in seperate files for easier readabilility and easier to update
# used distinct instead of drop duplicates because no need to specify on specific keys since whole rows data is duplicated. 