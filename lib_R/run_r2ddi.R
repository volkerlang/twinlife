library("r2ddi")

dir2xml(
  path_in = "temp/v2/en/",
  path_out = "r2ddi/v2/en/",
  missing_codes=-99:-70, 
  my_cores=30)
