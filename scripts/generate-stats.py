#!/usr/bin/env python3
"""Build a PNG stats card from the GitHub API. No third-party Vercel host."""

from __future__ import annotations

import json
import os
import subprocess
import urllib.request
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "dist" / "github-stats.png"
USERNAME = os.environ.get("GITHUB_USERNAME", "onahFran6")
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""

QUERY = """
query ($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      totalCount
      nodes {
        stargazerCount
        primaryLanguage { name }
      }
    }
    contributionsCollection {
      contributionCalendar { totalContributions }
    }
    pullRequests { totalCount }
    issues { totalCount }
  }
}
"""


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ):
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def fetch() -> dict:
    if TOKEN:
        body = json.dumps({"query": QUERY, "variables": {"login": USERNAME}}).encode()
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=body,
            headers={
                "Authorization": f"bearer {TOKEN}",
                "Content-Type": "application/json",
                "User-Agent": "onahfran6-profile-stats",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode())
    else:
        raw = subprocess.check_output(
            ["gh", "api", "graphql", "-f", f"query={QUERY}", "-F", f"login={USERNAME}"],
            text=True,
        )
        payload = json.loads(raw)
    user = payload.get("data", {}).get("user")
    if not user:
        raise SystemExit(f"GitHub API error: {payload}")
    return user


def draw_card(user: dict) -> None:
    repos = user["repositories"]["nodes"]
    stars = sum(n.get("stargazerCount") or 0 for n in repos)
    langs = Counter(
        n["primaryLanguage"]["name"]
        for n in repos
        if n.get("primaryLanguage") and n["primaryLanguage"].get("name")
    )
    top = langs.most_common(5)
    total_lang = sum(c for _, c in top) or 1

    stats = [
        ("Public repos", str(user["repositories"]["totalCount"])),
        ("Stars", str(stars)),
        ("Followers", str(user["followers"]["totalCount"])),
        ("Pull requests", str(user["pullRequests"]["totalCount"])),
        ("Issues", str(user["issues"]["totalCount"])),
        ("Contributions this year", str(user["contributionsCollection"]["contributionCalendar"]["totalContributions"])),
    ]

    w, h = 920, 380
    img = Image.new("RGB", (w, h), "#0d1117")
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((4, 4, w - 5, h - 5), radius=28, fill="#161b22", outline="#2bbc8a", width=3)

    title_f, label_f, value_f, small_f = font(28), font(18), font(22), font(16)
    d.text((36, 28), "GitHub stats", fill="#2bbc8a", font=title_f)

    y = 88
    for label, value in stats:
        d.text((40, y), label, fill="#8b949e", font=label_f)
        d.text((340, y), value, fill="#e6edf3", font=value_f)
        y += 42

    d.text((520, 88), "Top languages", fill="#2bbc8a", font=title_f)
    bar_x, bar_w, by = 520, 360, 150
    palette = ["#2bbc8a", "#58a6ff", "#d2a8ff", "#f0883e", "#79c0ff"]
    for i, (name, count) in enumerate(top):
        frac = count / total_lang
        d.text((bar_x, by), name, fill="#c9d1d9", font=small_f)
        d.rounded_rectangle((bar_x, by + 24, bar_x + bar_w, by + 36), radius=6, fill="#21262d")
        d.rounded_rectangle(
            (bar_x, by + 24, bar_x + max(12, int(bar_w * frac)), by + 36),
            radius=6,
            fill=palette[i % len(palette)],
        )
        by += 44

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    draw_card(fetch())
