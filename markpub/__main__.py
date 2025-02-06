#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MarkPub 应用程序入口点
"""

import sys
from pathlib import Path

# 确保可以导入 markpub 包
sys.path.insert(0, str(Path(__file__).parent.parent))

from markpub.ui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication


def main():
    """应用程序主入口"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main() 