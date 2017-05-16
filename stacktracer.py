import sublime,sublime_plugin
import os.path

stacktracer_current_paths = []
stacktracer_current_index = 0

class StackTracerCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		global stacktracer_current_paths, stacktracer_current_index

		file_paths_string = self.get_paths_string()
		if file_paths_string :
			stacktracer_current_paths = self.extract_valid_files(file_paths_string)
			stacktracer_current_index = 0

		if len(stacktracer_current_paths) > 0:
			self.view.window().show_quick_panel(stacktracer_current_paths, self.on_done, sublime.MONOSPACE_FONT,stacktracer_current_index, self.on_highlighted)

	def get_paths_string(self):
		file_paths_string = ''
		if len(self.view.sel()) > 0:
			file_paths_string = self.view.substr(self.view.sel()[0])
		return file_paths_string

	def extract_valid_files(self, file_paths_string):
		file_paths = list(map(lambda x: x.strip(), file_paths_string.splitlines()))
		if not file_paths:
			return []
		# sublime.error_message(str(len(file_paths)))
		return list(filter(lambda x: os.path.isfile(x.partition(':')[0]), file_paths))


	def on_highlighted(self, index):
		global stacktracer_current_paths, stacktracer_current_index
		stacktracer_current_index = index
		sublime.active_window().open_file(':'.join(list(stacktracer_current_paths[index].split(':')[:2])), sublime.ENCODED_POSITION | sublime.TRANSIENT)

	def on_done(self, index):
		if index == -1: return

		global stacktracer_current_paths, stacktracer_current_index
		stacktracer_current_index = index
		sublime.active_window().open_file(':'.join(list(stacktracer_current_paths[index].split(':')[:2])), sublime.ENCODED_POSITION)

class MoveToPreviousStackCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global stacktracer_current_paths, stacktracer_current_index
		if len(stacktracer_current_paths) > 0:
			if stacktracer_current_index < len(stacktracer_current_paths) - 1:
				stacktracer_current_index  = stacktracer_current_index + 1
			sublime.active_window().open_file(stacktracer_current_paths[stacktracer_current_index], sublime.ENCODED_POSITION)

class MoveToNextStackCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		global stacktracer_current_paths, stacktracer_current_index
		if len(stacktracer_current_paths) > 0:
			if stacktracer_current_index > 0:
				stacktracer_current_index = stacktracer_current_index - 1
			sublime.active_window().open_file(stacktracer_current_paths[stacktracer_current_index], sublime.ENCODED_POSITION)





