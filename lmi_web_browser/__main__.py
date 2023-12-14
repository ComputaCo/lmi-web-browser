import typer

from .web_browser import WebBrowser

app = typer.Typer('IDE for language models')

web_browser = WebBrowser()

@app.command()
def serve(port: int = typer.Option(..., help="The port to serve on")):
    web_browser.serve(port)

@app.command()
def cli():
    web_browser.cli()

if __name__ == "__main__":
    app()
