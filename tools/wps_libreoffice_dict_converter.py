#!/usr/bin/env python3
"""Convert LibreOffice Hunspell dictionaries to the WPS Office layout.

The tool intentionally performs a full preflight scan before writing files.
It shows the LibreOffice sources on the left and the WPS build targets on the
right, then enables conversion only when required inputs are present.
"""

from __future__ import annotations

import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSplitter,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


ROOT = Path(__file__).resolve().parents[1]
LO_ROOT = ROOT / "third-party/libreoffice-dictionaries-collection/dicts"
WPS_OLD_ROOT = ROOT / "third-party/wps-office-11.2.0.9255-dicts/dicts"
BUILD_ROOT = ROOT / "build/wps-libreoffice-dicts"
REPORT_PATH = BUILD_ROOT / "BUILD_SOURCE_MAP.txt"


SPECIAL_SOURCE_NAMES = {
    "be_BY": "be-official",
    "ca_ES": "ca",
    "de_AT": "de_AT_frami",
    "de_CH": "de_CH_frami",
    "de_DE": "de_DE_frami",
    "fr_FR": "fr",
    "gl": "gl_ES",
    "lt_LT": "lt",
}

OLD_WPS_FALLBACKS = {"km_KH", "ms_MY", "qu_EC", "sw_TZ"}

