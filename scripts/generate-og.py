#!/usr/bin/env python3
"""Render the blog's localized 1200 × 630 OpenGraph cards.

Requires Python 3.11+, rsvg-convert, fc-scan, and a Chinese font.
Example: python3 scripts/generate-og.py --cjk-font /path/to/MapleMono-NF-CN-Regular.ttf
The site's own Source Code Pro font is used for Latin text.
"""

import argparse
from functools import lru_cache
import html
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import tomllib
import unicodedata
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT = 1200, 630
BACKGROUND, AMBER, WHITE, GREY, BLUE, PINK = (
    "#151515", "#ffbf00", "#eaeaea", "#999999", "#63c0f5", "#fc60a8"
)


def text_width(text):
    """Widths in half-em cells for the monospaced Latin and CJK fonts."""
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in text)


def wrap_title(title, limit):
    # Keep English words together and allow breaks between Chinese characters.
    tokens = re.findall(r"[\x21-\x7e]+|\s+|[^\x00-\x7f]", title)
    lines, current = [], ""
    for token in tokens:
        if text_width(current + token) > limit and current.strip():
            # Avoid starting a Chinese line with closing punctuation.
            if token in "，。！？；：、）》」』”’":
                current += token
                continue
            lines.append(current.rstrip())
            current = ""
        current += token.lstrip() if not current else token
    if current.strip():
        lines.append(current.rstrip())
    line_count = len(lines)
    target = text_width(title) / line_count

    @lru_cache(maxsize=None)
    def balanced(start, remaining):
        while start < len(tokens) and tokens[start].isspace():
            start += 1
        if not remaining:
            return (0, []) if start == len(tokens) else (float("inf"), [])
        best = (float("inf"), [])
        for end in range(start + 1, len(tokens) + 1):
            line = "".join(tokens[start:end]).strip()
            if not line or text_width(line) > limit:
                continue
            if end < len(tokens) and tokens[end] in "，。！？；：、）》」』”’":
                continue
            cost, rest = balanced(end, remaining - 1)
            score = (text_width(line) - target) ** 2 + cost
            if score < best[0]:
                best = (score, [line] + rest)
        return best

    _, balanced_lines = balanced(0, line_count)
    return balanced_lines or lines


def title_layout(title, preferred_lines=None):
    if preferred_lines and re.sub(r"\s", "", "".join(preferred_lines)) != re.sub(r"\s", "", title):
        raise ValueError(f"OpenGraph line breaks must preserve the title: {title}")
    for size in range(64, 39, -2):
        # Both fonts use a 0.6-em Latin advance; reserve room for punctuation.
        lines = preferred_lines or wrap_title(title, int(1040 / (size * 0.6)))
        if len(lines) <= 3 and all(text_width(line.replace("`", "")) * size * 0.6 <= 1072 for line in lines):
            return size, lines
    raise ValueError(f"Title needs a different layout: {title}")


