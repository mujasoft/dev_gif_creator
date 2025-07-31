# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Mujaheed Khan
#
# This file is part of the gifs4docs project.
# You may use, distribute, and modify this code under the terms of the MIT
# license. See the LICENSE file in the project root for more information.


import subprocess
from pathlib import Path
import os


def test_single_file_conversion(tmp_path):
    """Convert one simple file and verify it exists"""

    mov = Path("tests") / "assets" / "pattern.mov"
    mov_path = Path(mov)
    gif_path = tmp_path / "pattern.gif"

    # Run gifs4docs CLI
    subprocess.run([
        "./gif4docs", "-i", mov_path, "-o", gif_path
    ], check=True)

    # Assert the GIF was created
    assert gif_path.exists()
    assert gif_path.stat().st_size > 0


def test_version():
    """Make sure version string is updated."""

    result = subprocess.run(["./gif4docs", "-v"],
                            capture_output=True,
                            text=True,
                            check=True
                            )

    # Capture stdout text
    output = result.stdout.strip()

    assert "gif4docs v1.0.3" in output


def test_help():
    """Make sure help text works."""

    result = subprocess.run(["./gif4docs", "-h"], capture_output=True,
                            text=True, check=True)
    assert "Usage" in result.stdout


def test_batch_file_conversion(tmp_path):
    """Convert one simple file and verify it exists"""

    mov_folder_path = Path("assets/videos")

    result = subprocess.run(["./gif4docs", "-d", mov_folder_path,
                             "-k", tmp_path],
                            capture_output=True,
                            text=True,
                            check=True
                            )

    # Capture stdout text
    output = result.stdout.strip()

    assert "Batch conversion completed successfully!" in output
