# Testing Vale rule 14

## Numbers greater than nine should be in numeric form
<!--This test will produce 38 warnings-->

### Test heading to test the following sixteen numbers

Ten
Eleven
Twelve
Thirteen
Fourteen
Fifteen
Nine hundred and sixteen
Six thousand and seventeen
Fifty thousand and five hundred
Eighteen billion
Ninety million
Twenty trillion
Seventy million eight thousand and one
Sixty billion forty million thirty thousand and nineteen
Five
Nine

### Test scope for tables

| billion | ninety | fifty|
|---------|---------|------|
| hundred |thousand |twenty|

### Test scope for list

- Hundred
- Twenty
- Five

## Numbers greater than 9999 should have comma separators
<!--This test will produce 5 warnings-->

1000
23400
8767862
90283737
347874838
1000000000
3
46
345
