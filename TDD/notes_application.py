class NotesApplication(object):
	"""
	This is the parent class
	"""
	##class constructor
	def __init__(self, author):
		self.author = author
		self.notes = []

	def create(self,note_content):
		"""
		A class function that takes a note and adds it to the list
		"""
		self.note_content = note_content
		if isinstance(note_content,str):
			if note_content is "":
				return "please type a string to continue"
			else:
				self.notes.append(note_content)
		if isinstance(note_content,int):
			self.notes.append(str(note_content))

	def list(self):
		pass

	def get(self,note_id):
		"""
		Takes the note's index and returns the content of that note as a string.
		"""
		return self.notes[note_id - 1]

	def search(self,search_text):
		"""
		 This function take a search string, search_text and returns all the notes
		"""
		if isinstance(search_text,str):
			for index,key_word in enumerate(self.notes):
				if key_word is not search_text:
					return "search terminated,word not found"
					
			else :
				return (str(index+1),key_word)
	def delete(self,note_id):
		"""
		This function deletes the note at the index note_id of the notes list.

		"""