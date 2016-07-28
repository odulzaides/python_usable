dict_1= {

       'Endurance':{'mult':[.56,.75], 'p_range':[]},
       'Tempo':{'mult':[.76,.95], 'p_range':[]},
       'VO2':{'mult':[.96,1.05],'p_range':[]}
}
def zones_calc(ftp):
    var_1 = ftp
    for v1 in dict_1.values():
        for v in v1['mult']:
            v1['p_range'].append(var_1 * v)
zones_calc(200)

for k,v in dict_1.iteritems():
	print k,v['p_range']

dict_2 = {
	'movies':{
		'comedies': ['big', 'king of Comedy'], 
		'drama':['One flew over the Cuckoos Nest', 'Apocalypse Now'],
		'comedy-drama':['Goerge', 'bernie\'s']
	},
	'documentaries':{
		'war':['Civil war', 'WW II'],
		'science':['planets', 'earth']
	},

	'shorts':{
		'10 minute': ['Aging', 'children'],
		'fact':['math', 'geology']
	}	
}
# Loop to print out dict_2
for keys, values in dict_2.iteritems():
	# print 'This is 1st FOR LOOP  ==>>' , keys.upper()
	print '='*40
	print "**** Here are the {} we have ****".format(keys.upper())
	print '='* 40, "\n"
	#Second FOR LOOP
	for k, item  in values.iteritems():
		
		print "\tThese are the {0} {1}".format(k.upper(), keys)
		print '\t','-'*50
		
		#print "this is the 3rd FOR LOOP"
		for i in item:
			print "\t\t",i
		
		print "\n"
	
