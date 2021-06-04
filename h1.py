def is_leap(year):
    leap = False
    
    if(year%4==0 and year in range(1900,10**5)):
        leap=True
    
    print(leap)

year = 2100
is_leap(year)