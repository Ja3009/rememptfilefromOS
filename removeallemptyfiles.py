import os
def delete_empty_files_using_walk(root_path):
	no_of_files_deleted = 0
	for (dir, _, files) in os.walk(root_path):
		for filename in files:
			file_path = os.path.join(dir, filename)
			if (
				os.path.isfile(file_path) and
				os.path.getsize(file_path) == 0
			):
				print("Deleting File >>>", file_path.replace('\\', '/'))
				os.remove(file_path)
				no_of_files_deleted += 1
	print(no_of_files_deleted, "file(s) have been deleted.")
if __name__ == "__main__":
	root_path = input('Enter the path: ')
	delete_empty_files_using_walk(root_path)