GENERATED_DICT_CONF = {
    "de_AT": {
        "DisplayName": "Deutsch (Österreich)",
        "DisplayName[zh_CN]": "德语 (奥地利)",
        "DisplayName[en_US]": "German (Austria)",
        "DisplayName[es_ES]": "Alemán (Austria)",
        "DisplayName[zh_TW]": "德文 (奧地利)",
        "DisplayName[zh_HK]": "德文 (奧地利)",
        "DisplayName[zh_MO]": "德文 (奧地利)",
        "DisplayName[zh_Hant_CN]": "德文 (奧地利)",
    },
    "de_CH": {
        "DisplayName": "Deutsch (Schweiz)",
        "DisplayName[zh_CN]": "德语 (瑞士)",
        "DisplayName[en_US]": "German (Switzerland)",
        "DisplayName[es_ES]": "Alemán (Suiza)",
        "DisplayName[zh_TW]": "德文 (瑞士)",
        "DisplayName[zh_HK]": "德文 (瑞士)",
        "DisplayName[zh_MO]": "德文 (瑞士)",
        "DisplayName[zh_Hant_CN]": "德文 (瑞士)",
    },
    "en_CA": {
        "DisplayName": "English (Canada)",
        "DisplayName[zh_CN]": "英语 (加拿大)",
        "DisplayName[en_US]": "English (Canada)",
        "DisplayName[es_ES]": "Inglés (Canadá)",
        "DisplayName[zh_TW]": "英文 (加拿大)",
        "DisplayName[zh_HK]": "英文 (加拿大)",
        "DisplayName[zh_MO]": "英文 (加拿大)",
        "DisplayName[zh_Hant_CN]": "英文 (加拿大)",
    },
    "en_ZA": {
        "DisplayName": "English (South Africa)",
        "DisplayName[zh_CN]": "英语 (南非)",
        "DisplayName[en_US]": "English (South Africa)",
        "DisplayName[es_ES]": "Inglés (Sudáfrica)",
        "DisplayName[zh_TW]": "英文 (南非)",
        "DisplayName[zh_HK]": "英文 (南非)",
        "DisplayName[zh_MO]": "英文 (南非)",
        "DisplayName[zh_Hant_CN]": "英文 (南非)",
    },
    "es_CR": {
        "DisplayName": "Español (Costa Rica)",
        "DisplayName[zh_CN]": "西班牙语 (哥斯达黎加)",
        "DisplayName[en_US]": "Spanish (Costa Rica)",
        "DisplayName[es_ES]": "Español (Costa Rica)",
        "DisplayName[zh_TW]": "西班牙文 (哥斯大黎加)",
        "DisplayName[zh_HK]": "西班牙文 (哥斯大黎加)",
        "DisplayName[zh_MO]": "西班牙文 (哥斯大黎加)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (哥斯大黎加)",
    },
    "es_CU": {
        "DisplayName": "Español (Cuba)",
        "DisplayName[zh_CN]": "西班牙语 (古巴)",
        "DisplayName[en_US]": "Spanish (Cuba)",
        "DisplayName[es_ES]": "Español (Cuba)",
        "DisplayName[zh_TW]": "西班牙文 (古巴)",
        "DisplayName[zh_HK]": "西班牙文 (古巴)",
        "DisplayName[zh_MO]": "西班牙文 (古巴)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (古巴)",
    },
    "es_DO": {
        "DisplayName": "Español (República Dominicana)",
        "DisplayName[zh_CN]": "西班牙语 (多米尼加共和国)",
        "DisplayName[en_US]": "Spanish (Dominican Republic)",
        "DisplayName[es_ES]": "Español (República Dominicana)",
        "DisplayName[zh_TW]": "西班牙文 (多明尼加共和國)",
        "DisplayName[zh_HK]": "西班牙文 (多明尼加共和國)",
        "DisplayName[zh_MO]": "西班牙文 (多明尼加共和國)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (多明尼加共和國)",
    },
    "es_EC": {
        "DisplayName": "Español (Ecuador)",
        "DisplayName[zh_CN]": "西班牙语 (厄瓜多尔)",
        "DisplayName[en_US]": "Spanish (Ecuador)",
        "DisplayName[es_ES]": "Español (Ecuador)",
        "DisplayName[zh_TW]": "西班牙文 (厄瓜多)",
        "DisplayName[zh_HK]": "西班牙文 (厄瓜多)",
        "DisplayName[zh_MO]": "西班牙文 (厄瓜多)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (厄瓜多)",
    },
    "es_GQ": {
        "DisplayName": "Español (Guinea Ecuatorial)",
        "DisplayName[zh_CN]": "西班牙语 (赤道几内亚)",
        "DisplayName[en_US]": "Spanish (Equatorial Guinea)",
        "DisplayName[es_ES]": "Español (Guinea Ecuatorial)",
        "DisplayName[zh_TW]": "西班牙文 (赤道幾內亞)",
        "DisplayName[zh_HK]": "西班牙文 (赤道幾內亞)",
        "DisplayName[zh_MO]": "西班牙文 (赤道幾內亞)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (赤道幾內亞)",
    },
    "es_GT": {
        "DisplayName": "Español (Guatemala)",
        "DisplayName[zh_CN]": "西班牙语 (危地马拉)",
        "DisplayName[en_US]": "Spanish (Guatemala)",
        "DisplayName[es_ES]": "Español (Guatemala)",
        "DisplayName[zh_TW]": "西班牙文 (瓜地馬拉)",
        "DisplayName[zh_HK]": "西班牙文 (瓜地馬拉)",
        "DisplayName[zh_MO]": "西班牙文 (瓜地馬拉)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (瓜地馬拉)",
    },
    "es_HN": {
        "DisplayName": "Español (Honduras)",
        "DisplayName[zh_CN]": "西班牙语 (洪都拉斯)",
        "DisplayName[en_US]": "Spanish (Honduras)",
        "DisplayName[es_ES]": "Español (Honduras)",
        "DisplayName[zh_TW]": "西班牙文 (洪都拉斯)",
        "DisplayName[zh_HK]": "西班牙文 (洪都拉斯)",
        "DisplayName[zh_MO]": "西班牙文 (洪都拉斯)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (洪都拉斯)",
    },
    "es_NI": {
        "DisplayName": "Español (Nicaragua)",
        "DisplayName[zh_CN]": "西班牙语 (尼加拉瓜)",
        "DisplayName[en_US]": "Spanish (Nicaragua)",
        "DisplayName[es_ES]": "Español (Nicaragua)",
        "DisplayName[zh_TW]": "西班牙文 (尼加拉瓜)",
        "DisplayName[zh_HK]": "西班牙文 (尼加拉瓜)",
        "DisplayName[zh_MO]": "西班牙文 (尼加拉瓜)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (尼加拉瓜)",
    },
    "es_PA": {
        "DisplayName": "Español (Panamá)",
        "DisplayName[zh_CN]": "西班牙语 (巴拿马)",
        "DisplayName[en_US]": "Spanish (Panama)",
        "DisplayName[es_ES]": "Español (Panamá)",
        "DisplayName[zh_TW]": "西班牙文 (巴拿馬)",
        "DisplayName[zh_HK]": "西班牙文 (巴拿馬)",
        "DisplayName[zh_MO]": "西班牙文 (巴拿馬)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (巴拿馬)",
    },
    "es_PE": {
        "DisplayName": "Español (Perú)",
        "DisplayName[zh_CN]": "西班牙语 (秘鲁)",
        "DisplayName[en_US]": "Spanish (Peru)",
        "DisplayName[es_ES]": "Español (Perú)",
        "DisplayName[zh_TW]": "西班牙文 (秘魯)",
        "DisplayName[zh_HK]": "西班牙文 (秘魯)",
        "DisplayName[zh_MO]": "西班牙文 (秘魯)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (秘魯)",
    },
    "es_PH": {
        "DisplayName": "Español (Filipinas)",
        "DisplayName[zh_CN]": "西班牙语 (菲律宾)",
        "DisplayName[en_US]": "Spanish (Philippines)",
        "DisplayName[es_ES]": "Español (Filipinas)",
        "DisplayName[zh_TW]": "西班牙文 (菲律賓)",
        "DisplayName[zh_HK]": "西班牙文 (菲律賓)",
        "DisplayName[zh_MO]": "西班牙文 (菲律賓)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (菲律賓)",
    },
    "es_PY": {
        "DisplayName": "Español (Paraguay)",
        "DisplayName[zh_CN]": "西班牙语 (巴拉圭)",
        "DisplayName[en_US]": "Spanish (Paraguay)",
        "DisplayName[es_ES]": "Español (Paraguay)",
        "DisplayName[zh_TW]": "西班牙文 (巴拉圭)",
        "DisplayName[zh_HK]": "西班牙文 (巴拉圭)",
        "DisplayName[zh_MO]": "西班牙文 (巴拉圭)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (巴拉圭)",
    },
    "es_SV": {
        "DisplayName": "Español (El Salvador)",
        "DisplayName[zh_CN]": "西班牙语 (萨尔瓦多)",
        "DisplayName[en_US]": "Spanish (El Salvador)",
        "DisplayName[es_ES]": "Español (El Salvador)",
        "DisplayName[zh_TW]": "西班牙文 (薩爾瓦多)",
        "DisplayName[zh_HK]": "西班牙文 (薩爾瓦多)",
        "DisplayName[zh_MO]": "西班牙文 (薩爾瓦多)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (薩爾瓦多)",
    },
    "es_US": {
        "DisplayName": "Español (Estados Unidos)",
        "DisplayName[zh_CN]": "西班牙语 (美国)",
        "DisplayName[en_US]": "Spanish (United States)",
        "DisplayName[es_ES]": "Español (Estados Unidos)",
        "DisplayName[zh_TW]": "西班牙文 (美國)",
        "DisplayName[zh_HK]": "西班牙文 (美國)",
        "DisplayName[zh_MO]": "西班牙文 (美國)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (美國)",
    },
    "es_UY": {
        "DisplayName": "Español (Uruguay)",
        "DisplayName[zh_CN]": "西班牙语 (乌拉圭)",
        "DisplayName[en_US]": "Spanish (Uruguay)",
        "DisplayName[es_ES]": "Español (Uruguay)",
        "DisplayName[zh_TW]": "西班牙文 (烏拉圭)",
        "DisplayName[zh_HK]": "西班牙文 (烏拉圭)",
        "DisplayName[zh_MO]": "西班牙文 (烏拉圭)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (烏拉圭)",
    },
    "es_VE": {
        "DisplayName": "Español (Venezuela)",
        "DisplayName[zh_CN]": "西班牙语 (委内瑞拉)",
        "DisplayName[en_US]": "Spanish (Venezuela)",
        "DisplayName[es_ES]": "Español (Venezuela)",
        "DisplayName[zh_TW]": "西班牙文 (委內瑞拉)",
        "DisplayName[zh_HK]": "西班牙文 (委內瑞拉)",
        "DisplayName[zh_MO]": "西班牙文 (委內瑞拉)",
        "DisplayName[zh_Hant_CN]": "西班牙文 (委內瑞拉)",
    },
}


