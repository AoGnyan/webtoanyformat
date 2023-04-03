# Convert .webp files to almost any picture format

This is a Python script that converts .webp files to almost any picture format. You can run the script in a Jupyter notebook and modify the input directory and output format to suit your needs.

## Prerequisites

Before using this script, you will need:

1. [Python](https://www.python.org) installed on your computer.
2.  Required Python Libraries
    - Pillow - a Python Imaging Library (PIL) fork.
    - os - a module that provides a portable way of using operating system dependent functionality.

3. [Vs code](https://code.visualstudio.com).

## Getting Started

To get started:

1. Open VSCode.
2. Open the folder where the files are (Ctrl+k followed by Ctrl+o)
3. Create a new file and select Jupyter notebook when prompted.
4. Copy and paste the code from this repository into the new Jupyter notebook file and run it.


# Adding Required Libraries

To run the script, you will need to install the following libraries:

1. Pillow - a Python Imaging Library (PIL) fork.
2. os - a module that provides a portable way of using operating system dependent functionality.

To install these libraries, you can use the pip package manager inside the jupyter notebook.

1. To install Pillow use:
pip install Pillow
2. To install os use:
pip install os

## Usage

To use the script, you will need to modify the input directory and the output format to match your needs. Here's how you can do it:

In the code, replace /path/to/webp/files with the path to the directory that contains the .webp files you want to convert.
In the code, replace /path/to/jpg/files with the path to the directory where you want to save the converted files. You can also replace .jpg with the file extension of your choice.
Run the script by pressing the "Run" button in the Jupyter notebook.
The script will convert all of the .webp files in the input directory to the specified output format and save them in the output directory. The original .webp files will be moved to a new folder named "old".

## Troubleshooting

If you encounter issues with the script:

1. Ensure that the python kernel is being read by your IDE.
2. Check that the input and output directories are correct.
3. Verify that you have the necessary permissions to read from and write to the directories.
4. Ensure that the file extension you specified is valid for the output format you want to use.

If you need further assistance, please feel free to open an issue in this repository.
