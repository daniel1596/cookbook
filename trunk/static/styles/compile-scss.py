from sass import compile
from subprocess import run

""""Notes on sass.compile() syntax

I tried using different syntax to only copy index.scss to index.css
However, libsass doesn't have a way to do that - unless I were to move variables.scss into a separate folder.
So, for now, I'll just have an empty "variables.css" file and it won't hurt anything.

It seems funky, but there really isn't a need to spend a ton of time on this now.

compile(filename=f'{sass_folder}/index.scss', output_style="compressed")  # returns the css as a string
"""


try:
	compile(dirname=("scss", "css"), output_style="compressed")
except Exception as e:
	print(e, end="\n\n")
	print("SCSS compilation failed.")
	run("pause", shell=True)
else:
	print("SCSS compilation succeeded.")