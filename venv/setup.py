from setuptools import find_packages, setup

setup(
	name='music_theory',
	packages=find_packages(include=['music_theory']),
	version='0.1.0',
	description='An open source Python library of Music Theory functions!',
	author='Devon Hubert',
	license='Open Source',
	install_requires=[],
	setup_requires=['pytest-runner'],
	tests_require=['pytest==4.4.1'],
	test_suite='tests',
)