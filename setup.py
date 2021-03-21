from setuptools import setup

setup (
	name='yoga-370',
	version='1.0',
	install_requires=[
		'click'
	],
	entry_points='''
		[console_scripts]
		yoga=project.cli:cli
	''',
)
