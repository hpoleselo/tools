import os

#print os.listdir(".")


class ExtensionSearcher(object):
	def __init__(self):
		self.receivedParam = "test.gcode"
		self.search()

	def search(self):
		# Lists all the files on the current folder that this Python script is running
		files = os.listdir(".")

		py_files = []

		# Search for files that have extension Python
		for file in files:
			if file.endswith('.py'):
				py_files.append(file)
			elif file == self.receivedParam:
				print("Sending to printer...")
		if file != self.receivedParam:
			print("Requested file: ") + self.receivedParam + " not found in the package directory."
			print("Files with the extension .py that have been found: ")
			for i in range(len(py_files)):
				print py_files[i]

def run():
	es = ExtensionSearcher()


if __name__ == "__main__":
	run()




