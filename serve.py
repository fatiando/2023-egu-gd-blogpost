"""
Use livereload to serve the blogpost as an html page
"""
import livereload

watch = [
    "blogpost.md",
    "references.bib",
    "figs/*",
]
build_dir = "_build"


server = livereload.Server()
make_html = livereload.shell("make html")
for path in watch:
    server.watch(path, func=make_html)
server.serve(root=build_dir, open_url_delay=1)
