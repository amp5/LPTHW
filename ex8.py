#defining the variable 'formatter' as having four strings 
formatter = "%r %r %r %r"
# prints out the variable 'formatter', having '1,2,3,4' as the four strings
print formatter % (1, 2, 3, 4)
#prints out the variable'formatter', having '"one", "two", "three", "four"' as the four strings
print formatter % ("one", "two", "three", "four")
#prints out the variable 'formatter', having 'T, F, F, T' as the four strings
print formatter % (True, False, False, True)
#prints out the variable 'formatter', having each %r defined as "%r %r %r %r". In total 16 '%r' will show up in results. 
print formatter % (formatter, formatter, formatter, formatter)
#prints out the variable 'formatter', having each line or string below one of the four strings. Note that on line 15 the string has a "'" within the string so when printed it will have double quotes vs. all of the other 3 strings above and below printing with only single quotes surrounding each string.
print formatter % (
    "I had this thing.", 
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
