Title: Experimenting with Vim emulations in all apps
Date: 2019-09-18 12:30
Category: vanity, vim

# Background

I spent more or less the first ten years of my career using Linux machines, and the next 11 years using Windows for my day-to-day work.  I used a Mac laptop for most of that time as my personal device, and I'd occasionally do small personal projects with it, but I never really used it for serious development.

I'm back to using Linux now, but the twist is that I access everything from applications running on a Mac laptop.  I've been going slightly crazy because the key bindings in the applications I use (primarily VS Code for development, iTerm2 as a terminal, and Emacs as my research notebook) all support slightly different navigation keys out of the box.  In particular, I found myself getting messed up on shortcuts that use the "meta" key.

# Keymap craziness

In Windows and Linux, the "Alt" key (on either side of the spacebar) is a great "meta" key.  Most system keystrokes use "Control" as the modifier, so "Alt" can mostly be interpreted freely as an Emacs-style modifier.  That's something I've especially relied on for navigation (moving forward a word, etc.).

On Macs, the "Command" key (also on either side fo the spacebar) is used heavily in system shortcuts.  That means that care is needed to interpret it as a "Meta" key: Command-f is usually interpreted as "find," but Emacs uses it for "forward-word," for example.

The result was that my setup had become a terrible comp
