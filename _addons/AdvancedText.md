---
permalink: /addons/advanced-text
title: "Advanced Text"
excerpt: "Extends RichTextLabel, adds support for Markdown, RenPy and much more."
published: true
author_profile: true
author: "Jeremi Biernacki"
layout: single
header:
  # teaser: assets/placeholder.png
  # overlay_image: assets/placeholder.png
  caption: "2.0 hotfix 1"
  actions:
    - label: "Download"
      url: "https://github.com/rakugoteam/AdvancedText/releases/latest"
---

- [🌳 repo](https://github.com/rakugoteam/AdvancedText)
- [⬇️ download](https://github.com/rakugoteam/AdvancedText/releases/latest)
- [📚 docs](https://rakugoteam.github.io/advanced-text-docs/2.0/)

Extends RichTextLabel and adds support for Markdown and RenPy
Soon there will be docs for most of the features.

## Features

- Supports Markdown and RenPy
- Variables use RakuVars `<var>` in Markdown, Renpy and BBCode
- Adds headers supports RenPy and BBCode
- Support [Emojis For Godot](https://github.com/rakugoteam/Emojis-For-Godot) use `:emoji:`
- Support [MaterialIcons For Godot](https://github.com/rakugoteam/Godot-Material-Icons) use `[icon=icon-name]`

### Nodes

- **AdvancedTextLabel** - A label that supports Markdown and RenPy
- **AdvancedTextButton** - **AdvancedTextLabel** that behaves like a button
- **AdvancedTextCheckButton** - **AdvancedTextLabel** that behaves like a check button

### Resources

- **TextParser** - base class for our TextParsers
- **ExtendedBBCodeParser**:
  - base of for our RenPy Markup and Markdown parsers
  - includes support for things mentioned in [Features](#features)
- **RenPyMarkup** - RenPy Markup Parser with extra tags so it is 100% replaceable with Godot's BBCode
- **MarkdownParser** - Markdown Parser with extra stuff so it is mostly replaceable with Godot's BBCode