@dataclass(frozen=True)
class Mapping:
    code: str
    source_base: Path | None
    fallback_base: Path | None
    dict_conf_source: Path | None
    generated_conf: dict[str, str] | None
    source_kind: str


@dataclass(frozen=True)
class Analysis:
    mappings: list[Mapping]
    errors: list[str]
    warnings: list[str]
    unmapped_sources: list[str]


def dictionary_pairs() -> dict[str, Path]:
    pairs: dict[str, Path] = {}
    if not LO_ROOT.exists():
        return pairs
    for aff_path in LO_ROOT.rglob("*.aff"):
        name = aff_path.stem
        if name.startswith("hyph_"):
            continue
        dic_path = aff_path.with_suffix(".dic")
        if dic_path.exists():
            pairs[name] = aff_path.with_suffix("")
    return pairs


def expected_codes(lo_pairs: dict[str, Path]) -> list[str]:
    codes: set[str] = set()
    if WPS_OLD_ROOT.exists():
        codes.update(path.name for path in WPS_OLD_ROOT.iterdir() if path.is_dir())
    codes.update(GENERATED_DICT_CONF)
    for code in ("de_AT", "de_CH", "en_CA", "en_ZA"):
        if source_name_for(code) in lo_pairs:
            codes.add(code)
    for code in lo_pairs:
        if code.startswith("es_"):
            codes.add(code)
    codes.discard("es")
    return sorted(codes)


