"""
web_search.py — Ferramenta de busca na internet para o Executor da Automaturgia.

Usa DuckDuckGo (sem API key) como backend primário.
Para resultados mais ricos, configure SERPER_API_KEY no ambiente.

Uso:
    python web_search.py "JAKA Pro 16 DH parameters" --max 5
    python web_search.py "palletization cobot cycle time" --max 10 --format json
"""

import sys
import json
import argparse
import urllib.parse
import urllib.request
import os


def search_duckduckgo(query: str, max_results: int = 5) -> list[dict]:
    """Busca via DuckDuckGo Instant Answer API (sem key, limitado)."""
    encoded = urllib.parse.quote_plus(query)
    url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1&skip_disambig=1"

    req = urllib.request.Request(url, headers={"User-Agent": "Automaturgia/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())

    results = []

    # Abstract (primeiro resultado direto)
    if data.get("Abstract"):
        results.append({
            "title": data.get("Heading", query),
            "url": data.get("AbstractURL", ""),
            "snippet": data["Abstract"],
            "source": "duckduckgo_abstract"
        })

    # Related Topics
    for topic in data.get("RelatedTopics", [])[:max_results]:
        if isinstance(topic, dict) and topic.get("Text"):
            results.append({
                "title": topic.get("Text", "")[:80],
                "url": topic.get("FirstURL", ""),
                "snippet": topic.get("Text", ""),
                "source": "duckduckgo_related"
            })

    return results[:max_results]


def search_serper(query: str, max_results: int = 5) -> list[dict]:
    """Busca via Serper.dev (requer SERPER_API_KEY). Resultados mais ricos."""
    api_key = os.environ.get("SERPER_API_KEY")
    if not api_key:
        raise ValueError("SERPER_API_KEY não configurado. Use DuckDuckGo ou configure a chave.")

    payload = json.dumps({"q": query, "num": max_results}).encode()
    req = urllib.request.Request(
        "https://google.serper.dev/search",
        data=payload,
        headers={"X-API-KEY": api_key, "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())

    results = []
    for item in data.get("organic", [])[:max_results]:
        results.append({
            "title": item.get("title", ""),
            "url": item.get("link", ""),
            "snippet": item.get("snippet", ""),
            "source": "serper_organic"
        })
    return results


def search(query: str, max_results: int = 5) -> list[dict]:
    """
    Ponto de entrada principal. Usa Serper se disponível, DuckDuckGo como fallback.

    Args:
        query:       Consulta de busca em linguagem natural ou técnica
        max_results: Número máximo de resultados (padrão: 5)

    Returns:
        Lista de dicts com keys: title, url, snippet, source
    """
    if os.environ.get("SERPER_API_KEY"):
        return search_serper(query, max_results)
    return search_duckduckgo(query, max_results)


def format_for_agent(results: list[dict]) -> str:
    """Formata resultados para ingestão por um agente de IA."""
    if not results:
        return "Nenhum resultado encontrado."

    lines = []
    for i, r in enumerate(results, 1):
        lines.append(f"[{i}] {r['title']}")
        lines.append(f"    URL: {r['url']}")
        lines.append(f"    {r['snippet']}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automaturgia Web Search Tool")
    parser.add_argument("query", help="Consulta de busca")
    parser.add_argument("--max", type=int, default=5, help="Número máximo de resultados")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    results = search(args.query, args.max)

    if args.format == "json":
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(format_for_agent(results))