def svg_card(post, language, cjk_family):
    title = post["title"]
    size, lines = title_layout(title, post.get("extra", {}).get("og_title_lines"))
    esc = html.escape
    font = esc(f"Source Code Pro ExtraLight, {cjk_family}", quote=True)
    badge = "ZH / 简体中文" if language == "zh" else "EN / ENGLISH"
    subtitle = "守望梦境" if language == "zh" else "LitoMore's Mind"
    accent = BLUE if language == "zh" else AMBER
    published = post.get("date")
    date_label = str(published)[:10] if published else ""
    if post.get("draft"):
        date_label = ("草稿" if language == "zh" else "DRAFT") + (
            " / " + date_label if date_label else ""
        )
    tags = post.get("taxonomies", {}).get("tags", [])
    tags_label = "[ " + ", ".join(tags) + " ]" if tags else ""
    tag_size = min(21, 1040 / max(text_width(tags_label) * 0.6, 1))
    # Reuse the site's striped favicon as a small, static amber mark.
    logo = ET.parse(ROOT / "static/favicon.svg").find("{http://www.w3.org/2000/svg}path").get("d")
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        f'<title>{esc(title)}</title>',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{BACKGROUND}"/>',
        '<rect width="1200" height="136" fill="#111111"/>',
        f'<path d="{logo}" fill="{AMBER}" transform="translate(64 57) scale(1.5)"/>',
        f'<g font-family="{font}" font-weight="400">',
        f'<text x="118" y="83" font-size="34" fill="{AMBER}">litomore.me</text>',
        f'<text x="119" y="112" font-size="18" fill="{GREY}">{esc(subtitle)}</text>',
        f'<rect x="914" y="56" width="222" height="44" rx="4" fill="none" stroke="{accent}" stroke-opacity="0.6"/>',
        f'<text x="1025" y="85" text-anchor="middle" font-size="19" fill="{accent}">{badge}</text>',
        f'<path d="M64 136 H1136" stroke="{AMBER}" stroke-width="1" stroke-dasharray="5 7"/>',
        f'<text x="64" y="192" font-size="20" fill="{GREY}">./{"zh/" if language == "zh" else ""}posts/</text>',
    ]
    baseline = 338 - (len(lines) - 1) * size * 0.66
    in_code = False
    for i, line in enumerate(lines):
        spans = []
        for part in re.split(r"(`)", line):
            if part == "`":
                in_code = not in_code
            elif part:
                spans.append(f'<tspan fill="{PINK if in_code else AMBER}">{esc(part)}</tspan>')
        elements.append(
            f'<text x="64" y="{baseline + i * size * 1.32:.2f}" font-size="{size}" xml:space="preserve">'
            + "".join(spans) + "</text>"
        )
    elements += [
        f'<path d="M64 518 H1136" stroke="{AMBER}" stroke-width="1" stroke-dasharray="5 7"/>',
        f'<text x="64" y="558" font-size="20" fill="{WHITE}">LitoMore</text>',
        f'<text x="1136" y="558" text-anchor="end" font-size="20" fill="{GREY}">{esc(date_label)}</text>',
        f'<text x="64" y="596" font-size="{tag_size:.2f}" fill="{BLUE}">{esc(tags_label)}</text>',
        "</g></svg>",
    ]
    return "\n".join(elements)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cjk-font", type=Path, required=True, help="Path to a Chinese .ttf/.otf font")
    args = parser.parse_args()
    if not args.cjk_font.is_file():
        parser.error("The Chinese font does not exist")
    for command in ("rsvg-convert", "fc-scan"):
        if not shutil.which(command):
            parser.error(f"Install {command} before rendering cards")

    output = ROOT / "static/og/posts"
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="litomore-og-") as temp:
        work = Path(temp)
        fonts = work / "fonts"
        fonts.mkdir()
        # Load only the selected fonts. Cache files stay in the temporary folder.
        shutil.copy2(ROOT / "themes/hacker/static/fonts/sourcecodepro-latin.woff", fonts)
        shutil.copy2(args.cjk_font, fonts)
        config = work / "fonts.conf"
        config.write_text(
            '<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">'
            f'<fontconfig><dir>{html.escape(str(fonts))}</dir>'
            f'<cachedir>{html.escape(str(work / "cache"))}</cachedir></fontconfig>'
        )
        env = dict(os.environ, FONTCONFIG_FILE=str(config), PANGOCAIRO_BACKEND="fontconfig")
        cjk_family = subprocess.check_output(
            ["fc-scan", "--format", "%{family[0]}", str(args.cjk_font)], env=env, text=True
        ).strip()
        count = 0
        for source in sorted((ROOT / "content/posts").glob("*.md")):
            if source.name.startswith("_"):
                continue
            post = tomllib.loads(source.read_text().split("+++", 2)[1])
            language = "zh" if source.name.endswith(".zh.md") else "en"
            stem = source.name.removesuffix(".zh.md").removesuffix(".md")
            slug = post.get("slug", re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem))
            destination = output / f"{slug}.{language}.png"
            image_url = "/" + str(destination.relative_to(ROOT / "static"))
            if post.get("extra", {}).get("images") != [image_url]:
                raise ValueError(f"Set [extra] images = [{image_url!r}] in {source.name}")
            svg = work / "card.svg"
            svg.write_text(svg_card(post, language, cjk_family))
            subprocess.run(["rsvg-convert", "--output", str(destination), str(svg)], check=True, env=env)
            count += 1
        print(f"Generated {count} localized OpenGraph images ({WIDTH} × {HEIGHT}) in {output}")


if __name__ == "__main__":
    main()