def source_name_for(code: str) -> str:
    return SPECIAL_SOURCE_NAMES.get(code, code)


def analyze() -> Analysis:
    errors: list[str] = []
    warnings: list[str] = []
    mappings: list[Mapping] = []

    if not LO_ROOT.exists():
        errors.append(f"LibreOffice dictionaries folder is missing: {LO_ROOT}")
    if not WPS_OLD_ROOT.exists():
        warnings.append(f"Old WPS dictionary folder is missing: {WPS_OLD_ROOT}")

    lo_pairs = dictionary_pairs()
    used_source_names: set[str] = set()

    for code in expected_codes(lo_pairs):
        source_name = source_name_for(code)
        source_base = lo_pairs.get(source_name)
        fallback_base = None
        source_kind = "LibreOffice"

        if source_base:
            used_source_names.add(source_name)
        elif code in OLD_WPS_FALLBACKS:
            candidate = WPS_OLD_ROOT / code / "main"
            if candidate.with_suffix(".aff").exists() and candidate.with_suffix(".dic").exists():
                fallback_base = candidate
                source_kind = "Old WPS fallback"
                warnings.append(f"{code}: no LibreOffice pair found; old WPS files will be used.")
            else:
                errors.append(f"{code}: missing LibreOffice pair and old WPS fallback files.")
        else:
            errors.append(f"{code}: missing LibreOffice pair for '{source_name}.aff/.dic'.")

        dict_conf_source = None
        build_conf = BUILD_ROOT / code / "dict.conf"
        old_conf = WPS_OLD_ROOT / code / "dict.conf"
        generated_conf = GENERATED_DICT_CONF.get(code)
        if build_conf.exists():
            dict_conf_source = build_conf
        elif old_conf.exists():
            dict_conf_source = old_conf
        elif generated_conf:
            pass
        else:
            errors.append(f"{code}: missing dict.conf source and no generated metadata is configured.")

        mappings.append(
            Mapping(
                code=code,
                source_base=source_base,
                fallback_base=fallback_base,
                dict_conf_source=dict_conf_source,
                generated_conf=generated_conf,
                source_kind=source_kind,
            )
        )

    unmapped = sorted(name for name in lo_pairs if name not in used_source_names and not name.startswith("hyph_"))
    if unmapped:
        warnings.append(
            "LibreOffice contains dictionary pairs that are not mapped to WPS targets: "
            + ", ".join(unmapped)
        )

    return Analysis(mappings=mappings, errors=errors, warnings=warnings, unmapped_sources=unmapped)


