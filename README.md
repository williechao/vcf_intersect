# vcf_intersect
### Summary
Different variant callers use different statistical models to find mutations between normal and tumor cells. This pipeline allows you to call common mutations found across different variant callers, resulting in very high confidence variant calls.

### Usage
Download the script and run it directly like 
```
python vcf_intersect.py -i "[file 1] [& or |] [file2] [& or |] [file 3] ..." -o [output_file]
```
(quotations are necessary)

#### NOTE
This program only provides the most rudementary information about the mutations, please refer back to the original VCFs to get more information about the mutations. A great way to do this is to import all your VCFs into IGV.

Email: willielwchao@gmail.com
