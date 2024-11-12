---
permalink: /kits/visual-novel-kit
title: "Visual Novel Kit"
excerpt: "Kit for creating visual novels."
published: true
author_profile: true
layout: single
header:
  teaser: assets/imgs_main/d_the_question.png
  overlay_image: assets/imgs_main/d_the_question.png
  caption: "WIP"
  actions:
    - label: "Download beta"
      url: "https://github.com/rakugoteam/VisualNovelKit/releases/download/1.0-beta.2/VisualNovelKit_1.0-beta.2.zip"
---

This combine Rakugo with addons and gui for visual novel development.

As this is still work in progress and release is not yet ready, so bellow is instructions for getting started.
It will be simpler and easier when it will be ready.

- [**Repo**](https://github.com/rakugoteam/VisualNovelKit)

# Project Setup

## Fresh Project
1. [Download Visual Novel Kit](https://github.com/rakugoteam/VisualNovelKit/releases/download/1.0-beta.2/VisualNovelKit_1.0-beta.2.zip)
2. Unpack it and open this folder as Godot Project and your are ready to go

## Update from 01.0-beta.1
1. [Download Visual Novel Kit Update](https://github.com/rakugoteam/VisualNovelKit/releases/download/1.0-beta.2/nvkit_1.0-beta.2.zip) 
2. Unpack it over *addons/vnkit* in side your project

## Customizing UI
All folders in this directory are UI scenes, and *Window/Window.tscn* is main one that content them all together.
Those are templates that will be updated in feature. 
So you should copy them to so other place and and start to change them. 
After that you must go *Edit > ProjectSettings* and in tab *Autoload* replace original *Window* scene with your version of it.
