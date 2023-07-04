"""
Use livereload to serve the blogpost as an html page
"""
import subprocess
import livereload

watch = [
    "blogpost.md",
    "references.bib",
    "figs/*",
]
build_dir = "_build"


# Build the website with make
command = "make html"
subprocess.run(command.split())

# Start the server and watch for changes
server = livereload.Server()
make_html = livereload.shell(command)
for path in watch:
    server.watch(path, func=make_html)
server.serve(root=build_dir, open_url_delay=1)
