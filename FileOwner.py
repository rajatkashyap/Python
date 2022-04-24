'''
Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
'''
class FileOwners:

    @staticmethod
    def group_by_owners(files):
		dict_files={}
		items=files.items()
		for k,v in items:
			#print v,k
			list_files=[]
			if v in dict_files:
				print dict_files[v]
				print k
				dict_files[v].append(k)
			else:
				dict_files[v]=[k]
				print dict_files
		return dict_files

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))