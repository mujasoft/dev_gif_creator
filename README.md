# vid2gif
![License](https://img.shields.io/badge/license-MIT-green)
![Shell](https://img.shields.io/badge/shell-bash-blue)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![Demo](https://img.shields.io/badge/demo-available-green)
[![Homebrew Tap](https://img.shields.io/badge/homebrew-install-green)](https://github.com/mujasoft/homebrew-tools)


Convert video files into **optimized GIFs** using `ffmpeg` — perfect for README demos and lightweight previews.

> I found myself using this script often, so I made it a standalone tool — something you can drop into your `$PATH` and run whenever you need a clean GIF from a video.

## Demo

![Demo GIF](Demo.gif)

## Why this exists?

- Works **entirely offline** — nothing is ever uploaded
- Ideal for GitHub project demos, bug reproductions or sharing animations
- Easier and safer than uploading to unreliable online converters


## Features

- Converts `.mp4`, `.mov`, `.mkv`, `.webm`, etc.
- Uses palette generation for smaller, smoother GIFs.
- Cleans up temporary files after use.
- Can append timestamps to avoid overwriting output file.
- Fully **offline**, no external dependencies besides `ffmpeg`.
- Pure Bash implementation — portable & dependency-free (except `ffmpeg`)

## Requirement(s)

[ffmpeg](https://ffmpeg.org) must be installed and in your `$PATH`

```bash
brew install ffmpeg
```

## Installation
### Option 1: Via Homebrew
```bash
brew tap mujasoft/tools
brew install vid2gif
```

### Option 2: Install globally.
```bash
chmod +x vid2gif
mv vid2gif /usr/local/bin/
```
### Option 3: Add to path
```bash
export PATH="$PATH:/path/to/this/repo"
```

## Usage

```bash
./vid2gif -i input.mov
./vid2gif -i clip.mp4 -o demo.gif
```

## Options

| Flag                | Description                                                           |
|--------------       |----------------------------------------------                         |
| `-i`                | Input video file (required)                                           |
| `-o`                | Output name (optional, default: `output`)                             |
| `-h --help`         | Show help message                                                     |
| `-v --version`      | Show tool version                                                     |
| `-t`                | Append a timestamp to output basename (Optional, default=False)       |



## License

MIT License — see [LICENSE](./LICENSE) for details.