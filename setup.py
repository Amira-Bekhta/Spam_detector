from setuptools import setup, find_packages

setup(
    name="spam_detector",  # Your project name
    version="0.1",  # Initial version
    packages=find_packages(where="src"),  # Automatically find packages in the 'src' directory
    package_dir={"": "src"},  # The packages are inside the 'src' folder
    install_requires=[  # Add any dependencies here
        # "numpy",
        # "pandas",
    ],
    include_package_data=True,  # If you want to include non-Python files (like data)
)