def write_generated_conf(path: Path, values: dict[str, str]) -> None:
    lines = ["[Dictionary]"]
    lines.extend(f"{key}={value}" for key, value in values.items())
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def convert(analysis: Analysis) -> None:
    BUILD_ROOT.mkdir(parents=True, exist_ok=True)
    report_lines = ["WPS LibreOffice dictionary build source map", ""]

    for item in analysis.mappings:
        out_dir = BUILD_ROOT / item.code
        out_dir.mkdir(parents=True, exist_ok=True)

        if item.dict_conf_source:
            if item.dict_conf_source != out_dir / "dict.conf":
                shutil.copy2(item.dict_conf_source, out_dir / "dict.conf")
        elif item.generated_conf:
            write_generated_conf(out_dir / "dict.conf", item.generated_conf)

        base = item.source_base or item.fallback_base
        if base is None:
            raise RuntimeError(f"{item.code}: no source files available")
        shutil.copy2(base.with_suffix(".aff"), out_dir / "main.aff")
        shutil.copy2(base.with_suffix(".dic"), out_dir / "main.dic")
        report_lines.append(
            f"{item.code}: {item.source_kind} -> {base.with_suffix('.aff')} / {base.with_suffix('.dic')}"
        )

    report_lines.extend(
        [
            "",
            f"Total folders: {len(analysis.mappings)}",
            f"LibreOffice mappings: {sum(1 for item in analysis.mappings if item.source_base)}",
            f"Old WPS fallbacks: {sum(1 for item in analysis.mappings if item.fallback_base)}",
        ]
    )
    REPORT_PATH.write_text("\n".join(report_lines) + "\n", encoding="utf-8")


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.analysis = Analysis([], [], [], [])
        self.setWindowTitle("LibreOffice to WPS Dictionary Converter")
        self.resize(1200, 760)

        root = QWidget()
        layout = QVBoxLayout(root)

        title = QLabel("LibreOffice to WPS Dictionary Converter")
        title.setStyleSheet("font-size: 20px; font-weight: 600;")
        layout.addWidget(title)

        paths = QLabel(
            f"LibreOffice: {LO_ROOT}\nWPS build: {BUILD_ROOT}"
        )
        paths.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        layout.addWidget(paths)

        splitter = QSplitter()
        self.left_tree = self.make_tree("LibreOffice sources")
        self.right_tree = self.make_tree("WPS build targets")
        splitter.addWidget(self.left_tree)
        splitter.addWidget(self.right_tree)
        splitter.setSizes([600, 600])
        layout.addWidget(splitter, 1)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setMinimumHeight(120)
        layout.addWidget(self.log)

        buttons = QHBoxLayout()
        self.analyze_button = QPushButton("Analyze")
        self.convert_button = QPushButton("Convert")
        self.convert_button.setEnabled(False)
        self.close_button = QPushButton("Close")
        buttons.addWidget(self.analyze_button)
        buttons.addWidget(self.convert_button)
        buttons.addStretch(1)
        buttons.addWidget(self.close_button)
        layout.addLayout(buttons)

        self.analyze_button.clicked.connect(self.run_analysis)
        self.convert_button.clicked.connect(self.run_conversion)
        self.close_button.clicked.connect(self.close)

        self.setCentralWidget(root)
        self.run_analysis()

    @staticmethod
    def make_tree(title: str) -> QTreeWidget:
        tree = QTreeWidget()
        tree.setHeaderLabels([title, "Status", "Path"])
        tree.header().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        tree.header().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        tree.header().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        return tree

    def run_analysis(self) -> None:
        self.analysis = analyze()
        self.populate_trees()
        lines = []
        if self.analysis.errors:
            lines.append("Blocking errors:")
            lines.extend(f"- {message}" for message in self.analysis.errors)
        else:
            lines.append("No blocking errors found.")
        if self.analysis.warnings:
            lines.append("")
            lines.append("Warnings:")
            lines.extend(f"- {message}" for message in self.analysis.warnings)
        lines.append("")
        lines.append(f"Ready mappings: {len(self.analysis.mappings)}")
        lines.append(f"Build output: {BUILD_ROOT}")
        self.log.setPlainText("\n".join(lines))
        self.convert_button.setEnabled(not self.analysis.errors)

    def populate_trees(self) -> None:
        self.left_tree.clear()
        self.right_tree.clear()
        for item in self.analysis.mappings:
            self.add_source_item(item)
            self.add_target_item(item)
        for name in self.analysis.unmapped_sources:
            source_base = dictionary_pairs().get(name)
            if source_base:
                row = QTreeWidgetItem([name, "Unmapped", str(source_base.parent)])
                self.color_row(row, "warning")
                self.left_tree.addTopLevelItem(row)

    def add_source_item(self, item: Mapping) -> None:
        if item.source_base:
            status = "OK"
            path = str(item.source_base.parent)
        elif item.fallback_base:
            status = "Fallback"
            path = str(item.fallback_base.parent)
        else:
            status = "Missing"
            path = ""
        row = QTreeWidgetItem([item.code, status, path])
        self.color_row(row, "ok" if status == "OK" else "warning" if status == "Fallback" else "error")
        self.left_tree.addTopLevelItem(row)

    def add_target_item(self, item: Mapping) -> None:
        out_dir = BUILD_ROOT / item.code
        status_parts = []
        for filename in ("dict.conf", "main.aff", "main.dic"):
            status_parts.append("OK" if (out_dir / filename).exists() else "Will create")
        status = ", ".join(status_parts)
        row = QTreeWidgetItem([item.code, status, str(out_dir)])
        self.color_row(row, "ok" if out_dir.exists() else "warning")
        self.right_tree.addTopLevelItem(row)

    @staticmethod
    def color_row(row: QTreeWidgetItem, kind: str) -> None:
        colors = {
            "ok": QColor("#1f7a3f"),
            "warning": QColor("#9a6a00"),
            "error": QColor("#b42318"),
        }
        color = colors[kind]
        for index in range(3):
            row.setForeground(index, color)

    def run_conversion(self) -> None:
        if self.analysis.errors:
            QMessageBox.critical(self, "Cannot convert", "Resolve blocking errors before converting.")
            return
        try:
            convert(self.analysis)
        except Exception as exc:  # noqa: BLE001 - shown to the user in the GUI.
            QMessageBox.critical(self, "Conversion failed", str(exc))
            return
        self.run_analysis()
        QMessageBox.information(self, "Conversion complete", f"Dictionaries were written to:\n{BUILD_ROOT}")


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
