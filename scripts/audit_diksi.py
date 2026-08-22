#!/usr/bin/env python3
"""Audit diksi dan ejaan rawan dalam sumber LaTeX TA.

Skrip ini sengaja tidak mengubah file. Tujuannya adalah membuat daftar kandidat
yang perlu dicek manual: bentuk tidak baku, serapan yang sering salah, frasa
akademik yang kurang rapi, dan istilah Inggris yang mungkin perlu dimiringkan.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


SKIP_DIRS = {
    ".git",
    "build",
    "reports",
    "scripts",
    "images",
    "algorithms",
    "listings",
    "tables",
}


RAWAN_TERMS: dict[str, str] = {
    "standarisasi": "Gunakan 'standardisasi'.",
    "terstandarisasi": "Gunakan 'mengikuti standar' atau 'berformat standar'.",
    "terstandardisasi": "Lebih aman pakai 'mengikuti standar' atau 'berformat standar'.",
    "terstandar": "Lebih formal: 'standar' atau 'mengikuti standar'.",
    "teoritis": "Gunakan 'teoretis'.",
    "praktek": "Gunakan 'praktik'.",
    "analisa": "Gunakan 'analisis'.",
    "metoda": "Gunakan 'metode'.",
    "resiko": "Gunakan 'risiko'.",
    "obyek": "Gunakan 'objek'.",
    "subyek": "Gunakan 'subjek'.",
    "sistim": "Gunakan 'sistem'.",
    "efektifitas": "Gunakan 'efektivitas'.",
    "aktifitas": "Gunakan 'aktivitas'.",
    "ijin": "Gunakan 'izin'.",
    "nasehat": "Gunakan 'nasihat'.",
    "otentikasi": "Gunakan 'autentikasi'.",
    "diinput": "Lebih baku: 'dimasukkan'.",
    "menginput": "Lebih baku: 'memasukkan'.",
    "output": "Dalam prose Indonesia, pertimbangkan 'keluaran'.",
    "input": "Dalam prose Indonesia, pertimbangkan 'masukan'.",
    "end-user": "Pertimbangkan 'pengguna akhir' atau italic bila istilah asing.",
}


PHRASE_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bdi mana\b", re.IGNORECASE), "Cek: sering lebih baik diganti 'yang', 'tempat', atau susun ulang kalimat."),
    (re.compile(r"\byang mana\b", re.IGNORECASE), "Cek: sering tidak perlu dalam ragam akademik."),
    (re.compile(r"\bantar\s+(komponen|sistem|layanan|muka|instansi)\b", re.IGNORECASE), "Cek: bentuk terikat 'antar-' biasanya dirangkai, mis. 'antarkomponen'."),
    (re.compile(r"\bnon-(intrusif|destruktif|termal|fungsional|teknis|formal)\b", re.IGNORECASE), "Cek: bentuk terikat 'non-' biasanya dirangkai, mis. 'nonintrusif'."),
]


ENGLISH_TERMS = [
    "audit trail",
    "best practice",
    "blueprint",
    "boundary",
    "computer vision",
    "dashboard",
    "deployment",
    "edge",
    "edge computing",
    "edge-cloud",
    "endpoint",
    "framework",
    "interface",
    "loose coupling",
    "manual override",
    "metadata",
    "middleware",
    "payload",
    "screening",
    "service",
    "state",
    "traceability",
    "websocket",
    "workflow",
]

ASPELL_DICT_DIR = ROOT / ".tools" / "aspell-id" / "aspell5-id-1.2-0"
TOKEN_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿ]+)?")

ASPELL_ALLOWLIST = {
    "akuisisi",
    "antarkomponen",
    "antarlapisan",
    "antarlayanan",
    "antarmuka",
    "artefak",
    "autentikasi",
    "beranotasi",
    "cloudflare",
    "dashboard",
    "deteksi",
    "diagram",
    "digital",
    "digitalisasi",
    "edge",
    "efektivitas",
    "ekosistem",
    "evaluasi",
    "fungsional",
    "identifikasi",
    "implementasi",
    "inferensi",
    "inspeksi",
    "integrasi",
    "integritas",
    "interoperabilitas",
    "kargo",
    "kontainer",
    "konteks",
    "konseptual",
    "layanan",
    "manifes",
    "metadata",
    "metodologi",
    "mongodb",
    "nonfungsional",
    "nonintrusif",
    "nondestruktif",
    "nontermal",
    "operasional",
    "orkestrasi",
    "pemindaian",
    "perancangan",
    "persistensi",
    "propagasi",
    "realisasi",
    "responsivitas",
    "skenario",
    "standardisasi",
    "teoretis",
    "terintegrasi",
    "terstruktur",
    "visualisasi",
    "websocket",
}


LATEX_COMMAND_RE = re.compile(r"\\[a-zA-Z@]+(?:\s*\[[^\]]*\])?(?:\s*\{[^{}]*\})?")
COMMENT_RE = re.compile(r"(?<!\\)%.*$")


@dataclass(frozen=True)
class Finding:
    path: Path
    line_no: int
    match: str
    message: str
    line: str


@dataclass(frozen=True)
class SpellFinding:
    word: str
    count: int
    examples: tuple[str, ...]


def iter_tex_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.tex"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts[:-1]):
            continue
        files.append(path)
    return sorted(files)


def strip_latex_for_words(line: str) -> str:
    line = COMMENT_RE.sub("", line)
    line = re.sub(r"\\(?:autocite|cite|ref|label|texttt|nolinkurl|url)\{[^{}]*\}", " ", line)
    line = LATEX_COMMAND_RE.sub(" ", line)
    return line


def is_inside_command_arg(line: str, start: int, end: int, commands: set[str]) -> bool:
    before = line[:start]
    open_pos = -1
    command = ""
    for candidate in commands:
        candidate_pos = before.rfind(rf"\{candidate}{{")
        if candidate_pos > open_pos:
            open_pos = candidate_pos
            command = candidate
    if open_pos == -1:
        return False
    close_pos = line.find("}", open_pos + len(command) + 2)
    return close_pos >= end


def audit_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    in_listing = False
    for line_no, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if r"\begin{lstlisting}" in raw_line:
            in_listing = True
        if in_listing:
            if r"\end{lstlisting}" in raw_line:
                in_listing = False
            continue

        line = COMMENT_RE.sub("", raw_line)
        searchable = strip_latex_for_words(line)

        for term, message in RAWAN_TERMS.items():
            pattern = re.compile(rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])", re.IGNORECASE)
            for match in pattern.finditer(searchable):
                findings.append(Finding(path, line_no, match.group(0), message, raw_line.strip()))

        for pattern, message in PHRASE_PATTERNS:
            for match in pattern.finditer(searchable):
                findings.append(Finding(path, line_no, match.group(0), message, raw_line.strip()))

        english_line = re.sub(r"\\(?:autocite|cite|ref|label|texttt|nolinkurl|url|includegraphics)\s*(?:\[[^\]]*\])?\{[^{}]*\}", " ", line)
        lower_line = english_line.lower()
        for term in ENGLISH_TERMS:
            for match in re.finditer(rf"(?<![a-z]){re.escape(term)}(?![a-z])", lower_line):
                if is_inside_command_arg(english_line, match.start(), match.end(), {"textit", "texttt", "nolinkurl"}):
                    continue
                findings.append(
                    Finding(
                        path,
                        line_no,
                        match.group(0),
                        "Cek: istilah asing mungkin perlu italic atau diterjemahkan bila dipakai sebagai istilah.",
                        raw_line.strip(),
                    )
                )
    return findings


def collect_words(root: Path) -> dict[str, list[str]]:
    words: dict[str, list[str]] = {}
    in_listing = False
    for path in iter_tex_files(root):
        rel = path.relative_to(root)
        for line_no, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if r"\begin{lstlisting}" in raw_line:
                in_listing = True
            if in_listing:
                if r"\end{lstlisting}" in raw_line:
                    in_listing = False
                continue

            line = strip_latex_for_words(raw_line)
            for match in TOKEN_RE.finditer(line):
                word = match.group(0).strip("-").lower()
                if len(word) < 4 or any(char.isdigit() for char in word):
                    continue
                if word in ASPELL_ALLOWLIST:
                    continue
                if word.isascii() and word.upper() == word:
                    continue
                words.setdefault(word, [])
                if len(words[word]) < 3:
                    words[word].append(f"{rel}:{line_no}: {raw_line.strip()}")
    return words


def run_aspell(words: dict[str, list[str]]) -> tuple[list[SpellFinding], str | None]:
    if not words:
        return [], None
    if not ASPELL_DICT_DIR.exists():
        return [], "Kamus aspell-id lokal belum tersedia."

    cmd = [
        "aspell",
        "--lang=id",
        "--master=id",
        f"--dict-dir={ASPELL_DICT_DIR}",
        "list",
    ]
    try:
        proc = subprocess.run(
            cmd,
            input="\n".join(sorted(words)) + "\n",
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError:
        return [], "Aspell belum tersedia di PATH."
    if proc.returncode not in (0, 1):
        return [], proc.stderr.strip() or "Aspell gagal dijalankan."

    spell_findings = [
        SpellFinding(word=word, count=len(words[word]), examples=tuple(words[word]))
        for word in sorted(set(proc.stdout.split()))
        if word in words
    ]
    spell_findings.sort(key=lambda item: (-item.count, item.word))
    return spell_findings, None


def render_markdown(
    findings: list[Finding],
    spell_findings: list[SpellFinding],
    spell_note: str | None,
    root: Path,
) -> str:
    lines = [
        "# Audit Diksi dan Ejaan Rawan",
        "",
        "Laporan ini dibuat otomatis dari sumber `.tex`. Setiap temuan adalah kandidat yang perlu dicek manual, bukan vonis final.",
        "",
        f"Total temuan pola rawan: {len(findings)}",
        f"Total kandidat spellcheck Aspell: {len(spell_findings)}",
        "",
    ]

    if spell_note:
        lines.extend([f"Catatan spellcheck: {spell_note}", ""])

    lines.extend(["## Pola Rawan", ""])
    if not findings:
        lines.append("Tidak ada temuan dari daftar pola yang diperiksa.")
    else:
        current: Path | None = None
        for item in findings:
            rel = item.path.relative_to(root)
            if current != rel:
                current = rel
                lines.extend(["", f"### {rel}", ""])
            safe_line = item.line.replace("|", "\\|")
            lines.append(f"- Baris {item.line_no}: `{item.match}` - {item.message}")
            lines.append(f"  Cuplikan: {safe_line}")

    lines.extend(["", "## Kandidat Spellcheck Aspell", ""])
    if not spell_findings:
        lines.append("Tidak ada kandidat tambahan dari spellcheck Aspell.")
    else:
        lines.append("Bagian ini memakai kamus `aspell-id` dan allowlist teknis lokal. Kandidat nama diri atau istilah teknis dapat ditambahkan ke allowlist.")
        for item in spell_findings[:200]:
            lines.append("")
            lines.append(f"- `{item.word}` - muncul {item.count} kali")
            for example in item.examples:
                safe_example = example.replace("|", "\\|")
                lines.append(f"  Contoh: {safe_example}")

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="reports/diksi-audit.md", help="Path laporan Markdown relatif terhadap root TA.")
    parser.add_argument("--spellcheck", action="store_true", help="Aktifkan pemeriksaan tambahan memakai aspell-id.")
    args = parser.parse_args()

    findings: list[Finding] = []
    for path in iter_tex_files(ROOT):
        findings.extend(audit_file(path))
    if args.spellcheck:
        spell_findings, spell_note = run_aspell(collect_words(ROOT))
    else:
        spell_findings, spell_note = [], "Spellcheck Aspell tidak diaktifkan. Jalankan dengan --spellcheck untuk audit kamus penuh."

    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_markdown(findings, spell_findings, spell_note, ROOT), encoding="utf-8")
    print(
        f"Wrote {output.relative_to(ROOT)} with "
        f"{len(findings)} pattern findings and {len(spell_findings)} aspell candidates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
