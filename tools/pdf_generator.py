"""
pdf_generator.py — Geração de PDF para entregas da Automaturge.

Converte conteúdo Markdown estruturado em PDF profissional.
Requer: pip install reportlab markdown weasyprint (ou usa pandoc via subprocess)

Uso:
    python pdf_generator.py input.md --output relatorio.pdf --title "Parâmetros DH JAKA Pro 16"
    python pdf_generator.py --content "# Título\n\n## Seção..." --output saida.pdf
"""

import sys
import os
import argparse
import subprocess
import tempfile


def generate_with_pandoc(markdown_content: str, output_path: str, title: str = "", author: str = "Automaturge") -> str:
    """
    Gera PDF via Pandoc (preferido — suporta LaTeX, tabelas, fórmulas matemáticas).
    Requer: pandoc + pdflatex ou xelatex instalados.
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        # Adiciona frontmatter YAML para metadados
        frontmatter = f"""---
title: "{title}"
author: "{author}"
date: "\\today"
geometry: margin=2.5cm
fontsize: 11pt
numbersections: true
toc: true
---

"""
        f.write(frontmatter + markdown_content)
        tmp_path = f.name

    try:
        cmd = [
            "pandoc", tmp_path,
            "-o", output_path,
            "--pdf-engine=xelatex",
            "-V", "lang=pt-BR",
            "-V", "colorlinks=true",
            "-V", "linkcolor=blue",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            raise RuntimeError(f"Pandoc error: {result.stderr}")
    finally:
        os.unlink(tmp_path)

    return output_path


def generate_with_weasyprint(markdown_content: str, output_path: str, title: str = "") -> str:
    """
    Gera PDF via WeasyPrint (fallback — não requer LaTeX).
    Requer: pip install weasyprint markdown
    """
    try:
        import markdown
        from weasyprint import HTML, CSS
    except ImportError:
        raise ImportError("Instale: pip install weasyprint markdown")

    # Converte markdown para HTML
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    body_html = md.convert(markdown_content)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
    body {{ font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 11pt; line-height: 1.6; margin: 0; padding: 0; color: #1a1a1a; }}
    h1, h2, h3 {{ color: #2c3e50; margin-top: 1.5em; }}
    h1 {{ font-size: 20pt; border-bottom: 2px solid #2c3e50; padding-bottom: 0.3em; }}
    h2 {{ font-size: 15pt; border-bottom: 1px solid #bdc3c7; padding-bottom: 0.2em; }}
    table {{ border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 10pt; }}
    th {{ background: #2c3e50; color: white; padding: 8px 12px; text-align: left; }}
    td {{ border: 1px solid #bdc3c7; padding: 6px 12px; }}
    tr:nth-child(even) {{ background: #f8f9fa; }}
    code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: monospace; font-size: 9pt; }}
    pre {{ background: #f4f4f4; padding: 1em; border-radius: 5px; overflow-x: auto; }}
    pre code {{ background: none; padding: 0; }}
    @page {{ margin: 2.5cm; @bottom-center {{ content: "Automaturge · " attr(title) " · Página " counter(page) " de " counter(pages); font-size: 8pt; color: #7f8c8d; }} }}
  </style>
</head>
<body>
  <h1>{title}</h1>
  {body_html}
</body>
</html>"""

    HTML(string=html).write_pdf(output_path)
    return output_path


def generate(content_markdown: str, output_path: str, title: str = "", author: str = "Automaturge") -> str:
    """
    Ponto de entrada principal. Tenta Pandoc, cai para WeasyPrint.

    Args:
        content_markdown: Conteúdo em Markdown (pode conter tabelas, fórmulas $$..$$)
        output_path:      Caminho de saída (ex: 'relatorio.pdf')
        title:            Título do documento
        author:           Autor (padrão: Automaturge)

    Returns:
        Caminho do arquivo PDF gerado
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    # Tenta Pandoc primeiro (melhor qualidade)
    if subprocess.run(["which", "pandoc"], capture_output=True).returncode == 0:
        try:
            return generate_with_pandoc(content_markdown, output_path, title, author)
        except Exception as e:
            print(f"[WARN] Pandoc falhou ({e}), tentando WeasyPrint...", file=sys.stderr)

    # Fallback: WeasyPrint
    return generate_with_weasyprint(content_markdown, output_path, title)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automaturge PDF Generator")
    parser.add_argument("--input", help="Arquivo .md de entrada")
    parser.add_argument("--content", help="Conteúdo Markdown direto (alternativa ao --input)")
    parser.add_argument("--output", required=True, help="Arquivo .pdf de saída")
    parser.add_argument("--title", default="", help="Título do documento")
    parser.add_argument("--author", default="Automaturge", help="Autor")
    args = parser.parse_args()

    if args.input:
        with open(args.input, encoding="utf-8") as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        content = sys.stdin.read()

    result = generate(content, args.output, args.title, args.author)
    print(f"PDF gerado: {result}")
