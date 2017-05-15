import sublime,sublime_plugin
import os.path

class stacktracerCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		paths_string = "/Users/qzhang/GitLab/ui/ui/lib/data_model/app/models/user_workers/permission.rb:11:in `flatten'\n/Users/qzhang/GitLab/ui/ui/lib/data_model/app/models/user_workers/permission.rb:11:in `_permissions'\n/Users/qzhang/GitLab/ui/ui/lib/data_model/app/models/user_workers/permission.rb:7:in `permissions'\n/Users/qzhang/GitLab/ui/ui/lib/data_model/app/models/user_workers/permission.rb:20:in `has_all_permissions?'\n/Users/qzhang/GitLab/ui/ui/lib/data_model/app/models/user_workers/permission.rb:34:in `has_any_permission_in_module?'\n/Users/qzhang/GitLab/ui/ui/config/initializers/navigations.rb:4:in `blo2ck in <top (required)>'\n hahhaha"
		self.paths_with_method = self.extract_valid_files(paths_string)
		# self.paths_with_col = self.get_file_list(paths_string)
		self.view.window().show_quick_panel(self.paths_with_method, self.on_highlighted, sublime.MONOSPACE_FONT,0, self.on_highlighted)

	def extract_valid_files(self, paths_string):
		file_paths = paths_string.splitlines()
		if not file_paths:
			return []
		return list(filter(lambda x: os.path.isfile(x.partition(':')[0]), file_paths))


	def on_highlighted(self, index):
		self.view.window().open_file(self.paths_with_method[index], sublime.ENCODED_POSITION, sublime.TRANSIENT)



