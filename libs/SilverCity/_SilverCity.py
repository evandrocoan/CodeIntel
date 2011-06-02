try:
	from _linux_libcpp6_x86._SilverCity import *
	platform = 'Linux 32 bits'
except ImportError:
	try:
		from _linux_libcpp6_x86_64._SilverCity import *
		platform = 'Linux 64 bits'
	except ImportError:
		try:
			from _win32._SilverCity import *
			platform = 'Windows 32 bits'
		except ImportError:
			try:
				from _macosx_universal._SilverCity import *
				platform = 'MacOS X Universal'
			except ImportError:
				raise
